## A KeyLogger in Python

Store everything you type on your Ubuntu.

Steps:
1.  Clone the Repo.
2.  Open the terminal:
        ```
        $ sudo apt install python3-xlib
        ```
3.  Change Dir to ```~/.config/autostart```
4.  Create a File ```logger.desktop```
5.  Paste the following (Replace {path} with the path of the cloned Directory):

        [Desktop Entry]
        Type=Application
        Exec=python3 {path}/keyLoggerPython/logger.py >> {path}/keyLoggerPython/log 2>&1 &
        Hidden=false
        NoDisplay=false
        X-GNOME-Autostart-enabled=true
        Name[en_IN]=My KeyStroke Logger
        Name=My KeyStroke Logger
        Comment=Use it well!
6.  Logs will be stored in the same directory under 'Logs' folder.  
7.  Reboot.
