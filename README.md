# RG353-WiFi-Penetration-Tool
Hacking WiFi Networks with the Anbernic RG353 line of hardware and other Retro Gaming Handhelds

This repo contains modified versions of WiFi hacking python scripts you can find elsewhere on the <a href="https://github.com/ZeroDayArcade">ZeroDayArcade GitHub</a>, now meant to run on Anbernic RG353 series hardware using RG353's built in WiFi module. This was specifically tested with the RG353PS, using the <a href="https://github.com/RetroGFX/UnofficialOS">UnofficialOS</a> operating system with the RG353P image from <a href="https://github.com/RetroGFX/UnofficialOS/releases/tag/20230427">release 20230427</a>. The scripts should work with UnofficalOS on other varients of the RG353 without modification assuming the same basic file structure and can easily be modified to run on many other Linux-based Retro Handhelds that have WiFi capabilites.

Although their is no easy way to put the built-in WiFi chip into monitor mode, it is still capable of reading packets in managed mode that are necessary for PMKID attacks. This means that on access points and routers that are vulnerable to the <a href="https://hashcat.net/forum/thread-7717.html">PMKID exploit</a> found by <a href="https://hashcat.net/forum/user-1.html">atom</a> and the hashcat team in 2018, this code can capture a PMKID and potentially crack the password of the WiFi network. 

The capture script script should be run first which will extract the PMKID from the first EAPoL frame that the access point sends back to the RG353 when the RG353 attemps to connect to it with a random password. Although the random password will obviously fail to connect, the PMKID, MAC addresses, and SSID will be stored by the script in an hashcat hc22000 format hash line and saved to a file `hashline.txt`. The hash line can then be use later for an offline attack using hashcat on a more powerful computer, or the user can immediately try to crack it with the cracking script that also comes with this codebase. 

The cracking script is more for demonstration purposes than anything, but for low hanging fruit (weak passwords) and with relatively small password lists, it can crack passwords without having to leave the RG353. I've added a very small sample `passlist.txt` file which can be used for testing, but you can also supply your own `passlist.txt` file containing larger and/or more sophisticated password dictionaries. This makes hacking on the go possible, and even if the password can't be cracked by the on-board script, the hash line that is saved to `hashline.txt` on the TFT2 slot Micro SD card can be cracked later with more powerful cracking tools as previously mentioned. 

## Steps to using the tool

1. ***Install UnofficialOS*** on your RG353P/PS/M/etc
2. Clone this repo and ***copy the RG353-WiFi-Pen directory*** to the "ports/" directory of the slot TFT2 (Roms) Micro SD card
3. With the TFT2 Micro SD back in the RG353, press the 'START' button and ***go to Network Settings*** and make sure WiFi is enabled
4. Select the target WiFi network and ***enter a random password for the network***
6. Exit the menus and ***navigate to "Ports"*** on the main interface
7. Enter "Ports" and ***select the "RG353-WiFi-Pen" directory***, you will see two options: ***capture*** and ***crack***
8. ***Select "capture"*** to run the PMKID capture script on you target network. If it is unable to capture PMKID it will timeout after a minute
9. If the PMKID capture was successfull you will see the PMKID, MAC addresses and SSID printed to the screen along the a hashcat format hash line which has been save to the Micro SD card. If the PMKID is all 0's, that likely means the access point you are targeting does not append a PMKID to the end of the first EAPol frame and is not vulnerable to this type of attack. Otherwise you're ready to crack
10. Now ***run the "crack" script*** from the same place you ran the capture script. If the password of the network is part of the `passlist.txt` dictionary, than the password will be cracked. Otherwise you can take the hash line saved to `hashline.txt` in the same RG353-WiFi-Pen directory for later cracking with hashcat or other cracking tools (you won't see it from the main menu but it's on the Micro SD if you put it in your computer).


# More ZDA Code and Content:
**Learn Reverse Engineering, Assembly, Code Injection and More:**  
🎓  <a href="https://zerodayarcade.com/tutorials">zerodayarcade.com/tutorials</a> 

**More WiFi Hacking with Simple Python Scripts:**  
<a href="https://github.com/ZeroDayArcade/wpa-password-cracking-with-pmkid/">Cracking WPA/WPA2 Passwords with PMKID</a>  
<a href="https://github.com/ZeroDayArcade/capture-handshake-wpa-wifi-hacking">Capturing WPA/WPA2 4-Way Handshake</a>  
<a href="https://github.com/ZeroDayArcade/cracking-wpa-with-handshake">Cracking WPA/WPA2 Passwords with 4-Way Handshake</a>  


# Find Hacking Bounties in Gaming:
🎮  <a href="https://zerodayarcade.com/bounties">zerodayarcade.com/bounties</a>



