import opendictavoice_modules.audio_manager
import opendictavoice_modules.builded_GUI
import opendictavoice_modules.voice_recognizer
import opendictavoice_modules.formatter
import opendictavoice_modules.keyboard_listener
import opendictavoice_modules.fifo

import threading
import pynput
import time
import os

class Main_App():

    def __init__(self, p_resources_path, p_rewritingrules_files):
        self.resources_path = p_resources_path
        self.rewritingrules_files = p_rewritingrules_files
        self.gui = opendictavoice_modules.builded_GUI.Builded_GUI(self.resources_path)
        self.formatter = opendictavoice_modules.formatter.Formatter(self.resources_path, self.rewritingrules_files)
        self.audio_manager = opendictavoice_modules.audio_manager.Audio_manager(self.resources_path)
        self.fifo = opendictavoice_modules.fifo.FIFO()


    def launch_record_in_thread(self):
        thread_record = threading.Thread(target=self.audio_manager.start_record)
        thread_record.start()


    def analyse_wav_in_thread(self, p_voice_recognizer, p_id):
        thread_stop_record = threading.Thread(target=self.analyse_wav, args=(p_voice_recognizer, p_id))
        thread_stop_record.start()


    def analyse_wav(self, p_voice_recognizer, p_id):

        print(self.fifo)
        #processing
        filepath = self.resources_path + '/temp/recorded_' + str(p_id) + '.wav'
        text = p_voice_recognizer.get_text_from_wav(filepath)
        os.remove(filepath)
        if text is None:
            opendictavoice_modules.audio_manager.Audio_manager(self.resources_path).play_error_sound()
            self.fifo.remove_process(p_id)

        else:
            #once text is recognized (or not), it is stored in the fifo list in the specific dict of the list.
            #Beware of the content of the list to ensure chars are printable to avoid security problems
            self.fifo.set_process_value(p_id, text)
            self.write_fifo_texts()


    def write_fifo_texts(self):

        print(self.fifo)
        while (not self.fifo.is_empty()):
            dict_process = self.fifo[0]

            if (dict_process['state'] == 'DONE'):
                text = dict_process['value']
                formated_text = self.formatter.format(text)

                #write value and take off from the fifo
                print('\n\n=========================')
                print("text that was recognized: " + text)
                print("text formatted: " + formated_text)
                print("(I put it in your editor)")
                print('=========================\n\n')

                pynput.keyboard.Controller().type(formated_text)
                self.fifo.remove_process(dict_process['id'])

            else:
                break

        print(self.fifo)


    def switch_focus(self):
        time.sleep(0.2)
        kb = pynput.keyboard.Controller()
        kb.press(pynput.keyboard.Key.alt)
        kb.press(pynput.keyboard.Key.tab)
        kb.release(pynput.keyboard.Key.alt)
        kb.release(pynput.keyboard.Key.tab)


    def start_rec(self, p_event=None):
        self.gui.set_stop_button_visible()
        self.launch_record_in_thread()


    def stop_rec(self, p_event=None):
        self.gui.set_rec_button_visible()
        temp_voice_recognizer = opendictavoice_modules.voice_recognizer.Voice_Recognizer()
        temp_voice_recognizer.set_language(self.gui.get_language())

        #FIFO object will return a number that will be used to name the file, like recorded_1.wav
        index = self.fifo.push_voice_recognition_process()
        self.audio_manager.stop_record_N_save(self.resources_path + '/temp/recorded_' + str(index) +'.wav')

        #then, instead of passing the filename as arg, we pass the index of the file in the fifo, like 1
        self.analyse_wav_in_thread(temp_voice_recognizer, index)


    def launch(self):
        self.gui.rec_button.bind("<Button-1>", self.start_rec)
        self.gui.stop_button.bind("<Button-1>", lambda event: [self.stop_rec(event), self.switch_focus()])
        opendictavoice_modules.keyboard_listener.Keyboard_listener(self.start_rec, self.stop_rec)

        #main loop
        self.gui.launch()

        #once main loop broken
        self.audio_manager.terminate()
