#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

def generate_dict(list_1, list_2, key):
  response = {}
  for item in list_1:
    for inner_item in list_2:
      if item[key] == inner_item[key]:
        new_item = {}
        new_item.update(item)
        new_item.update(inner_item)
        response[item[key]] = new_item
        continue
  return response    

if __name__ == '__main__':
  fields = {
    'list_1': {
      'required': True, 
      'type': "list"
    },
    'list_2': {
      'required': True, 
      'type': "list"
    },
    'key': {
      'required': True, 
      'type': "str"
    }
  }
  
  module = AnsibleModule(argument_spec=fields)
  list_1 = module.params['list_1']
  list_2 = module.params['list_2']
  key = module.params['key']
  response = generate_dict(list_1, list_2, key)
  module.exit_json(msg=response)