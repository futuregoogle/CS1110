# blackjack_checks.py
# L. Lee (LJL2), S. Marschner (SRM2), and W. White (WMW2)
# April 2021

"""Some light checking for module blackjack"""

import testcase as ca # Stands for "testing module"
import blackjack
import card as cardmod
import sys
import inspect  # Used to get function names automatically:
                # inspect.stack()[0] is the "highest" frame on the call stack


# Possible card lists and their scores.
test_cases_in_common = {
    (cardmod.Card(alt='AD'),): 11,  # A single ace
    (cardmod.Card(alt='2H'), cardmod.Card(alt='5S')): 7,    # No face cards
    (cardmod.Card(alt='2C'), cardmod.Card(alt='AH')): 13,   # Includes an ace
    (cardmod.Card(alt='KD'), cardmod.Card(alt='2D')): 12,   # Includes a king
    (cardmod.Card(alt='QH'), cardmod.Card(alt='7D')): 17,   # Includes a queen
    (cardmod.Card(alt='JS'), cardmod.Card(alt='8C')): 18,   # Includes a jack
    (cardmod.Card(alt='TH'), cardmod.Card(alt='AC')): 21,   # a ten and an ace
    (cardmod.Card(alt='AD'), cardmod.Card(alt='AH')): 22,   # Two aces
    (cardmod.Card(alt='2C'), cardmod.Card(alt='3C'), cardmod.Card(alt='4S')): 9,
    (cardmod.Card(alt='2C'),
     cardmod.Card(alt='2D'),
     cardmod.Card(alt='2H'),
     cardmod.Card(alt='2S'),
     cardmod.Card(alt='3C')): 11,
    (cardmod.Card(alt='5H'), cardmod.Card(alt='AS')): 16,
    (cardmod.Card(alt='KD'), cardmod.Card(alt='3C')): 13,
    (): 0  # empty list
}

# Possible hands and whether they are bust are not.
# Remember that in our rules, Aces count as 11.
test_cases_bust={
    (cardmod.Card(alt='AD'), cardmod.Card(alt="TC")): False,
    (cardmod.Card(alt='AC'), cardmod.Card(alt='TD'), cardmod.Card(alt='2C')): True,
    (cardmod.Card(alt='TS'), cardmod.Card(alt='TD'), cardmod.Card(alt='AC')): True,
    (cardmod.Card(alt='JC'), cardmod.Card(alt='TS'), cardmod.Card(alt='AC')): True,
    (cardmod.Card(alt='QH'),
     cardmod.Card(alt='TD'),
     cardmod.Card(alt='AS'),
     cardmod.Card(alt='AC')): True,
    (cardmod.Card(alt='AD'),): False,
    (cardmod.Card(alt='2H'), cardmod.Card(alt='5S')): False,
    (cardmod.Card(alt='2C'), cardmod.Card(alt='AH')): False,
    (cardmod.Card(alt='KD'), cardmod.Card(alt='2D')): False,
    (cardmod.Card(alt='QH'), cardmod.Card(alt='7D')): False,
    (cardmod.Card(alt='JS'), cardmod.Card(alt='8C')): False,
    (cardmod.Card(alt='TH'), cardmod.Card(alt='AC')): False,
    (cardmod.Card(alt='AD'), cardmod.Card(alt='AH')): True,
    (cardmod.Card(alt='2C'), cardmod.Card(alt='3C'), cardmod.Card(alt='4S')): False,
    (cardmod.Card(alt='2C'),
     cardmod.Card(alt='2D'),
     cardmod.Card(alt='2H'),
     cardmod.Card(alt='2S'),
     cardmod.Card(alt='3C')): False,
    (cardmod.Card(alt='5H'), cardmod.Card(alt='AS')): False,
    (cardmod.Card(alt='KD'), cardmod.Card(alt='3C')): False,
    (): False
}

# It's useful to have a dummy game around, where the actual player and dealer
# hands will later be overwritten in testing
def make_dummy_game():
    """Returns a dummy blackjack game."""
    return blackjack.Blackjack([cardmod.Card(alt='QC'),
                                  cardmod.Card(alt='TD'),
                                  cardmod.Card(alt='9H')])




def test_init(verbose):
    """Test initializer of blackjack objects.
    Extra info printed if `verbose` is True. """

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    # Small test
    c1 = cardmod.Card(0, 12)
    c2 = cardmod.Card(1, 10)
    c3 = cardmod.Card(2, 9)
    c4 = cardmod.Card(0, 1)
    start_deck = [c1, c2, c3, c4]
    if verbose:
        print("testing start deck of " + cardmod.cardlist_str(start_deck))

    game = blackjack.Blackjack(start_deck)
    ca.assert_equals(set([c1, c2]), set(game.playerHand))  # Sets ignore order
    ca.assert_equals([c3], game.dealerHand)
    ca.assert_equals([c4], start_deck)  # Check that cards were removed
    ca.assert_equals(id(start_deck), id(game.deck))

    # Bigger test.
    start_deck = cardmod.full_deck()
    if verbose:
        print("testing start deck of " + cardmod.cardlist_str(start_deck))
    game = blackjack.Blackjack(start_deck)
    ca.assert_true(set([cardmod.Card(0, 1), cardmod.Card(0, 2)]) ==
                   set(game.playerHand))
    ca.assert_equals([cardmod.Card(0, 3)], game.dealerHand)
    # Check card removal
    ca.assert_equals(cardmod.full_deck()[3:], start_deck)
    ca.assert_equals(start_deck, game.deck)

    print_done_message(True, tester_name)


