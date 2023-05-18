import scapy.all as scapy
import argparse
import requests
import os.path
import wget
import csv

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    #Check for errors i.e if the user does not specify the target IP Address
    #Quit the program if the argument is missing
    #While quitting also display an error message
    if not options.target:
        #Code to handle if interface is not specified
        parser.error("[-] Specificare l'indirizzo IP o la rete da scansionare in formato CIDR, utilizza --help per maggiori info.")
    return options

#Function that takes care of scanning the target
#Funzione che si occupa di eseguire la scansione del target
def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)
    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        result.append(client_dict)
    return result
    
#Verify the presence of the Mac Address database locally and, if not, download it from the IEEE site
#Verifica presenza del database Mac Address in locale e, in caso contrario, lo scarica dal sito della IEEE
def verify_mac_db():
	if os.path.isfile('mac_db.cvs'):
	  print ("Database MAC Address IEEE, trovato.")
	else:
	 print ("Download Database MAC Address dal sito dell'IEEE (ieee.org)...")
	 URL = "https://standards-oui.ieee.org/oui/oui.csv"
	 response = wget.download(URL, "mac_db.cvs")
	 print ("Database Scaricato")

#Importing the CSV file into a dictionary and looking up the Organizationally Unique Identifier (OUI)
#Importazione del file CSV in un dizionario e cerco Organizationally Unique Identifier (OUI
def import_cvs_mac_db(oui):
	with open('mac_db.cvs', mode='r', encoding="utf8") as csv_file:
		csv_reader = csv.DictReader(csv_file)
		first = True
		for riga in csv_reader:
			if (riga["Assignment"] == oui):
				#print(riga["Assignment"], riga["Organization Name"])
				vendor_name = riga["Organization Name"]
	return vendor_name

# Display of the found targers (IP, MAC and Vendor Name)
# Visualizzazione dei targer trovati (IP, MAC e Vendor Name)
def display_result(result):
    print("----------------------------------------------------------------------\nIP Address\t MAC Address\t    Vendor Name \n----------------------------------------------------------------------")
    for i in result:
       chars = ':-'
       mac = i["mac"].translate(str.maketrans('', '', chars))
       mac = mac[0:6].upper()
       vendor_name= import_cvs_mac_db(mac)
       print("{}\t{}".format(i["ip"], i["mac"]), "- "+vendor_name)

if __name__ == "__main__":
    options = get_args()
    verify_mac_db()
    scanned_output = scan(options.target)
    display_result(scanned_output)
