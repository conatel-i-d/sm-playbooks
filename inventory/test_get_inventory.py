#!/usr/bin/env python

from ansible.module_utils import urls
import json
result = urls.open_url("https://api/api/switch/inventory")
inventory = json.load(result.read())["item"]
print(json.dumps(inventory))