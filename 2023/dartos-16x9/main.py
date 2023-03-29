import os

def newFiles(fname):
    with open(f"{fname[0:-4]}.jpg", 'w') as f:f.write(f"../dartos/{fname}")

fileNames = os.listdir("../dartos")

for fname in fileNames:
    if(fname.endswith("-16x9.jpg")):
        newFiles(fname)


