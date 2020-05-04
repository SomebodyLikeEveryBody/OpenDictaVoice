REWRITINGRULES_FILENAME = ['../resources/rewritingrules/LaTEX.txt']

class Formatter: 
    def __init__(self, p_filenames_list):
        self.rulesfiles = p_filenames_list
        self.rewritingrules_dictionary = dict()

    #input: a string p_str
    #output: a text that should really be processed (e.g. if the text contains "virgule", then the symbol "," should be typed)
    def format(self, p_str):

        #rewriting rules are reloaded each time so that files can be modified dynamically
        self.load_rewritingrules()

        if p_str in self.rewritingrules_dictionary:
            return self.rewritingrules_dictionary[p_str]        
        
        if p_str == 'retour à la ligne':
            return '\n'

        return p_str

    #add the rewriting rules that are in the file filename
    #Each rewriting rules is of the form "recognized text -> text that should be displayed"
    #e.g. "comma -> ,"
    def load_rewritingrules(self):
        for filename in self.rulesfiles:
            file = open(filename, 'r')
            lines = file.readlines() 
            for line in lines:
                if line != "":
                    entry = line.split("->")
                    if(len(entry) >= 2):
                        self.rewritingrules_dictionary[entry[0].strip()] = entry[1].strip()

def test():
    F = Formatter(REWRITINGRULES_FILENAME)
    print(F.format("virgule"))
    print(F.format("comma"))

if __name__ == "__main__":
    test()
