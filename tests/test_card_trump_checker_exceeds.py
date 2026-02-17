from src.cardtrumpchecker import card_trump_checker

# Exceeds tests
def test_card_trump_checkerForHighColorOnly():
    result = card_trump_checker.card_trump_checker(('card1', 5, 'red'),
                                               ('card2', 5, 'green'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForLowNumHighColor_Reversed():
    result = card_trump_checker.card_trump_checker(('card2', 2, 'yellow'),
                                               ('card1', 6, 'red'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForSameNumDifferentColor():
    result = card_trump_checker.card_trump_checker(('card1', 7, 'green'),
                                               ('card2', 7, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForMinimumValues():
    result = card_trump_checker.card_trump_checker(('card1', 1, 'red'),
                                               ('card2', 1, 'red'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForMaximumValues():
    result = card_trump_checker.card_trump_checker(('joelle', 10, 'yellow'),
                                               ('wade', 10, 'yellow'))
    expected = "joelle"
    assert result == expected


def test_card_trump_checkerForSinglePointDifference():
    result = card_trump_checker.card_trump_checker(('chucky', 5, 'red'),
                                               ('daito', 6, 'green'))
    expected = "daito"
    assert result == expected


def test_card_trump_checkerForIdenticalCardsReverseOrder():
    result = card_trump_checker.card_trump_checker(('card2', 5, 'red'),
                                               ('card1', 5, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForBoundaryLowNum():
    result = card_trump_checker.card_trump_checker(('card1', 1, 'yellow'),
                                               ('card2', 2, 'green'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForBoundaryHighNum():
    result = card_trump_checker.card_trump_checker(('card1', 9, 'green'),
                                               ('card2', 10, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForAllColorsYellow():
    result = card_trump_checker.card_trump_checker(('i-R0k', 3, 'yellow'),
                                               ('Sho', 3, 'yellow'))
    expected = "i-R0k"
    assert result == expected


def test_card_trump_checkerForAllColorsGreen():
    result = card_trump_checker.card_trump_checker(('fnale', 7, 'green'),
                                               ('ogden', 7, 'green'))
    expected = "fnale"
    assert result == expected


def test_card_trump_checkerForColorPrecedenceAllCombinations():
    result = card_trump_checker.card_trump_checker(('card1', 1, 'yellow'),
                                               ('card2', 1, 'green'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForNearMaxValues():
    result = card_trump_checker.card_trump_checker(('card1', 9, 'yellow'),
                                               ('card2', 9, 'red'))
    expected = "card2"
    assert result == expected


def test_card_trump_checkerForMaxValues():
    # Capture the results of the function
    result = card_trump_checker.card_trump_checker(('card1', 10, 'red'),
                                               ('card2', 10, 'red'))
    expected = "card1"
    assert result == expected


def test_card_trump_checkerForHighNumHighColorReversed():
    result = card_trump_checker.card_trump_checker(('card2', 9, 'yellow'),
                                               ('card1', 4, 'green'))
    expected = "card2"
    assert result == expected
