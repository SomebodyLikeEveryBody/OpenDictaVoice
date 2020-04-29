import pyaudio
import wave
import threading

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
 
    def record(self, p_frames, p_stream):
        self.keep_record = True
        data = None

        print("recording...")
        while self.keep_record == True:
            data = p_stream.read(CHUNK)
            p_frames.append(data)

        print("finished recording")

    def start_record_N_save(self, p_filename):
        # start Recording
        print('start record n save')
        frames = []
        stream = self.pyaudio_obj.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

        self.keep_record = True
        data = None
        print("recording...")

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
        print("WE STOP")
