#Craig Ferguson (A0112586) Scripting for security assessment

# importing required librarys
from scapy.all import *
from urllib.request import urlretrieve 
import socket, nmap, os, subprocess, getpass, time, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#def created for the menu
def menu():
    #Number for menu tab
    n = 0

    #displaying menu options using commas to make options more readable
    #blank prints to give more space when loading selection
    print("-------------------------------------")
    print("1| Run A Port Scan On Local Machine \n",
          "2| Ping A Website Or PC \n",
          "3| Packet Sniffing \n",
          "4| Run Zenmap \n",
          "5| Install Recommended Security Tools - All Programs Will Be Needed For First Time Startup \n",
          "6| Install Individual Security Program \n",
          "7| Run Individual Security Program \n"
          "8| Shutdown or Restart Device \n",
          "9| Exit Program")
    print("-------------------------------------")
    
    #getting user input
    n = int(input("Enter Option between 1-9: "))
    print("-------------------------------------")
    #checking for input validity
    while n > 9 or n < 0:
        n = int(input("Enter A Valid Option between 1-9: "))
        print("-------------------------------------")
    #selecting user input and loading the relevant method
    if n == 1:
        portScanning()
    elif n == 2:
        pingWebsite()
    elif n == 3:
        packetSniffing()
    elif n == 4:
        runNmap()
    elif n == 5:
        installTools()
    elif n == 6:
        installProgram()
    elif n == 7:
        runProgram()
    elif n == 8:
        shutdownDevice()
    elif n == 9:
        exitProgram()

    
#portscanning def
def portScanning():
    nmScan = nmap.PortScanner()

    print("Scanning local host please wait...")

    # scan localhost for ports in range 21-443
    nmScan.scan('127.0.0.1', '21-443')

    for host in nmScan.all_hosts():
        print('Host : %s (%s)' % (host, nmScan[host].hostname()))
        print('State : %s' % nmScan[host].state())
        for proto in nmScan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nmScan[host][proto].keys()
            #lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

    #declares scan complete and returns to main menu
    print("Port Scanning Complete")
    menu_call()
    
    
#ping def
def pingWebsite():

    target_address = " "
    #getting target IP
    target_address = input("enter the addres to ping ")
    #Giving the user the option to exit
    subprocess.run(["ping", target_address])
    print("Ping A Website Or PC Complete ")
    #will return user to main menu after ping
    #may replace with pingWebsite menu if needed
    menu_call()

#packet sniffing def
def packetSniffing():
# Will sniff inputted packets and ask user if they want
# to run wireshark to capture packets & analyse them using wireshark
# NOTE: Wireshark needs to be installed to view


    num_to_sniff = 0
    #asks how many packets want to be sniffed
    num_to_sniff = int(input("enter the number of packets to sniff: "))
    #sniff for selected packets
    a=sniff(count=num_to_sniff) 
    #print out the summary of packets
    a.nsummary()

    print("Packet Sniffing Complete"
          "\n")

    #Asks the user if they would like to run wireshark to start a packet capture
    #and warns the user that wireshark must be installed in order to do so
    #includes details for the menu option which will install the program
    print("Would you like to open wireshark to capture and analyse packets ? \n"
          "NOTE: WIRESHARK MUST BE INSTALLED IN ORDER TO START\n"
          "see main menu option 5 for full tool installation \n"
          "or use option 6 to install program(s) individually \n"
          "\n"
          "1 = Start wireshark \n" 
          "2 = return to menu")
    wireshark = int(input("Input number: "))
    
    #Will start wireshark with option 1 or return to main menu with option 2
    if wireshark == 1:
        os.system('start wireshark')
        menu_call()
    elif wireshark == 2:
        menu()    
    

#Run Nmap def
def runNmap():
# Needs zenmap/Nmap installed to work
#Runs zenmap
#Note: NMap currently does not work
    
    print("NOTE: ZENMAP MUST BE INSTALLED IN ORDER TO START\n"
          "see main menu option 5 for full tool installation \n"
          "or use option 6 to install program(s) individually \n")
    print("starting Zenmap")
    os.system('start zenmap')    
    print("Zenmap opened ")
    menu_call()
        

#Bulk download and install def
def installTools():

    #Gets the file path for the python install
    path = (sys.executable).strip("python.exe")

    #Notifes the user that they are about to bulk install all the recommended security tools
    print("press 1 to install all recommended security tools \n"
    "press 2 to return to the main menu\n"
    "if you would like to install a specific program\n"
    "then select option 6 from the main menu")
    
    #Menu for options
    #1 will run through all recommended tools to install
    #if user has error they must check enviroment variables in win10
    #alternatively pip install can be replaced with URLs
    #time.sleep(3) added otherwise it goes so fast it seems that it doesnt do anything
    tools = int(input("Input number: "))
    if tools == 1:
        os.chdir(path)
        print("installing scapy")
        os.system("python -m pip install scapy")
        time.sleep(3)
        print("scapy sucessfully installed")
        print("installing zenmap")
        os.system("python -m pip install python-nmap")
        time.sleep(3)
        print("zenmap sucessfully installed")
        print("\n")
        print("Downloading wireshark")

        #url for wireshark
        url = 'https://1.na.dl.wireshark.org/win64/Wireshark-win64-3.6.2.exe'
        print("Wireshark download may take a while please be patient")        
        #gets username for the download path
        usrname = getpass.getuser()
        #download path for the program
        destination = f'C:\\Users\\{usrname}\\downloads\\Wireshark.exe'
        #download the requested item
        download = urlretrieve(url, destination)
        #wireshark update
        print("\n Wireshark download complete starting installer")
        #executes downloaded exe
        os.system(destination)

        #url for 7zip
        url1 = 'https://www.7-zip.org/a/7z2107-x64.exe'
        print("7zip download has started")        
        #gets username for the download path
        usrname = getpass.getuser()
        #download path for the program
        destination1 = f'C:\\Users\\{usrname}\\downloads\\7zip.exe'
        #download the requested item
        download1 = urlretrieve(url1, destination1)
        #wireshark update
        print("\n 7zip download complete starting installer")
        #executes downloaded exe
        os.system(destination1)

        #lets the user know that all tools are being installed
        #3 second pause to make it look like its doing something
        time.sleep(3)
        print("Installing all required libraries")
        print("----------------------------------")

        #notifies user that the installation is complete and returns to the main menu
        time.sleep(3)
        print("Installation of all recommended security tools complete ")
        menu_call()

    elif tools == 2:
        menu_call()
            
