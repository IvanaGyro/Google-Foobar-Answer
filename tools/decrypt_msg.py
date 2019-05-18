#!/usr/bin/env python

import base64
import json

MESSAGE = '''
your message
'''

KEY = 'your username'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(json.loads(''.join(result).replace("'", '"')))
