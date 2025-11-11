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
        lines = text.splitlines()
        width = max(len(s) for s in lines)
        res = ['* ' + '-' * (width-2) + ' *']
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')
        res.append('* ' + '-' * (width-2) + ' *')
        return '\n'.join(res)
    else:
        lines = text.splitlines()
        width = max(len(s) for s in lines)
        res = ['+ ' + '-' * (width-2) + ' +']
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')
        res.append('+ ' + '-' * (width-2) + ' +')
        return '\n'.join(res)

def MessageInput(messaging):
    while messaging == True:
        #get input
        s = input("")
        
        ident = s.split()
        user = ident[0]
        
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
                del ident[0]
                print(MessageBorder(user, ConcatMessage(ident)))
            else:
                messaging = False
                print("exit")
        elif len(ident) > 1:
            if ident[1] != " " and ident[1] != "":
                del ident[0]
                print(f"{MessageBorder(user, ConcatMessage(ident)):>10}")
            else:
                print("exit")
                messaging = False
        
        MessageInput(messaging)

print("To print a message you must prefix it with\n'usr'+usernumber then enter a space")
MessageInput(corresponding)
