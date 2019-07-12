#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

def generate_dict(dict_1, dict_2):
  for key, value in dict_1.items():
    if dict_2.get(key) is not None:
      dict_1[key].update(dict_2[key])
  return dict_1 

if __name__ == '__main__':
  fields = {
    'dict_1': {
      'required': True, 
      'type': "dict"
    },
    'dict_2': {
      'required': True, 
      'type': "dict"
    }
  }
  
  module = AnsibleModule(argument_spec=fields)
  dict_1 = module.params['dict_1']
  dict_2 = module.params['dict_2']
  response = generate_dict(dict_1, dict_2)
  module.exit_json(msg=response)