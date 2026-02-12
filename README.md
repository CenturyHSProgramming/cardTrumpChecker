# cardTrumpChecker()
You are tasked with writing a function that receives two cards each in the form of a tuple, and your job is to determine with of the two cards trumps the other.

**Notes:**
----------
The rules are as follows:
* cards are numbered from 1 - 10
* each card has one of three different colors:
  * green,
  * yellow, and
  * red.
* Higher numbers always trump (beat) lower numbers
  * color doesn't matter if one number is higher than the other
* When the numbers are the same...
  * yellow trumps (beats) green
  * red trumps (beats) yellow
* If both cards have the same number and color, the first card played always wins
  * it was played first

**Inputs:**
----------
cardTrumpChecker() receives two inputs (tuples): the first card and the second card

* NOTE: each card will be a tuple, like so: **(*card*, *rank*, *color*)**
  * **card** is a string: *"card1"* or *"card2"*
  * **rank** is an integer: between 1 and 10
  * **color** is an string: *"red"* *"yellow"* or *"green"*
  * Example: ("card1", 9, "red")
  * WARNING: regardless of the name of the first or second card, the first tuple is always considered the first card played (in the off-chance the card has a different name than 'card1' or 'card2')

**Output:**
------------
cardTrumpChecker() returns 1 output (a string): **card**

 * NOTE: always return the value of the first card (example: if the first card name is `"Jeff"`, return `"Jeff"` and not the string `"card1"`)

**Hints:**
------------
For this challenge, since you are using tuples, you're going to want to review indexing with tuples (or unpacking a tuple).
For exceeds, be careful with the names of the cards, 
* they could be a different name than `card1` or `card2`.
* they could even be switched.
* Example: if the card that wins is called `phred`, then your function should return `phred`

**Examples:**
inputs => output/s
--------------------------------
* ('card1', 5, 'yellow') ('card2', 7, 'green') => card2
* ('card1', 5, 'red') ('card2', 5, 'yellow') => card1
* ('card1', 10, 'green') ('card2', 10, 'yellow') => card2
* ('card1', 2, 'green') ('card2', 1, 'red') => card1
* ('card1', 10, 'red') ('card2', 10, 'red') => card1
