
REWRITINGRULESFILENAME = '../resources/rewritingrules/LaTEX.txt'

class Formatter:
    
    #input: a string p_str
    #output: a text that should really be processed (e.g. if the text contains "virgule", then the symbol "," should be typed)
    def format(self, p_str):

        #rewriting rules are reloaded each time so that files can be modified dynamically
        self.initRewritingRules()
        self.addRewritingRules(REWRITINGRULESFILENAME)

        if p_str in self.rewritingRulesDictionary:
            return self.rewritingRulesDictionary[p_str]        
        
        if p_str == 'retour à la ligne':
            return '\n'

        return p_str

    #initialize rewriting rules
    def initRewritingRules(self):
        self.rewritingRulesDictionary = {}
    
    #add the rewriting rules that are in the file filename
    #Each rewriting rules is of the form "recognized text -> text that should be displayed"
    #e.g. "comma -> ,"
    def addRewritingRules(self, filename):
        file = open(filename, 'r') 
        lines = file.readlines() 
        for line in lines:
            if line != "":
                entry = line.split("->")
                if(len(entry) >= 2):
                    self.rewritingRulesDictionary[entry[0].strip()] = entry[1].strip()



def test():
    F = Formatter()
    print(F.format("virgule"))
    
test()