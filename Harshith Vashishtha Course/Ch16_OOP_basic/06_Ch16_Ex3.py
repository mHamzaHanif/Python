class DataBase:
    # creting object varable
    counter = 0
    def __init__(self, name, email, password):
        DataBase.counter += 1  #increment in class variable
        self. name = name.title()
        self.email = email
        self.password = password
    
#objs
user1 = DataBase('hamza', 'hamzaarain1999@gmail.com', 'hamun12')
user2 = DataBase('wajiha', 'wajihaarain2000@gmail.com', 'interpreter')
user3 = DataBase('mahnoor', 'mahiraarain1994@gmail.com', 'compiler')

#Calling class variable
print(DataBase.counter)