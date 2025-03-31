# 🧠 A Not-So-Jarvis Voice Assistant

This is a minimal yet functional voice assistant inspired by **Jarvis** from Iron Man. While it may not control your whole house (yet), it can **listen to your voice**, understand your question via **Gemini 2.0**, and **speak the answer back to you**.

---

## 🚀 Features

- 🎙️ Voice-controlled interface
- 🤖 LLM-powered responses using Google Gemini 2.0 Flash (via LangChain)
- 🧠 Real-time speech recognition with `SpeechRecognition`
- 🔊 Converts text responses to audio using `gTTS`
- 🎧 Plays responses using `pygame`

---

## 🛠️ Tech Stack

- **Language:** Python
- **Speech Recognition:** `SpeechRecognition`, `PyAudio`
- **LLM:** `langchain_google_genai` with Gemini 2.0 Flash
- **Text-to-Speech:** `gTTS`
- **Audio Output:** `pygame`
- **Environment Variables:** `dotenv`

---

## 🔁 System Architecture

1. **🎧 Voice Input** → You speak into the microphone
2. **🧠 STT** → Converts your voice to text
3. **🤖 Orchestrator** → Sends text to Gemini LLM for processing
4. **🔊 TTS** → Converts the response to audio
5. **🎧 Audio Playback** → Speaks the response back to you

📌 *Refer to the included architecture diagram for a visual overview.*

---

## 🧪 Planned Updates

- 🗣️ **Interruption-based Input:** Allow users to interrupt audio responses with new questions in real-time.
- 🧠 **Contextual Memory:** Handle multi-turn conversations using local context storage.
- 🌐 **API Integrations:** Integrate weather, reminder, and calendar APIs.
- 🧭 **LangGraph Integration:** Flow-based orchestration for better scalability and visualization.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/voice-assistant-not-so-jarvis.git
cd voice-assistant-not-so-jarvis
pip install -r requirements.txt
```

Add your Google API key to a `.env` file:
```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```bash
python src/main.py
```

Say "stop" anytime to exit the loop.

---

## 📸 Screenshot

Include the architecture diagram image here 👇

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

---

Made with ❤️ and Python after rewatching Iron Man. If you had a Jarvis, what would you ask it first?

---

