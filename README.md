# Selinux Denial Writer
This script allows you to address selinux denials 

# Want to make your ROMs permissive selinux to enforcing?
It's possible but time consuming work 

Lemme guide you with steps how you can do it 

# Steps
Clone this repo:
```
git clone https://github.com/Xeno761/selinux_denial_writer.git
```
Get in the cloned directory:
```
cd selinux_denial_writer
```
Now open another termux session to get logcat related to denials and paste:
```
su -c logcat | grep "avc" > /sdcard/logcat.log
```
Keep this running in background and open all your apps one by one , it will record all denials of those apps 
Once done exit the session and go back to previous session with selinux_denial_writer directory
