from User import User
from Admin import Admin

user = User('Ahmad')
user.getUsername()
user.username = "Ali"
user.getUsername()

admin = Admin("Mr. Admin")
admin.username = "Another Admin!"
admin.getUsername()