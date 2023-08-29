clear > /dev/tty0
echo "$(python3 /storage/roms/ports/RG353-WiFi-Pen/ascii_art.py)" > /dev/tty0
sleep 2
clear > /dev/tty0
echo "Attempting PMKID Capture:" > /dev/tty0
echo "-------------------------" > /dev/tty0
echo "Restarting WiFi..." > /dev/tty0
connmanctl disable wifi
sleep 3
connmanctl enable wifi
echo "$(python3 /storage/roms/ports/RG353-WiFi-Pen/capture_pmkid.py)" > /dev/tty0
sleep 6
clear > /dev/tty0