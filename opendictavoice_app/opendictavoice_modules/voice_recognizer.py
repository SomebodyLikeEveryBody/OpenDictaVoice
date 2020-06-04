import opendictavoice_modules.audio_manager

import speech_recognition

class Voice_Recognizer:

    #by default the language is french
    def __init__(self, p_language='fr-FR'):
        self._language = p_language

    #input: p_wavpath is the path to a .wav file
    #output: the recognized text
    #this function is private and does not delete the wav file
    def get_text_from_wav(self, p_wavpath):
        ret_str = None

        try:
            recognizer = speech_recognition.Recognizer()
            with speech_recognition.AudioFile(p_wavpath) as source:
                audio = recognizer.record(source)  # read the entire audio file

            # recognize speech using Google_STT --> We'll see if we continue with another STT engine
            try:
                ret_str = recognizer.recognize_google(audio, language=self._language)
            except speech_recognition.UnknownValueError:
                print("Google could not understand audio")
            except speech_recognition.RequestError as e:
                print("Google error; {0}".format(e))

        except Exception as ex:
            print(str(ex))

        return ret_str


    def set_language(self, p_language):
        self._language = p_language

    ########################
    # Attribute management #
    ########################

    @property
    def language(self):
        return self._language

    @language.setter
    def language (self, p_value):
        raise PermissionError("You need to use method [set_language()] to modify language attribute")
