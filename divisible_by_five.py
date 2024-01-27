# repeat the given list of numbers and print only those divisible by 5

# create a function that would print numbers that are divisible by 5
def  print_divisible_by_5 (numbers):
    # check if it is divisible by 5 then print if it is
    for scores in numbers:
        if scores % 5 == 0:
            print (scores)

ask_user_input = input ("Type your scores: ")
users_score = [int(num) for num in ask_user_input.split()]

print ("These are your scores that is divisible by 5:")
print_divisible_by_5(users_score)