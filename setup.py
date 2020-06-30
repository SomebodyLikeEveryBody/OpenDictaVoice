from distutils.core import setup

setup(name='OpenDictaVoice',
      version='1.0',
      description='A python3 program to do voice dictation',
      author='Francois Schwarzentruber and Victor Vague',
      author_email='frippon@supersonique.pouet',
      url='https://www.gitlab.org/lien_vers_le_repo',
      packages=['opendictavoice_app',
                'opendictavoice_app.opendictavoice_modules'],
      py_modules=['opendictavoice_app.opendictavoice_main',
                  'opendictavoice_app.opendictavoice_modules.audio_manager',
                  'opendictavoice_app.opendictavoice_modules.builded_GUI',
                  'opendictavoice_app.opendictavoice_modules.fifo',
                  'opendictavoice_app.opendictavoice_modules.keyboard_listener',
                  'opendictavoice_app.opendictavoice_modules.main_app',
                  'opendictavoice_app.opendictavoice_modules.voice_recognizer'],
      data_files=[('./opendictavoices_app/resources', '')],
      requires=['PyAudio', 'pynput', 'pythonxlib', 'six', 'SpeechRecognition']
)
