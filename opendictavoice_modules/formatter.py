REWRITINGRULES_FILENAME = ['../resources/rewritingrules/LaTEX.txt']

class Formatter: 
    def __init__(self, p_filenames_list):
        self._rules_files = p_filenames_list
        self._rewritingrules_dictionary = {'retour à la ligne ': '\n', 'Retour à la ligne ': '\n'}

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
        for filename in self._rules_files:
            file = open(filename, 'r')
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
    F = Formatter(REWRITINGRULES_FILENAME)
    print(F.format("virgule"))
    print(F.format("comma"))

if __name__ == "__main__":
    test()
