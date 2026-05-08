# INSTAGRAM USER CLASS

class User:
    # Constructor/ Initializing an object (__init__)
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        #initializing followers = 0 because the number an instagram user's followers can't
        #be pre-determined and can either increase or decrease

        # The person I'm following's account
        self.followers = 0

        # my account
        self.following = 0
        print("New user being created...")

    # Methods would manipulate the class attributes to compute some computation
    # Method always has the 'self' parameter
    def follow(self, user):
        # User to be followed
        user.followers += 1

        # User doing the following (me)
        self.following += 1



user_1 = User("001", "Geraldine")
print(f"{user_1.name} : {user_1.id}")

# Adding attributes
# user_1.id = "001"
# user_1.name = "Geraldine"


user_2 = User("002", "Nnene")
# user_2.id = "002"
# user_2.name = "Nnene"
print(f"{user_2.name} : {user_2.id}")

#USER 1 DECIDED TO FOLLOW USER 2
user_1.follow(user_2)
print(f"Number of followers for {user_1.name}: {user_1.followers}")
print(f"Number being followed by {user_1.name}: {user_1.following}")

print(f"Number of followers for {user_2.name}: {user_2.followers}")
print(f"Number being followed by {user_2.name}: {user_2.following}")


