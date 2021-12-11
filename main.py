import os
import time
import math
#import main
from Script import scripts


def conv(files):
    global types
    types = ""
    for i in files:
        types += str(i)

# what is Noman?...

# Noman is actually a python programming
# language for programming Dev tools by simple 
# commands which then Noman Decodes to a set of complex commands for developing robotics, digis and also usb sticks..
# By generating a fake digi payload and tricking the usb to inject the code into the computer and disconnect. 
# It is fast relliable and can be used by hackers, ammature programmers and a noobie.

#rhegion [ rgba(5, 255, 50, 0.05) ]
class Noad(object):
    def Files(self):
        while(True):
            #endregion
            
            cHmd = (input("/> "))
            
            #rhegion [ rgba(140, 255, 50, 0.05) ]
            if cHmd == "cls" or "clear":
                try    : os.system("cls")
                except : os.system("clear")
            #endregion
            
            
            #rhegion [ rgba(255, 205, 50, 0.06) ]
            if "-o" in cHmd:
                cmd        = str(cHmd.replace("-o ", "")); 
                File_Found = str(print(cmd)); 
                File_Found; 
                
                if ".nmn" in cmd:
                    found     = False
                    try:
                        found = open(cmd, 'r')
                        found = True
                    except:
                        found = False
                    if found:
                        scripts(cmd)
                        print(" File [~] Found.")
                    else:
                        print(" Invalid {!} File path.")
                        continue
                else:
                    print(" File [!] Not Found.")
                    
                #endregion

#region [ rgba(170, 100, 50, 0.06) ]
if "__main__" == __name__:
    Noad.Files(Noad)
#endregion
