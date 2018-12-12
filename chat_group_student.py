S_ALONE = 0
S_TALKING = 1

# ==============================================================================
# Group class:
# member fields:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
# ==============================================================================


class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    def is_member(self, name):

        # IMPLEMENTATION
        # ---- start your code ---- #
        if (name in self.members):
            return True

        return False
        # ---- end of your code --- #

    # implement
    def leave(self, name):
        """
        leave the system, and the group
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        self.disconnect(name)
        del self.members[name]
         

        # ---- end of your code --- #
        return

    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """

        found = False
        group_key = 0
        # IMPLEMENTATION
        # ---- start your code ---- #
        for i in range (1,self.grp_ever+1):
            if name in self.chat_grps[i]:
                found = True
                group_key = i

        # ---- end of your code --- #
        return found, group_key

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)

        # IMPLEMENTATION
        # ---- start your code ---- #
        if (self.members[me] == 1 and self.members[peer] == 1):
            print ("both are in a group aready!")
        else:
            if (self.members[me] == 0 and self.members[peer] == 0):
                self.chat_grps[self.grp_ever+1] = [me,peer]
                self.grp_ever += 1
            elif (self.members[me] == 1):
                grpNum = 0
                for i in range (1,self.grp_ever+1):
                    if me in self.chat_grps[i]:
                        grpNum = i
                        break
                self.chat_grps[grpNum].append(peer)
            else:
                grpNum = 0
                for i in range (1,self.grp_ever+1):
                    if peer in self.chat_grps[i]:
                        grpNum = i
                        break
                self.chat_grps[grpNum].append(me)
        # ---- end of your code --- #
        return

    # implement
    def disconnect(self, me):
        """
        find myself in the group, quit, but stay in the system
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        grpNum = 0
        for i in range (1,self.grp_ever+1):
            if me in self.chat_grps[i]:
                grpNum = i
                break
        
        if (len(self.chat_grps[grpNum]) <= 2):
            del self.chat_grps[grpNum]
        else:
            self.chat_grps[grpNum] = self.list_me(me)[1:]

        # ---- end of your code --- #
        return

    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    # implement
    def list_me(self, me):
        """
        return a list, "me" followed by other peers in my group
        """
        my_list = []
        # IMPLEMENTATION
        # ---- start your code ---- #
        my_list.append(me)
        for i in range (1,self.grp_ever+1):
            if me in self.chat_grps[i]:
                my_list.append(nm for nm in self.chat_grps[i] if nm != me)

        # ---- end of your code --- #
        return my_list


if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    g.join('c')
    g.join('d')
    print(g.list_all())

    g.connect('a', 'b')
    print(g.list_all())
    g.connect('c', 'a')
    print(g.list_all())
    g.leave('c')
    print(g.list_all())
    g.disconnect('b')
    print(g.list_all())
