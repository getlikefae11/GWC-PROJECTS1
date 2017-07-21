class User:
    # Define the fields and methods for your object here.
    def __init__(self, newUsername, newUserID):
        self.username = newUsername
        self.userID = newUserID
        self.friends = []

    def getUserName(self):
          return self.username

    def getUserID(self):
         return self.userID

    def getFriends(self):
        return self.friends

    def addFriends(self, friendID):
        self.frinds.append(friendID)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users=[]
    def numUsers(self):
        return len(self.users)
    def adduser(self, username):
        user_id=len(self.users)
        self.users.append(username, user_id)
    def getuserID(self, username):
        for user in self.users:
            if username==user.getUserName():
                return user_id
    def addconnection(self, user1, user2):
        user1_id = self.getuserID(user1)
        user2_id = self.getUserID(user2)

        user1 = self.users[user1_id]
        user2 = self.users[user2_id]

        self.users[user2_id].addFriends(user1_id)
        self.users[user1_id].addFriends(user2_id)

    def printUsers(self):
        print("this is the Network")
        for user in self.users:
            print("\tuser {}: {}".format(user.getUserID, user.getUserName))

    def printConnections(self, username):
        user = self.users[self.getUserID(username)]
        connections = user.getfriends()
        print("\t{}'s connections:".format(user.getUserName()))
        for friendID in connections:
            friend = self.users[friends]
            print("\t{}".format(friend.getUserName()))



def main():
    # Define the program flow for your user interface here.
    mynetwork = Network()
    done = False
    while not done:
        action = input("\nwhat would you like to do ? Add a user(u), Add a connection (c), Print Friend list (p), Print Connections (pc), exit(e)")

        if action== "u":
            username = input("what username")
            mynetwork.adduser(username)
        elif action== "c":
            if mynetwork.numUsers()<2:
                print("ERROR. Don't have enough users")
                continue
            else:
                user1 = input("First user?")
                user2 = input("Second user?")
            mynetwork.addConnection(user1,user2)
        elif action== "p":
            mynetwork.printUsers()
        elif action== "pc":
            user=input("what user?")
            mynetwork.printConnections(user)

        elif action== "e":
            print("sorry to see you go")
            done = True
        else:
            print("ERROR. STUPID DOG YOU MAKE ME GO MAD")



# Runs your program.
if __name__ == '__main__':
    main()
