#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To parse the command line parameters
import argparse


def main():
  parser = argparse.ArgumentParser(description='Parse script_file target_lang to optional output_file', epilog='An example command: python spcg.py script_file c out_file')
  parser.add_argument('script_file', help='A SPCG script file to generate the code from.')
  parser.add_argument('target_lang', help='The target language')
  parser.add_argument('output_file', nargs='?', default='a.out', help='The file for the generated code (default: a.out).')

  args = parser.parse_args()
  
  d = vars(args)
  print(d)
#  print(d['output_file'])


if __name__ == "__main__": main()
