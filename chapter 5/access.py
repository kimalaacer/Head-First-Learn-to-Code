def allow_access(person):
    if person =="Dr Evil":
        answer = True
    else:
        answer= False
    return answer

access1=allow_access('codie')
access2=allow_access('Dr Evil')
print(access1)
print(access2)
