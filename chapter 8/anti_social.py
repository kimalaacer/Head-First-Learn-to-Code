users={}
users['Kim']={'email':'kim@oreilly.com','gender':'f','age':27,'friends': ['John','Josh']}
users['John']={'email':'john@oreilly.com','gender':'m','age':24,'friends': ['Kim','Josh']}
users['Josh']={'email':'josh@oreilly.com','gender':'m','age':32,'friends': ['Kim']}

max=1000
for name in users:
    user = users[name]
    friends = user['friends']
    if len(friends) < max:
        most_anti_social = name

print('The most anti social user is:', most_anti_social)
