import speech_recognition
import os
import pyaudio

class Voice_Recognizer:

    #by default the language is french
    def __init__(self, p_language='fr-FR'):
        self._language = p_language

    #input: p_wavpath is the path to a .wav file
    #output: the recognized text
    #this function is private and does not delete the wav file
    def _wav_to_text(self, p_wavpath):
        ret_str = ""

        try:
            recognizer = speech_recognition.Recognizer()
            with speech_recognition.AudioFile(p_wavpath) as source:
                audio = recognizer.record(source)  # read the entire audio file

            # recognize speech using Google_STT --> We'll see if we continue with another STT engine
            try:
                ret_str = recognizer.recognize_google(audio, language=self._language)
            except speech_recognition.UnknownValueError:
                print("Google could not understand audio")
                self.play_error_sound()
            except speech_recognition.RequestError as e:
                print("Google error; {0}".format(e))

        except Exception as ex:
            print(str(ex))

        return ret_str


    def get_text_from_wav(self, p_filename):
        recognized_text = self._wav_to_text(p_filename)
        os.remove(p_filename)
        return recognized_text

    def set_language(self, p_language):
        self._language = p_language

    def play_wav(self, p_filename):
        temp__pyaudio_obj = pyaudio.PyAudio()
        wf = wave.open(p_filename, 'rb')
        stream = temp__pyaudio_obj.open(format=temp__pyaudio_obj.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

        data = wf.readframes(CHUNK)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        temp__pyaudio_obj.terminate()

    def play_error_sound(self):
        self.play_wav(self._resources_path + '/sounds/error.wav')

    ########################
    # Attribute management #
    ########################

    @property
    def language(self):
        return self._language

    @language.setter
    def language (self, p_value):
        raise PermissionError("You need to use method [set_language()] to modify language attribute")
