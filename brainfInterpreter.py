import colorama

def run(program):
    program = "".join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'],program)) #deal with disallowed characters
    for line in _iterRunner(program):
        pass

def _iterRunner(program,position=0,variables=[0],pointer=0):
    variables = [0]
    while position < len(program):
        match program[position]:
            case ">":
                pointer += 1
                if len(variables) <= pointer:
                    variables.append(0)
            case "<":
                if pointer > 0:
                    pointer -= 1
                else:
                    raise ValueError("Invalid pointer. you were at 0 and moved to the left")
            case "+":
                variables[pointer] += 1
            case "-":
                variables[pointer] -= 1
            case ".":
                print(chr(variables[pointer]),end="")
            case ",":
                variables[pointer] = ord((input("")+"\x00")[0])
            case "[":
                if variables[pointer]==0:
                    brackets = 1 #find matching close
                    for i in range(position+1,len(program)):
                        match program[i]:
                            case "[":
                                brackets+=1
                            case "]":
                                brackets-=1
                        if brackets==0:
                            position=i
                            break
                    else:
                        raise ValueError(f"never found a ] at position {position}")
            case "]":
                brackets = 1 #find matching open
                for i in range(1,position+1):
                    match program[position-i]:
                        case "[":
                            brackets-=1
                        case "]":
                            brackets+=1
                    if brackets==0:
                        position=position-i-1
                        break
                else:
                    raise ValueError(f"never found a [ at position {position}")
            
        position+=1
        yield (position,variables,pointer)


def printMem(mem,pointer):
    print("[",end="")
    for i in mem[:pointer]:
        print(f"{i}, ",end="")
    print(f"{colorama.Back.YELLOW}{colorama.Fore.BLACK}{mem[pointer]}{colorama.Style.RESET_ALL}",end="")
    if pointer == len(mem)-1:
        print("]")
        return
    
    print(", ",end="")
    for i in mem[pointer+1:-1]:
        print(f"{i}, ",end="")
    print(mem[-1],"]")

def debug(program):
    #debug points should be marked with ! exclamation marks
    program = "".join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-', '!'],program)) #deal with disallowed characters
    running = True
    if "!" not in program:
        running = False
        program = " "+program
    lastCommand = None
    for line in _iterRunner(program):
        if running:
            if line[0]>=len(program):
                return
            if program[line[0]]=="!":
                running = False
                print(f"stopped at command #{line[0]}")
            else:
                continue
        if line[0]>=len(program):
            return
        print("\n\nmemory: ",end="")
        printMem(line[1],line[2])
        print(program[(line[0]-20) if line[0]>20 else 0:line[0]]+colorama.Back.YELLOW+colorama.Fore.BLACK+program[line[0]]+colorama.Style.RESET_ALL+program[line[0]+1:line[0]+20])
        command=input(": ")
        while True:
            match command:
                case "n":
                    break
                case "c":
                    running= True
                    break
                case "":
                    if lastCommand:
                        command = lastCommand
                    else:
                        print("command wasn't passed")
                        command=input(": ")
                case _:
                    print("command wasn't passed")
                    command=input(": ")
        lastCommand=command

if __name__ == "__main__":
    run("++[-]++++++++++++++++++++.")
    run("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
    print()
    debug("++++++++[>++++[>++>+++<<-]>+>+[<]<-]>>.>+.")