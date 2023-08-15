# CRBasic Program Generator
Created by Alex Blackmer and Cody Oppermann

Used by Weathernet LLC and Utah Department of Transportation

Last updated 8/8/2023
# Overview
[CRBasic Program Generator.pyw](CRBasic%20Program%20Generator.pyw) is used to create CRBasic programs used in weather station loggers. Each program is generated from the user's inputs based on present weather station instrumentation. 

# Using the Program:
To start the program, run the executable file located in the dist folder at [CRBasic Program Generator.exe](dist%2FCRBasic%20Program%20Generator.exe). This file consists of the python script [CRBasic Program Generator.pyw](CRBasic%20Program%20Generator.pyw) coupled with a Python 3 build. [CRBasic Program Generator.exe](dist%2FCRBasic%20Program%20Generator.exe) should run in any Windows environment.

# Editing the Program:
To make changes such as adding an instrument, changing scripted CRBasic output, or general debugging, edit the Python file [CRBasic Program Generator.pyw](CRBasic%20Program%20Generator.pyw).

# Creating the Executable:
After implementing changes in [CRBasic Program Generator.pyw](CRBasic%20Program%20Generator.pyw), package up the script and Python build using PyInstaller. This module neatly consolidates the script and build into an easy to run Windows Executable file that can be distributed to any Windows environment. 
* Install Pyinstaller [(How to Guide)](https://pyinstaller.org/en/stable/).
* Run the following command in the directory containing [CRBasic Program Generator.pyw](CRBasic%20Program%20Generator.pyw):
  * ***pyinstaller '.\CRBasic Program Generator.pyw' --onefile***
* The executable file will be found in the **dist** folder and can then be distributed to other Windows computers.

# Resources
[GUI Programming Example (Tkinter)](https://www.tutorialspoint.com/python3/python_gui_programming.htm)
