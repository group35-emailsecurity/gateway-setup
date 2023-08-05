# Overview
- There are 3x Raspberry Pi devices / servers on the same network each with static IP addresses.  
- The server hostnames should be external.test, gateway.test, internal.test  
- external.test and gateway.test should each have a user called 'user'.  
- internal.test should have a user called 'user1' (an organisation - can have multiple 'internal' users).  
- Emails sent from user@external.test to user1@internal.test will pass through the gateway server for filtering of malicious content. 
- Each email that passes through the gateway server for filtering is recorded and can be viewed via a web app on the gateway server (this includes both allowed and denied emails).
- Additionally, if the internal server were to send outbound emails to the external server:
    - A TLS connection is enforced for outbound emails in transit between the gateway server and the external server, thus encrypting the communication channel.  
    - _TO DO: encryption of email contents_

# Setup
## Configure Gateway server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname gateway.test`  
- Create user: `sudo adduser user && sudo adduser user sudo`  
- Login as user.  
- Clone this repository somewhere inside the 'home' directory.  
- Edit the transport-maps file to include the IP address of the internal and external servers (replace \<INTERNAL SERVER IP ADDRESS> with the IP address of the internal server. Retain the square brackets. Do the same for the IP address of the external server.)  
- Enter the 'postfix' directory: `cd postfix`  
- Make the setup.sh script executable: `chmod +x setup.sh`  
- Run the setup.sh script with elevated privileges: `sudo ./setup.sh`  
- Postfix will install or reinstall. Choose the 'Internet Site' option, and enter 'gateway.test' as the domain.  
- The gateway should now be set up.  
- Run `sudo tail -f /var/log/mail.log` to view the live gateway Postfix log.

# System Testing
## Configure External server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname external.test`  
- Create user: `sudo adduser user && sudo adduser user sudo`  
- Login as user.  
- Install Postfix: `sudo apt install postfix`. Choose the 'Internet Site' option, and enter 'external.test' as the domain.  
- Ensure emails sent from the external server to the internal server are routed through the gateway server by adding the following line to the /etc/hosts file: `<GATEWAY SERVER IP ADDRESS>    internal.test` (where \<GATEWAY SERVER IP ADDRESS> is the IP address of the gateway server).  
- Open Claws Mail and configure as follows: Email address should be user@external.test. Server type should be 'Local mbox file'. SMTP server address should be 'internal.test'.  
- _TO DO: Email contents encryption - generate public key_

## Configure Internal server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname internal.test`  
- Create user1: `sudo adduser user1 && sudo adduser user1 sudo`  
- Login as user1.   
- Install Postfix: `sudo apt install postfix`. Choose the 'Internet Site' option, and enter 'internal.test' as the domain.  
- Ensure emails sent from the internal server to the external server are routed through the gateway server by adding the following line to the /etc/hosts file: `<GATEWAY SERVER IP ADDRESS>    external.test` (where \<GATEWAY SERVER IP ADDRESS> is the IP address of the gateway server).  
- Open Claws Mail and configure as follows:  Email address should be user1@internal.test. Server type should be 'Local mbox file'. SMTP server address should be 'external.test'.  
- _TO DO: Email contents encryption - import external server public key and setup PGP/MIME_

## Send emails from External server
- Login as 'user' on the external server.  
- Open Claws Mail and try sending emails to user1@internal.test

## Send emails from Internal server
- Login as 'user1' on the internal server.  
- Open Claws Mail and try sending emails to user@external.test

# Web App
## Accessing the web app
- Enter the 'webapp' directory and run the start.py file: `python start.py`

## Running the web app
- _TO DO: web app instructions_
