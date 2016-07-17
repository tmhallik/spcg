# template - a documented example code generation template
# Demonstrates the language template format with 'C' template

# Naming scheme: [lang].py , where lang is how it can be invoked as a lang parameter in command line

from enum import Enum

# The element list used by the code generation process

class ElemEnum(Enum):
    TEMPLATE_BASE, INDENT_LEVEL_DEFAULT, PRINT, READ,\
    VARIABLE, FUNCTION, LANG_FILE_EXTENSION = range(7)
   
structures = {

 #TEMPLATE_BASE describes the coding "frame" (?) that the compiler requires it to have
  ElemEnum.INDENT_LEVEL_DEFAULT : 2,
  ElemEnum.TEMPLATE_BASE : '#include<stdio.h>\n{PRECODE}\nint main() {\n{CODE}\n  return 0;\n}',
  ElemEnum.LANG_FILE_EXTENSION : 'cc',
}



commands = {
  
  # All parameters are already converted into strings
  
  ElemEnum.PRINT : 'printf({PARAM});'
}

def PRINT_process():
  pass


