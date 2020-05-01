import opendictavoice_modules.recorder
import opendictavoice_modules.GUI
import opendictavoice_modules.voice_recognizer
import threading
import pyperclip
import pyautogui

WAV_FILENAME = './recorded.wav'
RESOURCES_PATH = './resources/'

def launch_record_in_thread(p_recorder):
    thread_record = threading.Thread(target=p_recorder.start_record)
    thread_record.start()

def stop_record_then_analyse(p_recorder, p_voice_recognizer, p_gui, p_filename):
def analyse_wav_to_get_text(p_filename):
    recognized_text = recognize_wav(p_filename)
    print(recognized_text)
    pyperclip.copy(recognized_text)
    pyautogui.PAUSE = 0.2
    pyautogui.hotkey('alt', 'tab')   
    pyautogui.write(recognized_text)
    #pyautogui.hotkey('ctrl', 'v')   
    os.remove(p_filename)

def stop_record_then_analyse(p_recorder, p_filename):
    p_recorder.stop_record_N_save(p_filename)
    p_voice_recognizer.wav_to_formated_text(p_filename)

def main():
    recorder = opendictavoice_modules.recorder.Recorder()
    voice_recognizer = opendictavoice_modules.voice_recognizer.Voice_Recognizer()
    gui = opendictavoice_modules.GUI.builded_GUI(RESOURCES_PATH)

    gui.rec_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), launch_record_in_thread(recorder)])
    gui.stop_button.bind("<Button-1>", lambda event : [gui.switch_buttons(event), stop_record_then_analyse(recorder, voice_recognizer, gui, WAV_FILENAME)])
    gui.launch()

if __name__ == "__main__":
    main()
