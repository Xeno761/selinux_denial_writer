# Selinux Denial Writer
This script allows you to address selinux denials 

# Want to make your ROMs permissive selinux to enforcing?
It's possible but time consuming work 

Lemme guide you with steps how you can do it 

# Steps
Clone this repo:
```
git clone https://github.com/Xeno761/selinux_denial_writer.git && pkg install python3 -y
```
Get in the cloned directory:
```
cd selinux_denial_writer
```
Now open another termux session to get logcat related to denials and paste:
```
su -c logcat | grep "avc" > /sdcard/logcat.log
```
Keep this running in background and open all your apps one by one , it will record all denials of those apps <br>
Once done exit the session and go back to previous session with selinux_denial_writer directory

Now after we have our logcat file in /sdcard
We'll execute:
```
python3 sepolicy.py /sdcard/logcat.log > /sdcard/denials
```
Done....
Now with MT Manager or any other tool that you use copy the content of /sdcard/denials to /system/etc/selinux/plat_sepolicy.cil <br>
Then reboot 


# Note :
You need to do this process till the logcat stop generating any more logs ( this can even take 100-200 reboots)
Enjoy... Don't forget to give credits if you used this method to fix selinux in your ROM <br>
Mostly after addressing denials related to surfaceflinger and system apps you can boot in enforcing but you need to keep doing the process till no more logs are generated for no issues at all
