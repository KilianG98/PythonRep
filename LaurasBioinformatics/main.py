import Pattern

if __name__ =="__main__":
    flag = False
    iFileName = input("Pls enter Inputfilenname in .txt format: ")
    patt = input("Pls enter restriction pattern: ")
    circ = input("Pls enter True, if DNA is circular ")

    if circ == "True" :
        flag = True
    with open ("outfile.txt", "w")as outfile:
        with open(iFileName, "r") as f:
            for line in f:
                sol=(Pattern.pattern(line, patt, flag))
                outfile.write("cuts: ")
                outfile.write("".join(map(str, sol[0])))
                outfile.write("fragment lengths: ")
                outfile.write("".join(map(str, sol[1])))


