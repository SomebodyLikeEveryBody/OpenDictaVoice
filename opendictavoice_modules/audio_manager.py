import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
 
class Audio_manager:
    def __init__(self, p_resources_path):
        self.resources_path = p_resources_path
        self.pyaudio_obj = pyaudio.PyAudio()
        self.keep_record = False
        self.audio_frames = []
        self.stream = None
 
    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def terminate(self):
        self.keep_record = False
        self.stop_stream()
        self.pyaudio_obj.terminate()

    def start_record(self):
        self.audio_frames = []
        self.stream = self.pyaudio_obj.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

        self.keep_record = True
        data = None
        while self.keep_record == True:
            data = self.stream.read(CHUNK)
            self.audio_frames.append(data)

        self.stop_stream()

    def stop_record_N_save(self, p_filename):
        self.keep_record = False

        #save 
        waveFile = wave.open(p_filename, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(self.pyaudio_obj.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(self.audio_frames))
        waveFile.close()
        self.audio_frames = []

    def play_wav(self, p_filename):
        temp_pyaudio_obj = pyaudio.PyAudio()
        wf = wave.open(p_filename, 'rb')
        stream = temp_pyaudio_obj.open(format=temp_pyaudio_obj.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

        data = wf.readframes(CHUNK)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        temp_pyaudio_obj.terminate()

    def play_error_sound(self):
        self.play_wav(self.resources_path + '/sounds/error.wav')
