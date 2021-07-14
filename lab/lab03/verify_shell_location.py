# verify_shell_location.py
# Prof Lillian Lee (LJL2), Molly Feldman (MQF3), and Amol Tandel (AT766)
# Feb 2021

"""Check if the user has placed this and all the first-module-lab files in 
Desktop->correct directory (folder)"""

import os
import sys
import platform
LDIRNAME = "lab03"


#if not (sys.version_info[0] == 3 and sys.version_info[1] >= 6):
if sys.version_info[0] <= 2:
    print("\n.... CS1110 problem: unexpected Python version " +
          str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "....\n")
    print("Please ask your lab staff for help with your Python installation.")
    sys.exit(1)


if platform.system() == "Windows":
    import getpass
    if os.path.isdir('C:\\Users\cit-labs'):
        # some lab machines used to have a different setup for home directories
        desired_dir = ('C:\\' + 
                       os.path.join('Users', 'cit-labs', 'Desktop', LDIRNAME))
    else:
        desired_dir = ('C:\\' +  
                       os.path.join('Users', 
                                    getpass.getuser(), 
                                    'Desktop', 
                                    LDIRNAME))
else:
    desired_dir = os.path.expanduser("~/Desktop/" + LDIRNAME)
sl="The working  directory"

if os.getcwd() != desired_dir:
        print()
        print("CS1110 WARNING: your working directory (folder) may not be right.")
        print("  We were expecting " + desired_dir)
        print("  but your working dir is " + os.getcwd())
        print()
        print("*** Ask a staff member to check your directory setup. ***")
        print()
tl=sl.replace("  ", " ")
sl=(tl+" " + "contains the files for this lab.\nHurrah!")
filenames = ["verify_shell_location.py",
              "greetings.py",
              "last_task.py"]
test_results = []

for f in filenames:
    test_results.append(os.path.isfile(f))

if all(test_results):
    print
    s1="Everything looks good!"
    print(sl)
else:
    print("CS1110 problem: This directory seems to be missing at least one file.")
    print("Diagnostic info: ")
    for i in range(len(filenames)):
        print (filenames[i] + ": " + ("found" if test_results[i] else "not found"))
    print("\n*** Ask a staff member for help. ***")
