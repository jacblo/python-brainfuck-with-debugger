# python-brainfuck-with-debugger
python implementation of brainfuck with a debugger

## Setup
python 3.10 is required (for match case statements. if you want to use earlier versions see porting section at the end of the README)
install colorama or run -
```
python -m pip install -r requirements.txt
```
to install automatically

## Usage
simple run - 
```python
import brainfInterpreter

brainfInterpreter.run("""
Code:        Psudocode:
++++++++    add 8 to cell#0 (for loop)
[           start looping (if the cell the pointer is on is 0 it will end the loop)
>++++       add 4 to cell#1 (for inner loop)
[           inner loop (if the cell the pointer is on is 0 it will end the loop)
>++         add 2 to cell#2 (2*4*8 because of loops)
>+++        add 3 to cell#3 (3*4*8 because of loops)
<<          go back to cell#1
-           subtract one from cell#1 (loop)
]           goto/loop command end
>+          go to cell#2 and add 1 (1*8 because of loop)
>+          go to cell#3 and add 1 (1*8 because of loop)
[<]         go back to the first cell you find which is 0
            (that being cell#1 from the previous loop that ran 4 times)
<-          subtract 1 from the next cell to the left
]           goto/loop command end
>>.         print the cell 2 to the right (cell#2)
>+.         add one to the cell on the right and print it (cell#3)""")
```
which prints - 
```
Hi
```
symbols that arent []<>+-,. and ! if it's the debugger, are ignored as if they were comments


For teminal debugger - 

```python
import brainfInterpreter

brainfInterpreter.debug("+++++!+++[>++++[>++>!+++<<-]>+>+[<]<-]>>.>+.")
```
Breakpoins are marked with an exclamation mark (!)

Type in n to step to the next command

Or type c to jump to the next breakpoint

If no breakpoints are set, it will start the debugger at the beginning of the program.

The debugger allowes you to view all variables. Pointer position and position in program are highlighted.


## Fine control
If you want fine control over the debugger use the _iterRunner function.
```python
import brainfInterpreter

def main():
  for command in _iterRunner("+++++!+++[>++++[>++>!+++<<-]>+>+[<]<-]>>.>+."):
    print(line) #every time a command is run it will yield status in the following format - (position, variables, pointer_position)

if __name__ == "__main__":
  main()
```
_iterRunner takes the following arguments - program, position (starting position - default: 0) ,variables (starting variables - default: [0]) ,pointer (starting pointer - default: 0)

all optional arguments are to give you fine control over how the code runs, so for instance if you want to have a program be able to stop the code at some point and run an extra line in there, you can give the _iterRunner the variables and position from the code where you stopped it and tell it to run with a added line


## Porting to earlier versions of python
Python 3.10 includes match case statments which vastly speed up if elif else chains for many tasks. In order to port the code to earlier versions of python you must replace all match case statments with if elif else chains.
for instance - 
```python
match x:
  case 24:
    print("x was 24")
  
  case 10:
    print("x was 10")
  
  case 15:
    print("x was 15")
  
  case _:
    print("x wasn't 10, 24 or 15")
```
would turn into - 
```python
if x == 24:
  print("x was 24")

elif x == 10:
  print("x was 10")

elif x == 15:
  print("x was 15")

else:
  print("x wasn't 10, 24 or 15")
```
all cases must be turned into if/elif statements, apart from the optional case _: which turns into an else statment

##### warning if elif elif else is substantially slower than match case statements. so expect slowdowns with older versions of python
