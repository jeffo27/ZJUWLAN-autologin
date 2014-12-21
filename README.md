# ZJUWLAN autologin

This script helps automatically login the ZJUWLAN at startup.

First, manually run the script to store your username and password locally.

* For Ubuntu users:

In the terminal type `$ python WLANlogin.py`, enter your username
and password, and a number whatever you like.

The script will create a file named **.info** storing your password 
in a simply encrypted form.(don't put any trust on it, this encryption
can only protect your password from human eyes) 

To run the script automatically on startup, open the terminal and type:

`$ crontab -e`

In the config file, type:

`@reboot /path/to/file/WLANlogin.py`

Save the changes and exit. We're done.

* For Windows users:

Double click the `WLANlogin.py` file and enter the entries as showed above.

To run the script automatically on startup, first change the dafault program
to execute the script into `pythonw.exe`, you will find it where python is 
installed, usually in `C:\Python2X`. This operation forbids the scirpt to
create a bothering `cmd` window. 

Then, create a shortcut of `WLANlogin.py`and store it to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`, making the script run at startup. Then
we are done.



