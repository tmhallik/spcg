#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To parse the command line parameters
import argparse

# To terminate the program w/ exit()
import sys

# To have a Python Enum
from enum import Enum

# EXPERIMENTAL: import a language template for testing
import lang_templates.template

# To access the GrammarTree that stores the script grammar
import grammar_tree

# To enable string-based imports
import importlib

# Used to check against in open_file() to protect script files
script_extensions = set(["s", "sc", "scg", "spcg"])

# Set the script file limit to 16M to limit input exploits
MAX_FILE_SIZE = 1000000

# A flag used to skip file write operations in the case of errors
FAILED_GENERATION = False

# To codify the language templates
lang_template_dict = { 'template' : \
  importlib.import_module("lang_templates.template"), }



# Modularly open a read-only input file and a writable output file
def open_file(filename, write=False):
  mode = "r"
  f = None
  if write:
    mode = "w"
#    print(filename)
  tmp_str = filename.split(".")
# Check for script file extensions
  if write and tmp_str[-1] in script_extensions:
      Y = 'y'
      i = input("It looks like you are trying to overwrite a script file (\'{0}\'). Are you sure? Type \'y\' to continue, anything else to abort.> ".format(filename))
      if i != Y:
        print("Terminating the code generator.")
        sys.exit()
  try:
    f = open(filename, mode)
  except FileNotFoundError:
    print("File \'{0}\' not found. Aborting the code generation.".format(filename))
    sys.exit(1)
  return f

# Parses command-line parameters and returns a dict of them
def parse_parameters():
  parser = argparse.ArgumentParser(description='Parse script_file target_lang to optional output_file', epilog='An example command: python3 spcg.py script_file c out_file')
  parser.add_argument('script_file', help='A SPCG script file to generate the code from.')
  parser.add_argument('target_lang', help='The target language')
  parser.add_argument('output_file', nargs='?', default='a.out', help='The file for the generated code (default: a.out).')

  args = parser.parse_args()  
  return vars(args)

# To add the indentation spaces
def add_spaces(n):
  tmp_str = ''
  for i in range(0, n):
    tmp_str = tmp_str + ' '
  return tmp_str

# Generates a program code output to a file from a script file
def main():

  # Produce a parameter dictionary 'd'
  d = parse_parameters()

  # Check the validity of the lang parameter
  lang_extension = lang_templates.template.structures[lang_templates.template.ElemEnum.LANG_FILE_EXTENSION]

  # Reference the right template language template - succeed/abort
  language_template_module = None
  try:
    language_template_module = importlib.import_module("lang_templates.{0}".format(d['target_lang']))
  except NameError:
    print('Language template \'{0}\' not found. Exiting.'.format(d['target_lang']))

  # Change the default output file to reflect the name of the script file, e.g. script_name.lang_ext
  if d["output_file"] == 'a.out':
    d["output_file"] = d["script_file"].split(".")[0]

  # Open the script file
  script_file = open_file(d["script_file"])

  output_filename = d["output_file"]+'.'+lang_extension

  # Open the output file
  output_file = open_file(output_filename, write=True)

  # Read the script file into a line list
  try:
    file_text = script_file.read().split('\n')
  except MemoryError as e:
    print(e)
    sys.exit()
  
  # Close the read script file
  script_file.close()

  # Contains the generated code lines
  code_lines = ''

  # Contains potential precode
  precode = ''

  # To shorten the references
  elem_enum_ref = language_template_module.ElemEnum
  structures_ref = language_template_module.structures

  # Loop over the script file line by line
  for line in file_text:
    # Split the line to read the first command symbol
    param_list = []
    tmp_split = line.split(' ')
    tmp_dict_list = []
    for i in range(0, len(tmp_split)):
      # Read the command symbol to guide the parsing
      try:
        # Deal with the trailing, free-form arguments
        if len(tmp_dict_list) > 0 and 'PARAM' in tmp_dict_list[-1]:
          tmp_dict_list.append(tmp_dict_list[-1]['PARAM'])
          if 'end' in tmp_dict_list[-1]:
            tmp_str0 = ''
            for j in range(i, len(tmp_split)):
              tmp_str0 = tmp_str0 + tmp_split[j]
              if j < len(tmp_split):
                tmp_str0 = tmp_str0 + ' '
            param_list.append(tmp_str0)
          code_lines = code_lines + add_spaces(structures_ref[elem_enum_ref.INDENT_LEVEL_DEFAULT]) + language_template_module.commands[tmp_dict_list[-1]['end']](param_list) + '\n'
        else:
          # Keep parsing the command symbols
          tmp_dict_list.append(grammar_tree.grammar[tmp_split[i]])
      except KeyError:
        # To disqualify the generation
        print('Error: grammar symbol \'{0}\' not found.'.format(tmp_split[0]))
        FAILED_GENERATION = True
      
        # Continue to collect all of the errors

  # Compile the code file template i.e. code generate
#  print(structures_ref[elem_enum_ref.TEMPLATE_BASE])
  tmp_generate = structures_ref[elem_enum_ref.TEMPLATE_BASE].format(CODE = code_lines, PRECODE = precode)
#  print(tmp_generate)
  written_count = output_file.write(tmp_generate)
  print("{0} bytes were written to {1}".format(written_count, output_filename))
  output_file.close()
  

#  print(d)
#  print(d['output_file'])


if __name__ == "__main__": main()
