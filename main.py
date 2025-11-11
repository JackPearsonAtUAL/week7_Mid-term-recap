"""
11/10/2025 (UK)
Terminal Chat Boxes
Jack Pearson
"""

def ConcatMessage(m):
    phrase = ""
    for w in range(len(m)):
        phrase += m[w]
    
    return phrase

def MessageInput():
    #get input
    
    print("While using please input identifier then text")
    s = input("")
    
    ident = s.split()
    user = ident[0]
    
    """
    Check the identifier is using usr, 
    the number doesn't matter just yet
    if there is no usr, ask for one
    """
    if user[0, 2] != usr:
        e = True
        i = input("User number please")
        
        while e == True:
            try:
                i = int(i)
                e = False
            except:
                print("Error please put in just a positive intager") 
    
    #check the user identifier
    #identifier is 0 for left, anything else for the right
    if ident[0] == "usr1":
        del ident[0]
        print(ConcatMessage(ident), user)
    else:
        del ident[0]
        print(f"{ConcatMessage(ident), user:>10}")
