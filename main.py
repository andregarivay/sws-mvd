"""
Spreetail Work Sample
Multi Value Dictionary
Andre Garivay
"""

"""
Function: KEYS
Returns all the keys in the dictionary. Order is not guaranteed.
RETURNS: List of keys
"""
def keys():
    counter = 1
    if len(dict) == 0:
        print("(empty set)")
        return
    for key in dict:
        print(str(counter) + ") " + str(key))
        counter += 1

"""
Function: MEMBERS
Returns the collection of strings for the given key. Return order is not guaranteed. Returns an error if the key does not exists.
PARAM: Key
RETURNS: List of members or ERROR
"""
def members(key):
    counter = 1
    if key not in dict:
        print("ERROR, key does not exist.")
    else:
        members = dict.get(key)
        for i in range(len(members)):
            print(str(counter) + ") " + members[i])

"""
Function: ADD
Adds a member to a collection for a given key. Displays an error if the member already exists for the key.
PARAM: Key
PARAM: Member
RETURNS: 'Added' or ERROR
"""
def add(key, member):
    if (key in dict and member in dict[key]):
        print("ERROR, member already exists for key")
    else:
        if key in dict:
            dict[key].append(member)
        else:
            dict[key] = [member]
        print("Added")


"""
Function: REMOVE
Removes a member from a key. If the last member is removed from the key, the key is removed from the dictionary. If the key or member does not exist, displays an
error.
PARAM: Key
PARAM: Member
RETURNS: 'Removed' or ERROR
"""
def remove(key, member):
    if key not in dict:
        print("ERROR, key does not exist")
    elif member not in dict[key]:
        print("ERROR, member does not exist")
    else:
        dict[key].remove(member)
        if (len(dict[key]) == 0):
            del dict[key]
        print("Removed")

"""
Function: REMOVEALL
Removes all members for a key and removes the key from the dictionary. Returns an error if the key does not exist.
PARAM: Key
RETURNS: 'Removed' or ERROR
"""
def remove_all(key):
    if key not in dict:
        print("ERROR, key does not exist")
    else:
        del dict[key] # we do not clear the members here, as deleting the key will remove the members as well
        print("Removed")

"""
Function: CLEAR
Removes all keys and all members from the dictionary.
RETURNS: 'Cleared'
"""
def clear():
    dict.clear() # python has a built in clear function for dictionaries, which we use here
    print("Cleared")

"""
Function: KEYEXISTS
Returns whether a key exists or not.
PARAM: Key
RETURNS: Boolean
"""
def key_exists(key):
    print(key in dict)

"""
Function: MEMBEREXISTS
Returns whether a member exists within a key. Returns false if the key does not exist.
PARAM: Key
PARAM: Member
RETURNS: Boolean
"""
def member_exists(key, member):
    print(member in dict[key])

"""
Function: ALLMEMBERS
Returns all the members in the dictionary. Returns nothing if there are none. Order is not guaranteed.
RETURNS: List of members
"""
def all_members():
    counter = 1
    for key in dict:
        for member in dict[key]:
            print(str(counter) + ") " + member)

"""
Function: ITEMS
Returns all keys in the dictionary and all of their members. Returns nothing if there are none. Order is not guaranteed.
RETURNS: List of keys and members
"""
def items():
    counter = 1
    for key in dict:
        for member in dict[key]:
            print(str(counter) + ") " + key + ": " + member)

dict = {}
cmd = ''
while cmd != 'QUIT':
    cmd = input(">") # get user input
    params = cmd.split() # split parameters
    cmd = params[0] # grab command name

    if cmd == 'KEYS':
        if (len(params) == 1):
            keys()
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'MEMBERS':
        if (len(params) == 2):
            members(params[1])
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'ADD':
        if (len(params) == 3):
            add(params[1], params[2])
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'REMOVE':
        if (len(params) == 3):
            remove(params[1], params[2])
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'REMOVEALL':
        if (len(params) == 2):
            remove_all(params[1])
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'CLEAR':
        if (len(params) == 1):
            clear()
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'KEYEXISTS':
        if (len(params) == 2):
            key_exists(params[1])
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'MEMBEREXISTS':
        if (len(params) == 3):
            member_exists(params[1], params[2])
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'ALLMEMBERS':
        if (len(params) == 1):
            all_members()
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'ITEMS':
        if (len(params) == 1):
            items()
        else:
            print("ERROR, invalid number of parameters")
    elif cmd == 'QUIT':
        quit() # simply quits the program
    else:
        print("Invalid command.")
