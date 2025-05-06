# Grammar Scoring Engine

A Python-based application that analyzes speech and provides grammar scoring feedback using machine learning.

## Features

- Audio recording and file upload support
- Speech-to-text conversion
- Grammar analysis and scoring
- Real-time feedback
- User-friendly interface

## Prerequisites

- Python 3.11 or higher
- PortAudio (for audio recording)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nikshitha1312/Grammar_Scoring_Engine_SHL_assess.git
cd Grammar_Scoring_Engine_SHL_assess
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

3. Use the interface to:
   - Record audio directly
   - Upload audio files
   - View grammar scores
   - Get feedback

## Project Structure

- `app.py`: Main application file
- `requirements.txt`: Python dependencies
- `grammer (1).ipynb`: Jupyter notebook with model training code

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for the web interface
- PyAudio for audio processing
- LanguageTool for grammar checking 