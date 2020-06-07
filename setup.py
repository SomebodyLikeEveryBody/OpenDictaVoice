# -*- coding: utf-8 -*-
# Python 3

import sys, os
from cx_Freeze import setup, Executable

#############################################################################
#                              Options build                                #
#############################################################################

script_dir = os.path.dirname(os.path.realpath(__file__))
path = sys.path + [script_dir]
includes = []
excludes = []
packages = []

# copier les fichiers non-Python et/ou repertoires et leur contenu:
include_files = []

if sys.platform == "win32":
    pass
    # include_files += [...] : ajouter les recopies specifiques à Windows

elif sys.platform == "linux2":
    pass
    # include_files += [...] : ajouter les recopies specifiques à Linux

else:
    pass
    # include_files += [...] : cas du Mac OSX non traite ici

# pour que les bibliotheques binaires de /usr/lib soient recopiees aussi sous Linux
binpath_includes = []
if sys.platform == "linux2":
    binpath_includes += ["/usr/lib"]

# niveau d'optimisation pour la compilation en bytecodes
optimize = 0

# si True, n'affiche que les warning et les erreurs pendant le traitement cx_freeze
silent = False

# construction du dictionnaire des options
options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages,
           "include_files": include_files,
           "bin_path_includes": binpath_includes,
           "optimize": optimize,
           "silent": silent
           }

# pour inclure sous Windows les dll system de Windows necessaires
if sys.platform == "win32":
    options["include_msvcr"] = True

#############################################################################
#                              Target build                                 #
#############################################################################
base = None
icone = None

if sys.platform == "win32":
    base = "Win32GUI"  # pour application graphique sous Windows
    # base = "Console" # pour application en console sous Windows
    icone = "icone.ico"

cible_1 = Executable(
    script="main.py",
    base=base,
    icon=icone
    )

#############################################################################
#                               Setup build                                 #
#############################################################################
setup(
    name="monprogramme",
    version="1.00",
    description="monprogramme",
    author="auteurduprogramme",
    options={"build_exe": options},
    executables=[cible_1]
)
