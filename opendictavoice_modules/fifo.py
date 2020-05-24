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
        ret_counter = self._counter
        #push a new voice_recognition process in the fifo
        self._fifo.append({'id': self._counter, 'state': 'PROCESSING', 'value': ''})
        self._counter += 1

        return ret_counter

    def remove_process(self, p_id):
        dict_2_remove = self.get_process(p_id)
        self._fifo.remove(dict_2_remove)
        self._counter -= 1

    def get_process(self, p_id):
        try:
            ret_dict =  next(dict_el for dict_el in self._fifo if dict_el['id'] == p_id)
        except StopIteration:
            raise ValueError("ERROR, voice_recognition_process ID " + str(p_id) + "Doesn't exist")

        return ret_dict

    def get_list(self):
        return self._fifo

    def __iter__(self):
        for dict_process in self._fifo:
            yield dict_process

    def __getitem__(self, p_value):
        return (self._fifo[p_value])

    def __repr__(self):
        return str(self._fifo)

    def is_empty(self):
        return (self._fifo == [])

    def set_process_value(self, p_id, p_value):
        dict_process = self.get_process(p_id)
        dict_process['value'] = p_value
        dict_process['state'] = 'DONE'

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

