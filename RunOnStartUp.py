"""
This is an auto startup script example

It creates a file called 'StartupTestFile.txt' 
in your desktop or wherever you want whenever 
you start your computer.

*** WAIT DON'T RUN THIS PROGRAM YET ***
Before you run this program in the create_file() 
function set the desktop variable to where you 
want the file to be generated. 

Credit: https://www.geeksforgeeks.org/autorun-a-python-script-on-windows-startup/
"""

# module to edit the windows registry 
import winreg as reg 
import os  
import sys

def create_file():
    """This creates a file"""
    print('Creating File')
    text = "This file is a startup file"
    
    # Where to create the file
    # Note: You can change the var name to whatever 
    # you want I just used desktop because that's how 
    # I tested it.
    desktop = r'path/to/your/desktop'
    file_path = os.path.join(desktop, 'StartupTestFile.txt')
    
    with open(file_path, 'w') as fp:
        fp.write(text)
	

def AddToRegistry():
    # get the startup flag if it exists
    flag_file = os.path.join(os.path.expanduser("~"), '.startup_flag.txt')  # hidden flag file

    # check if the .exe is already registered via the startup flag
    if os.path.exists(flag_file):
        print("Registry already set, skipping.")
        return

    # takes the abs path of where this file is being executed
    address=sys.executable
    
    # key we want to change is HKEY_CURRENT_USER 
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = reg.HKEY_CURRENT_USER
    key_value = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    # to avoid errors put in try loop
    try:
        # open the registry with the key and find it's value
        reg_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
        # set the path to the address 
        reg.SetValueEx(reg_key, "hello_world_autorun", 0, reg.REG_SZ, address)
        # close the registry
        reg.CloseKey(reg_key)

        # create a startup flag that will be checked to notify 
        # that this has already been added to the registry
        with open(flag_file, 'w') as f:
            f.write('Registry entry added.')

        print("Added to registry. Flag created.")
    except Exception as e:
        print("Failed to write to registry:", e)

 
# Driver Code
if __name__=="__main__":
	AddToRegistry()
	create_file()
