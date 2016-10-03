'''
The flanker.addresslib package exposes a simple address parsing library that
can handle email addresses and urls.

See the address.py module for the public interfaces to the library and the
parser.py module for the implementation of the recursive descent parser
used to parse email addresses and urls.
'''
import re

from flanker.addresslib.plugins import yahoo
from flanker.addresslib.plugins import aol
from flanker.addresslib.plugins import gmail
from flanker.addresslib.plugins import icloud
from flanker.addresslib.plugins import hotmail
from flanker.addresslib.plugins import google


YAHOO_PATTERN = re.compile(r'''mta[0-9]+\.am[0-9]+\.yahoodns\.net$''')
GMAIL_PATTERN = re.compile(r'''.*gmail-smtp-in\.l\.google.com$''')
AOL_PATTERN = re.compile(r'''.*\.mx\.aol\.com$''')
ICLOUD_PATTERN = re.compile(r'''.*\.mail\.icloud\.com$''')
HOTMAIL_PATTERN = re.compile(r'''mx[0-9]\.hotmail\.com''')
GOOGLE_PATTERN = re.compile(r'''(.*aspmx\.l\.google\.com$)|(aspmx.*\.googlemail.com$)''', re.IGNORECASE)

CUSTOM_GRAMMAR_LIST = [
    (YAHOO_PATTERN, yahoo),
    (GMAIL_PATTERN, gmail),
    (AOL_PATTERN, aol),
    (ICLOUD_PATTERN, icloud),
    (HOTMAIL_PATTERN, hotmail),
    (GOOGLE_PATTERN, google),
]
