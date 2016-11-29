"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    rolls = []
    while num_rolls > 0:
        rolls.append(dice())
        num_rolls -= 1
    if 1 in rolls:
        return 1
    return sum(rolls)
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    if num_rolls == 0:
        current, remainder = opponent_score, 0
        while current >= 1:
            remainder = current % 10
            current //= 10
            if remainder > current: return remainder + 1
        return current + 1
    else:
        return roll_dice(num_rolls, dice)
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    score_zero = score0 % 100
    score_one = score1 % 100
    def reverse(n):
        first_digit = n // 10
        second_digit = n % 10
        return second_digit * 10 + first_digit
    return reverse(score_zero) == score_one
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1, select_dice(score0, score1))
        else:
            score1 += take_turn(strategy1(score1, score0), score0, select_dice(score0, score1))
        if is_swap(score0, score1):
            score0, score1 = score1, score0
        who = other(who)
    # END Question 5
    return score0, score1

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    # BEGIN Question 6
    def average(*args):
        current, result = 0, 0
        while current < num_samples:
            result += fn(*args)
            current += 1
        return result / num_samples
    return average
    # END Question 6

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    n = 1
    max_val, max_rol, hold = 0, 0, 0
    while n <= 10:
        hold = make_averaged(roll_dice, num_samples)(n, dice)
        if hold > max_val: 
            max_val = hold
            max_rol = n
        n += 1
    return max_rol
    # END Question 7

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))


    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    first_digit = opponent_score % 100 // 10 + 1
    second_digit = opponent_score % 100 % 10 + 1
    if first_digit >= second_digit: second_digit = first_digit
    if second_digit >= margin: num_rolls = 0
    return num_rolls # Replace this statement
    # END Question 8

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS if rolling 0 dice results in a harmful swap. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    # BEGIN Question 9
    new_score = score + max(int(i) for i in str(opponent_score)) + 1
    if is_swap(new_score, opponent_score):
        if new_score <= opponent_score and opponent_score - score >= margin:
            num_rolls = 0
    else:
        num_rolls = bacon_strategy(score, opponent_score, margin, num_rolls)
    return num_rolls # Replace this statement
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN Question 10
    """new_score = score + max(int(i) for i in str(opponent_score)) + 1
    max_digit = max(int(i) for i in str(opponent_score))
    if (new_score + opponent_score) % 7 == 0:
        return 0
    else:
        if (score + opponent_score) % 7 == 0:
            if 100 - score < 10:
                return swap_strategy(score, opponent_score, 10, 2)
            elif opponent_score - score > 20:
                return swap_strategy(score, opponent_score, 20, 6)
            elif score - opponent_score > 20:
                return swap_strategy(score, opponent_score, 20, 3)
            elif 20 > opponent_score - score > 10:
                return swap_strategy(score, opponent_score, 20, 5)
            elif 20 > score - opponent_score > 10:
                return swap_strategy(score, opponent_score, 20, 3)
            else:
                return swap_strategy(score, opponent_score, 20, 4)
        else:
            if 100 - score < 10:
                return swap_strategy(score, opponent_score, 10, 3)
            elif (opponent_score - score > 20):
                return swap_strategy(score, opponent_score, 20, 9)
            elif score - opponent_score > 20:
                return swap_strategy(score, opponent_score, 20, 4)
            elif 20 > opponent_score - score > 10:
                return swap_strategy(score, opponent_score, 20, 8)
            elif 20 > score - opponent_score > 10:
                return swap_strategy(score, opponent_score, 20, 5)
            else:
                return swap_strategy(score, opponent_score, 20, 6)"""
    new_score = score + max(int(i) for i in str(opponent_score)) + 1
    max_digit = max(int(i) for i in str(opponent_score))
    if (new_score + opponent_score) % 7 == 0:
        return 0
    else:
        if (score + opponent_score) % 7 == 0:
            if opponent_score - score > 20:
                return swap_strategy(score, opponent_score, 5, 6)
            elif score - opponent_score > 20:
                return swap_strategy(score, opponent_score, 5, 3)
            elif 20 > opponent_score - score > 10:
                return swap_strategy(score, opponent_score, 5, 5)
            elif 20 > score - opponent_score > 10:
                return swap_strategy(score, opponent_score, 5, 3)
            else:
                return swap_strategy(score, opponent_score, 5, 4)
        else:
            if (opponent_score - score > 20):
                return swap_strategy(score, opponent_score, 9, 9)
            elif score - opponent_score > 20:
                return swap_strategy(score, opponent_score, 9, 4)
            elif 20 > opponent_score - score > 10:
                return swap_strategy(score, opponent_score, 9, 8)
            elif 20 > score - opponent_score > 10:
                return swap_strategy(score, opponent_score, 9, 5)
            else:
                return swap_strategy(score, opponent_score, 9, 6)

    # END Question 10


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--final', action='store_true',
                        help='Display the final_strategy win rate against always_roll(5)')
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
    elif args.final:
        from hog_eval import final_win_rate
        win_rate = final_win_rate()
        print('Your final_strategy win rate is')
        print('    ', win_rate)
        print('(or {}%)'.format(round(win_rate * 100, 2)))
