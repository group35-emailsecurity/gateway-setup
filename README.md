# Overview
- There are 3x Raspberry Pi devices / VMs on the same network each with static IP addresses.  
- The device hostnames should be origin.test, gateway.test, destination.test  
- origin.test and gateway.test should each have a user called 'user'.  
- destination.test should have a user called 'user1' (the destination - like an organisation - can have multiple users).  
- Emails sent from user@origin.test to user1@destination.test will pass through the gateway device for filtering. 
- Each email that is filtered by the gateway device is stored and can be viewed via a web app (this includes both allowed and denied emails).
- Additionally, if the protected destination device were to send outbound emails:
    - A TLS connection is enforced for outbound emails in transit between the gateway device and any external server.  
    - _TO DO: encryption of email content_

# Setup
## Configure Gateway server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname gateway.test`  
- Create user: `sudo adduser user && sudo adduser user sudo`  
- Login as user.  
- Clone this repository somewhere inside the 'home' directory.  
- Edit the transport-maps file to include the IP address of the destination server (replace \<DESTINATION SERVER IP ADDRESS> with the IP address of the destination server. Retain the square brackets. Do the same for the IP address of the origin server.)  
- Enter the 'postfix' directory: `cd postfix`  
- Make the setup.sh script executable: `chmod +x setup.sh`  
- Run the setup.sh script with elevated privileges: `sudo ./setup.sh`  
- Postfix will install or reinstall. Choose the 'Internet Site' option, and enter 'gateway.test' as the domain.  
- The gateway should now be set up.  
- Run `sudo tail -f /var/log/mail.log` to view the live gateway Postfix log.

# End-to-End Testing
## Configure Origin server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname origin.test`  
- Create user: `sudo adduser user && sudo adduser user sudo`  
- Login as user.  
- Install Postfix: `sudo apt install postfix`. Choose the 'Internet Site' option, and enter 'origin.test' as the domain.  
- Ensure emails sent from the origin server to @destination.test email addresses are routed through the gateway server by adding the following line to the /etc/hosts file: `<GATEWAY SERVER IP ADDRESS>    destination.test` (where \<GATEWAY SERVER IP ADDRESS> is the IP address of the gateway server).  
- Open Claws Mail and configure as follows: Email address should be user@origin.test. Server type should be 'Local mbox file'. SMTP server address should be 'destination.test'.

## Configure Destination server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname destination.test`  
- Create user1: `sudo adduser user1 && sudo adduser user1 sudo`  
- Login as user1.   
- Install Postfix: `sudo apt install postfix`. Choose the 'Internet Site' option, and enter 'destination.test' as the domain.  
- Ensure emails sent from the destination server to @origin.test email addresses are routed through the gateway server by adding the following line to the /etc/hosts file: `<GATEWAY SERVER IP ADDRESS>    origin.test` (where \<GATEWAY SERVER IP ADDRESS> is the IP address of the gateway server).  
- Open Claws Mail and configure as follows:  Email address should be user1@destination.test. Server type should be 'Local mbox file'. SMTP server address should be 'origin.test'.

## Send emails from Origin server
- Login as 'user' on the origin server.  
- Open Claws Mail and try sending emails to user1@destination.test

## Send emails from Destination server
- Login as 'user1' on the destination server.  
- Open Claws Mail and try sending emails to user@origin.test

# Web App
## Accessing the web app
- Enter the 'webapp' directory and run the start.py file: `python start.py`

## Running the web app
- _TO DO: web app instructions_
