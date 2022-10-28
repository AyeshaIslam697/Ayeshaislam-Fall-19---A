# Book lab 1




# Practice code 5.3 using a if else condition

# a) Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

alien_color = 'green'
if alien_color == 'green':
    print('You have earn 5 points')


# b)Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


alien_color = 'red'
if alien_color == 'green':
    print('You have eared 5 points')
else:
    print('Please try again.')



# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.


# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.

alien_color = 'Green'
if alien_color == 'Green':
    print('You have earn 5 points')
else:
    print('The player just earned 10 points.')



# Write one version of this program that runs the if block and another that runs the else block.

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")