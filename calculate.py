def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2

def solve(question_list):
    if len(question_list)==1:
        return int(question_list[0])
    elif len(question_list)==3:
        return operate(int(question_list[0]), question_list[1], int(question_list[2]))
    else:
        return operate(solve(question_list[:-2]), question_list[-2], int(question_list[-1])) 

num1=int(input('enter number:'))
num2=int(input('enter number:'))
operate1=input('inter operater:')
print(operate(num1,operate1,num2))