
## live usb
create a live usb stick containing a bootable linux distro using mac OS

The result will be bootable on normal (non-mac) computers. 
```bash
# first download a bootable iso file

# define usb stick
diskutil list
export DISK=<number>

# define iso
export FOLDER=$HOME/Downloads
export ISO=$FOLDER/distro-64bit.iso
export IMG=$FOLDER/distro.img
export DMG=$IMG.dmg

# convert iso to img.dmg
hdiutil convert -format UDRW -o $IMG $ISO

# create disk
diskutil unmountDisk /dev/disk$DISK

sudo dd if=$DMG of=/dev/rdisk$DISK
```


