import streamlit as st
from audio import transcribe_audio, generate_text_file

def display_transcription(transcription):
    for utterance in transcription.utterances:
        st.write(f"Speaker {utterance.speaker}: {utterance.text}")

def main():
    st.title("Audio Transcription App")

    # File upload
    file = st.file_uploader("Upload an audio file (.mp3)", type=["mp3"])

    if file is not None:
        st.write("Transcription:")
        transcript = transcribe_audio(file)
        display_transcription(transcript)

        # Download PDF button
        # if st.button("Download Transcription as PDF"):
        #     filename = "transcription.pdf"
        #     generate_pdf(transcript, filename)
        #     with open(filename, "rb") as file:
        #         btn = st.download_button(
        #             label="Click to download",
        #             data=file,
        #             file_name=filename,
        #             mime="application/pdf"
        #             )
        #         st.success(f"Transcription downloaded as {filename}")
        if  st.button("Download Transcription as Text"):
            filename = "transcription.txt"
            generate_text_file(transcript, filename)
            with open(filename, "rb") as file:
                btn = st.download_button(
                    label="Click to download",
                    data=file,
                    file_name=filename,
                    mime="text/plain"
                )
            st.success(f"Transcription downloaded as {filename}")

if __name__ == "__main__":
    main()
