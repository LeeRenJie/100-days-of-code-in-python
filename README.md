# 100-days-of-code-in-python
Udemy Angela Yu's course that has 100 projects for students to make each day with classes with duration of 1~2 hours each day.<br>
This repository will store all the related projects. If you are intrested in any code files, please run the code in an IDE for python, although i recommend running it in replit as some modules are imported based on the website.<hr>

Below is my summary of what I've learned everyday and the link to fork the project in Repl.it(Online IDE):

<b>Day 1</b> (https://repl.it/@LeeRen1/D1-Band-name-generatorPOTD):<br>
A band name generator from the input of users of their country and a random pet name.
1. Used the print function, input function , and creating a variable.
2. Learned about commenting
3. Learned that "\n" brings the cursor/content to the next line in the same print function

<b>Day 2</b> (https://repl.it/@LeeRen1/D24-Tip-calculator-startPOTD):<br>
Created a simple calculator that takes in input of the total bill, percentage of tips to be given and the amount of people to split the bill. 
1. Applied the f string(found it really convenient)
2. Reminded me that inputs are in string data type and has to be converted into float/integers before dong any calculations
3. Reminded me how to round off with a specified decimal number "rounding_off=Round(2.666666,2)" = 2.66

<b>Day 3</b> (https://repl.it/@LeeRen1/D36-Treasure-islandPOTD):<br>
Created a storytelling like treasure island adventure where each steps u take lead to different outcomes.
1. Applied ASCII Art (figures made by numbers and symbols) via: https://ascii.co.uk/art
2. Learned if/elif/else statements & nested if/elif/else & multiple ifs
3. Reminded me that indentation is important in python
4. Had fun! 😆

<b>Day 4</b> (https://repl.it/@LeeRen1/D44-rock-paper-scissors-POTD):<br>
Created a simple rock-paper-scissors game👊🤚✌ where the computer's move is randomly generated using the random.choice after putting all moves into a list and selecting randomly.
1. Overall,learned about lists and how flexible it is whether it is to extend the list, replacing the item, choose a specific item with index starting from 0 from front and -1 from back, extending the list with another list from input and more
2. Learned that nested list and list_name[1][1] means choosing the second nested list in the general list and then choosing the second item from the selected list.
3. Revised if/elif/else statements and nested ifs
4. Learned about the python random module and differentiating between random.randint(starting index,ending index)/random.float()/random.choice(list_name)
5. Aware of index error and in most situation the index has to -1 since the computer starts counting from 0

<b>Day 5</b> (https://repl.it/@LeeRen1/D55-Password-generatorPOTD#main.py):<br>
Created a password generator that takes the user input for number of lettters/symbols/numbers wanted in the password then generated two types of password, first is following the sequence where it goes from letters to numbers and the second harder password is to shuffle the sequence od the password so that there is no specific pattern to ensure maximum security.🔒
1. Learned the fundamentals of for loops and for loop with a range[for x in range(start, end, step/gap)] 
2. Learned that I cant shuffle strings with the random.shuffle but i can shuffle a list!
3. Learned how to convert a list into a string (line 46-49)
4. Learned the logic behind for loops and it took my some time to finally understand the concept.😵 Definitely need more practice with the algorithm and structure

<b>Day 6</b> <br>
(https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json):<br>
Applied while loops in the website Reeborg's World to solve the maze challenge where the robot spins at every move and you have to reach to the flag without hitting the walls.(The tip was to follow the right side)
1. Code for: Hurdle 1 to 4 and POTD:MAZE in the file(two different challenges)
2. Learned about while loops where it will continue to execute if the condition is true
3. Learned to differentiate when to use for loops(To iterate/do something with each item in a list) and while loop(do the whole code block when the condition is true)
4. Realized that I can use tab for indentation and there is an argument whether programmers should use tabs or 4 spaces to indent.(Stats shows that programmers that use spaces has a higher average salary and I have no idea why🤣)
5. Learned to nest if statements into while loops
6. Learned about creating functions and calling them
7. Had fun and headache at the same time.

<b>Day 7</b> (https://repl.it/@LeeRen1/D75-HangmanPOTD#main.py):<br>
Built the hangman game. User has to guess a word and has limited chances.
1. Learned how to import modules and import the list/variables into the main file.
2. Reminded me the way to apply while and for loop
3. Had to figure out the logic step by step and focus on the indentation
4. Learned "in" to check if a statement is true (If x in y) 

<b>Day 8</b> (https://repl.it/@LeeRen1/D84-caesar-cipherPOTD#main.py):<br>
Created a program that can encrpyt or decrypt the user's input based on the number of shift they enter(move alphabets front or back). The encoded word can be decoded if the shift is the same.<br>(For example: To encode: Word=hello shift=5 > encoded word=mjqqt(shifted behind 5 alphabets) To decode: Word=mjqqt, shift=5(same shift amount) > decoded word=hello)
1. Applied functions, if-else statements, while loops, for loops, and many more that I learned in the past few days
2. Reminded me how to  import variables from another file(the ASCII art in this case)
3. Reminded me of the concept of modulo "%"
4.  Reminded me of the logic behind for loops and used it to debug the program
5. Learned about parameters and arguments, functions, functions with more than one inputs, the difference between positional arguments and keyword arguments
6. Needed to review the code several times to understand the logic behind..

<b>Day 9</b> (https://repl.it/@LeeRen1/D9-blind-auction-startPOTD#main.py):<br>
Created a program based on the concept of a silent auction where the concept is that nobody knows how much the bidders has bid and at the end of the auctionn the bidder with highest bid wins!
1. Learned about dictionaries, {key : value, key : value}, Adding another key+value, Edit a key to another value, Nesting dictionaries in list and vice versa, Nesting dict .in dict.,Looping through dict., access value from nested dict. and more.
2. Reminded me the logic and concept of while loops, for loops , if/else statement. 
3. Learned that dictionaries will be useful in the future to access data in keys.

<b>Day 10</b> (https://repl.it/@LeeRen1/D10-calculatorPOTD):<br>
Created a basic calculator that could do addition/subtraction/multiplication/division. The calculator can loop through so that the user could use the first answer to make another calculation or restart a brand new calculation.
1. Learned about recursion. Which is calling the function inside the same function so that it executes on a certain condition. (line 31 & line 56)
2. Learned about flagging with while loops. Which is to check if a certain condition is true until the condition becomes false where it will proceed to execute other codes. 
3. Reminded me of the concept of key and value of the dictionary.
4. Learned that the input function itself could be used as an output and therefore could be used as a condition. (line 51)
5. Learned the difference between print and return. 
<hr>

<b>Day 11</b> (https://repl.it/@LeeRen1/D11-blackjackPOTD):<br>
Built a Blackjack  game (Player with cards closest to 21 wins/sum of scores must be above 17/if two cards=21=blackjack=wins the game immediately)
1. Applied the knowledge used in the past 10 days.
2. Used docstring (6 quotes/""" definition""") to define a function's purpose (when you use the function or hover over it the definition of the function will be shown)
3.  Applied flagging and recursion again.
4. Reminded me that the functions you created should be before the line where you call it or it wont work.
5. Learned about the sum() function and list.remove(item) function.
6. It was hard but fun 😊

<b>Day 12</b> (https://repl.it/@LeeRen1/D12-Number-Guessing-GamePOTD#main.py):<br>
Created a number guessing game that uses most of the knowledge of past few days and add on with creating Constants. The user can choose between easy / hard to determine their turns avaialable to guess a number between 1 to 10.
1. Learned about constants (Variables that you are not gonna change its value again like the pi value)
2. Learned about global and local scopes(basically the location where u define your variables and whether it could be accessed within a function/while/for loop/if-else statement etc. Focuses on the indentation)
3. Learned about the (global varible_name) that takes a variable into the function to allow it to be modified. But the return statement is recommended.
4. Recapped about flagging
5. Tried to complete the challenge before viewing the solution therefore I have two different solutions. (Top is from the video/ Bottom is mine)
6. Used <a href="http://patorjk.com/software/taag/#p=display&h=1&v=1&f=Big&t=GUESS%20THE%20NUMBER">this website</a>
 to create ASCII art based on the words I typed in
            
<b>Day 13</b> ():<br>
