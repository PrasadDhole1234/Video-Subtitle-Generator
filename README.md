# Video Subtitle Generator (English + Hindi)

This project automatically generates English and Hindi subtitles from `.mp4` videos using [faster-whisper](https://github.com/guillaumekln/faster-whisper) for transcription and [Google Translate](https://pypi.org/project/googletrans/) for translation.

---

## 📌 Features

* Extracts audio from `.mp4` videos using **ffmpeg**
* Transcribes audio with **faster-whisper**
* Detects spoken language automatically
* Generates **English subtitles (SRT)**
* Translates text to **Hindi** and generates Hindi SRT files
* Stores subtitles in separate folders for better organization
* Retry mechanism for translation timeouts

---

## 🛠️ Tech Stack

* **Python 3.9+**
* [faster-whisper](https://github.com/guillaumekln/faster-whisper)
* [ffmpeg](https://ffmpeg.org/)
* [googletrans](https://pypi.org/project/googletrans/)
* Built-in modules: `os`, `math`, `subprocess`, `time`

---

## 📂 Project Structure

```
Video-Subtitle-Generator/
│── input_folder/            # Place input .mp4 videos here
│── output/
│   ├── english_subtitles/   # Generated English .srt files
│   └── hindi_subtitles/     # Generated Hindi .srt files
│── subtitle_generator.py    # Main script
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
```

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/video-subtitle-generator.git
cd video-subtitle-generator
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\.venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install **ffmpeg** (required for audio extraction):

* Ubuntu:

```bash
sudo apt update && sudo apt install ffmpeg
```

* macOS (Homebrew):

```bash
brew install ffmpeg
```

* Windows: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to PATH.

---

## ▶️ Usage

1. Place `.mp4` video files into `input_folder/`
2. Run the script:

```bash
python subtitle_generator.py
```

3. Subtitles will be generated in:

   * `output/english_subtitles/`
   * `output/hindi_subtitles/`

---

## 📜 Example Output

For a video `interview.mp4`, you will get:

```
output/english_subtitles/interview_en_subtitles.srt
output/hindi_subtitles/interview_hi_subtitles.srt
```

---

## ❗ Troubleshooting

* **`ffmpeg not found`** → Install ffmpeg and ensure it’s added to PATH
* **Poor transcription** → Try a larger whisper model (`medium`, `large`)
* **Translation timeout** → Script retries automatically, but unstable networks may cause failures
* **Wrong timestamps** → Ensure correct frame rate; extracting audio separately helps

---

## 📌 Roadmap

* Add subtitle burning into `.mp4` (hardcoded subtitles)
* Support for multiple languages beyond Hindi
* Batch translation with faster APIs (DeepL, Google Cloud Translate)
* GUI/Web interface for non-technical users

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch (`feature-new-lang`)
3. Commit your changes
4. Open a Pull Request

---
