
smoothies=['coconut','strawberry','banana','tropical','acai berry']
has_coconut=[True,False,False,True,False]
length=len(has_coconut)
for i in range(length):
    if has_coconut[i]:
        print(smoothies[i], 'contains coconut')
