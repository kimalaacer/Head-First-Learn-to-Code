# easy way to sum numbers using the sum function in python
  # marbles=[10,13,39,14,41,9,3]
  # print('The total is:', sum(marbles))

# another way is to use iteration over the list
  #def compute_sum(list):
      #sum=0
      #for number in list:
        #sum=sum+number
      #return sum
    #print('The total is:', compute_sum(marbles))

# the below code is for recursive
marbles=[10,13,39,14,41,9,3]
def recursive_compute_sum(list):
    if len(list)==0:
        return 0
    else:
        first=list[0]
        rest=list[1:]
        sum=first+recursive_compute_sum(rest)
        return sum
sum=recursive_compute_sum(marbles)
print('The total is:',sum)
