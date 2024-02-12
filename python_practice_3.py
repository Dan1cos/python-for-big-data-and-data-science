#Task 1
fav_num = 5
if fav_num%2==0:
    print(fav_num*2)
else:
    print(fav_num*3+1)


#Task 2
my_list = []
if not my_list:
    my_list.append("Hello")
print("List: ", my_list)


#Task 3
my_name = "Artem"
name_converted = my_name.lower()
if name_converted.find('a')!=-1 or name_converted.find('i')!=-1:
    print("A or I is in the name")
if name_converted.find('o')!=-1 and name_converted.find('n')!=-1:
    print("O and N is in the name")
elif name_converted.find('n')!=-1:
    print("Only N is in the name")
else:
    print("There is no N in the name, but there might be O")


#Task 4
range_list = [num for num in range(10) if num%2==0]
print(range_list)


#Task 5
dict_compreh = {(str(num) if num%2==0 else str(num+10)):(num if num%2==0 else num+5) for num in range(10)}
print(dict_compreh)


#Task 6
list_words = ['hello', 'i', 'dont', 'care']
list_mod_words = [word[:3].upper() for word in list_words]
print(list_mod_words)


#Task 7
number = 10
while number>0:
    print("Number is: ", number)
    number-=1


#Task 8
for i in range(21):
    if i%2==1:
        print(i)


#Task 9
elems_list = [True, False, None, False, True, None]
i = 0
tuple_list = []
for val in elems_list:
    tuple_list.append((i, val))
    i+=1
print(tuple_list)


#Task 10
books_dict = dict()
books_dict['The Great Gatsby'] = 1
books_dict['1984'] = 3
books_dict['Pride and Prejudice'] = 5
books_dict["One Flew Over the Cuckoo's Nest"] = 2
books_dict['The Catcher in the Rye'] = 4
books_dict['Perfume: The Story of a Murderer'] = 10

for k,v in books_dict.items():
    books_dict[k] = v+5

print(books_dict)


#Task 11
n = 8
for i in range(1,n+1):
    st = ""
    for j in range(i):
        st+="#"
    print(st)


#Task 12
from random import randint
tries = 1
num_to_guess = randint(1, 100)
guess = 0
while guess!=num_to_guess:
    guess = int(input("Enter a number: "))
    if guess<num_to_guess:
        print("Number is bigger")
    else:
        print("Number is lower")
    tries+=1
print(f"Congratulations you've won, the number was {num_to_guess}, you've taken {tries} tries to guess the number")