#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To parse the command line parameters
import argparse

# To terminate the program w/ exit()
import sys

# EXPERIMENTAL: import a language template for testing
import lang_templates.template

# Used to check against in open_file() to protect script files
script_extensions = set(["s", "sc", "scg", "spcg"])

# Check for script file extensions

# Modularly open a read-only input file and a writable output file
def open_file(filename, write=False):
  mode = "r"
  f = None
  if write:
    mode = "w"
#    print(filename)
  tmp_str = filename.split(".")
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

# Generates a program code output to a file from a script file
def main():
  # Produce a parameter dictionary 'd'
  d = parse_parameters()

  # Check the validity of the lang parameter
  lang_extension = lang_templates.template.structures[lang_templates.template.ElemEnum.LANG_FILE_EXTENSION]

  # Change the default output file to reflect the name of the script file, e.g. script_name.lang_ext
  if d["output_file"] == 'a.out':
    d["output_file"] = d["script_file"].split(".")[0]

  # Open the script file
  script_file = open_file(d["script_file"])

  # Open the output file
  output_file = open_file(d["output_file"]+'.'+lang_extension, write=True)

#  print(d)
#  print(d['output_file'])


if __name__ == "__main__": main()
