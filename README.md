# Simple-Python-Network-Scanner
A Python script based on "Network-Scanner" by dharmil18 (https://github.com/dharmil18/Network-Scanner/)
The scritp scans a network for connected devices and based on the OUI contained in the Mac Addres shows the vendor name. The script checks for the existence of a local copy of the IEEE OUI database and, if not present, downloads it from the official IEEE site (ieee.org)

## Setup
Download this repository and run it locally,

```bash
python3 simple_net_scan.py -t ip_address
or
python3 simple_net_scan.py --target ip_address
```
where ip_address is the IP Address of the target machine. Example: 10.122.0.1

The script also accepts a range of ip addresses to be scanned for. For that in the ip_address field you need to provide the range. Example: 10.122.0.1/24
This tells the script that start scanning from 10.122.0.1 to 10.122.0.254

## Output


#### Output of the first time of the Script for a single target IP Address
```bash
root@kali:~/Desktop/Network Scanner# python3 simple_net_scan.py -t 10.0.2.3

Download OUI Database from the IEEE website (ieee.org)...
100% [..........................................................................] 3155687 / 3155687
Download Complete!
----------------------------------------------------------------------
IP Address       MAC Address        Vendor Name
----------------------------------------------------------------------
10.0.2.3	  08:00:27:24:58:5a   - PCS Systemtechnik GmbH 


#### Output of the Script for a single target IP Address

```bash
root@kali:~/Desktop/Network Scanner# python3 simple_net_scan.py -t 10.0.2.3
---------------------------------------------------------------------------
IP Address	MAC Address         Vendor Name
---------------------------------------------------------------------------
10.0.2.3	  08:00:27:24:58:5a   - PCS Systemtechnik GmbH  
```

**OR**
```bash
root@kali:~/Desktop/Network Scanner# python3 simple_net_scan.py --target 10.0.2.3
---------------------------------------------------------------------------
IP Address	MAC Address         Vendor Name
---------------------------------------------------------------------------
10.0.2.3	  08:00:27:24:58:5a   - PCS Systemtechnik GmbH
```


#### Output of the Script for a range of target IP Address

```bash
root@kali:~/Desktop/Network Scanner# python3 simple_net_scan.py --target 10.0.2.1/24
-----------------------------------
IP Address	MAC Address
-----------------------------------
10.0.2.1	  78:2B:CB:12:35:00   - Dell Inc.
10.0.2.2	  78:2B:CB:12:35:01   - Dell Inc.
10.0.2.15	  08:00:27:e6:e5:59   - PCS Systemtechnik GmbH
10.0.2.3	  08:00:27:24:58:5a   - PCS Systemtechnik GmbH
```
