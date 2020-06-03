# -*- coding: utf-8 -*-

"""
    Entry point of OpenDictaVoice Software

    There are 2 constants that can be modified:

    RESOURCES_PATH:        the path to the resources of the program

    REWRITINGRULES_FILES:  a list of files that are used to format the recognized text
                           for examples: (coma --> ,) or (retour à la ligne --> \\n)
                           By default, there are 2 rewritingrules files, LaTEX.txt and basic.txt
                           which you can modify to add you own rules if you want
"""

import opendictavoice_modules.main_app

RESOURCES_PATH = './resources/'
REWRITINGRULES_FILES = [
                            'LaTEX.txt',
                            'basic.txt'
                       ]

def main():
    """
        Entry point of OpenDictaVoice Software
        It uses main_app module, which is the whole OpenDictaVoice's wrapper module

        :return: None
        :rtype: None
    """

    main_app = opendictavoice_modules.main_app.Main_App(RESOURCES_PATH, REWRITINGRULES_FILES)
    main_app.launch()

if __name__ == "__main__":
    main()
