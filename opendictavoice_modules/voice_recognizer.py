import speech_recognition
import pyperclip
import os

class Voice_Recognizer:
    def __init__(self):
        self.pouet = 'prout'

    def wav_to_text(self, p_wavpath):
        ret_str = ""

        try:
            recognizer = speech_recognition.Recognizer()
            with speech_recognition.AudioFile(p_wavpath) as source:
                audio = recognizer.record(source)  # read the entire audio file

            # recognize speech using Google_STT --> We'll see if we continue with another STT engine
            try:
                ret_str = self.format_recognized_text(recognizer.recognize_google(audio, language='fr-FR'))
            except speech_recognition.UnknownValueError:
                print("Google could not understand audio")
            except speech_recognition.RequestError as e:
                print("Google error; {0}".format(e))

        except Exception as ex:
            print(str(ex))

        return ret_str


    def format_recognized_text(self, p_str):
        ret_str = p_str
    #   ret_str = ret_str.replace('retour à la ligne', '\n')
    #   ret_str = ret_str.replace('virgule', ',')

        return ret_str

    def wav_to_formated_text(self, p_filename):
        recognized_text = self.wav_to_text(p_filename)
        print(recognized_text)
        pyperclip.copy(recognized_text)
        os.remove(p_filename)
