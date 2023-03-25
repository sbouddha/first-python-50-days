import os
# os.system("cls" if os.name == "nt" else "clear")

#Creating our ver first class
#First letter should be Capital in class name, it is called Pascal Case

class User:
    def __init__(self, user_id, user_name):
        self.id=user_id
        self.name=user_name
        self.project = 'Not Yet Decided'
        print(f'New user {user_name} is being created...')

#creating object from a Class
user_1=User('001', 'Siddharth' )
user_2=User('002', 'Pratima' )
user_3=User('001', 'Elon' )

print(f'The username for the user_1 is {user_1.name}')
print(f'The Project for the user_1 is {user_1.project}')


#Using Methods
class Car:
    def __init__(self, seats):
        self.seats=seats

    def enter_race_mode(self):
        self.seats=2
#Very important to have (self) in all the methods inside the class

#Normal
safar_car=Car(6)
print(f'The seats in Safari in normal mode are {safar_car.seats}')

#Going in race mode
safar_car.enter_race_mode()
print(f'The seats in Safari in Sport mode are {safar_car.seats}')

#Clear the screen
os.system("cls" if os.name == "nt" else "clear")

#Instagram Class
print('Below is instagram Class')


class Insta_Users:
    def __init__(self, id, name) -> None:
        self.user_id = id
        self.user_name = name
        self.following = 0
        self.followers = 0
        
    def follow(self, user):
        self.following +=1
        user.followers +=1

insta_user_1 = Insta_Users('001','Pratima')
insta_user_2 = Insta_Users('002','Siddharth')

insta_user_1.follow(insta_user_2)

print(f'User 1 : {insta_user_1.user_name} is following {insta_user_1.following}')
print(f'User 1 : {insta_user_1.user_name} has {insta_user_1.followers} followers ')
print(f'User 2 : {insta_user_2.user_name} is following {insta_user_2.following}')
print(f'User 2 : {insta_user_2.user_name} has {insta_user_2.followers} followers ')




