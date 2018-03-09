from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/bme590")

class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    password = fields.CharField()

u = User('user1@email.com', last_name='Ross', first_name='Bob')
u2 = User('user2@email.com', last_name='Ross', first_name='Rob')

u.save()
u2.save()

for user in User.objects.raw({"first_name":"Rob"}):
        print(user)
	print(user.first_name)
	print(user.last_name)
