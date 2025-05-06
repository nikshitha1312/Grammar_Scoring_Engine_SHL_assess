# Grammar Scoring Engine

A web application that evaluates grammar in spoken English using machine learning. The application provides real-time audio recording capabilities and gives feedback on grammar usage.

## Features

- Real-time audio recording
- Audio file upload support
- Grammar scoring with feedback
- User-friendly interface
- Responsive design

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A working microphone (for recording functionality)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/grammar-scoring-engine.git
cd grammar-scoring-engine
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

## Usage

1. **Recording Audio**:
   - Adjust the recording duration using the slider
   - Click "Start Recording" to begin
   - Wait for the recording to complete

2. **Uploading Audio**:
   - Click "Browse files" to upload a WAV or MP3 file
   - Wait for the upload to complete

3. **Processing**:
   - Click "Process Audio" to analyze the grammar
   - Wait for the results
   - View your score and feedback

## Deployment

### Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository and branch
6. Set the main file path to `app.py`
7. Click "Deploy"

### Deploying to Heroku

1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

2. Create a `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

3. Deploy to Heroku:
```bash
heroku create your-app-name
git push heroku main
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for the web framework
- SoundDevice for audio recording capabilities
- All contributors and users of the application 