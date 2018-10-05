
import random


def give_instruction():
    print("Welcome to the simplified version of the game, Blackjack")
    print("You will first draw two cards from 1~10 and then you will be asked if you wanted to draw a third card.")
    print("The purpose of the game is to have higher total number than the dealer, who will draw only two cards.")
    print("However, if your total number exceeds 21, you will lose regardless of the dealer's number")
    print("Good luck, and enjoy.")
    print(" ")
    print(" ")


def draw_card():
    number = random.randint(1, 10)
    return number


def draw_third_card(player_total):
    y_or_no = input("Would you like to draw the third card? (y/n): ")
    if y_or_no == "y":
        player_third_card = draw_card()
        print("You drew ", player_third_card, ".")
        player_total_number = player_total + player_third_card
        print("Your total is now ", player_total_number, ".")
        return player_total_number
    else:
        player_total_number = player_total
        return player_total_number


def player_draws():
    player_first_card = draw_card()
    player_second_card = draw_card()
    player_total_number = player_first_card + player_second_card
    print("Your drew ", player_first_card, "and ", player_second_card, ".")
    print("Your total is ", player_total_number, ".")
    return player_total_number


def dealer_draws():
    dealer_first_card = draw_card()
    dealer_second_card = draw_card()
    dealer_total_number = dealer_first_card + dealer_second_card
    print(" ")
    print("The dealer drew", dealer_first_card, "and", dealer_second_card, ".")
    print("The dealer's total number is", dealer_total_number, ".")
    return dealer_total_number


def win_lose_or_push(player_total_number, dealer_total_number):
    if dealer_total_number == player_total_number:
        print("Your total and the dealer's total are the same.")
        print("It is a push (draw).")
    elif dealer_total_number > player_total_number:
        print("The dealer's total is higher than yours")
        print("You lose.")
    else:
        print("Your total is higher than the dealer's")
        print("You won!")


def main():
    give_instruction()
    player_total_number = player_draws()
    player_total_number = draw_third_card(player_total_number)
    if player_total_number > 21:
        print(" ")
        print("Your total exceeds 21. You lose.")
    else:
        dealer_total_number = dealer_draws()
        print(" ")
        win_lose_or_push(player_total_number, dealer_total_number)


main()
