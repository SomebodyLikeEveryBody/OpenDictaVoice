import speech_recognition
import os

class Voice_Recognizer:

    #by default the language is french
    def __init__(self, p_audio_manager):
        self._language = 'fr-FR'
        self._audio_manager = p_audio_manager

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
                self._audio_manager.play_error_sound()
            except speech_recognition.RequestError as e:
                print("Google error; {0}".format(e))

        except Exception as ex:
            print(str(ex))

        return ret_str


    def wav_to_text(self, p_filename):
        recognized_text = self._wav_to_text(p_filename)
        os.remove(p_filename)
        return recognized_text


    def set_language(self, language):
        self._language = language

    ########################
    # Attribute management #
    ########################

    @property
    def language(self):
        return self._language
    
    @language.setter
    def language (self, p_value):
        self._language = str(p_value)

    @property
    def audio_manager(self):
        return self._audio_manager
    
    @audio_manager.setter
    def audio_manager(self, p_value):
        self._audio_manager = p_value

