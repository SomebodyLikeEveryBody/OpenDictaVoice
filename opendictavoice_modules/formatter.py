# -*- coding: utf-8 -*-

"""
   Module containing the definition of Formatter class,
   which is supposed to manage the string replacements defined in rewritingrules files
   (located in RESOURCES_PATH/rewritingrules/)
"""

class Formatter:
    """
        Class which is supposed to manage the string replacements defined in rewritingrules files

        Attributes:
        ----------

        self._resources_directory        : str  : path of the ressources folder
        self._rewritingrules_files       : list : a list of the files names containing the replacement rules
        self._rewritingrules_dictionary  : dict : a dict of all rules, organized as {'pattern1': 'replacement1', 'pattern2': 'replacement2', ...}

        Methods:
        -------

        self.build_rewritingrules()
        self.build_resources_directory()
        self.raise_exception_if_no_well_formated()
        self.check_then_add_rules()
        self.format()
        self.load()
    """


    def __init__(self, p_resources_directory, p_filenames_list=None):
        """
            Constructor method, initialize all class attributes

            :param p_resources_directory: raw string of the path of resources folder
            :type p_resources_path: str
            :param p_filenames_list: list or rewritingrules files (only the name of the file, not its path)
            :type p_resources_path: list
            :return: None
            :rtype: None
        """
        self._resources_directory = self.build_resources_directory(p_resources_directory)
        self._rewritingrules_files = self.build_rewritingrules_files_list(p_filenames_list)
        self._rewritingrules_dictionary = {'retour à la ligne ': '\n', 'Retour à la ligne ': '\n'}


    def build_rewritingrules_files_list(self, p_files_list):
        """
            Checks if all files in p_files_list are well formatted and returns it

            :param p_files_list: list or rewritingrules files (only the name of the file, not its path)
            :type p_files_list: list of rewritingrules files
            :return: p_list,
            :rtype: list
        """
        map(lambda file_el: self.raise_exception_if_not_well_formated(file_el), p_files_list)
        return p_files_list


    def build_resources_directory(self, p_dir):
        """
            Checks if all files in p_files_list are well formatted and returns it

            :param p_files_list: list or rewritingrules files (only the name of the file, not its path)
            :type p_files_list: list of rewritingrules files
            :return: p_list,
            :rtype: list
        """
        ret_dir = str(p_dir)
        if ret_dir[-1] == '/':
            ret_dir = ret_dir[:-1]

        return ret_dir


    def raise_exception_if_not_well_formated(self, p_filename):
        #parse the file and see if its format is correct, if not, raise and exception
        pass

    def check_then_add_rule(self, p_filename):
        self.raise_exception_if_not_well_formated(p_filename)
        self._rewritingrules_files.append(p_filename)

    #input: a string p_str
    #output: a text that should really be processed (e.g. if the text contains "virgule", then the symbol "," should be typed)
    def format(self, p_str):

        #rewriting rules are reloaded each time so that files can be modified dynamically
        self.load_rewritingrules()

        p_str = p_str + ' '
        for key in self._rewritingrules_dictionary:
            p_str = p_str.replace(str(key), str(self._rewritingrules_dictionary[key]))

        return p_str

    #add the rewriting rules that are in the file filename
    #Each rewriting rules is of the form "recognized text -> text that should be displayed"
    #e.g. "comma -> ,"
    def load_rewritingrules(self):
        for filename in self._rewritingrules_files:
            file = open(self._resources_directory + '/rewritingrules/' + filename, 'r')
            lines = file.readlines()
            for line in lines:
                if line != "":
                    entry = line.split("->")
                    if(len(entry) >= 2):
                        self._rewritingrules_dictionary[entry[0].strip()] = entry[1].strip()

    ########################
    # Attribute management #
    ########################

    @property
    def rules_files(self):
        return self._rules_files

    @rules_files.setter
    def rules_files(self, p_value):
        if (type(p_value) is not list):
            raise TypeError("[rules_files] attribute must be a affected with a list type")

        self._rules_files = p_value

    @property
    def rewritingrules_dictionnary(self):
        return self._rewritingrules_dictionnary

    @rewritingrules_dictionnary.setter
    def rewritingrules_dictionnary(self, p_value):
        if (type(p_value) is not dict):
            raise TypeError("[rewritingrules_dictionnary] attribute must be a affected with a dict type")

        self._rewritingrules_dictionnary = p_value

################
# Test section #
################

def test():
    F = Formatter('../resources/rewritingrules/LaTEX.txt')
    print(F.format("virgule"))
    print(F.format("comma"))

if __name__ == "__main__":
    test()
