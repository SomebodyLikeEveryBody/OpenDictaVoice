import pyaudio
import wave
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "file.wav"
 
class Recorder:
    def __init__(self):
        self.pyaudio_obj = pyaudio.PyAudio()
        self.keep_record = False
 
    def start_record_N_save(self, p_filename):
        # start Recording
        frames = []
        stream = self.pyaudio_obj.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

        print("recording...")
        self.keep_record = True
        while self.keep_record == True:
            data = stream.read(CHUNK)
            frames.append(data)

        print("finished recording")

        # stop Recording
        stream.stop_stream()
        stream.close()
        self.pyaudio_obj.terminate()
 
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(self.pyaudio_obj.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

    def stop_record(self):
        self.keep_record = False
