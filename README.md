# ZJUWLAN autologin


This script is a toy for ubuntu users.

First, manually run the script to store your username and password locally.

In the terminal type `$ python WLANlogin.py`, enter your username
and password, and a number whatever you like.

The script will create a file named **.info** storing your password 
in a simply encrypted form.(don't put any trust on it, this encryption
can only protect your password from human eyes) 

To run the script automatically on startup, open the terminal and type:

`$ crontab -e`

In the config file, type:

`@reboot /path/to/file/WLANlogin.py`

Save the changes and exit, then we are done.
