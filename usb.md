
## windows ISO -> USB

```bash
#(fedora). See https://github.com/slacka/WinUSB otherwise.
sudo dnf install grub2 grub2-tools wxGTK3-devel gcc-c++ git
git clone https://github.com/slacka/WinUSB.git && cd WinUSB
./configure && make && sudo make install
winusb --help
```
