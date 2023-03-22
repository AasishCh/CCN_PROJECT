import pywhisper

import pyaudio
import wave
 

print('Enter the input type:')
print('\t1. Microphone')
print('\t2. Input audio file')
n = int(input('Enter 1 or 2:'))

if n==1 or n==2:
    if n==1:
        # Record in chunks of 1024 samples
        chunk = 1024 
        
        # 16 bits per sample
        sample_format = pyaudio.paInt16 
        chanels = 2
        
        # Record at 44400 samples per second
        smpl_rt = 44400 
        seconds = 4
        filename = "path_of_file.wav"
        
        # Create an interface to PortAudio
        pa = pyaudio.PyAudio() 
        
        stream = pa.open(format=sample_format, channels=chanels,
                        rate=smpl_rt, input=True,
                        frames_per_buffer=chunk)
        
        print('Recording...')
        
        # Initialize array that be used for storing frames
        frames = [] 
        
        # Store data in chunks for 8 seconds
        #for i in range(0, int(smpl_rt / chunk * seconds)):
        while True:
            try:
                data = stream.read(chunk)
                frames.append(data)
            except KeyboardInterrupt:
                break

        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        
        # Terminate - PortAudio interface
        pa.terminate()
        
        print('Done !!! ')
        
        # Save the recorded data in a .wav format
        sf = wave.open(filename, 'wb')
        sf.setnchannels(chanels)
        sf.setsampwidth(pa.get_sample_size(sample_format))
        sf.setframerate(smpl_rt)
        sf.writeframes(b''.join(frames))
        sf.close()

        model = pywhisper.load_model("base")

        audio = pywhisper.load_audio("path_of_file.wav")
        audio = pywhisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = pywhisper.log_mel_spectrogram(audio).to(model.device)

        # detect the spoken language
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = pywhisper.DecodingOptions(fp16 = False)
        result = pywhisper.decode(model, mel, options)

        # print the recognized text
        print(result.text)

    if n==2:
        model = pywhisper.load_model("base")
        # load audio and pad/trim it to fit 30 seconds
        audio = pywhisper.load_audio("sample_audio.wav")
        audio = pywhisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = pywhisper.log_mel_spectrogram(audio).to(model.device)

        # detect the spoken language
        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = pywhisper.DecodingOptions(fp16 = False)
        result = pywhisper.decode(model, mel, options)

        # print the recognized text
        print(result.text)
else:
    print('Wrong Input Entered')

