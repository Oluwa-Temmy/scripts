# Scripts Repo
This is just a bunch of scripts that I make that can be used

## RunOnStartUp.py
This script adds itself to the Windows startup registry so that it runs automatically when the system starts.<br/> It does this by accessing the Windows registry to add a key under <br/>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run, which<br/> ensures that the script or executable is launched upon user login.

The script also creates a simple text file on the user's desktop to demonstrate file creation,<br/> and a hidden flag file is used to ensure that the registry key is only added once.

### How To
(Windows)<br/>
`pyinstall --onefile RunOnStartUp.py`<br/>
then put that .exe file into this dir
`C:\Users\current_user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`<br/>
because your accessing the registry, you have to run the script as an administrator<br/>
``