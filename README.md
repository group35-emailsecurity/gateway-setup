# Overview
- There are 3x Raspberry Pi devices / servers on the same network each with static IP addresses.  
- The server hostnames should be external.test, gateway.test, internal.test  
- external.test and gateway.test should each have a user called 'user'.  
- internal.test should have a user called 'user1' (an organisation - can have multiple 'internal' users).  
- Emails sent from user@external.test to user1@internal.test will pass through the gateway server for filtering of malicious content. 
- Each email that passes through the gateway server for filtering is recorded and can be viewed via a web app on the gateway server (this includes both allowed and denied emails).
- Additionally, if the internal server were to send outbound emails to the external server:
    - A TLS connection is enforced for outbound emails in transit between the gateway server and the external server, thus encrypting the communication channel.  
    - Procedures for implementing PGP/MIME encryption are provided below. PGP/MIME encryption is when the email contents are encrypted by the sender with the intended recipient's public key, whereby the intended recipient is the only person who can decrypt the email with their private key (and an additional passphrase).  
    - Procedures for signing a email with PGP keys are provided below. Signing an email with PGP keys is a way to verify that the owner of the sending email address was the one who sent the email.  

# Gateway setup
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

## Configure Internal server
- Set a static IP address by editing the /etc/dhcpcd.conf file. Uncomment and edit the 'Example static IP configuration' section.  
- Set the hostname: `sudo hostnamectl set-hostname internal.test`  
- Create user1: `sudo adduser user1 && sudo adduser user1 sudo`  
- Login as user1.   
- Install Postfix: `sudo apt install postfix`. Choose the 'Internet Site' option, and enter 'internal.test' as the domain.  
- Ensure emails sent from the internal server to the external server are routed through the gateway server by adding the following line to the /etc/hosts file: `<GATEWAY SERVER IP ADDRESS>    external.test` (where \<GATEWAY SERVER IP ADDRESS> is the IP address of the gateway server).  
- Open Claws Mail and configure as follows:  Email address should be user1@internal.test. Server type should be 'Local mbox file'. SMTP server address should be 'external.test'.  

## Send emails from External server
- Login as 'user' on the external server.  
- Open Claws Mail and try sending emails to user1@internal.test

## Send emails from Internal server
- Login as 'user1' on the internal server.  
- Open Claws Mail and try sending emails to user@external.test

## PGP/MIME encryption procedure
### Configure External server
- Install Claws Mail plugins: `sudo apt install claws-mail-plugins`  
- In Claws Mail, nagivate to Configuration -> Plugins -> Load. Select: pgpmime.so and pgpcore.so. Close the Plugins window.  
- Navigate to Configuration -> Preferences for current account -> GPG. Click 'Generate a new key pair'. Enter a passphrase, remember it. Copy the fingerprint. There is no need to export it to a key server.  
- In a terminal, run: `gpg --list-keys`. The copied fingerprint should be in the list of keys.  
- Export the public key file by entering: `gpg --output ~/external-public-key.pub --export [FINGERPRINT]` where [FINGERPRINT] is the fingerprint that was copied.  
- For the purposes of this demo, email the public key file (external-public-key.pub) as an attachment to user1@internal.test. Note that in reality, the public key should be shared via a 'web of trust', whereby multiple parties are in agreement that a public key belongs to a specific party.  

### Configure Internal server
- Check the inbox for the email from the external user containing their public key. Save the file to the ~ home directory.  
- In a terminal, import the public key into the local keyring by running: `gpg --import ~/external-public-key.pub`  
- Run `gpg --list-keys` to confirm the external server's public key has been imported to the keyring.  
- Install Claws Mail plugins: `sudo apt install claws-mail-plugins`  
- In Claws Mail, nagivate to Configuration -> Plugins -> Load. Select: pgpmime.so and pgpcore.so. Close the Plugins window.  
- Compose a new email addressed to user@external.test  
- Select Options -> Privacy System -> PGP/MIME. Select Options -> Encrypt  
- Send the email. Claws Mail will match the email's 'To' address (user@external.test) to that address' public key that was imported into the keyring. Click through the 'Encryption warning'. Click through the 'Encrypt to user (user@external.test)' prompt. The email will then be sent.  

### External server
- The encrypted email should arrive in the external server's inbox. Open it and when prompted enter the passphrase that was chosen when creating the keys. The decrypted email contents should now be visible.    
- The external user may be prompted again to enter their passphrase again to decrypt further emails during their session.  

## PGP signing
### Configure Internal server
- In Claws Mail. Navigate to Configuration -> Preferences for current account -> GPG. Select 'Select key by your email address'. 'Click 'Generate a new key pair'. Enter a passphrase, remember it. There is no need to export it to a key server.  
- In a terminal, run: `gpg --list-keys`. The copied fingerprint should be in the list of keys.  
- Export the public key file by entering: `gpg --output ~/internal-public-key.pub --export [FINGERPRINT]` where [FINGERPRINT] is the fingerprint that was copied.  
- For the purposes of this demo, email the public key file (internal-public-key.pub) as an attachment to user@external.test. Note that in reality, the public key should be shared via a 'web of trust', whereby multiple parties are in agreement that a public key belongs to a specific party.  

### Configure External server
- Check the inbox for the email from the internal user containing their public key. Save the file to the ~ home directory.  
- In a terminal, import the public key into the local keyring by running: `gpg --import ~/internal-public-key.pub`  
- Run `gpg --list-keys` to confirm the internal server's public key has been imported to the keyring.  

### Internal server
- In Claws Mail, compose a new email addressed to user@external.test  
- Select Options -> Privacy System -> PGP/MIME. Select Options -> Sign  
- Send the email. When prompted, enter the passphrase chosen earlier. This will sign the email with the user1@internal.test private key. The email will then be sent.  

### External server
- In Claws Mail, check the inbox for the signed email from user1@internal.test. Select the email.  
- At the bottom of the window, it should read 'This signature has not been checked'. Click the padlock next to this sentence. The text 'Good signature from user1 <user1@internal.test>' should appear, thus verifying that the email was signed with the user1@internal.test private key that pairs with the user1@internal.test public key in the external user's keyring.  

# Web App
## Accessing the web app
- Enter the 'webapp' directory and run the start.py file: `python start.py`

## Running the web app
- _TO DO: web app instructions_
