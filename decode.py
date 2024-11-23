#get cipher from user and converts it to lower case
cipher = str(input("Write the cipher you wish to bruteforce:\n")).lower()

#variables
shift = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i  in range(0,25):
    #decoded string
    decode = ""

    #next shift
    shift += 1

    #loop throught each letter
    for letter in cipher:
        if letter == "":
            decode = decode + ""
        else:
            decode = decode + alphabet[alphabet.index(letter) + shift]

    #return result      
    print("The cipher shifted by {} is:\n".format(shift),decode,"\n")
