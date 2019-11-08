#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

def generate_dict(list, key):
  response = {}
  for item in list:
    response[item[key]] = item
  return response    

if __name__ == '__main__':
  fields = {
    'list': {
      'required': True, 
      'type': "list"
    },
    'key': {
      'required': True, 
      'type': "str"
    }
  }
  
  module = AnsibleModule(argument_spec=fields)
  list = module.params['list']
  key = module.params['key']
  response = generate_dict(list, key)
  module.exit_json(**response)