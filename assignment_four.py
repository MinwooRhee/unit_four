
import random


def give_instruction():
    print("Welcome to the simplified version of the game, Blackjack")
    print("You will first draw two cards from 1~10 and then you will be asked if you wanted to draw a third card.")
    print("The purpose of the game is to have higher total number than the dealer, who will draw only two cards.")
    print("However, if your total number exceeds 21, you will lose regardless of the dealer's number")
    print("Good luck, and enjoy.")


def draw_card():
    number = random.randint(1, 10)
    return number


def draw_third_card():
    y_or_no = input("Would you to draw the third card?(y/n): ")
    if y_or_no == "y":
        player_third_card = draw_card()
        print("You drew ", player_third_card, ".")
        player_total_number = player_total_number + player_third_card
        print("Your total is now ", player_total_number, ".")


def dealer_draws():
    dealer_first_card = draw_card()
    dealer_second_card = draw_card()



def main():
    give_instruction()
    player_first_card = draw_card()
    player_second_card = draw_card()
    player_total_number = player_first_card + player_second_card
    print("Your drew ", player_first_card, "and ", player_second_card, ".")
    print("Your total is ", player_first_card + player_second_card, ".")


