def quiz_decimal(low, high):

    print('Type a number between' ,str(low), 'and' ,str(high),)
    user_value = float(raw_input())
    if int(user_value) == user_value:
        user_value = int(user_value)
        if user_value < low:
            print('No, ' + str(user_value) + ' is less than ' + str(low))
        elif user_value > high:
            print('No, ' + str(user_value) + ' is greater than ' + str(high))
        else:
            print('Good! ' + str(low) + ' < ' + str(user_value) + ' < '+ str(high))