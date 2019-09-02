#this list is to sort the best solutions by desecneding order.

def bubble_sort(scores,solution_numbers):
    swapped=True
    while swapped:
        swapped=False
        for i in range(0,len(scores)-1):
            if scores[i]<scores[i+1]:
                temp=scores[i]
                scores[i]=scores[i+1]
                scores[i+1]=temp
                swapped=True
                temp=solution_numbers[i]
                solution_numbers[i]=solution_numbers[i+1]
                solution_numbers[i+1]=temp
                swapped=True

scores=[60,50,60,58,54,54,
        58,50,52,54,48,69,
        34,55,51,52,44,51,
        69,64,66,55,52,61,
        46,31,57,52,44,18,
        41,53,55,61,51,44]

number_of_scores=len(scores)
solution_numbers=list(range(number_of_scores))

bubble_sort(scores, solution_numbers)

print ('Top 5 Best Bubble Solutions:')
# print('Bubble solution #',str(solution_numbers[0]),'score:', scores[0])
# print('Bubble solution #',str(solution_numbers[1]),'score:', scores[1])
# print('Bubble solution #',str(solution_numbers[2]),'score:', scores[2])
# print('Bubble solution #',str(solution_numbers[3]),'score:', scores[3])
# print('Bubble solution #',str(solution_numbers[4]),'score:', scores[4])
for i in range(0,5):
    print(str(i+1)+')','Bubble solution #'+str(solution_numbers[i]),'score:', scores[i])
