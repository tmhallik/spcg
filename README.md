# spcg
Scripted Program Code Generator -- creates a source code programs to a target language from line-by-line parsed script

The input-output presentation: script, lang -> program_code_on_lang

This is my inspirational pro bono project to show case the automatization potential of the repetitious dumb work of a
programmer and ironically elimate my own jobs. LOL Seriously though, I realized that I have certain typos per lines ratio
that I cannot eliminate UNLESS I make ze evil maschins to do it, especially when switching from one language to another.
As the basic tasks are mostly same on every language, it would be best if the programmer focused on the design and the
computer generated the code. Practically, I'll try to create a couple of basic functions such as:
 *printing
 *reading input
 *variable table to store references
 *simple (unnested) functions
 
 For the script symbol, I will try to steal them from some simple-yet-cool languages like Pascal.
 
 Optimizing is not my focus. I want the generated code to be easy to read and frankly most people for what I know
 do not even know what optimization-related symbols like "pragma" is. Simplicity and doing more with less is the best way
 to optimize a business across the board.
 
 I'll try to make it look call compilers (an option flag like --run-compiler or even specific --compiler-path for the
 ones with multiple installed compiler versions), so that I can test run the generated code and collect the compiler
 / shell output. There will be a simple scripting language with examples and stuff to make it as extremely laymanish. 
 I decided to initially implement language support for Python and Haskel first. Mostly because I'll try the super simple
 python first to see if my interpreter works and then focus on learning about Haskell implementations as I want to learn
 me some functional programming. Even Assembler does do immutable variables, so a language like Haskell that has a good
 practice of mutable variants feels very intriguing. I'll have fun making myself perma-unemployed. :D

As a contribution policy, feel free. If you add new files i.e. append code, I'll accept and credit you. In case of editing
my mediocre code, I want to try it first 

The Unlicense statement:

"This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>"

