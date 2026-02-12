from src.cardtrumpchecker import card_trump_checker


# Proficient tests
def test_card_trump_checkerForHighNumOnly():
    result = card_trump_checker.card_trump_checker(('card1', 8, 'green'),
                                               ('card2', 3, 'green'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForLowNumLowColor():
    result = card_trump_checker.card_trump_checker(('card1', 1, 'green'),
                                               ('card2', 2, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForMidRangeValues():
    result = card_trump_checker.card_trump_checker(('card1', 5, 'yellow'),
                                               ('card2', 5, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForMidRangeNumHighColor():
    result = card_trump_checker.card_trump_checker(('card1', 5, 'red'),
                                               ('card2', 6, 'green'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForAllHighValues():
    result = card_trump_checker.card_trump_checker(('card1', 10, 'yellow'),
                                               ('card2', 10, 'green'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForAllLowValues():
    result = card_trump_checker.card_trump_checker(('card1', 1, 'red'),
                                               ('card2', 1, 'yellow'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForLowColor_LowNum():
    # Capture the results of the function
    result = card_trump_checker.card_trump_checker(('card1', 3, 'green'),
                                               ('card2', 4, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForHighNum_HighColor_2():
    # Capture the results of the function
    result = card_trump_checker.card_trump_checker(('card1', 10, 'red'),
                                               ('card2', 7, 'green'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForRedBeatsYellow():
    result = card_trump_checker.card_trump_checker(('card1', 5, 'yellow'),
                                               ('card2', 5, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForYellowBeatsGreen():
    result = card_trump_checker.card_trump_checker(('card1', 7, 'green'),
                                               ('card2', 7, 'yellow'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForHigherNumberAlwaysWins():
    result = card_trump_checker.card_trump_checker(('card1', 3, 'red'),
                                               ('card2', 8, 'green'))
    expected = "card2"
    assert result == expected
