import opendictavoice_modules.recorder
import opendictavoice_modules.builded_GUI
import opendictavoice_modules.voice_recognizer
import opendictavoice_modules.formatter
import threading
import pyperclip
import pyautogui

WAV_FILENAME = './recorded.wav'
RESOURCES_PATH = './resources/'


def launch_record_in_thread(p_recorder):
    thread_record = threading.Thread(target=p_recorder.start_record)
    thread_record.start()

def stop_record_in_thread(p_recorder, p_voice_recognizer, p_formatter, p_filename):
    thread_stop_record = threading.Thread(target=stop_record_then_analyse, args=(p_recorder, p_voice_recognizer, p_formatter, p_filename))
    thread_stop_record.start()

def stop_record_then_analyse(p_recorder, p_voice_recognizer, p_formatter, p_filename):
    p_recorder.stop_record_N_save(p_filename)
    text = p_voice_recognizer.wav_to_text(p_filename)
    print("text that was recognized: " + text)
    print("(I put it in your editor)")
    pyperclip.copy(p_formatter.format(text))
    pyautogui.PAUSE = 0.4
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'v')


def main():
    recorder = opendictavoice_modules.recorder.Recorder()
    voice_recognizer = opendictavoice_modules.voice_recognizer.Voice_Recognizer()
    gui = opendictavoice_modules.builded_GUI.Builded_GUI(RESOURCES_PATH)
    formatter = opendictavoice_modules.formatter.Formatter()

    gui.rec_button.bind("<Button-1>", lambda event: [gui.switch_buttons(
        event), voice_recognizer.set_language(gui.get_language()), launch_record_in_thread(recorder)])
    gui.stop_button.bind("<Button-1>", lambda event: [gui.switch_buttons(
        event), stop_record_in_thread(recorder, voice_recognizer, formatter, WAV_FILENAME)])
    gui.launch()


if __name__ == "__main__":
    main()
