#!/usr/bin/env bash

# Check if Postfix is installed
dpkg --status "postfix" &> /dev/null

# If Postfix is installed, uninstall it
if [ $? -eq 0 ]; then
    apt purge postfix
fi

# Install Postfix
apt install postfix &&

# Copy files required for the destination relay to work
cp transport-maps relay-recipient-maps /etc/postfix &&

# Copy filter handler and filter service
cp filter-handler.sh filter-service.py /etc/postfix &&

# Make filter handler and filter service executable
chmod +x /etc/postfix/filter-handler.sh /etc/postfix/filter-service.py &&

# Append additional settings to the main.cf config file
cat main.cf-additional-settings >> /etc/postfix/main.cf &&

# Append additional settings to the master.cf config file
cat master.cf-additional-settings >> /etc/postfix/master.cf &&

# Set the relay maps
postmap /etc/postfix/transport-maps &&
postmap /etc/postfix/relay-recipient-maps &&

# Reload Postfix
postfix reload
