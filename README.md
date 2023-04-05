# CCN_PROJECT - Group 9
# Team Members
* Aasish Chunduri
* Yaswanth Mareedu
* Govind Rahul Mathamsetti
* Manoj Kumar Reddy Janapala
# INTRODUCTION (Voice-to-Text)
Voice-to-text conversion is a technology that allows a computer to transcribe human speech into written text. The goal of a voice-to-text conversion project is to develop a system that can accurately transcribe spoken language into text in real-time. This technology has many applications, including accessibility for people with disabilities, and automated speech recognition for customer service and other applications. In a voice-to-text conversion project, the system typically employs a combination of machine learning algorithms and signal processing techniques to analyze speech and transcribe it into text. 
## Methodology:
### 1. Speech Signal Capture
The user will use the system's microphone to capture the speech signal. The microphone will be used to take the input in .mp3 format by the web application.
### 2. Speech-to-Text Conversion:
Once the speech signal is received, the web application will send the input to the model via WebRTC, and the model will use natural language processing (NLP) techniques to transcribe the speech to text. The NLP engine will use a combination of acoustic and language models to analyze the speech and convert it to text.
### 3. Output and User Interface:
The final output will be sent to the web application from the cloud model via WebRTC. The user interface will be designed to be user-friendly and intuitive, with features such as recording the speech and displaying the speech in the text format.

We are taking the following github repository as reference to implement our project.<br />
Link: https://github.com/fcakyon/pywhisper

# Architecture
We are planning to use client-server architecture, with a Flask server and front end Web application as the client.
# Project Plan based on two weeks iteration
## Iteration 1
* Gather requirements for the project.
* Determine the appropriate technologies, packages, programming languages, and deployment procedures that will be utilized in the project, and ensure that all team  members have a clear understanding of their roles and responsibilities.
* Familiarize with the technologies and the concepts using, to gain a better understanding of their functionalities and potential challenges.
* Setting up the development environment and installing all necessary software, including any libraries or frameworks required for the project, to ensure smooth implementation and testing.
## Update on Iteration 1

### Technologies:

* We have explored several technologies to implement our voice-to-text conversion model. One of the most important aspects of the project is choosing the appropriate API for converting speech to text. We considered several options such as the Google Cloud Speech-to-Text API and SpeechRecognition, but we have decided to use the pywhisper API. This API is used to convert speech to text and also includes a pre-trained model for faster implementation.

* To support real-time communication between the web application and the model, we plan to use WebRTC technology. This will allow for efficient and low-latency transmission of audio data. The model will be deployed in the cloud using cloud providers such as Heroku or AWS, which will provide scalability, reliability, and security.

* We also explored using Django to build APIs that can receive and respond to requests from a WebRTC application. This API can be used to connect to the machine learning model for voice-to-text conversion.

### Packages: 

The packages that we are planning to use to build the machine learning model include pywhisper, pyaudio, and wave.

* pywhisper is used for loading the pre-trained model and converting audio to text. It is a wrapper for the TensorFlow library, which is a popular library for implementing neural networks and deep learning models.

* pyaudio is used for recording the audio from the microphone. It provides a simple interface for capturing audio from the microphone, which can then be saved as a wave file using the wave package.

* wave is used to save the audio file after recording through the microphone. It provides a simple interface for working with wave files, including reading and writing wave files.

### recording_audio.py

The current version of our model.py file implements the basic functionality of the model. It takes input from the microphone and saves the audio file to the system, which can then be used as input to the model for converting it into text.

We are planning to implement two ways of reading the input:

1.	Input as a file from the system, which can be useful for testing or for providing pre-recorded audio input to the model.
2.	Input from the microphone, which will be the primary mode of input for the model in real-time use.


In summary, we have researched and chosen appropriate technologies, APIs, packages, and programming languages for our project. We have also set up the development environment and installed all necessary software, including libraries and frameworks required for the project. Our current implementation includes the basic functionality of the model, and we have plans to implement additional features such as reading input from a file and real-time conversion of speech to text using the microphone.


## Iteration 2
* Building the model for converting speech to text.
* Conduct initial testing of the model to evaluate its accuracy and identify areas for improvement.
* Making necessary adjustments to increase the accuracy of the model.
* Verifying the entire functionality of the model to ensure it meets the project requirements.

## Update on Iteration 2

### Functionality-Code:
* The code is a Python script that uses the PyAudio library to record audio from a microphone and save it as a WAV file. It also uses the Wave module to handle WAV file read/write operations.

#### The main points describing how the script works:

* The script imports necessary libraries such as PyAudio and Wave, which are used for audio input/output operations.

* The script sets up various variables to configure the audio recording, including the chunk size, sample format, number of channels, sample rate, and recording duration.

* An instance of the PyAudio class is created, which provides access to the PortAudio library, allowing the script to interface with the microphone.

* The script opens an audio stream with the specified configuration, using the PyAudio open() method.

* The script begins recording audio by reading data from the audio stream in chunks and appending it to an array of frames. The recording can be stopped at any time by interrupting the script with a KeyboardInterrupt exception.

* After the recording is complete, the script closes the audio stream and terminates the PyAudio interface.

* Finally, the script uses the Wave module to create a new WAV file and write the recorded audio data to it.The script then loads a pre-trained PyWhisper model and uses it to detect the language of the recorded audio, create a log-Mel spectrogram, and decode the audio to generate recognized text.

* Also Gathered a set of audio files with various types of speech, accents, and background noise to use for testing.

* When tested the model with various audio files, the output matched the spoken words and phrases in each file, even if the files contain different speakers, accents, or background noise. The model able to transcribe a wide range of audio files with consistent accuracy.

## Iteration 3
* Set up the Webrtc environment.
* Create a user interface that is used to interact with the Webrtc.
* Integrate the server model (NLP engine) with the application via Webrtc locally.
* Check the entire functionality of the system and if there are any issues debug and eliminate them to ensure smooth functioning of the application.
## Iteration 4
* Deploy the project on the cloud provider's platform and initiate system testing.
* Test the working condition of the system and check for any issues or errors.
* If issues are found, analyze the root cause and take necessary actions to resolve them.
## Iteration 5
* Prepare the documentation for the project.
* Create the presentation and deliver the final project.
