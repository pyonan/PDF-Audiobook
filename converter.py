import PyPDF2
import pyttsx3
import os
import sys

def pdf_to_audio(pdf_path, output_file="output.mp3", speed="normal"):

    # Speed settings
    speed_map = {
        "slow": 120,
        "normal": 150,
        "fast": 200
    }

    # Fix 1: handle wrong case input like "Fast" or "NORMAL"
    speed = speed.lower().strip()
    if speed not in speed_map:
        print(f"'{speed}' is not valid. Choose slow, normal, or fast. Using normal.")
        speed = "normal"
    rate = speed_map[speed]

    # Fix 2: check if the PDF file actually exists before opening it
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' not found. Make sure the PDF is in the same folder.")
        return

    # Delete previous output if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
        print("Deleted previous output.mp3")

    # Step 1: Extract text from PDF
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)

            # Fix 3: check if PDF is password protected
            if reader.is_encrypted:
                print("Error: This PDF is password protected. Please use an unlocked PDF.")
                return

            total_pages = len(reader.pages)
            text = ""

            for i, page in enumerate(reader.pages):
                print(f"Reading page {i + 1} of {total_pages}...")
                extracted = page.extract_text()
                if extracted:
                    text += extracted + " "

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    if not text.strip():
        print("No text found in PDF. It might be a scanned image-based PDF.")
        return

    print(f"\nDone reading! Extracted {len(text)} characters.")
    print("Converting to audio, please wait...\n")

    # Step 2: Convert text to speech
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.save_to_file(text, output_file)
        engine.runAndWait()
    except Exception as e:
        print(f"Error during audio conversion: {e}")
        return

    print(f"Audio saved as: {output_file}")

    # Step 3: Auto-play the audio
    # Fix 4: handle Mac and Linux too, not just Windows
    print("Playing audio now...")
    try:
        if sys.platform == "win32":
            os.startfile(output_file)
        elif sys.platform == "darwin":
            os.system(f"open '{output_file}'")
        else:
            os.system(f"xdg-open '{output_file}'")
    except Exception as e:
        print(f"Could not auto-play. Open '{output_file}' manually.")


# --- Run it ---
sp = input("Enter speed (slow / normal / fast): ")
pdf_to_audio("sample.pdf", speed=sp)