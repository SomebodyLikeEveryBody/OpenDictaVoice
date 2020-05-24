# -*- coding: utf-8 -*-

"""
   Module containing the definition of Audio_manager class,
   which is supposed to manage all audio problematics (record audio, save the audio as wav file, ...)
"""



import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

class Audio_manager:
    """
        Class which is supposed to manage all audio problematics (record audio, save the audio as wav file, ...)
        All attributes of the class are private


        Attributes:
        ----------

        self._resources_path : str                   : path of the resources folder
        self._pyaudio_obj    : pyaudio object        : pyaudio object used to manage audio problematics
        self._keep_record    : boolean               : used to point out to Audio_manager object when stop the recording
        self._audio_frames   : list                  : list containing all recorded CHUNK bytes frames
        self._stream         : pyaudio.Stream object : stream returned by pyaudio.open() when the record starts

        Methods:
        -------

        self.stop_stream()
        self.terminate()
        self.start_record()
        self.stop_record_N_save()
        self.play_wav()
        self.play_error_sound()
    """


    def __init__(self, p_resources_path):
        """
            Constructor method, initialize all class attributes

            :param p_resources_path: raw string of the path of resources folder
            :type p_resources_path: str
            :return: None
            :rtype: None
        """

        self._resources_path = str(p_resources_path)
        self._pyaudio_obj = pyaudio.PyAudio()
        self._keep_record = False
        self._audio_frames = []
        self._stream = None

    def stop_stream(self):
        """
            Closes self._stream object

            :return: None
            :rtype: None
        """

        if self._stream is not None:
            self._stream.stop_stream()
            self._stream.close()
            self._stream = None

    def terminate(self):
        """
            Terminates self.pyaudio_obj object

            :return: None
            :rtype: None
        """

        self._keep_record = False
        self.stop_stream()
        self.pyaudio_obj.terminate()

    def start_record(self):
        """
            Start recording using self._pyaudio_obj and store al bytes datas in self._audio_frames

            :return: None
            :rtype: None
        """

        self._audio_frames = []
        self._stream = self.pyaudio_obj.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

        self._keep_record = True
        data = None
        while self._keep_record == True:
            data = self._stream.read(CHUNK)
            self._audio_frames.append(data)

        self.stop_stream()

    def stop_record_N_save(self, p_filename):
        """
            Stop recording and write the datas stored in self._audio_frames in a file in a file named filename

            :param p_filename: raw string that indicates the path and the name of the file to save
            :type p_resources_path: str
            :return: None
            :rtype: None
        """

        self._keep_record = False

        #save
        waveFile = wave.open(p_filename, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(self.pyaudio_obj.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(self._audio_frames))
        waveFile.close()
        self._audio_frames = []

    def play_wav(self, p_filename):
        """
            Plays a sound file.

            :param p_filename: raw string that indicates the path and the name of the file to save
            :type p_filename: str
            :return: None
            :rtype: None
        """

        temp__pyaudio_obj = pyaudio.PyAudio()
        wf = wave.open(p_filename, 'rb')
        stream = temp__pyaudio_obj.open(format=temp__pyaudio_obj.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

        data = wf.readframes(CHUNK)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        temp__pyaudio_obj.terminate()

    def play_error_sound(self):
        """
            Plays a sound that is supposed to indicate that an error occured in the software
            (unrocognized audio for example)

            :return: None
            :rtype: None
        """
        self.play_wav(self._resources_path + '/sounds/error.wav')


    ########################
    # Attribute management #
    ########################

    @property
    def resources_path(self):
        return self._resources_path

    @resources_path.setter
    def resources_path(self, p_value):
        self._resources_path = str(p_value)

    @property
    def pyaudio_obj(self):
        return self._pyaudio_obj

    @pyaudio_obj.setter
    def pyaudio_obj(self, p_value):
        raise PermissionError("It is not authorized to modify [pyaudio_obj] attribute")

    @property
    def keep_record(self):
        raise PermissionError("It is not authorized to access or modify [keep_record] attribute")
        return None

    @keep_record.setter
    def keep_record(self):
        raise PermissionError("It is not authorized to access or modify [keep_record] attribute")

    @property
    def audio_frames(self):
        raise PermissionError("It is not authorized to access or modify [audio_frames] attribute")
        return None

    @audio_frames.setter
    def keep_record(self):
        raise PermissionError("It is not authorized to access or modify [audio_frames] attribute")

    @property
    def stream(self):
        raise PermissionError("It is not authorized to access or modify [stream] attribute")
        return None

    @stream.setter
    def keep_record(self):
        raise PermissionError("It is not authorized to access or modify [stream] attribute")
