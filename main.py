import opendictavoice_modules.audio_manager
import opendictavoice_modules.builded_GUI
import opendictavoice_modules.voice_recognizer
import opendictavoice_modules.formatter
import opendictavoice_modules.keyboard_listener
import opendictavoice_modules.fifo

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

def analyse_wav_in_thread(p_voice_recognizer, p_formatter, p_id):

    #here too we will pass the index of the file in the fifo instead of the filename, like 1
    thread_stop_record = threading.Thread(target=analyse_wav, args=(p_voice_recognizer, p_formatter, p_id))
    thread_stop_record.start()

def analyse_wav(p_voice_recognizer, p_formatter, p_id):

    #processing
    filepath = RESOURCES_PATH + '/temp/recorded_' + str(p_id) + '.wav'
    text = p_voice_recognizer.get_text_from_wav(opendictavoice_modules.audio_manager.Audio_manager(self._resources_path).play_error_sound()filepath)
    if text is None:
        opendictavoice_modules.audio_manager.Audio_manager(RESOURCES_PATH).play_error_sound()

    #once text is recognized (or not), it is stored in the fifo list in the specific dict of the list.
    #Beware of the content of the list to ensure chars are printable to avoid security problems
    formatedText = p_formatter.format(text)

    print('\n\n=========================')
    print("text that was recognized: " + text)
    print("text formatted: " + formatedText)
    print("(I put it in your editor)")
    print('=========================\n\n')

    #this action will be done with the fifo, like we parse the fifo list, when the dict state is "DONE",
    #we pynput, else, we wait
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
    formatter = opendictavoice_modules.formatter.Formatter(RESOURCES_PATH, REWRITINGRULES_FILES)
    audio_manager = opendictavoice_modules.audio_manager.Audio_manager(RESOURCES_PATH)
    fifo = opendictavoice_modules.fifo.FIFO()


    #audio_manager is only needed to record here, so we can have one audio_manager
    #but we probably will need multiple voice_recognizers, one per file to analyse in threads
    #I see things like this: wonce record is stopped, we launch analize in thread with a generated
    #voice recognizer, and wonce it's done, we notify the FIFO
    #the FIFO might be a list of dicts, like [{id: 42, state: "PROCESSING", value: ''}, {id: 43, state: 'DONE', value: 'pouet'}, {id: 44, state: 'DONE', value: "hello tout le monde"}]
    #id is an int and state might be "PROCESSING" or "DONE", value is the text returned and empty if processing
    #the thing is, how to process the result of the FIFO without an infinite loop ?

    def start_rec(p_event=None):
        gui.set_stop_button_visible()
        launch_record_in_thread(audio_manager)

    def stop_rec(p_event=None):
        gui.set_rec_button_visible()
        voice_recognizer = opendictavoice_modules.voice_recognizer.Voice_Recognizer()
        voice_recognizer.set_language(gui.get_language())

        #FIFO object will return a number that will be used to name the file, like recorded_1.wav
        index = fifo.push_voice_recognition_process()
        audio_manager.stop_record_N_save(RESOURCES_PATH + '/temp/recorded_' + str(index) +'.wav')

        #then, instead of passing the filename as arg, we pass the index of the file in the fifo, like 1
        analyse_wav_in_thread(voice_recognizer, formatter, index)
        print(fifo.get_list())

    gui.rec_button.bind("<Button-1>", start_rec)
    gui.stop_button.bind("<Button-1>", lambda event: [stop_rec(event), switch_focus()])
    opendictavoice_modules.keyboard_listener.Keyboard_listener(start_rec, stop_rec)

    #main loop
    gui.launch()

    #once main loop broken
    audio_manager.terminate()

if __name__ == "__main__":
    main()
