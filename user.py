class User :
   """
   this class generates news isntance of user

   """

   userlist = []

   def __init__(self,firstname,lastname,username,password):
       self.firstname = firstname
       self.lastname = lastname
       self.username = username
       self.password = password

   def  save_user(self):

         """
         save-user method is used to  create new user objects to the user_list 

         """     
         User.user_list.append(self)
   

   def delete_user(self):
         """
         delete method deletes saved user from the userlist
         """
        User.userlist.remove(self)
    @classmethod
    def display_users(cls):
        """
        display method return info from the userlist
        """
        
        return cls.userlist
    @classmethod
    def find_by_number(cls,number):
        """
        find by number method takes a username and return the user  if its matches the number
        """

        for user in cls.userlist:
            if user.password == number:
                return user

    @classmethod
    def user_exist(cls,number):
        for user in cls.userlist:
            if user.username == number:
                return True
                return False
