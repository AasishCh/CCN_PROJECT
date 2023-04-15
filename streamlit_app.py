import streamlit as st
import pywhisper
import pyaudio
import wave
from translate import Translator
from gtts import gTTS
from tempfile import NamedTemporaryFile
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text, lang=lang)
    with NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        file_name = f.name
        tts.save(file_name)
    return file_name

st.title("Voice to Text Conversion")
audio = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a"])

def loadmodel():
    model = pywhisper.load_model("base")
    return model

if st.sidebar.button("Load Pywhisper Model"):
    model = loadmodel()
    st.sidebar.success("PyWhisper Model Load Completed Successfully")

if st.sidebar.button("Record Audio"):
    model = loadmodel()
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

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    st.sidebar.success("Audio Recording Completed")
    audio = pywhisper.load_audio("output.wav")
    audio = pywhisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = pywhisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    st.text("Transcription Completed")
    st.text(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = pywhisper.DecodingOptions(fp16 = False)
    result = pywhisper.decode(model, mel, options)


    
    st.text(result.text)

    st.session_state.text_inp = result.text

if st.sidebar.button("Transcribe Audio"):
    if audio is not None:
        model = loadmodel()
        st.sidebar.success("Transcribing Audio")
        try:
            transcribe = model.transcribe(audio.name)
        except:
            st.sidebar.error("Please record audio first")

        st.sidebar.success("Transcription Completed")
        st.text(transcribe["text"])
        st.session_state.text_inp = transcribe["text"]
    else:
        st.sidebar.error('Please upload audio file or record audio')

if 'text_inp' in st.session_state and st.session_state.text_inp:
    language = st.selectbox("Select language for the output speech:", [
                ("English", "en"),
                ("Spanish", "es"),
                ("French", "fr"),
                ("German", "de"),
                ("Italian", "it"),
                ("Portuguese", "pt"),
                ("Russian", "ru")
            ], format_func=lambda x: x[0])

    st.write("Selected language:", language[0])

    translator = Translator(to_lang=language[1])
    translation = translator.translate(st.session_state.text_inp)

    if st.button("Convert Text to Speech"):
        audio_file = text_to_speech(translation, lang=language[1])
        st.text(st.session_state.text_inp)
        st.audio(audio_file, format="audio/mp3")
        os.unlink(audio_file)
