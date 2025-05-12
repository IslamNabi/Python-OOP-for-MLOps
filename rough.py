#lst = [1,2,3]
#my_str = "practicing MLOps"
#my_int = 150

#print(type(lst))
#print(type(my_str))
#print(type(my_int))

#lst.clear()
#print(lst)
#my_str = my_str.capitalize()
#print(my_str)

#a = 'x'
#b = 'y'
#print(a+b)

#from oops_project import chatbook
# user2 = chatbook()

#lst = [1,2,3]

#function 
#a1 = len(lst)
#print(a1)

# method belongs to a class we call method using object

from oops_project import chatbook
user1 = chatbook()
print(user1.id)

# using static method directly from class rather than obj 
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)


#user2 = chatbook()
#print(user2.id)

#user3 = chatbook()
#print(user3.id)

#getter and setter
#print(user1.get_name())
#user1.set_name('Islam')
#print(user1.get_name())