### THIS WILL WORK ONLY IF YOUR PACKAGE MANAGER IS `APT`
sudo apt update -y && sudo apt upgrade  && sudo apt full-upgrade 
sudo apt autopurge  && sudo apt autoremove  && sudo apt autoclean

check=$(dpkg -l | grep "aptitude") # check if `aptitude` installed
if [[ $check == "" ]]; then
	sudo apt install aptitude && sudo aptitude purge ~c # Install `aptitude` then remove all UNUSED apps or packages and just it :]
else
	sudo aptitude purge ~c # This to remove all UNUSED apps or packages :]
fi
### This if you have flatpak then remove the `#` at the beginning next line :] IF you don't have flatpak just keep it OR remove NEXT LINE(NOT RECOMMENDED)
#sudo flatpak update
### To run this program use 'bash upgrade.sh' or use `chmod u+x update.sh` to run './upgrade.sh' without use bash every time
sudo -k  # This to exit the super user mode (root account)
### NOTE : you can return it run every time you login (AUTOMATIC) but this you need to figure out by yourself SOME SEARCH WON't HURT YOU  ^_^
