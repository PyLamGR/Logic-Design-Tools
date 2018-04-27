from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=['sys', 'os', 'PyQt5'],
                    includes=['GUI'],
                    excludes=[],
                    include_files=['GUI\PyLamLogo.png'])

import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable(script='Logic Design Solver.py',
               base=base,
               icon='GUI/favicon.ico',
               copyright='Dada\'s Workshop 2017',
               trademarks='Dada\'s Workshop 2017')
]

setup(
    name='Logic Design Solver',
    version='1.0.0',
    description='A solver for simple Logic Design exercises.',
    options=dict(build_exe=buildOptions),
    executables=executables
)