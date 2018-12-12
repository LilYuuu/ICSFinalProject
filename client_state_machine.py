"""
Created on Sun Apr  5 00:00:32 2015

@author: zhengzhang
"""
from chat_utils import *
import json
from cryptography.fernet import Fernet

class ClientSM:
    def __init__(self, s):
        self.state = S_OFFLINE
        self.peer = ''
        self.me = ''
        self.out_msg = ''
        self.s = s
        self.key = ''

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
    
    def set_key(self,key):
        self.key = key

    def set_myname(self, name):
        self.me = name

    def get_myname(self):
        return self.me

    def connect_to(self, peer):
        msg = json.dumps({"action":"connect", "target":peer})
        mysend(self.s, msg)
        response = json.loads(myrecv(self.s))
        if response["status"] == "success":
            self.peer = peer
            self.out_msg += 'You are connected with '+ self.peer + '\n'
            return (True)
        elif response["status"] == "busy":
            self.out_msg += 'User is busy. Please try again later\n'
        elif response["status"] == "self":
            self.out_msg += 'Cannot talk to yourself (sick)\n'
        else:
            self.out_msg += 'User is not online, try again later\n'
        return(False)

    def disconnect(self):
        msg = json.dumps({"action":"disconnect"})
        mysend(self.s, msg)
        self.out_msg += 'You are disconnected from ' + self.peer + '\n'
        self.peer = ''

    def proc(self, my_msg, peer_msg):
        self.out_msg = ''
#==============================================================================
# Once logged in, do a few things: get peer listing, connect, search
# And, of course, if you are so bored, just go
# This is event handling instate "S_LOGGEDIN"
#==============================================================================
        if self.state == S_LOGGEDIN:
            # todo: can't deal with multiple lines yet
            if len(my_msg) > 0:

                if my_msg == 'q':
                    self.out_msg += 'See you next time!\n'
                    self.state = S_OFFLINE

                elif my_msg == 'time':
                    mysend(self.s, json.dumps({"action":"time"}))
                    time_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += "Time is: " + time_in

                elif my_msg == 'who':
                    mysend(self.s, json.dumps({"action":"list"}))
                    logged_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += 'Here are all the users in the system:\n'
                    self.out_msg += logged_in

                elif my_msg[0] == 'c':
                    peer = my_msg[1:]
                    peer = peer.strip()
                    if self.connect_to(peer) == True:
                        self.state = S_CHATTING
                        self.out_msg += 'Connect to ' + peer + '. Chat away!\n\n'
                        self.out_msg += '-----------------------------------\n'
                    else:
                        self.out_msg += 'Connection unsuccessful\n'

                elif my_msg[0] == '?':
                    term = my_msg[1:].strip()
                    f = Fernet(self.key)
                    term_encrypted = f.encrypt(term.encode('utf-8'))
                    mysend(self.s, json.dumps({"action":"search", "target":term_encrypted.decode('utf-8')}))
                    search_rslt = json.loads(myrecv(self.s))["results"].strip()
                    search_rslt_decrypted = f.decrypt(search_rslt.encode('utf-8'))
                    del f
                    if (len(search_rslt_decrypted)) > 0:
                        self.out_msg += 'Encrypted search result: ' + search_rslt + '\n'
                        self.out_msg += search_rslt_decrypted.decode('utf-8') + '\n\n'
                    else:
                        self.out_msg += '\'' + term + '\'' + ' not found\n\n'

                elif my_msg[0] == 'p' and my_msg[1:].isdigit():
                    poem_idx = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"poem", "target":poem_idx}))
                    poem = json.loads(myrecv(self.s))["results"]
                    if (len(poem) > 0):
                        self.out_msg += poem + '\n\n'
                    else:
                        self.out_msg += 'Sonnet ' + poem_idx + ' not found\n\n'
                        
                elif my_msg[0] == 'g':
                     mysend(self.s, json.dumps({"action":"game"}))
                   #  self.out_msg += 'Enjoy the game!\n"

                else:
                    self.out_msg += menu

            if len(peer_msg) > 0:
                try:
                    peer_msg = json.loads(peer_msg)
                except Exception as err :
                    self.out_msg += " json.loads failed " + str(err)
                    return self.out_msg
            
                if peer_msg["action"] == "connect":

                    # ----------your code here------#
                    print('request from:',peer_msg['from'])
                   # if (self.connect_to (peer_msg['from'])):
                    self.state = S_CHATTING
                    print("Chat away!")
                   # else:
                    #    print('connection unsuccessful')
                    
                    
                  #  self.connect_to(peer_msg['from']) #???
                   # pass



                    # ----------end of your code----#
                    
#==============================================================================
# Start chatting, 'bye' for quit
# This is event handling instate "S_CHATTING"
#==============================================================================
        elif self.state == S_CHATTING:
            f = Fernet(self.key)
            if len(my_msg) > 0:     # my stuff going out
                
                my_msg_encrypted = f.encrypt(my_msg.encode('utf-8'))
                mysend(self.s, json.dumps({"action":"exchange", "from":"[" + self.me + "]", "message":my_msg_encrypted.decode('utf-8')}))
                print()
                if my_msg == 'bye':
                    self.disconnect()
                    ''' print(peer_msg)
                    server_msg = json.loads(peer_msg)
                    print (server_msg)
                    server_send_key = server_msg['key']
                    self.set_key(server_send_key.encode('utf-8'))
                    '''
                  #  self.state = S_LOGGEDIN
                 #   self.peer = ''
            if len(peer_msg) > 0:    # peer's stuff, coming in
                

                # ----------your code here------#
                peer_msg = json.loads(peer_msg)
                if(peer_msg['action'] == 'keyPass'):
                    server_send_key = peer_msg['key']
                    self.set_key(server_send_key.encode('utf-8'))
                    self.state = S_LOGGEDIN
                    self.peer = ''
             #   peer_msg_decrypted = f.decrypt(peer_msg['msg'].encode('utf-8'))
                if (peer_msg['action'] == 'exchange'):
                    peer_msg_decrypted = f.decrypt(peer_msg['msg'].encode('utf-8'))
                    print(peer_msg['from'],':')
                    print('encrypted message: ' + peer_msg['msg'])
                    print('\ndecrypted message: ' + peer_msg_decrypted.decode('utf-8'))
                    print('\n')
                   # print(peer_msg['msg'],'\n')
                elif (peer_msg['action'] == 'disconnect'):
                    print(peer_msg['msg'])
                   # print (peer_msg['msg'])
                    



                # ----------end of your code----#
                
            # Display the menu again
            if self.state == S_LOGGEDIN:
                self.out_msg += menu
#==============================================================================
# invalid state
#==============================================================================
        else:
            self.out_msg += 'How did you wind up here??\n'
            print_state(self.state)

        return self.out_msg
