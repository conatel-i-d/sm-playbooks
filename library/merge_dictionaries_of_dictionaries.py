#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

def merge_dictionary_elements(dict_1, dict_2):
  # Function that returns the result of merging the contents of each key in dict_1 and dict_2.
  # The function assumes that the content of each key is also a dictionary.
  # After the followign transformation, the returned dictionary will be dict_1.

  # Update the content of all dict_1 keys that are also present in dict_2
  for key in dict_1:
    if dict_2.get(key) is not None:
      dict_1[key].update(dict_2[key])
  # Create in dict_1 all the keys that are only present in dict_2
  for key in dict_2:
    if dict_1.get(key) is None:
      dict_1[key] = dict_2[key]
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
  response = merge_dictionary_elements(dict_1, dict_2)
  module.exit_json(msg=response)