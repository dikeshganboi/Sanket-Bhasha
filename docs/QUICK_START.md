# Sanket Bhasha - Quick Start Guide

Get up and running with Sanket Bhasha in 5 minutes!

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sanket-bhasha.git
cd sanket-bhasha
```

### 2. Set Up Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

### 6. Open Your Browser

Navigate to: `http://localhost:8000`

---

## 🎯 Basic Usage

### Text Input Mode

1. Select your language from the dropdown (default: Hindi)
2. Type your text in the input box
3. Click **"Convert to ISL"** button
4. Watch the sign language animation!

### Voice Input Mode

1. Click the 🎤 **microphone button**
2. Allow microphone permissions when prompted
3. Speak clearly in your selected language
4. The text will be automatically detected and converted

### Text-to-Speech

- Click the **blue speaker button** (🔊) next to the input box to hear what you typed
- Click the green **"Listen"** buttons to hear the original or translated text

---

## 🌐 Supported Languages

| Language  | Code | Example Phrase                          |
| --------- | ---- | --------------------------------------- |
| English   | en   | Hello, how are you?                     |
| Hindi     | hi   | नमस्ते, आप कैसे हैं?                    |
| Marathi   | mr   | नमस्कार, तुम्ही कसे आहात?               |
| Tamil     | ta   | வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்? |
| Telugu    | te   | హలో, మీరు ఎలా ఉన్నారు?                  |
| Bengali   | bn   | হ্যালো, আপনি কেমন আছেন?                 |
| Kannada   | kn   | ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?                   |
| Gujarati  | gu   | હેલો, તમે કેમ છો?                       |
| Malayalam | ml   | ഹലോ, നിങ്ങൾ എങ്ങനെയുണ്ട്?               |
| Punjabi   | pa   | ਹੈਲੋ, ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?                   |
| Odia      | or   | ହେଲୋ, ଆପଣ କେମିତି ଅଛନ୍ତି?                |
| Assamese  | as   | হেল', আপুনি কেনে আছে?                   |

---

## ⚙️ Configuration

### Language Selection

Change the default language in `A2SL/translation_service.py`:

```python
DEFAULT_LANGUAGE = 'hi'  # Change to your preferred language code
```

### Adding Custom ISL Videos

1. Place your MP4 video files in the `static/` directory
2. Name them according to the word they represent (e.g., `hello.mp4`)
3. The system will automatically map words to videos

---

## 🐛 Troubleshooting

### Microphone Not Working

- **Check browser**: Chrome/Edge work best (NOT iOS Safari)
- **Check permissions**: Allow microphone access when prompted
- **Check URL**: Must use `localhost` or HTTPS (not devtunnels.ms)

### Translation Not Working

- **Check internet**: Google Translate API requires internet connection
- **Check language**: Ensure the selected language is supported

### Video Not Playing

- **Check file**: Ensure the ISL video file exists in `static/`
- **Check format**: Only MP4 format is supported
- **Check browser**: Update to the latest version

### Installation Errors

```bash
# If you get module errors, reinstall dependencies:
pip install --upgrade -r requirements.txt

# If migrations fail:
python manage.py migrate --run-syncdb
```

---

## 📱 Mobile Usage

### Best Practices

- Use Chrome on Android for full functionality
- iOS Safari supports text input and TTS (NOT voice recognition)
- Rotate to landscape for better video viewing
- Tap anywhere outside the video to prevent fullscreen

---

## 🧪 Testing

Run the test suite to verify everything works:

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_integration.py

# Run with coverage
pytest --cov=A2SL tests/
```

---

## 🆘 Common Issues

### "service-not-allowed" Error

- This occurs when using non-HTTPS domains or tunnels
- **Solution**: Use `localhost` or proper HTTPS domain

### No Voice Detected

- Speak clearly and close to the microphone
- Check microphone permissions in browser settings
- Try reloading the page

### Animation Not Loading

- Check browser console for errors (F12)
- Verify video file exists in `static/` folder
- Clear browser cache and reload

---

## 📚 Next Steps

- Read [MULTILINGUAL.md](MULTILINGUAL.md) for language features
- Read [TEXT_TO_SPEECH_FEATURE.md](TEXT_TO_SPEECH_FEATURE.md) for TTS details
- Read [TESTING_GUIDE.md](TESTING_GUIDE.md) for testing procedures
- Check [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute

---

## 💡 Tips & Tricks

### Keyboard Shortcuts

- `Enter` key in text input = Submit
- `Esc` key = Clear input

### Browser Recommendations

- **Desktop**: Chrome, Edge, Firefox
- **Android**: Chrome (full features)
- **iOS**: Safari (limited to text input and TTS)

### Performance Tips

- Close other tabs for better performance
- Use wired internet for voice recognition
- Keep browser updated for best compatibility

---

## 🤝 Need Help?

- 📖 Read the full [README.md](../README.md)
- 🐛 Report issues on GitHub
- 💬 Join community discussions
- 📧 Contact maintainers

---

**संकेत भाषा** - Happy Converting! 🤟
