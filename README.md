# ZJUWLAN autologin


This script is a toy for ubuntu users.

first, manually run the script to store your username and password locally.

in the terminal type `$ python WiFi.py`, enter your username
and password, and a number whatever you like.

the script will create a file named **.info** storing your password 
in a simply encrypted form.(don't put any trust on it, this encryption
can only protect your password from human eyes) 

To run the script automatically on startup, open the terminal and type:

`$ crontab -e`

in the config file, type:

`@reboot /path/to/file/WiFi.py`

save the changes and exit, then we are done.