def test_str(verbose):
    """Test __str__ function for Blackjack objects.
    Extra info printed if `verbose` is True."""

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    # Test cases:
    # Keys are tuples of the form (playerhand, dealerhand)
    # Values are the desired output of __str__
    test_cases = {
        ((cardmod.Card(alt='QH'), cardmod.Card(alt='TD')),
         (cardmod.Card(alt='9H'),)): 'player: 20; dealer: 9',
        ((),
         (cardmod.Card(alt='9H'),)): 'player: 0; dealer: 9',
        ((),
         (cardmod.Card(alt='9H'), cardmod.Card(alt="AH"))): 'player: 0; dealer: 20',
        ((cardmod.Card(alt='9H'), cardmod.Card(alt="TH")),
         (cardmod.Card(alt='3S'), cardmod.Card(alt='KH'), cardmod.Card(alt='9C'))):
        'player: 19; dealer: 22'
    }

    game = make_dummy_game()
    for tc in test_cases:
        phand = list(tc[0])
        dhand = list(tc[1])
        if verbose:
            print('\tTesting ' +
                  cardmod.cardlist_str(phand) + ' and ' + cardmod.cardlist_str(dhand))
        answer = test_cases[tc]
        game.playerHand = phand
        game.dealerHand = dhand
        output = str(game)
        ca.assert_equals(answer, output)

    print_done_message(True, tester_name)


def test_score(verbose):
    """Test _score function.
    Extra info printed if `verbose` is True."""

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    for tc in test_cases_in_common:
        if verbose:
            print('\tTesting ' + cardmod.cardlist_str(tc))
        answer = test_cases_in_common[tc]
        output = blackjack._score(list(tc))  # Convert tuple to list
        ca.assert_equals(answer, output)

    print_done_message(True, tester_name)


def test_dealerScore(verbose):
    """Test dealerScore function.
    Extra info printed if `verbose` is True."""

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    game = make_dummy_game()
    for tc in test_cases_in_common:
        if verbose:
            print('\tTesting ' + cardmod.cardlist_str(tc))
        answer = test_cases_in_common[tc]
        game.dealerHand = list(tc)  # Set the dealerHand to be a test case.
        output = game.dealerScore()
        ca.assert_equals(answer, output)

    print_done_message(True, tester_name)


def test_playerScore(verbose):
    """Test playerScore function.
    Extra info printed if `verbose` is True."""

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    game = make_dummy_game()
    for tc in test_cases_in_common:
        if verbose:
            print('\tTesting ' + cardmod.cardlist_str(tc))
        answer = test_cases_in_common[tc]
        game.playerHand = list(tc)  # Set the playerHand to be a test case.
        output = game.playerScore()
        ca.assert_equals(answer, output)

    print_done_message(True, tester_name)


def test_dealerBust(verbose):
    """Test dealerBust function.
    Extra info printed if `verbose` is True."""

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    game = make_dummy_game()
    for tc in test_cases_bust:
        if verbose:
            print('\tTesting ' + cardmod.cardlist_str(tc))
        answer = test_cases_bust[tc]
        game.dealerHand = list(tc)
        output = game.dealerBust()
        ca.assert_equals(answer, output)

    print_done_message(True, tester_name)


def test_playerBust(verbose):
    """Test playerBust function.
    Extra info printed if `verbose` is True."""

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    game = make_dummy_game()
    for tc in test_cases_bust:
        if verbose:
            print('\tTesting ' + cardmod.cardlist_str(tc))
        answer = test_cases_bust[tc]
        game.playerHand = list(tc)
        output = game.playerBust()
        ca.assert_equals(answer, output)

    print_done_message(True, tester_name)


def ask_to_quit(verbose, nextfn=None):
    """Ask if user wishes to test the next function nextfn;
       terminate execution if not.
    Does nothing if `verbose` is False.
    If nextfn, the name of the next function, isn't given, Python uses the
      value None"""
    if verbose:
        if nextfn is None:
            nextfn = "the next function"
        msg = 'Press q to quit, anything else to start running '
        msg += nextfn + '(). '
        response = input(msg)
        if response == "q":
            sys.exit()


def print_done_message(verbose, tester_name):
    """If verbose is True, print that tester_name ran without errors.
    If verbose if False, do nothing."""
    if verbose:
        print(tester_name + str(" ran without errors"))


# Script code
if __name__ == '__main__':

    verbose = True  # Default mode is to give lots of output.
                    # False means give less output

    # Handling arguments from the command line
    if len(sys.argv) > 1:
        # Was called with at least one argument
        if len(sys.argv) == 2 and sys.argv[1] in ["quiet"]:
            # called by "python <this file's name> quiet"
            verbose = False
        else:
            print("Invalid argument(s), only possible argument is 'quiet'.")
            sys.exit()

    fns_to_run = [test_init,
                  test_score, # This function should already be correct,
                              # since we wrote it for you.
                  test_dealerScore,
                  test_playerScore,
                  test_dealerBust,
                  test_playerBust,
                  test_str]


    for ind in range(len(fns_to_run)):
        fn = fns_to_run[ind]
        fn(verbose)
        if ind < (len(fns_to_run)-1):  # not the last test
            ask_to_quit(verbose, nextfn=fns_to_run[ind+1].__name__)

    print("All checks for blackjack passed")
