# PDF to Audiobook Converter

A Python project that converts text from a PDF file into an audio file (.mp3). Just drop in a PDF, run the script, and listen!

---

## Features

- Extracts text from PDF files page by page
- Converts text to speech and saves it as an `.mp3` file
- Auto-plays the audio after conversion
- Choose reading speed: slow, normal, or fast
- Shows live progress while reading (Page 1 of 10...)
- Automatically deletes the previous output before creating a new one
- Handles common errors gracefully (missing file, encrypted PDF, scanned PDFs)
- Works on Windows, Mac, and Linux

---

## Demo

```
Enter speed (slow / normal / fast): normal
Reading page 1 of 5...
Reading page 2 of 5...
Reading page 3 of 5...
Reading page 4 of 5...
Reading page 5 of 5...

Done reading! Extracted 18423 characters.
Converting to audio, please wait...

Audio saved as: output.mp3
Playing audio now...
```

---

## Requirements

- Python 3.7+
- pip (comes with Python)

### Libraries used

| Library | Purpose |
|--------|---------|
| `PyPDF2` | Extracts text from PDF files |
| `pyttsx3` | Converts text to speech (works offline) |
| `os` | File management and auto-play (built-in) |
| `sys` | Detects operating system (built-in) |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/pyonan/PDF-Audiobook.git
cd PDF-Audiobook
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Place your PDF file in the project folder
2. Rename it to `sample.pdf` (or change the filename in the script)
3. Run the script:

```bash
python converter.py
```

4. When prompted, type your preferred speed:

```
Enter speed (slow / normal / fast): fast
```

5. The audio will be saved as `output.mp3` and will auto-play when done!

---

## Changing the PDF file

By default the script reads `sample.pdf`. To use a different file, open `converter.py` and change the last line:

```python
# Change "sample.pdf" to your file name
pdf_to_audio("sample.pdf", speed=sp)
```

For example:
```python
pdf_to_audio("mybook.pdf", speed=sp)
```

---

## Speed options

| Option | Words per minute |
|--------|----------------|
| `slow` | 120 wpm |
| `normal` | 150 wpm |
| `fast` | 200 wpm |

---

## Known Limitations

- **Scanned PDFs** — PDFs that are images of text (not real text) will not work. The script will let you know if no text was found. You would need OCR (like `pytesseract`) to handle those.
- **Password protected PDFs** — Encrypted PDFs are not supported. Please unlock the PDF first.
- **Complex formatting** — Tables, columns, and heavy formatting in PDFs may cause the extracted text to read slightly out of order.

---

## Project Structure

```
PDF-Audiobook/
├── converter.py        # Main script
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── .gitignore          # Files excluded from Git
└── sample.pdf          # Your input PDF (not included)
```

---

## .gitignore

The following are excluded from the repository:

```
venv/
output.mp3
sample.pdf
__pycache__/
*.pyc
```

---

## Future Improvements

- [ ] Support for choosing output file name
- [ ] GUI interface using Tkinter
- [ ] OCR support for scanned PDFs using pytesseract
- [ ] Multiple voice options
- [ ] Chapter detection and splitting into multiple audio files

---

## Author

**pyonan**
GitHub: [github.com/pyonan](https://github.com/pyonan)
