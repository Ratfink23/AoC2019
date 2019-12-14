# This did not work....

def secure_container(start=382345, finish=843167):
    # check if number has adjacent digits
    # check if never decreases
    # check if no adjacent matching digits
    password_num = 0
    for num_check in range(start,finish+1):
        adj_digit = False
        never_desc = False
        double_digit = False
        str_num = str(num_check)
        last_str = int(str_num[0])
        for c in str_num[1:]:
            c = int(c)
            if c < last_str:
                never_desc = False
                break
            if c == last_str:
                if double_digit:
                    double_digit = False
                    adj_digit = False
                else:
                    adj_digit = True
                    double_digit = True
                never_desc = True
            else:
                never_desc = True
                double_digit = False
            last_str = c
        if never_desc and adj_digit:
            password_num += 1
            print(str_num)
    return password_num


# from Reddit
from collections import Counter

def check1(s):
    return list(s) == sorted(s) and len(set(s)) < len(s)

def check2(s):
    return list(s) == sorted(s) and 2 in Counter(s).values()

print(sum(check1(str(x)) for x in range(382345, 843167)))
print(sum(check2(str(x)) for x in range(382345, 843167)))