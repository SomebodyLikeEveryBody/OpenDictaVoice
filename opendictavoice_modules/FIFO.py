class FIFO:
    def __init__(self):
        #a list of dicts like this:
        #[
        #    {id: 42, state: 'PROCESSING', value: ''},
        #    {id: 43, state: 'DONE', value: 'coucou tout le monde'},
        #    {id: 44, state: 'PROCESSING', value: ''},
        #    {id: int(), state: Enum('PROCESSING', 'DONE'), value: String()}
        #]
        self._fifo = list()
        self._counter = 0

    def pop(self):
        return self._fifo.pop(0)

    def push_voice_recognition_process(self):
        ret_counter = 0
        #push a new voice_recognition process in the fifo
        self._fifo.push({'id': self._counter, state: 'PROCESSING', value: ''})
        ret_counter = self._counter
        self._counter += 1

        return ret_counter

    def get_process(self, p_id):
    try:
        ret_dict =  next(dict_el for dict_el in self._fifo if dict_el['id'] == p_id)
    except StopIteration:
        raise ValueError("ERROR, voice_recognition_process ID " + str(p_id) + "Doesn't exist")

    return ret_dict

    def update_process():


    ########################
    # Attribute management #
    ########################

    @property
    def fifo(self):
        raise PermissionError("It is not authorized to access or modify [fifo] attribute")
        return None

    @fifo.setter
    def fifo(self, p_value):
        raise PermissionError("It is not authorized to access or modify [fifo] attribute")

