clear > /dev/tty0
echo "Attempting Crack with PMKID:" > /dev/tty0
echo "----------------------------" > /dev/tty0
echo "$(python3 /storage/roms/ports/RG353-WiFi-Pen/crack_pmkid.py)" > /dev/tty0
sleep 6
clear > /dev/tty0