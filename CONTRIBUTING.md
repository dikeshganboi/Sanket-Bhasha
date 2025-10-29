# Contributing to Sanket Bhasha

First off, thank you for considering contributing to Sanket Bhasha! It's people like you that make Sanket Bhasha such a great tool for the Indian Sign Language community.

## Code of Conduct

This project and everyone participating in it is governed by respect, inclusivity, and collaboration. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**When submitting a bug report, include:**

- A clear and descriptive title
- Steps to reproduce the behavior
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Browser and OS information
- Python version

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- List any similar features in other applications

### Your First Code Contribution

Unsure where to begin? You can start by looking through these:

- **Beginner issues**: Issues that should only require a few lines of code
- **Help wanted issues**: Issues that might be more involved but are great for new contributors

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Follow the code style** guidelines below
3. **Add tests** if you've added code that should be tested
4. **Ensure the test suite passes**: `pytest`
5. **Update documentation** for any changed functionality
6. **Write a clear commit message**

## Development Setup

### Prerequisites

```bash
# Python 3.8+
python --version

# pip
pip --version
```

### Setup

```bash
# Clone your fork
git clone https://github.com/your-username/sanket-bhasha.git
cd sanket-bhasha

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements_test.txt

# Run migrations
python manage.py migrate

# Run tests
pytest
```

## Style Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

```python
# Good
def process_text(input_text, language_code):
    """
    Process input text for translation.

    Args:
        input_text (str): The text to process
        language_code (str): Language code (e.g., 'hi', 'en')

    Returns:
        str: Processed text
    """
    cleaned_text = input_text.strip()
    return cleaned_text

# Use descriptive variable names
user_input = request.POST.get('sen')
detected_language = detect_language(user_input)

# Add type hints where possible
def translate_text(text: str, target_lang: str = 'en') -> str:
    pass
```

### Git Commit Messages

```
Add: New feature description
Fix: Bug description
Update: Changed feature description
Remove: Removed feature description
Docs: Documentation changes
Test: Test-related changes
Refactor: Code refactoring
```

Examples:

```bash
git commit -m "Add: Support for Punjabi language"
git commit -m "Fix: Speech recognition error on mobile"
git commit -m "Update: Improve translation accuracy for Tamil"
git commit -m "Docs: Add installation guide for Windows"
```

## Adding New Languages

To add support for a new language:

1. **Update `translation_service.py`**:

```python
SUPPORTED_LANGUAGES = {
    'ur': {  # Urdu example
        'name': 'Urdu',
        'code': 'ur',
        'speech_code': 'ur-PK',
        'native_name': 'اردو',
        'flag': '🇵🇰',
        'active': True
    }
}
```

2. **Update frontend placeholders** in `templates/animation.html`:

```javascript
const placeholderMap = {
  ur: "اپنا پیغام ٹائپ کریں...",
  // ...
};
```

3. **Add speech recognition mapping**:

```javascript
const languageMap = {
  ur: "ur-PK",
  // ...
};
```

4. **Add TTS mapping**:

```javascript
const ttsLanguageMap = {
  ur: "ur-PK",
  // ...
};
```

5. **Test thoroughly**:

```bash
pytest tests/test_multilingual.py
```

6. **Update documentation** in README.md

## Adding ISL Videos

To add new ISL gesture videos:

1. **Video Requirements**:

   - Format: MP4
   - Resolution: 720x480 or higher
   - Duration: 1-3 seconds per gesture
   - Background: Transparent or consistent
   - File naming: `{word}.mp4` (lowercase)

2. **Place video** in `static/` directory

3. **Update word mapping** if needed in `views.py`

4. **Test playback** in the application

## Testing

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_integration.py

# With coverage
pytest --cov=A2SL tests/

# Verbose output
pytest -v
```

### Writing Tests

```python
import pytest
from django.test import Client

def test_home_page():
    """Test home page loads correctly."""
    client = Client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'Sanket Bhasha' in str(response.content)
```

## Documentation

- Update README.md for user-facing changes
- Update inline code comments for complex logic
- Add docstrings to new functions/classes
- Update CHANGELOG.md with your changes

## Community

- Be respectful and inclusive
- Help others who are learning
- Share your knowledge and experience
- Give credit where credit is due

## Questions?

Feel free to:

- Open an issue for discussion
- Join our community discussions
- Reach out to maintainers

---

Thank you for contributing to Sanket Bhasha! 🤟

**संकेत भाषा** - Together we bridge communication gaps!
