# -*- coding: utf-8 -*-

"""
    Module containing the definition of FIFO class,
    which is supposed to manage the order in which recognized texts are returned.

    Indeed, for ergonomic reasons, the program is made so that the user can start recording again while
    the previous sound is not finished translating.

    If the second sound was translated and returned while the first was still being processed,
    then a sentence said after another would be written before the latter.

    That's why the FIFO class exists, to store translating processes and return it in correct order.

    Explanations:
    ============

    The FIFO object has 1 attribute:
    - self._fifo: a list containing the translating processes. Each new translating process is appended
                  to this list

    A translating Process is a dict with 3 keys:
    - id: the id of the translating process, which is technically len(self._fifo)
          at the moment it is appened to the fifo

    - state: string that can be "PROCESSING" if translate is not done yet, or "DONE" if it is
    - value: string of the translation, that is empty('') if translate is not done yet

    For examples:
    {id: 42, state: 'PROCESSING', value: ''}
    or
    {id: 42, state: 'DONE', value: 'Hello everybody'}

    Each time a translation is done, we can check if self._fifo[0] has the state "DONE",
    if yes, we return its value, remove the process from the list and we check again self._fifo[0]
    which is the following process, etc etc

"""

class FIFO:
    """
        Class which is supposed to manage the order in which recognized texts are returned.

        Attributes:
        ----------

        self._fifo      : list : a list containing all the processes

        Methods:
        -------

        self.push_voice_recognition_process()
        self.remove_process()
        self.get_process()
        self.is_empty()
        self.set_process_value()
        self.__iter__()
        self.__getitem__()
        self.__repr__()
    """

    def __init__(self):
        """
            Constructor method, initialize all class attributes

            :return: None
            :rtype: None
        """
        self._fifo = list()

    def push_voice_recognition_process(self):
        """
            Aooends to the fifo an empty process ({id: len(self._fifo), state: "PROCESSING", value: ""})
            and returns the id affected to the process

            :return: the id affected to the process
            :rtype: int
        """

        ret_counter = len(self._fifo)
        self._fifo.append({'id': ret_counter, 'state': 'PROCESSING', 'value': ''})

        return ret_counter

    def remove_process(self, p_id):
        dict_2_remove = self.get_process(p_id)
        self._fifo.remove(dict_2_remove)

    def get_process(self, p_id):
        try:
            ret_dict =  next(dict_el for dict_el in self._fifo if dict_el['id'] == p_id)
        except StopIteration:
            raise ValueError("ERROR, voice_recognition_process ID " + str(p_id) + "Doesn't exist")

        return ret_dict

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

