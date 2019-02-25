import json
import os

fileDirectory = "/Users/ethansong/Documents/Pycharm Projects/HollywoodEthan/part2_output.dat"
outputNegDirectory = "/Users/ethansong/Documents/Pycharm Projects/HollywoodEthan/part3_neg.csv"
outputPosDirectory = "/Users/ethansong/Documents/Pycharm Projects/HollywoodEthan/part3_pos.csv"

data = open(fileDirectory, "r")
outputNeg = open(outputNegDirectory, "w")
outputPos = open(outputPosDirectory, "w")
for lines in data:
    score = float(lines[lines.find("[")+1:lines.find(",")])
    print(score)
    if(score<0):
        dataToWrite = (lines[lines.find("n: [") + 4:lines.find("]}}")])
        outputNeg.writelines((dataToWrite))
        outputNeg.writelines("\n")
    else:
        dataToWritePos = (lines[lines.find("n: [") + 4:lines.find("]}}")])
        outputPos.writelines((dataToWritePos))
        outputPos.writelines("\n")




