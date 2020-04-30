import speech_recognition
import os
import opendictavoice_modules.recorder
import opendictavoice_modules.GUI
import threading

WAV_FILENAME = './recorded.wav'

def recognize_wav(wavpath):
    ret_str = ""

    try:
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(wavpath) as source:
            audio = recognizer.record(source)  # read the entire audio file

        # recognize speech using Google_STT --> We'll see if we continue with another STT engine
        try:
            ret_str = format_recognized_text(recognizer.recognize_google(audio, language='fr-FR'))
        except speech_recognition.UnknownValueError:
            print("Google could not understand audio")
        except speech_recognition.RequestError as e:
            print("Google error; {0}".format(e))

    except Exception as ex:
        print(str(ex))

    return ret_str


def format_recognized_text(p_str):
    ret_str = p_str
#   ret_str = ret_str.replace('retour à la ligne', '\n')
#   ret_str = ret_str.replace('virgule', ',')

    return ret_str

def test_record():
    print('recording')

def test_stop_record():
    print('stopped recording')

def launch_record_in_thread(p_recorder):
    thread_record = threading.Thread(target=p_recorder.start_record_N_save, args=(WAV_FILENAME,))
    thread_record.start()

def analyse_wav_to_get_text(p_filename):
    recognized_text = recognize_wav(p_filename)
    print(recognized_text)
    os.remove(p_filename)

def main():
    recorder = opendictavoice_modules.recorder.Recorder()
    gui = opendictavoice_modules.GUI.builded_GUI()

    gui.rec_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), launch_record_in_thread(recorder)])
    gui.stop_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), recorder.stop_record(), analyse_wav_to_get_text(WAV_FILENAME)])
    gui.launch()

if __name__ == "__main__":
    main()
