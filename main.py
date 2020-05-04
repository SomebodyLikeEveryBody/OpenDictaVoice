import opendictavoice_modules.audio_manager
import opendictavoice_modules.builded_GUI
import opendictavoice_modules.voice_recognizer
import opendictavoice_modules.formatter
import threading
import pyperclip
import pyautogui

WAV_FILENAME = './recorded.wav'
RESOURCES_PATH = './resources/'


def launch_record_in_thread(p_audio_manager):
    thread_record = threading.Thread(target=p_audio_manager.start_record)
    thread_record.start()

def stop_record_in_thread(p_audio_manager, p_voice_recognizer, p_formatter, p_filename):
    thread_stop_record = threading.Thread(target=stop_record_then_analyse, args=(p_audio_manager, p_voice_recognizer, p_formatter, p_filename))
    thread_stop_record.start()

def stop_record_then_analyse(p_audio_manager, p_voice_recognizer, p_formatter, p_filename):
    p_audio_manager.stop_record_N_save(p_filename)
    text = p_voice_recognizer.wav_to_text(p_filename)
    print('\n\n=========================')
    print("text that was recognized: " + text)
    print("(I put it in your editor)")
    print('=========================\n\n')
    pyperclip.copy(p_formatter.format(text))
    pyautogui.PAUSE = 0.4
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'v')

def main():
    audio_manager = opendictavoice_modules.audio_manager.Audio_manager(RESOURCES_PATH)
    voice_recognizer = opendictavoice_modules.voice_recognizer.Voice_Recognizer(audio_manager)
    gui = opendictavoice_modules.builded_GUI.Builded_GUI(RESOURCES_PATH)
    formatter = opendictavoice_modules.formatter.Formatter([RESOURCES_PATH + 'rewritingrules/LaTEX.txt'])

    gui.rec_button.bind("<Button-1>", lambda event: [gui.switch_buttons(
        event), voice_recognizer.set_language(gui.get_language()), launch_record_in_thread(audio_manager)])

    gui.stop_button.bind("<Button-1>", lambda event: [gui.switch_buttons(
        event), stop_record_in_thread(audio_manager, voice_recognizer, formatter, WAV_FILENAME)])

    #main loop
    gui.launch()

    #once main loop broken
    audio_manager.terminate()

if __name__ == "__main__":
    main()
