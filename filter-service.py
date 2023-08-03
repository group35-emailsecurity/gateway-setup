#!/usr/bin/env python

import sys
import re

# This script must return an exit code of 0 or 1
# Exit code 0: No threat detected. This exit code will result in the email being delivered to the intended recipient.
# Exit code 1: Threat detected. This exit code will result in the email being discarded.

# TODO: We can filter the email and create logs here (Note: the email is available via stdin and can be parsed line by line, as shown below)

for line in sys.stdin:
	if re.search(r'viagra', line, re.IGNORECASE):
		print('The word "viagra" was found in the email.')
		# Exit with code 1
		sys.exit(1)

print('The email body did not contain any suspicious words.')
# Exit with code 0
sys.exit(0)
