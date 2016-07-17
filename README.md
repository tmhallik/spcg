# spcg
Scripted Program Code Generator -- creates a source code programs to a target language from line-by-line parsed script

The input-output presentation: script, lang -> program_code_in_lang

It is a software that converts a simple script key words into target programming language. The following things are going
to be implemented:

* printing text
* reading input
* variable table to store references
* simple functions

The script notation will be kept readable by utilizing exclusively alphanumeric notation. It is notable that alphanumeric
characters are easy to type with a virtual keyboard without constantly having to open a special character menu.
 
TODO: add the command list with the command symbols and extensive examples here

TODO: add a specification to the Scripted Code Generator (.scg) file type. It is text/plain and it would help to place a check for the file extension to make it more difficult to accidentally rewrite the script files with the output.

An Extra Feature: Make a GUI menu-tool to generate the script files and exterminating the last place to commit a time-wasting typo.

Optimizing is not a focus. An auto-generated code is repetitive and some compilers have methods to optimize that during
compiling time.
 
An Advanced Extra Feature: a feature to test the generated code by compiling it and running it, with a possibility to test it against expected output file and to diff the program output and the expected output.

Contribution policy: fork away in any cases that do not involve a minor fixes like typos and such. For anything bigger than that, you should use this repo as a base and rename your own fork, mostly because this project is not intended to be anything major and more like a brief learning project.

This software is licensed under Unlicensed -- no credit line required.
