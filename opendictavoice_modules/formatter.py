class Formatter:

    #input: a string p_str
    #output: a text that should really be processed (e.g. if the text contains "virgule", then the symbol "," should be typed)
    def format(self, p_str):
        ret_str = p_str
        ret_str = ret_str.replace('retour à la ligne', '\n')
        ret_str = ret_str.replace('virgule', ',')
        return ret_str
