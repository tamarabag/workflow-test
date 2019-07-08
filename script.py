import math
import os
import sys

import requests

# print(sys.version)
print(sys.executable)


def Hello(who='World'):
    return f"Hello {who}"


name = input('your name?')
# r = requests.get("http://www.google.com")
# print(r.status_code)

print(Hello(name))