#Install individual program def
def installProgram():
    #Menu for installing individual programs

    print("press 1 to install scapy\n"
          "press 2 to install zenmap\n"
          "press 3 to install wireshark\n"
          "press 4 to install 7zip\n"
          "press 5 to return to the main menu")

    #After user has installed a program
    #option will call the installProgram() menu back should they wish
    #to install any thing else
    #This saves the user time
    install = int(input("Enter Option between 1-5: "))
    if install == 1:
        print("installing scapy")
        os.system("python -m pip install scapy")
        time.sleep(3)
        print("scapy sucessfully installed")
        installProgram()
    elif install == 2:
        print("installing zenmap")
        os.system("python -m pip install python-nmap")
        time.sleep(3)
        print("zenmap sucessfully installed")
        installProgram()
    elif install == 3:
        #Have to do url downloads for wireshark and 7zip
        #url for wireshark
        url = 'https://1.na.dl.wireshark.org/win64/Wireshark-win64-3.6.2.exe'
        print("Wireshark download may take a while please be patient")        
        #gets username for the download path
        usrname = getpass.getuser()
        #download path for the program
        destination = f'C:\\Users\\{usrname}\\downloads\\Wireshark.exe'
        #download the requested item
        download = urlretrieve(url, destination)
        #wireshark update
        print("\n Wireshark download complete starting installer")
        #executes downloaded exe
        os.system(destination)
        installProgram()
    elif install == 4:
        #url for 7zip
        url1 = 'https://www.7-zip.org/a/7z2107-x64.exe'
        print("7zip download has started")        
        #gets username for the download path
        usrname = getpass.getuser()
        #download path for the program
        destination1 = f'C:\\Users\\{usrname}\\downloads\\7zip.exe'
        #download the requested item
        download1 = urlretrieve(url1, destination1)
        #wireshark update
        print("\n 7zip download complete starting installer")
        #executes downloaded exe
        os.system(destination1)
        installProgram()
    elif install == 5:
        menu_call()

#Run program def
def runProgram():

    #Menu for running individual programs
    program = int(input("\n"
                        "Which tool would you like to run ? \n"
                        "press 1 to run scapy\n"
                        "press 2 to run zenmap\n"
                        "press 3 to run wireshark\n"
                        "press 4 to run 7zip\n"
                        "press 5 to return to the main menu\n"
                        "Enter your choice here: "))
    #Runs the seleted programs then
    #brings up the runProgram() menu should they wish
    #to run additional software
    if program  == 1:
        ("Running scapy")
        os.system('start scapy')
        runProgram()
    elif program == 2:
        ("Running zenmap")
        os.system('start zenmap')
        runProgram()
    elif program == 3:
        ("Running wireshark")
        os.system('start wireshark')
        runProgram()
    elif program == 4:
        ("Running 7Zip")
        os.system('start 7zFM')
        runProgram()
    elif program == 5:
        menu_call()


#Shutdown def
def shutdownDevice():
    #displaying a warning that this will actually shutdown the users machine
    print("WARNING !!! \n","THIS WILL FORCE SHUTDOWN YOUR COMPUTER WITHOUT WARNING \n","CHOOSE CAREFULLY")

    power = int(input("Would you like to shutdown or restart your PC ? \n"
                        "press 1 to Shutdown PC\n"
                        "press 2 to Restart PC\n"
                        "press 3 to cancel\n"
                        "Enter your choice here: "))

    #Will either shutdown or restart the machine unless the user cancels
    #Shutdown/restart happens without warning after a prompt window(win10)

    if power  == 1:
        ("Shutting down PC in 1 minute.\n"
         "please save your work\n"
         "All unsaved work will be lost")
        os.system('shutdown -s')
    elif power == 2:
        ("Restarting PC in 1 minute.\n"
         "please save your work\n"
         "All unsaved work will be lost")
        os.system('shutdown -r')
    elif power == 3:
        ("Returning to main menu")
        menu_call()
       
    # -s will shutdown the PC, replacing -s with -r will restart it    
           

#Exit program def
def exitProgram():
    #takes the number inputed from the menu to exit the program
    #may throw and error when exitting ?
    #Tried exit(), quit() and sys.exit() to same result
    #added a 0 and fixed issue
    print("Exiting Program...")
    sys.exit(0)


#menu_call() gives the user the option to return to the menu after completion of running the option
def menu_call():
    print("")
    cont = input("Do You Want To Return To The Menu?... 'y/n': ")
    if cont == "y" or cont == "Y":
        menu()
    else:
        print("Exiting...")
        sys.exit(0)

#initialising the menu and starts the program
menu()

