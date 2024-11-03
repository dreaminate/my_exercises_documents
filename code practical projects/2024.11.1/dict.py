# list1=[num for num in range(10) if num%2==0]
# list2=[x for x in range(10) if x%2 !=0]
# dict1=dict(zip(list1,list2))
# dict2={key : value for key in list1  for value in list2}
# dict1.update([('e', 5), ('f', 6)])
# # dict1=dict1.keys()
# print(dict1,end="\n")
# print(list1)
# print(list2)
# print(dict2)
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

print(users.items())

for username, user_info in users.items():
    print(user_info)
    print(username)
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")