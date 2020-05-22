# OpenDictaVoice

## Description:

A voice dictation program written in **python3** to do voice dictation.

## How to use:

### Step 1: Download the program

Run the shell command:
```bash
git clone https://gitlab.com/Sleb/opendictavoice.git
```

### step 2: Install dependencies


If you are using **Linux or MacOS**, it is necessary to install **portaudio** so that Python will be able to use the microphone once you allow it.
To install it, run the shell command:
```bash
sudo apt-get install portaudio
```

secondly, if you are using **Linux**, it is necessary to install **tkinter for python3** (which is installed by default on Windows and MacOs).
To install it, run the shell command:
```bash
sudo apt-get install python3-tk
```


Thirdly, OpenDictaVoice need the following modules installed to work (speechRecognition, pyaudio, keyboard, wave, pynput)

**You can install all dependancies automatically** by running the command
```bash
pip install -r ./dependencies.txt
```

But if you prefer to do it manually, just follow steps bellow:

1) The OpenDictaVoice program uses **SpeechRecognotion** module to work, wich is available here:
[https://pypi.org/project/SpeechRecognition/](https://pypi.org/project/SpeechRecognition/)

To install it, run the shell command:
```bash
pip install SpeechRecognition
```

2) Pyaudio: To install it, run the shell command: 
- pyaudio
```bash
pip install pyaudio
```

3) Keyboard: To install it, run the shell command:
- keyboard
```bash
pip install keyboard
```

4) Wave: To install it, run the shell command:
- wave
```bash
pip install wave
```

5) Pynpu: To install it, run the shell command:
- pynput
```bash
pip install pynput
```

### Step 3: run the program

Run the shell command:
```bash
python3 ./main.py
```

It will open a window with low opacity that is always in the foreground.


Then, put the focus on the element you want to write in (notepad or gedit for example), and when you want to speak, hold **CTRL + SHIFT** keys to launch the record.


When you release the CTRL + SHIFT keys, it will analyse the recorded sound and write the text.

