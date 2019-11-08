#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

def generate_dict(list, key, list_name):
  response = {}
  for item in list:
    if response.get(item[key]) is None:
      item_to_be_appended = item.copy()
      del item_to_be_appended[key]
      response[item[key]] = {
        list_name: [item_to_be_appended]
      }
    else:
      item_to_be_appended = item.copy()
      del item_to_be_appended[key]
      response[item[key]][list_name].append(item_to_be_appended)
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
    },
    'list_name': {
      'required': True, 
      'type': "str"
    }
  }
  
  module = AnsibleModule(argument_spec=fields)
  list = module.params['list']
  key = module.params['key']
  list_name = module.params['list_name']
  response = generate_dict(list, key, list_name)
  module.exit_json(**response)