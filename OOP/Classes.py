# class User:
#     pass
#     # used to avoid the error in python 
#     # Classes in Python are in PascalCase
# user_1 = User()

# # Creating Attributes for your class
# user_1.id = "001"
# user_1.username = "sparsh"

# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "iota"

# now this is a non_followed way of creating classes.
# Is there a way to make this process simpler?
# Yep, there is. Use the __init__ function called the Constructor (initializor)
# __init__ is a spical funcions that are called everytime u make an ibject

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "iota")
print(user_1.id, user_1.username, user_1.followers, user_1.following)

user_2 = User("002", "ass")
print(user_2.id,user_2.username, user_2.followers, user_2.following)

# User 1 follows user 2 here
user_1.follow(user_2)
print(user_1.id, user_1.username, user_1.followers, user_1.following)
print(user_2.id,user_2.username, user_2.followers, user_2.following)