### hello

#################################################################
# FILE : README
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs2 ex12 2020
# DESCRIPTION: the main program for the boggle program
# STUDENTS WE DISCUSSED THE EXERCISE WITH:
# WEB PAGES WE USED:
#################################################################

Additions to the code:

1. main menu:
    we chose to add a main menu screen as an additional decorative feature

2. instructions:
    we chose to implement an instructions screen as an additional decorative
    feature

3. get hint:
    we added the functionality in the game to enable the player to ask for a
    hint.
    if the player asks for a hint we use the function find_length_n_words with
    a random number for n, either 3 or 4, and the hint word and coordinates
    will return from the function. from there we use a method of Game class to
    emphasize the letters of the word on the board for 0.5 seconds. we also
    make sure we dont show hints of words the player has already found.
    because we needed the hints to be found in a very fast pace so the player
    wont feel any delay, we have 2 separate sub-functions for
    find_length_n_words, a recursive function and a combinations based
    function, the recursive function preforms better for higher n values, while
     the combination based function has very good performance for lower n
     values, and a very bad runtime (worse then O(e^n)), the results of our
     runtime analysis can be seen in the added files:
     a. project_extras/combinations_based.png - analysis of ~10 runs of the
     combination based function, with the graph of (e**n)/2 for reference.
     b. project_extras/combinations_based_vs_recursive.png - analysis of ~300
     runs of the combination based and recursive functions.

you can also see the entire structure of the project:
    a. project_extras/game flow chart.jpg - a flow chart of the entire program
    b. project_extras/classes chart.jpg - an inheritance chart of all the
    classes in the program
