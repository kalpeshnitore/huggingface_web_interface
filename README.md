# 🚀 Hugging Face Web Interface

A web interface to interact with various Hugging Face NLP models.  


## ✨ १. Key Features / मुख्य वैशिष्ट्ये
- 🤖 **Multiple Models**: GPT-2, BERT, T5, DistilBERT
- 💬 **Text Operations**: Generation, Q&A, Summarization
- 🎨 **Simple UI**: Easy dropdown selection
- ⚡ **Fast Results**: Quick model inference
- 🔄 **Easy Extensions**: Add new models with config

## 🛠️ २. Installation / स्थापना
### System Requirements
- Python 3.8+
- pip

### Setup Steps
```bash
# Clone repository
git clone https://github.com/kalpeshnitore/huggingface-web-interface.git
cd huggingface-web-interface

# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```
Then visit `http://localhost:5000` in your browser.

## 🧩 मॉडेल्स जोडणे / Adding Models
Edit `app/models.py` to add new models:
```python
MODELS_INFO = {
    "model-name": {
        "name": "Display Name",
        "task": "model-task-type",  # text-generation, question-answering etc.
        "description": "Model description"
    }
}
```

## 🤝 योगदान / Contributing
We welcome contributions! Follow these steps:

1. 🍴 Fork the project
2. 🌿 Create your feature branch (`git checkout -b new-feature`)
3. 💾 Commit your changes (`git commit -am 'Add new feature'`)
4. 🚀 Push to the branch (`git push origin new-feature`)
5. 🔄 Create a Pull Request

### Suggested Areas for Contribution:
- 🌐 Add more language support
- 📊 Improve UI/UX
- 🧠 Add new model types
- 🐛 Fix bugs

## 📜 License / परवाना
MIT License - See [LICENSE](LICENSE) file for details.

---

### Additional Icons for Reference:
🔧 🛠️ ⚙️ 🖥️ 💻 📱 🧩 🧠 🔍 📈 🔥 🎉 💡 📚 🌈 🛡️ ⏱️ 📂 📁

```

**Key Features:**
1. **Bilingual Support**: English + Marathi (Devanagari) text
2. **Modern Icons**: Using GitHub-supported emoji icons
3. **Clear Sections**: Follows your requested structure
4. **Code Formatting**: Proper Markdown syntax for commands
5. **Badges**: Python version and framework indicators

**How to Use:**
1. Copy this entire code block
2. Replace your existing `README.md` file content
3. Customize the repository URL and other details
4. Commit and push to GitHub

The icons used are all standard GitHub-flavored Markdown emojis that will render properly on any GitHub repository. You can find more icons at [GitHub Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet).
