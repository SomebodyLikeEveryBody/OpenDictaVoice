import opendictavoice_modules.main_app

RESOURCES_PATH = './resources/'
REWRITINGRULES_FILES = [
                            'LaTEX.txt',
                            'basic.txt'
                       ]

def main():
    main_app = opendictavoice_modules.main_app.Main_App(RESOURCES_PATH, REWRITINGRULES_FILES)
    main_app.launch()

if __name__ == "__main__":
    main()
