users={}
users['Kim']={'email':'kim@oreilly.com','gender':'f','age':27,'friends': ['John','Josh']}
users['John']={'email':'john@oreilly.com','gender':'m','age':24,'friends': ['Kim','Josh']}
users['Josh']={'email':'josh@oreilly.com','gender':'m','age':32,'friends': ['Kim']}

def avg_age(username):
    global users
    user=users[username]
    friends=user['friends']
    sum=0
    for i in friends:
        friend=users[i]
        sum=sum+friend['age']
    average=sum/len(friends)
    print(username+"'s friends have an average age of", average)

avg_age('Kim')
avg_age('John')
avg_age('Josh')
