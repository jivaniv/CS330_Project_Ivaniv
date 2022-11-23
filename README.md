# CS330_Project_Ivaniv
Author: Julia Ivaniv

This repository cosists of two files containing the code for this project, a memo for the professor, a PNG file for the FA state transition diagram, and
this README file. 

The first file Ivaniv_J_part1.py is the code for part 1 of the project. This code asks for user input so that the user can enter the access code one value
at a time. After each value, the code run through a series of if/else statements to decide whether the access/locking code has been entered or not. The
user should only enter integers between 0-9, but if the user inputs any other value the code will just ignore it. The user can enter nothing to exit the
loop/code. The user input is never echoed. The access code is 182821 and the locking code is 182824. The code returns unlock/lock when these codes are
entered, respectively.

The second file Ivaniv_J_part2.py is the code for part 2 of the project. This code uses a random number generator to determine how many symbols an intruder
must enter on average to unlock the lock. The same loop containing if/else statements is used as in part 1, but instead of user input, the code generates
random numbers. After each number, the code checks if the access code (182824) has been entered. This test is repeated 100 times to obtain significant 
results. The code ouputs the minimum, maximum, and average number of symbols generated before the access code is entered. 

To run these to .py files in your terminal:

git clone https://github.com/jivaniv/CS330_Project_Ivaniv.git

cd CS330_Project_Ivaniv.git

python Ivaniv_J_part1.py

python Ivaniv_J_part2.py

Generate unit test coverage in your terminal:

pip install coverage

coverage run Ivaniv_J_part1.py unittest discover or coverage run Ivaniv_J_part2.py unittest discover

coverage report -m

//

This code has been tested in google collab, visual studio code, and my mac's local terminal. 


