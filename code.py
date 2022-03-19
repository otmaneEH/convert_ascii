# convert_ascii
convert_ascii
asci = input("entre number ou char = ")


def chr_asci ():
    global asci
    if (isinstance(asci, int)==True):
        return print( chr(asci))
    elif (isinstance(asci, str)==True):
        return ord(asci)
    
print(chr_asci())
