# Minwoo Rhee
# 10/08/18
# assignment_four
# a simplified version of the game, Blackjack

import random


def give_instruction():
    """
    give instructions about the rules of the game
    :return: None
    """
    print("Welcome to the simplified version of the game, Blackjack")
    print("You will first draw two cards from 1~10 and then you will be asked if you wanted to draw a third card.")
    print("The purpose of the game is to have higher total number than the dealer, who will draw only two cards.")
    print("However, if your total number exceeds 21, you will lose regardless of the dealer's number")
    print("Good luck, and enjoy.")
    print(" ")  # printing blank lines to make the program easier to read.
    print(" ")


def draw_card():
    """
    draw a card from the deck of 10 cards, each having a value from 1 to 10
    :return: a random number from 1 to 10
    """
    number = random.randint(1, 10)
    return number


def player_draws():
    """
    draws two cards for the player and print the total number of the player
    :return: total number of the player
    """
    player_first_card = draw_card()
    player_second_card = draw_card()
    player_total_number = player_first_card + player_second_card
    print("Your drew ", player_first_card, "and ", player_second_card, ".")
    print("Your total is ", player_total_number, ".")
    return player_total_number


def draw_third_card(player_total):
    """
    asks the player if they wanted a third card
    if the answer is yes (y), draw the third card and print the new total number of the player
    :param player_total: total number of the player before the third draw
    :return: total number of the player after the third draw
    """
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


def dealer_draws():
    """
    draws two cards for the dealer and print the total number of the dealer
    :return: total number of the dealer
    """
    dealer_first_card = draw_card()
    dealer_second_card = draw_card()
    dealer_total_number = dealer_first_card + dealer_second_card
    print(" ")
    print("The dealer drew", dealer_first_card, "and", dealer_second_card, ".")
    print("The dealer's total number is", dealer_total_number, ".")
    return dealer_total_number


def win_lose_or_push(player_total_number, dealer_total_number):
    """
    compares the player's total number to the dealer's, determines the result of the game
    :param player_total_number: total number of the player
    :param dealer_total_number: total number of the dealer
    :return: None
    """
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
