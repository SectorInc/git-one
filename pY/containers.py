# # # tuple & list. tuple cannot change its values but list can change its values. tuple is faster than list because it is immutable. tuple is used to store a collection of items that cannot be changed, while list is used to store a collection of items that can be changed.
# # tuple=('bob',123,('and'))
# # list=['bob',123,('and')]  
# # #set & dictionary. set is a collection of unique items, while dictionary is a collection of key-value pairs. set is unordered, while dictionary is ordered. set is used to store a collection of unique items, while dictionary is used to store a collection of key-value pairs.
# # baset={'bob',123,('and')}
# # cdictionary={'name':'bob','age':123,'hobby':'and'}   #no individual value but a key-value pairing

# # a_tuple=(1,2,3,'a string')
# # a_list=[1,2,3,3,'a string']
# # # a_list.append('another string')
# # #print(a_list)
# # a_set={1,2,3,4}
# # print(set(a_list)) #this will convert the list to a set and remove the duplicate values
# # a_dictionary={'name':'bob','age':123,'hobby':'and'}
# # a_dictionary['new name']='alice' #this will change the value of the key 'name' in the dictionary
# # print(a_dictionary['name']) #this will print the value of the key 'name' in the dictionary
# # #getting values from a container using slicing and indexing
# user_list=['emma','bob','alice','john','jane']
# print(user_list[-1]) #this will print the first value in the list
# print(user_list[0:4:2]) #slicing
# #8,6,4,2
ex_list=[1,2,3,4,5,6,7,8,9]
print(ex_list[-2::-2])



