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
## Iteration 2
* Building the model for converting speech to text.
* Conduct initial testing of the model to evaluate its accuracy and identify areas for improvement.
* Making necessary adjustments to increase the accuracy of the model.
* Verifying the entire functionality of the model to ensure it meets the project requirements.
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
