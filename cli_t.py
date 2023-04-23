import socket
import sys
import streamlit as st
import pywhisper
import pyaudio
import wave
from translate import Translator
from gtts import gTTS
from tempfile import NamedTemporaryFile
import os
import requests
import pydub

def text_to_speech(text, lang='en'):
    url = "http://172.20.6.88:5000/texttovoice"
    data = {'text': text, 'lang': lang}
    r = requests.post(url, data=data)
    if r.status_code == 200:
        with open('audio.mp3', 'wb') as f:
            f.write(r.content)
        return 'audio.mp3'
    else:
        return None


url = "http://172.20.6.88:5000/transcribe"


st.title("Voice to Text Conversion")
audio = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])


if st.sidebar.button("Record Audio"):
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 
    RATE = 16000
    RECORD_SECONDS = 7
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
        WAVE_OUTPUT_FILENAME = temp_file.name

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    url = "http://172.20.6.88:5000/transcribe"

    with open(WAVE_OUTPUT_FILENAME, 'rb') as f:
        r = requests.post(url, files={'audio': f})

      # Delete the temporary file

    transcription = r.json()
    os.unlink(WAVE_OUTPUT_FILENAME)
    print("Transcription:", transcription)
    st.text(transcription['text'])

    st.session_state.text_inp = transcription['text']

if st.sidebar.button("Transcribe Audio"):
    CHANNELS = 1 
    if audio is not None:
        audio_file = pydub.AudioSegment.from_file(audio)
        print('adudio name:',audio)
        WAVE_OUTPUT_FILENAME = "temp.wav"
        st.sidebar.success("Transcribing Audio")

        url = "http://172.20.6.88:5000/transcribe"
        
        
        try:
            with NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
                WAVE_OUTPUT_FILENAME = temp_file.name

                # Convert audio file to wave object and write to temporary file
                with wave.open(temp_file, 'wb') as wave_file:
                    wave_file.setnchannels(audio_file.channels)
                    wave_file.setsampwidth(audio_file.sample_width)
                    wave_file.setframerate(audio_file.frame_rate)
                    wave_file.writeframesraw(audio_file._data)

            #print("Temporary file created:", temp_file_name)

            # Process the temporary WAV file here

        finally:
            # Ensure that the temporary file is properly closed and the handle is released
            try:
                temp_file.close()
            except:
                pass

        
        with open(WAVE_OUTPUT_FILENAME, 'rb') as f:
            r = requests.post(url, files={'audio': f})
        try:
            transcription = r.json()
            print(transcription)
            temp_file.close()
        except ValueError:
            st.sidebar.error("Error parsing server response")
            transcription = None

        if transcription:
            os.unlink(WAVE_OUTPUT_FILENAME)
            print("Transcription:", transcription)
            try:
                st.text(transcription['text'])
                st.session_state.text_inp = transcription['text']
            except:
                st.text("Internal Server Error")
                
    else:
        st.sidebar.error('Please upload audio file or record audio')

if 'text_inp' in st.session_state and st.session_state.text_inp:
    url = "http://172.20.6.88:5000/texttovoice"
    language = st.selectbox("Select language for the output speech:", [
                ("English", "en"),
                ("Spanish", "es"),
                ("French", "fr"),
                ("German", "de"),
                ("Italian", "it"),
                ("Portuguese", "pt"),
                ("Russian", "ru")
            ], format_func=lambda x: x[0])
    
    text = st.session_state.text_inp
    if text:
        st.write("Selected language:", language[0])

        translator = Translator(to_lang=language[1])
        translation = translator.translate(text)
        if st.button("Convert Text to Speech"):
            audio_file = text_to_speech(translation, lang=language[1])
            if audio_file:
                st.audio(audio_file, format="audio/mp3")
                os.unlink(audio_file)
            else:
                st.write("Error converting text to speech")
    else:
        st.write("Please enter text to convert to speech")


    


