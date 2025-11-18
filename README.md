# 🎥 YouTube Video Summarizer

A powerful, AI-driven web application that turns long YouTube videos into concise, readable summaries. Built with **Streamlit** and **Hugging Face Transformers**.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

https://github.com/ramaabdelgadir/youtube-summarizer/assets/Screenshot.png

## 📖 About The Project

Watching long educational videos or tech talks can be time-consuming. This app helps you learn faster by:
1. **Extracting** the transcript from a YouTube video.
2. **Splitting** the text into efficient chunks (handling token limits).
3. **Generating** a coherent summary using the **BART Large CNN** model.

You can use the **Streamlit web app** for a friendly UI or the **command-line version** if you prefer running directly from the terminal.

## ✨ Key Features

* **Smart Extraction:** Supports standard URLs, short links (`youtu.be`), and embeds.
* **Long Video Support:** Uses intelligent text chunking to process videos of any length.
* **Map-Reduce Summarization:** Hierarchical processing ensures no details are lost.
* **Clean UI:** A responsive interface built with Streamlit.
* **Transparency:** View the full transcript alongside the summary for verification.

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io/) - Frontend UI
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) - NLP Pipeline (`facebook/bart-large-cnn`)
* [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) - Data extraction

## 📂 Project Structure

```text
YouTube-Summarizer/
├── streamlit_app.py       # Main Streamlit web interface
├── app.py                 # Command-line (CLI) version
├── src/
│   ├── extract_transcript.py  # Logic for parsing URLs + fetching transcripts
│   ├── summarize.py           # AI model + summarization pipeline
│   └── utils.py               # Helper functions (e.g., chunking)
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```
## 🛠 Installation & Setup

To run this project locally, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/ramaabdelgadir/youtube-summarizer.git](https://github.com/ramaabdelgadir/youtube-summarizer.git)
cd youtube-summarizer
```
Here is the complete Markdown block ready for you to copy and paste.

Markdown

## 🛠 Installation & Setup

To run this project locally, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/youtube-summarizer.git](https://github.com/yourusername/youtube-summarizer.git)
cd youtube-summarizer
```
**2. Create a Virtual Environment (Recommended)**
```
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
**3. Install Dependencies**
```
pip install -r requirements.txt
```

## ▶️ How to Use

**Option 1: Streamlit Web App (Recommended)
Launch the interactive web interface:**
```
streamlit run streamlit_app.py
```
- Then open your browser to the local URL shown (usually http://localhost:8501).

**Option 2: Command-Line Interface (CLI)
Run the script directly in your terminal:**

```
python app.py
```
- Follow the on-screen prompt to paste your YouTube URL.

## ⚠️ Limitations

- Captions Required: The video must have English captions (manual or auto-generated) available on YouTube.
- Hardware: The BART model is large. On a machine without a GPU, processing long videos may take 1-2 minutes.
- Accuracy: Auto-generated captions from YouTube may contain phonetic errors.

## 🎥 Demo

Check out the app in action:

https://github.com/ramaabdelgadir/youtube-summarizer/assets/Demo.mp4

---
*👤 Author
Rama Abdelgadir*\
*AI Developer | Passionate about practical, user-friendly AI tools.*