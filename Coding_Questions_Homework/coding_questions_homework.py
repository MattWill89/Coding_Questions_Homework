# Question 1
def hello_name(USERNAME):
    print('Hello_' + USERNAME + '!!!')

hello_name('Fill in name here')

# Question 2
def first_odds():
    for i in range(1, 101, 2):
        print(i)
first_odds()

# Question 3
def max_number_in_list(a_list):
    if not a_list:
        return None
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

result = max_number_in_list([1, 2, 3, 4])  
print(result)  

# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Question 5
def is_consecutive(a_list):
    if not a_list:
        return False
    for i in range(len(a_list) - 1):
        if a_list[i] != a_list[i+1] - 1:
            return False
        return True
    
print(is_consecutive([1, 2, 3, 4, 5]))  
print(is_consecutive([1, 2, 4, 5]))     
print(is_consecutive([]))              
