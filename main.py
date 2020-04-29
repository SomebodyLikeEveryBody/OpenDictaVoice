import speech_recognition
import os
import opendictavoice_modules.recorder
import opendictavoice_modules.GUI
import threading

WAV_FILENAME = './recorded.wav'

def recognize_wav(wavpath):
    try:
        # Recognize audio
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(wavpath) as source:
            audio = recognizer.record(source)  # read the entire audio file

    except Exception as ex:
        print(str(ex))

    # recognize speech using Google_STT --> We'll see if we continue with another STT engine
    try:
        return format_recognized_text(recognizer.recognize_google(audio, language='fr-FR'))
    except speech_recognition.UnknownValueError:
        print("Google could not understand audio")
        return ""
    except speech_recognition.RequestError as e:
        print("Google error; {0}".format(e))
        return ""

def format_recognized_text(p_str):
    ret_str = p_str
#   ret_str = ret_str.replace('retour à la ligne', '\n')
#   ret_str = ret_str.replace('virgule', ',')

    return ret_str

def test_record():
    print('recording')

def test_stop_record():
    print('stopped recording')

def ouaich(p_recorder):
    x = threading.Thread(target=p_recorder.start_record_N_save, args=(WAV_FILENAME,))
    x.start()

def main():
    recorder = opendictavoice_modules.recorder.Recorder()
    gui = opendictavoice_modules.GUI.builded_GUI()
#    gui.rec_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), recorder.start_record_N_save(WAV_FILENAME)])
    x = threading.Thread(target=(lambda x: [recorder.start_record_N_save(x)]), args=(WAV_FILENAME,))
    gui.rec_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), ouaich(recorder)])


    gui.stop_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), recorder.stop_record()])
    gui.launch()
    #recognized_text = recognize_wav('./file.wav')
    #print("Google thinks you said:\n\n" + recognized_text + "\n\n")
    #os.remove('./file.wav')


if __name__ == "__main__":
    main()
