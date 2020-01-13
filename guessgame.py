#guess number game
guess = 18
number_of_guess = 1
print("you have 3 chance guess number between 1 to 30")
while(number_of_guess <= 3):
    num = int(input("your guess number is: "))
    if num<guess:
        print("you entered small number!")
    elif num>guess:
        print("you entered grater number!")
    else:
        print("you win ")
        print("you have taken chance to win = ",number_of_guess)
        break
    print(3-number_of_guess,"number of remaning guess")
    number_of_guess +=1
if number_of_guess>3:
    print("game over try agen!")
