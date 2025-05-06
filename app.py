import streamlit as st
import time
import random  # For simulation purposes
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import wave
import tempfile
import os

# Set page configuration
st.set_page_config(
    page_title="Grammar Scoring Engine",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    .score-display {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 2rem 0;
    }
    .message {
        font-size: 1.2rem;
        text-align: center;
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 10px;
    }
    .good-score {
        background-color: #d4edda;
        color: #155724;
    }
    .low-score {
        background-color: #f8d7da;
        color: #721c24;
    }
    .recording-indicator {
        color: #dc3545;
        animation: blink 1s infinite;
    }
    @keyframes blink {
        50% { opacity: 0; }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'score' not in st.session_state:
    st.session_state.score = None
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'audio_data' not in st.session_state:
    st.session_state.audio_data = None
if 'sample_rate' not in st.session_state:
    st.session_state.sample_rate = 44100

# Audio recording function
def record_audio(duration=5):
    st.session_state.recording = True
    st.session_state.audio_data = sd.rec(
        int(duration * st.session_state.sample_rate),
        samplerate=st.session_state.sample_rate,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    st.session_state.recording = False
    return st.session_state.audio_data

# Save audio to temporary file
def save_audio_to_temp(audio_data, sample_rate):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for 'int16'
        wf.setframerate(sample_rate)
        wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())
    return temp_file.name

# Main heading
st.title("Grammar Scoring Engine")
st.markdown("---")

# Recording section
st.subheader("Record Your Speech")
col1, col2 = st.columns(2)

with col1:
    duration = st.slider("Recording Duration (seconds)", min_value=3, max_value=30, value=5)
    
    if st.button("🎤 Start Recording"):
        if not st.session_state.recording:
            st.session_state.audio_data = record_audio(duration)
            temp_file = save_audio_to_temp(st.session_state.audio_data, st.session_state.sample_rate)
            st.session_state.uploaded_file = temp_file
            st.success("Recording completed! Click 'Process Audio' to analyze.")

with col2:
    if st.session_state.recording:
        st.markdown("""
            <div class='recording-indicator' style='text-align: center;'>
                <span style='font-size: 2rem;'>●</span>
                <p>Recording in progress...</p>
            </div>
        """, unsafe_allow_html=True)

# File uploader
st.subheader("Or Upload Audio File")
uploaded_file = st.file_uploader("Upload your audio file", type=['wav', 'mp3'])

# Process button
if uploaded_file is not None or hasattr(st.session_state, 'uploaded_file'):
    if st.button("Process Audio"):
        st.session_state.processing = True
        
        # Show processing message with emoji
        st.markdown("""
            <div style='text-align: center; margin: 2rem 0;'>
                <span style='font-size: 3rem;'>✅</span>
                <p style='font-size: 1.2rem;'>Please wait while we evaluate your grammar...</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Simulate processing time
        time.sleep(3)
        
        # Simulate score (replace with actual model prediction)
        st.session_state.score = random.randint(0, 100)
        st.session_state.processing = False

# Display results
if st.session_state.score is not None:
    # Display score
    st.markdown(f"""
        <div class='score-display'>
            Score: {st.session_state.score}/100
        </div>
    """, unsafe_allow_html=True)
    
    # Display appropriate message
    if st.session_state.score < 50:
        st.markdown("""
            <div class='message low-score'>
                Don't worry, try again! You're on the path to improvement — never get demotivated.
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class='message good-score'>
                Well done! Keep improving and aim even higher — you're doing great!
            </div>
        """, unsafe_allow_html=True)
    
    # Add a retry button
    if st.button("Try Again"):
        st.session_state.score = None
        if hasattr(st.session_state, 'uploaded_file'):
            os.unlink(st.session_state.uploaded_file)
            del st.session_state.uploaded_file
        st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        Made with ❤️ by Grammar Scoring Engine
    </div>
""", unsafe_allow_html=True) 