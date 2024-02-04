import random
from higher_lower_game_data import data


def acc(info):
    return random.choice(info)


def formatting(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, {description}, from {country}'


def option(opt):
    if opt == 'A':
        if a_acc_followers > b_acc_followers:
            return 'A'
    elif opt == 'B':
        if b_acc_followers > a_acc_followers:
            return 'B'
    else:
        return 'C'


def ok(score, opt):
    if option(opt) == 'A':
        data.remove(account_a)
        print("You're right.")
        return score + 1
    elif option(opt) == 'B':
        data.remove(account_b)
        print("You're right.")
        return score + 1
    else:
        print("Sorry, that's wrong.")
        return score


print("Welcome to my higher lower game!!!")
replay = True
while replay:
    play = input("Would you like to play? Type 'y' or 'n': ").lower()
    if play == 'y':
        data = data

        account_a = acc(data)
        account_b = acc(data)

        formatted_a = formatting(account_a)
        formatted_b = formatting(account_b)

        a_acc_followers = account_a['follower_count']
        b_acc_followers = account_b['follower_count']

        print(f"Compare A: {formatted_a}")
        print(f"Compare B: {formatted_b}")
        looper = True
        count = 0
        while looper:
            Comparison = input("Who has more followers? Type 'A' or 'B': ").upper()
            count = ok(count, Comparison)
            if option(Comparison) != 'A' and option(Comparison) != 'B':
                looper = False
                print(f"\nFinal score: {count}")
            else:
                if option(Comparison) == 'A':
                    account_a = account_b
                account_b = acc(data)

                formatted_a = formatting(account_a)
                formatted_b = formatting(account_b)

                a_acc_followers = account_a['follower_count']
                b_acc_followers = account_b['follower_count']

                print(f"Current score: {count}")

                print(f"Compare A: {formatted_a}")
                print(f"Compare B: {formatted_b}")
    elif play == 'n':
        print("GoodBye!!!")
        replay = False
    else:
        print("You did not select a defined option.\n")

