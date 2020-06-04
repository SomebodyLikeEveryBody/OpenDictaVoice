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
            Appends to the fifo an empty process ({id: len(self._fifo), state: "PROCESSING", value: ""})

            :return: the id affected to the process
            :rtype: int
        """

        ret_counter = len(self._fifo)
        self._fifo.append({'id': ret_counter, 'state': 'PROCESSING', 'value': ''})

        return ret_counter

    def remove_process(self, p_id):
        """
            Remove from the fifo the process which id is p_id

            :param p_id: id of the process to remove
            :type p_id: int
            :return: None
            :rtype: None
        """
        dict_2_remove = self.get_process(p_id)
        self._fifo.remove(dict_2_remove)

    def get_process(self, p_id):
        """
            Returns the process in the fifo which id is p_id

            :param p_id: id of the process to return
            :type p_id: int
            :return: the process which id is p_id
            :rtype: dict
        """
        try:
            ret_dict =  next(dict_el for dict_el in self._fifo if dict_el['id'] == p_id)
        except StopIteration:
            raise ValueError("ERROR, voice_recognition_process ID " + str(p_id) + "Doesn't exist")

        return ret_dict

    def __iter__(self):
        """
            Allow to make the fifo object iterable, so we can browse the fifo object with a for loop
            directly without needing to have access to self._fifo

            More concreteley, it allows to do this:
            my_fifo = FIFO()
            for process in my_fifo:
                print(process['value'])

            instead of:
            my_fifo = FIFO()
            for process in my_fifo._fifo:
                print(process['value'])

            :return: None
            :rtype: None
        """
        for dict_process in self._fifo:
            yield dict_process

    def __getitem__(self, p_index):
        """
            Allow to make the fifo object subscriptable, so we can access to a process with an index
            directly without needing to have access to self._fifo

            More concreteley, it allows to do this:
            my_fifo = FIFO()
            print(my_fifo[3])

            instead of:
            my_fifo = FIFO()
            ptint(my_fifo._fifo[3])

            :param p_index: index of the element to return from the self._fifo list
            :type p_index: int
            :return: the process in the self._fifo list at index p_index
            :rtype: dict
        """

        return (self._fifo[p_index])

    def __repr__(self):
        """
            Makes that print(my_fifo) will print self._fifo

            :return: self._fifo
            :rtype: list
        """

        return str(self._fifo)

    def is_empty(self):
        """
            Tests if my_fifo is empty, implied if the list self._fifo is empty

            :return: True if self._fifo is empty, False if it is not
            :rtype: bool
        """

        return (self._fifo == [])

    def set_process_value(self, p_id, p_value):
        """
            Method called to set a process status to translated, by setting its value to the text translate and
            its state to "DONE"

            :param p_id: id of the process to set
            :type p_id: int
            :param p_value: value of the text translated
            :type p_id: str
            :return: None
            :rtype: None
        """

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

