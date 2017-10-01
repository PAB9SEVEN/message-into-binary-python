message=raw_input("enter the message to be converted")
coded=""
for letter in message:
    if(letter == " "):
        coded+=" " 
    else:
        y=bin(ord(letter))
        x=y[2:]
        coded+=x + " "
print coded
        
