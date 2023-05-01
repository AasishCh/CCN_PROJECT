# CCN_PROJECT - Group 9
# Team Members
* Aasish Chunduri
* Yaswanth Mareedu
* Govind Rahul Mathamsetti
* Manoj Kumar Reddy Janapala
# INTRODUCTION (Voice-to-Text)



# Final Implementation 
* Our code has been updated to include the WebRTC protocol, which enables real-time voice-to-text conversion using the DeepSpeech model. This update allows the application to seamlessly convert spoken words to text in real-time, resulting in a more efficient and user-friendly experience.

## Step by step implementation

Step1: Install Anaconda
  * Install Anaconda on your computer by downloading and running the installation file from the official Anaconda website.
  
Step2: Clone the repository
  command: git clone https://github.com/AasishCh/CCN_PROJECT
  
Step3: Create Virtual Environment and Install Packages
  * Create a new virtual environment and install all the packages and libraries described in the "requirements.txt" file.
  commands:
    1. conda create --name ccn_project
    2. pip install pywhisper==1.0.6
    3. pip install streamlit==1.20.0
    4. pip install gtts==2.3.1
    5. pip install pyaudio==0.2.13
    6. pip install numpy==1.24.2
    7. pip installtranslate==3.6.1
    8. pip install pydub==0.25.1
    9. pip install deepspeech==0.9.3
    10. pip install wave==0.0.2

Step4: Place all the files in appropriate folders
  * Activate the virtual environment by running the following command: “codeconda activate myenv”, This will activate the virtual environment you just created, allowing you to use the Python packages and environment settings specific to that environment. The python code and the audio file should be placed in the "ccn_project" virtual environment(Where the anaconda is installed). Make sure that streamlit_app.py and path_of_file.wav under same folder. On my laptop the path is C:/ProgramData/Anaconda3/envs/sample_ccn.

Step5:
  * Navigate to the folder where your code and required packages exist. Once in the correct directory, run the command "streamlit run streamlit_app.py" to start the application. This will launch a local server and open the application in your default web browser. 
  commands:
    streamlit run streamlit_app.py
Step6:
  * If any errors occur, check that all required dependencies are installed by running the following command: “pip install -r requirements.txt”
  * We have used SERVEO which is used to expose the local servers to the internet. It used SSH to create a secure tunnel between the users local machine and a publicly accessible server. 
  * To use Serveo to make your local Streamlit web application public and accessible to all users, follow these steps:
  

Make sure your Streamlit web application is running locally on your machine and is accessible through your web browser at http://localhost:8501.<br>
Open a terminal or command prompt and enter the following command, replacing example with a unique subdomain name <br>
Commands:
**ssh -R voicetotext.serveo.net:80:localhost:8501 serveo.net** <br>
Press Enter to run the command. Serveo will establish an SSH tunnel to your local machine and generate a public URL that you can use to access your Streamlit web application.<br>
Copy the public URL provided by Serveo and share it with your users. They can open the URL in their web browser to access your Streamlit web application.

## System Requirements

CPU: A modern multi-core processor capable of running deep learning models efficiently. An Intel Core i5 or equivalent is recommended.
Memory: A minimum of 8GB RAM is recommended for smooth operation. For better performance, 16GB or more is preferred.
Disk Space: At least 2GB of free disk space for storing the deep learning models, libraries, and other project files.
Operating System: Windows, macOS, or Linux. 

