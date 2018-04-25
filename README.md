# Rpi-ParsecUI
Graphical user interface for Parsec on the Raspberry PI

-----------------------


First off, and most importantly - I am not affiliated with parsec!

I do not own any of the resources used to make this GUI!

I did this project for fun, it's really the first thing i ever made worth sharing.

----------------------

Thank you for using the unoficial Parsec GUI for the raspberry PI!

----------------------

Known problems:

1- (No saved passwords functionality)-Working

2- No more than 1 server supported

3- Settings/help/about not implemented -Next

4- (No loading indicator)- Introduced threading- (pretty much working***)


5- Fonts are not the ones intended

6- Title bar not removed (but "fake bar" buttons work)

7- If the server becomes unavailable after clicking "play button" (and before finishing connection cycle) the UI will crash

8- Error dialog window needs some make-up

9- "fake bar" is not able to move the window

10- nickname display not working

*** - Might look like it's "loading forever" when email and password fields are empty, or email is not a valid email (missing "@" or ".")

----------------------------------------------

Find me on discord! @WrongMan#2784

----------------------------------------------

Needs parsec raspbian version installed: https://parsecgaming.com/downloads



Download Compiled version here: https://github.com/wrong1man/Rpi-ParsecUI/releases/

Extract on the PI! Run file in dist folder. Needs xwindows (raspbian with a desktop); probably needs python3 (probably already installed)


Code version - start from log2_0.py. Needs xwindows; python3 +imported modules
