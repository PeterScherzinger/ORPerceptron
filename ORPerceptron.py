### Four-Input OR-Training Using a Single-Layer Perceptron Network ###
### Written by Peter Scherzinger, 10148046                         ###
from random import uniform
import re

def parseText():
    ## Open the file with read only permit
    f = open('in.txt', "r")

    ## use readlines to read all lines in the file
    ## The variable "lines" is a list containing all lines
    lines = f.readlines()
   
    

## close the file after reading the lines.
    f.close()
    return lines

def step(num,thresh):
    
    if num > thresh:
        return 1
    else:
        return 0

def changeWeights(inputs, weights, error, rate):
    print "weights were: ", weights
    for i in range(0,4):
        weights[i]=round(weights[i]+ (rate*float(inputs[i])*float(error)) ,2)

def output(ans):
    for i in ans:
        text_file = open("out.txt", "a")
        text_file.write("["+str(i)+"]")
        text_file.write("\n")

def expected(inputs):
    sums=0
    for i in inputs:
        sums=sums+int(i)
    if sums>0:
        return 1
    
    return 0
    

def solve(inputs,weights,hits,answers):
 
    x=0
    print inputs
    for i in range(0,4):
        x+=float(inputs[i])*weights[i]
    #print x
    ans=step(x,0)
    expec=expected(inputs)
    print "perceptron output: ", ans
    print "expected output", expec
    if ans==expec:
        print "success"
        answers.append(ans)
        #count hits
        return 1
        
        
    else:
        changeWeights(inputs,weights,1,.1)
        return 0
    

def setWeights():
    weights=[]
    for i in range(0,4):
        w=uniform(-.5, .5)
        w=round(w,2)
        weights.append(w)
    
    return weights

def main():
    problems=parseText()
    answers=[]

    
    hits=0
    for i in problems:
        x=i
        x=x.strip('[')
        
        x=x.strip('\n')
        x=x.strip(']')
        x=x.split(' ')
        hits+= solve(x,weights,hits,answers)
        print "hits are: ", hits
        
    if hits==len(problems):
        print "enoch success"
        output(answers)
    else:
        main()
        
if __name__ == "__main__":
        weights=setWeights()
        main()
