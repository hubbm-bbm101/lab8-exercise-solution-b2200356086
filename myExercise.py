import sys
x=sys.argv[1]
y=sys.argv[2]
students={}
with open(x,"r") as f:
    lines=f.readlines()
for line in lines:
    linex=line.split(":")
    u=linex[1].split()
    students[linex[0]]=linex[1]

for z in y.split(","):
    try:
        students[z]
    except:
        print("No record of ", z,"was found!", end="\n")
    else:
        print("Name:",z,",University:",students[z],end="")

