# Generates pwd list based on parameters

# !NotJosh
def changechar(location, pwd, newchar):
    pwd[location] = newchar
    return pwd


def main():
    print("Let's generate some passwords!")
    charcount = int(input("How long is the password (fixed length): "))
    lowercase = False
    uppercase = False
    symbols = False
    numbers = False
    combos = 0
    totalslots = 0

    lowercasealpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercasealpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbolsalpha = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}',
                    ']', '|', "\\", ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/']
    numbersalpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    masterlist = []

    if input("Lowercase? y/n : ") == "y":
        lowercase = True
        totalslots += 26
        masterlist += lowercasealpha
    if input("Uppercase? y/n : ") == "y":
        uppercase = True
        totalslots += 26
        masterlist += uppercasealpha
    if input("Symbols? y/n : ") == "y":
        symbols = True
        totalslots += 32
        masterlist += symbolsalpha
    if input("Numbers? y/n : ") == "y":
        numbers = True
        totalslots += 10
        masterlist += numbersalpha

    partpwdstr = ""
    partpwd = []
    if input("Do you know any characters? : ") == "y":
        partpwdstr = str(input("Write out password with '-' in unknown character places: "))
        partpwd = [char for char in partpwdstr]
        print(partpwdstr)
        print(partpwd)

    if len(partpwdstr) == 0:
        totalcombos = pow(totalslots, charcount)

        print("Total combinations generating: " + str(totalcombos))
        print("Masterlist: " + ''.join(masterlist))

        # 26 upper case
        # 26 lower case
        # 10 numbers
        # 32 symbols

        thepwd = []
        totallist = []
        finaltotallines = []

        # init of pwd
        for x in range(0, charcount):
            thepwd += masterlist[0]

        # ''.join(list)  returns the string of a list for totallist

        for x in range(0, totalcombos - 1):
            combos += 1
            if (combos >= 1000000):
                print(x)
                combos = 0
            finaltotallines += ''.join(thepwd + list("\n"))
            tempint = 0
            currentchar = thepwd[tempint]

            while currentchar == masterlist[len(masterlist) - 1]:
                thepwd = changechar(tempint, thepwd, masterlist[len(masterlist) - 1])
                tempint += 1
                currentchar = thepwd[tempint]

            # this line changes the letter designated by moving it one up the scale
            thepwd = changechar(tempint, thepwd, masterlist[masterlist.index(thepwd[tempint]) + 1])

            # resets every slot before it

            if tempint != 0:
                for spot in range(0, tempint):
                    thepwd = changechar(spot, thepwd, masterlist[0])

        finaltotallines += ''.join(thepwd + list("\n"))
        f = open("pwdlist.txt", "a")
        f.writelines(finaltotallines)
        f.close()
    else:
        tempcharcount = charcount
        for char in partpwd:
            if char != "-":
                tempcharcount -= 1
        totalcombos = pow(totalslots, tempcharcount)
        print("Total combinations generating: " + str(totalcombos))
        print("Masterlist: " + ''.join(masterlist))

        # 26 upper case
        # 26 lower case
        # 10 numbers
        # 32 symbols

        thepwd = []
        totallist = []
        finaltotallines = []

        # init of pwd
        for x in range(0, charcount):
            if(partpwd[x]=="-"):
                thepwd += masterlist[0]
            else:
                thepwd+=partpwd[x]

        # ''.join(list)  returns the string of a list for totallist
        lockedinchars = []

        for char in thepwd:
            if(char!=masterlist[0]):
                lockedinchars.append("True")
            else:
                lockedinchars.append("False")

        print(lockedinchars)
        for x in range(0, totalcombos - 1):
            combos += 1
            if (combos >= 1000000):
                print(x)
                combos = 0
            finaltotallines += ''.join(thepwd + list("\n"))
            tempint = 0
            currentchar = thepwd[tempint]

            #creates boolean list of locked in chars...




            while currentchar == masterlist[len(masterlist) - 1] or lockedinchars[tempint]=="True":
                #thepwd = changechar(tempint, thepwd, masterlist[len(masterlist) - 1])
                tempint += 1
                currentchar = thepwd[tempint]

            # this line changes the letter designated by moving it one up the scale
            thepwd = changechar(tempint, thepwd, masterlist[masterlist.index(thepwd[tempint]) + 1])

            # resets every slot before it

            if tempint != 0:
                for spot in range(0, tempint):
                    if not lockedinchars[spot]=="True":
                        thepwd = changechar(spot, thepwd, masterlist[0])

        finaltotallines += ''.join(thepwd + list("\n"))
        f = open("pwdlist.txt", "a")
        f.writelines(finaltotallines)
        f.close()


if __name__ == '__main__':
    main()
