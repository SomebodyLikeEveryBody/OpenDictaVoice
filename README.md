# OpenDictaVoice

## Description:

A voice dictation program wrote in python to do voice dictation.

## How to use:

### Step 1: Download the program

Run the shell command:
```bash
git clone https://gitlab.com/Sleb/opendictavoice.git
```

### step 2: Install dependencies

The OpenDictaVoice program uses **SpeechRecognotion** module to work, wich is available here: 
[https://pypi.org/project/SpeechRecognition/](https://pypi.org/project/SpeechRecognition/)

To install it, run the shell command:
```bash
pip install SpeechRecognition
```

Secondly, if you are using **Linux or MacOS**, it is necessary to install **portaudio** so that Python will be able to use the microphone once you allow it.
To install it, run the shell command:
```bash
sudo apt-get install portaudio
```

Thirdly, if you are using **Linux**, it is necessary to install **tkinter for python3** (which is installed by default on Windows and MacOs).
To install it, run the shell command:
```bash
sudo apt-get install python3-tk
```

And finally, OpenDictaVoice need the following modules installed to work:
- pyaudio
- keyboard
- wave
- pynput

### Step 3: run the program

Run the shell command:
```bash
python ./main.py
```

It will automatically start to record.

When you are finished, press CTRL + C.

It will print the result on screen.

Very shortly, it will be pasted in the clipboard or implement more usefull features.
