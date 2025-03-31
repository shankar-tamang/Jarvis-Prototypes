# src/__init__.py

# Optional: Define package version
__version__ = "1.0.0"

# Import key classes/functions to make them available at the package level.
from .orchestrator import Orchestrator
from .stt import SpeechRecognizer
from .tts import TextToSpeech
from .audio_player import AudioPlayer

# Define __all__ to specify what is exported when 'from my_voice_assistant import *' is used.
__all__ = ["Orchestrator", "SpeechRecognizer", "TextToSpeech", "AudioPlayer"]
