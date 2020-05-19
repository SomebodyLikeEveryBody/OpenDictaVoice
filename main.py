import opendictavoice_modules.audio_manager
import opendictavoice_modules.builded_GUI
import opendictavoice_modules.voice_recognizer
import opendictavoice_modules.formatter
import opendictavoice_modules.keyboard_listener

import threading
import pynput
import time

RESOURCES_PATH = './resources/'
REWRITINGRULES_FILES = [
                            'LaTEX.txt',
                            'basic.txt'
                       ]

def launch_record_in_thread(p_audio_manager):
    thread_record = threading.Thread(target=p_audio_manager.start_record)
    thread_record.start()

def stop_record_then_analyse_in_thread(p_audio_manager, p_voice_recognizer, p_formatter, p_filename):
    thread_stop_record = threading.Thread(target=stop_record_then_analyse, args=(p_audio_manager, p_voice_recognizer, p_formatter, p_filename))
    thread_stop_record.start()

def stop_record_then_analyse(p_audio_manager, p_voice_recognizer, p_formatter, p_filename):
    p_audio_manager.stop_record_N_save(p_filename)
    text = p_voice_recognizer.get_text_from_wav(p_filename)
    formatedText = p_formatter.format(text)
    print('\n\n=========================')
    print("text that was recognized: " + text)
    print("text formatted: " + formatedText)
    print("(I put it in your editor)")
    print('=========================\n\n')
    pynput.keyboard.Controller().type(formatedText)

def switch_focus():
    time.sleep(0.2)
    kb = pynput.keyboard.Controller()
    kb.press(pynput.keyboard.Key.alt)
    kb.press(pynput.keyboard.Key.tab)
    kb.release(pynput.keyboard.Key.alt)
    kb.release(pynput.keyboard.Key.tab)

def main():
    gui = opendictavoice_modules.builded_GUI.Builded_GUI(RESOURCES_PATH)
    audio_manager = opendictavoice_modules.audio_manager.Audio_manager(RESOURCES_PATH)
    voice_recognizer = opendictavoice_modules.voice_recognizer.Voice_Recognizer(audio_manager)
    formatter = opendictavoice_modules.formatter.Formatter(RESOURCES_PATH, REWRITINGRULES_FILES)
    def start_rec(p_event=None):
        gui.set_stop_button_visible()
        launch_record_in_thread(audio_manager)
        
    def stop_rec(p_event=None):
        gui.set_rec_button_visible()
        voice_recognizer.set_language(gui.get_language())
        stop_record_then_analyse_in_thread(audio_manager, voice_recognizer, formatter, RESOURCES_PATH + '/temp/recorded.wav')
        
    gui.rec_button.bind("<Button-1>", start_rec)
    gui.stop_button.bind("<Button-1>", lambda event: [stop_rec(event), switch_focus()])
    opendictavoice_modules.keyboard_listener.Keyboard_listener(start_rec, stop_rec)
    
    #main loop
    gui.launch()

    #once main loop broken
    audio_manager.terminate()

if __name__ == "__main__":
    main()
