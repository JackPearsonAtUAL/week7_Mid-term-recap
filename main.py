"""
11/10/2025 (UK)
Terminal Chat Boxes
Jack Pearson
"""
corresponding = True

def CheckUser():
    e = True
    i = input("User number please")
  
    while e == True:
        try:
            i = int(i)
            e = False
        except:
            print("Error please put in just a positive intager") 
    
    return "usr"+str(i)

def ConcatMessage(m):
    phrase = " "
    for w in range(len(m)):
        phrase += m[w] + " "
    return phrase

def MessageBorder(user, text):
    if user == "usr0":
        """
        Code from Bunyk on Stack Overflow
        ref: https://stackoverflow.com/questions/20756516/python-create-a-text-border-with-dynamic-size
        """
        lines = text.splitlines()# split the inputted text into list
        width = max(len(s) for s in lines)# make the texbox width equal to the largest line in the "lines" list
        res = ['    * ' + '-' * (width-2) + ' *']# creates an array and the top border for the text, with an indent to denote the main user

        # loop iterates through each entry in the "lines" list
        for s in lines:
            res.append('    │' + (s + ' ' * width)[:width] + '│')# puts text inside the border, with an indent to denote the main user
        res.append('    * ' + '-' * (width-2) + ' *')# creates the bottom border for the text, with an indent to denote the main user
        return '\n'.join(res) # sends back the list as a joined string using new line to seperarte them
    else:
        lines = text.splitlines()# split the inputted text into list
        width = max(len(s) for s in lines)# make the texbox width equal to the largest line in the "lines" list
        res = ['+ ' + '-' * (width-2) + ' +']# creates an array and the top border for the text
        
        # loop iterates through each entry in the "lines" list
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')# puts text inside the border
        res.append('+ ' + '-' * (width-2) + ' +')# creates the bottom border for the text
        return '\n'.join(res)# sends back the list as a joined string using new line to seperarte them

def MessageInput(messaging):
    while messaging == True:
        
        s = input("")# get input

        
        ident = s.split()# put the inputted text into a list of words
        user = ident[0]# gets the user ID
        
        """
        Check the identifier is using usr, 
        the number doesn't matter just yet
        if there is no usr, ask for one
        """
        if user[:3] != "usr":
            user = CheckUser()
        
        #check the user identifier
        #identifier is 0 for left, anything else for the right
        if user == "usr0" and len(ident) > 1:
            if ident[1] != " " and ident[1] != "":
                del ident[0]# removes the ID from the eventual string
                """
                outputs the text using the MessageBorder() function, 
                with the user denoting the format
                and ConcatMessage(ident) gives the text
                """
                print(MessageBorder(user, ConcatMessage(ident)))
            else:
                messaging = False # ends messaging loop
                print("exit")
        elif len(ident) > 1:
            if ident[1] != " " and ident[1] != "":
                del ident[0]# removes the ID from the eventual string
                """
                outputs the text using the MessageBorder() function, 
                with the user denoting the format
                and ConcatMessage(ident) gives the text
                """
                print(MessageBorder(user, ConcatMessage(ident)))
            else:               
                messaging = False # ends messaging loop
                print("exit")
                
        if messaging == True:
            MessageInput(True)# repeat the texting function

print("To print a message you must prefix it with\n'usr'+usernumber then enter a space")
MessageInput(corresponding)
