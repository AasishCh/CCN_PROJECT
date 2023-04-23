from flask import Flask, request
from gtts import gTTS
from tempfile import NamedTemporaryFile
import os

app = Flask(__name__)

@app.route('/texttovoice', methods=['POST'])
def text_to_voice():
    try:
        if 'text' not in request.form:
            return "Error: No text provided"
        
        text = request.form['text']
        lang = request.form.get('lang', 'en')
        
        tts = gTTS(text=text, lang=lang)
        with NamedTemporaryFile(delete=False, suffix='.mp3') as f:
            file_name = f.name
            tts.save(file_name)
        
        with open(file_name, 'rb') as f:
            audio_data = f.read()

        os.unlink(file_name)
        
        return audio_data
        
    except KeyboardInterrupt:
        return "Error: Interrupted by user"
    except Exception as e:
        print("Error:", e)
        return "Error: Internal server error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
