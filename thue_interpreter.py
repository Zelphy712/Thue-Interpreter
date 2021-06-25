#!/usr/bin/python

import sys
import random

class thue_interpreter:
    def __init__(self,fileName = "",verbose = False):
        self.program = []
        self.fileName = fileName
        self.state = ""
        self.verbose = verbose

    def setFileName(self,fileName):
        self.fileName = fileName

    def loadProgramFromFile(self):
        if self.fileName != "":
            file = open(self.fileName,"r")
            for line in file:
                if line.rstrip('\n') != "":
                    self.program.append(line.rstrip('\n'))
            file.close()
            if self.program[len(self.program)-2] == "::=":
                self.state=self.program.pop()
                self.program.pop()
            else:
                print(f"Syntax error: No end program terminator (::=) found on line {len(self.program)-2}")
                sys.exit()

    def runLine(self):
        validLines = []
        for line in self.program:
            if line.split("::=")[0] in self.state:
                validLines.append(line)
        if len(validLines) == 0:
            print(f"Final state = {self.state}")
            sys.exit()
        else:
            if self.verbose:
                print(f"State = {self.state}")
            line = validLines[random.randrange(len(validLines))]
            if "~" in line.split("::=")[1]:
                print(line.split("::=")[1].replace("~",""))
                self.state = self.state.replace(line.split("::=")[0],"")
            elif line.split("::=")[1] == ":::":
                inputStr = str(input("The program has requested input:"))
                self.state = self.state.replace(line.split("::=")[0],inputStr)
            else:    
                self.state = self.state.replace(line.split("::=")[0],line.split("::=")[1])

            


def main():
    file = ""
    verbosity = False
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == "-f":
            # print(sys.argv[i+1])
            file = sys.argv[i+1]
            i+=1 #skip the next value
        elif sys.argv[i] == "-v":
            verbosity = True
            pass
            #show a line for each step of the program
        else:
            pass
    thue = thue_interpreter(file,verbosity)
    thue.loadProgramFromFile()
    while True:
        thue.runLine()

main()