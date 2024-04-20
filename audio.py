import assemblyai as aai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Setting up AssemblyAI API key
api_key = "your_Api_key"
aai.settings.api_key = api_key

# Function to transcribe audio file and return transcription
def transcribe_audio(file_url):
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcriber = aai.Transcriber()
    return transcriber.transcribe(file_url, config=config)

# Function to generate PDF file from transcription
# def generate_pdf(transcription, filename):
#     c = canvas.Canvas(filename, pagesize=letter)
#     text = ""
#     for utterance in transcription.utterances:
#         text += f"Speaker {utterance.speaker}: {utterance.text}\n\n"
#     c.drawString(100, 750, text)
#     c.save()
def generate_text_file(transcription, filename):
    with open(filename, "w") as file:
        for utterance in transcription.utterances:
            file.write(f"Speaker {utterance.speaker}: {utterance.text}\n\n")

    