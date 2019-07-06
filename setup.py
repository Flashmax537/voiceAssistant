import os
from cx_Freeze import setup, Executable
import sys

os.environ['TCL_LIBRARY'] = 'c:/python3/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/python3/tcl/tk8.6'
buildOptions = dict( packages = [], excludes = [], include_files=['c:/python3/DLLs/tcl86t.dll', 'c:/python3/DLLs/tk86t.dll'] )

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

setup(
    name='codeby',
    version = '1.0',
    description = '',
    options = dict(build_exe = buildOptions),executables =  [Executable("voiceAssistant.py", base=base)]
)