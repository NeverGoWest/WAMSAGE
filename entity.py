# WAMSAGE - West and Moon's Super Awesome Game Engine - entity classes

def printlist(lst):
    for i in lst:
        print(i)
    return lst

class Entity:
    
    def var(self): # easier and more flexible var definitions, keep init for engine specific variables.
        pass

    def __init__(self, src, name, desc, *content): # container, name, description, container, contents
        self.debug = 1 # debug mode, useful for testing.. and removing bugs.
        self.name = name # name of the entity
        self.desc = desc # description of the entity
        self.src = src # entity source, it's container usually
        self.cont = content
        self.var()

    def getcont(self, dbg=0): # returns all the objects found in self.cont
        contents = [] # the content to be returned
        contents.extend(self.cont)
        if dbg:
            return printlist(contents)
        else:
            return contents

    def addcont(self, ent, dbg=0): # add an object to contents of self
        self.cont.append(ent)
        if dbg:
            print("DBG: added {} to {}".format(ent.name, self.name))
        return self.cont

    def remcont(self, ent, dbg=0): # remove an object from contents of self
        self.cont.pop(index(ent))
        if dbg:
            print("DBG: removed {} from {}".format(ent.name, self.name))
        return self.cont

    def indcont(self, ent, dbg=0): # find an object in contents of self
        result = self.cont.index(ent)
        if dbg:
            print("DBG: index of {} in {}: {}".format(ent.name, self.name, result))
        return result

        
    


