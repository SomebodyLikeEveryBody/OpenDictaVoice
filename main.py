import speech_recognition
import os

def recognize(wavpath):
    try:
        # Recognize audio
        r = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(wavpath) as source:
            audio = r.record(source)  # read the entire audio file

    except Exception as ex:
        print(str(ex))

    recognized_text = ''

    # recognize speech using Google_STT --> We'll see if we continue with another STT engine
    try:
        recognized_text = r.recognize_google(audio, language='fr-FR')
        print("Google thinks you said:\n\n" + format_recognized_text(recognized_text) + "\n\n")
    except speech_recognition.UnknownValueError:
        print("Google could not understand audio")
    except speech_recognition.RequestError as e:
        print("Google error; {0}".format(e))
    return recognized_text 

def format_recognized_text(p_str):
#   With Google STT engine:
#   "à la ligne" --> \n
#   "virgule" --> ,

    ret_str = p_str
#    ret_str = ret_str.replace('retour à la ligne', '\n')
#    ret_str = ret_str.replace('virgule', ',')

    return ret_str

if __name__ == "__main__":
    os.system('arecord -r 44100 file.wav')
    recognize('./file.wav')
    os.remove('./file.wav')
