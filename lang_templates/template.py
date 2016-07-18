# template - a documented example code generation template
# Demonstrates the language template format with 'C' template

# Naming scheme: [lang].py , where lang is how it can be invoked as a lang parameter in command line

# The element list used by the code generation process

class ElemEnum:
    TEMPLATE_BASE, INDENT_LEVEL_DEFAULT, PRINT, READ,\
    VARIABLE, FUNCTION, LANG_FILE_EXTENSION = range(7)
   
structures = {

 #TEMPLATE_BASE describes the coding "frame" (?) that the compiler requires it to have
  ElemEnum.INDENT_LEVEL_DEFAULT : 2,
  ElemEnum.TEMPLATE_BASE : '#include<stdio.h>\n{PRECODE}\nint main() {{\n{CODE}\n  return 0;\n}}',
  ElemEnum.LANG_FILE_EXTENSION : 'cc',
}


def PRINT_process(param_list):
  command_template = 'printf(\'{PARAM}\');'
  tmp_str = ''
  for i in param_list:
    tmp_str = tmp_str + i
    if len(param_list) > 0 and i is not param_list[-1]:
      # Separate the params with a delimiter
      tmp_str = tmp_str + ' '
  return command_template.format(PARAM = tmp_str)

def READ_process(param_list):
  tmp_str = ''
  command_template = 'gets({PARAM});'
  if len(param_list) > 0:
    tmp_str = param_list[-1]
  return command_template.format(PARAM = tmp_str)


commands = {
  
  # All parameters are already converted into strings
  
  ElemEnum.PRINT : PRINT_process,
  ElemEnum.READ : READ_process,
  'PRINT' : PRINT_process,
  'READ' : READ_process

}


