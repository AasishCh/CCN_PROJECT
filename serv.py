from flask import Flask, request, jsonify
import pywhisper
import os
import sys



app = Flask(__name__)

def loadmodel():
    model = pywhisper.load_model("base")
    return model

model = loadmodel()

@app.route('/transcrib', methods=['POST'])
def transcribe_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file'}), 400

        audio = request.files['audio']
        audio_path = audio.filename
        audio.save(audio_path)

        transcription = model.transcribe(audio_path)
        os.remove(audio_path)
        print('output',transcription)
        return jsonify(transcription)
    
    except KeyboardInterrupt:
        return jsonify({'error': 'Interrupted by user'}), 500
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run()
