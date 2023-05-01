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

## Update on Iteration 3

* In this iteration, a new feature has been added to the project that allows users to translate a given text into multiple speech outputs with different languages. This means that the user can choose from a variety of languages and have the translated text converted to speech in the language of their choice. This new feature enhances the usability of the project by providing a way for users to consume the translated text without having to read it.

* As for the project's current progress, it has been deployed locally for testing and development purposes.This means that the project is being run on a local machine or network, rather than being hosted on a remote server.

* At present, the project does not utilize WebRTC (Web Real-Time Communication) as a means of communication. However, it is scheduled to be integrated soon. WebRTC is a technology that enables real-time communication, including audio, video, and data transfer, between web browsers and mobile applications. In this project, the audio file is processed locally on the user's device, and the resulting text is presented on the Streamlit user interface.

* Once the audio is converted to text, the user has the option to translate the text into any language of their choice using the Translate package. The package supports multiple languages and can perform translations in real-time, allowing the user to quickly and easily understand the content of the audio file.

#### To achieve this goal, we used following packages:

* Streamlit: It is a web front-end interface that provides an easy-to-use and intuitive user interface to interact with the project.

* Pywhisper: It is an API that is used for audio data augmentation and to load the Pywhisper model to convert audio to text. This API provides various features like noise reduction, speed adjustment, and pitch adjustment to enhance the quality of the audio file.

* Pyaudio: This package is used to record audio in the form of frames using the microphone. Pyaudio records the audio and saves it in a buffer.

* Translate: This package is used to translate text from one language to another. The user can select the source and target language, and the package will perform the translation.

* Gtts: This is an API that is used for converting text to audio. The user can select the desired language and the package will generate the corresponding audio file.

* Tempfile: NamedTemporaryFile is used to create temporary .mp3 files which provide automatic cleanup and can be used as context managers. The temporary files are used to store the audio files generated by Gtts.

* Os: This package is used in the process of deleting temporary files created. Once the audio files are generated, they are no longer required, and therefore, they are deleted to free up storage space.

## Iteration 4
* Deploy the project on the cloud provider's platform and initiate system testing.
* Test the working condition of the system and check for any issues or errors.
* If issues are found, analyze the root cause and take necessary actions to resolve them.

## Update on Iteration 4

### Client-Server Architecture:
* The client-server architecture has been implemented in the project where the client runs on one laptop, and it contains two servers where transcribing speech to text is on one server, and converting text to voice of prescribed language is on the other server. 
* This architecture separates the two critical tasks into separate servers, and it enables efficient use of resources. 
* The architecture also enables scalability and allows for easy deployment on remote servers.

### New feature:
* The new feature added to the project enables users to translate a given text into multiple speech outputs with different languages. This means that users can choose from a variety of languages and have the translated text converted to speech in the language of their choice.
* This new feature enhances the usability of the project by providing a way for users to consume the translated text without having to read it. 
* The Translate package supports multiple languages and can perform translations in real-time, allowing the user to quickly and easily understand the content of the audio file.

* The audio file is processed locally on the user's device, and the resulting text is presented on the Streamlit user interface. This means that the processing of the audio file is performed on the client-side, which reduces the load on the servers. 
* Once the audio is converted to text, the user has the option to translate the text into any language of their choice using the Translate package.

### Final Implementation 
* Our code has been updated to include the WebRTC protocol, which enables real-time voice-to-text conversion using the DeepSearch model. This update allows the application to seamlessly convert spoken words to text in real-time, resulting in a more efficient and user-friendly experience.

## Step by step implementation

* Install Anaconda on your computer by downloading and running the installation file from the official Anaconda website. 
* Create a new virtual environment using the packages described in the "requirements.txt" file. To create a new virtual environment, open a terminal or command prompt and run the following command: “conda create --name myenv --file requirements.txt”, Replace "myenv" with the name you want to give your virtual environment.
* Place all the required files, such as "streamlit_app.py" and any audio files needed for the transcribing function, into the virtual environment folder you just created. This will help ensure that your code and data are kept separate from other projects and packages on your system.
* Activate the virtual environment by running the following command: “codeconda activate myenv”, This will activate the virtual environment you just created, allowing you to use the Python packages and environment settings specific to that environment. The python code and the audio file should be placed in the "sample_ccn" virtual environment. Make sure that streamlit_app.py and path_of_file.wav under same folder
On my laptop the path is C:/ProgramData/Anaconda3/envs/sample_ccn

* Navigate to the folder where your code and required packages exist. Once in the correct directory, run the command "streamlit run streamlit_app.py" to start the application. This will launch a local server and open the application in your default web browser.
* If any errors occur, check that all required dependencies are installed by running the following command: “pip install -r requirements.txt”

## Iteration 5 
* Prepare the documentation for the project.
* Create the presentation and deliver the final project.
