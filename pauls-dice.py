#
# paulsdice.py
#
# Paul Kaefer
# Created: 3/6/2012
#
# Paul's Dice: a command-line, text-based dice-rolling utility. That's right, utility.
#
# References:
#     substrings: http://www.astro.ufl.edu/~warner/prog/python.html
#     look for a character within a string: http://docs.python.org/library/stdtypes.html#str.find
#

import random       # for the dice and coins; for all general randomness *salutes*

# Program version #

about_string = "Paul's Dice, Version 1.0, Created 2012"
bar = "============================================================"

print ""
print about_string
print ""

# Function Declarations #

def roll(dice_size, number):
    total=0
    for i in range(0,number):
        total+=random.randrange(dice_size)+1
    return total

def xky(x, y):
    rolls = range(0,x)
    for i in range(0,x):
        rolls[i] = 0
    for i in range(0,x):
        rolls[i] = roll(10, 1)
    print ""
    print bar
    print ""
    print "Raw rolls:        "+repr(rolls)
    print ""
    print "Raw sum: "+repr(sum(rolls))
    rolls = sorted(rolls, reverse=True)
    print ""
    print "Sorted rolls:     "+repr(rolls)
    print ""
    exploding_dice = 0
    total = 0
    for i in range(0,y):
        if ( rolls[i] == 10 ):
            exploding_dice += 1
            # Explode!
            print "Exploding die number "+repr(exploding_dice)
            keep_going = True 
            running_sum = 10
            while ( keep_going ):
                newroll = roll(10, 1)
                print " next: "+repr(newroll)
                running_sum += newroll
                if ( newroll != 10 ):
                    keep_going = False
            # end while loop
            total += running_sum
        else: # not a 10
            total += rolls[i]
    print "\n"+repr(x)+"k"+repr(y)+" sum: "+repr(total)
    print ""
    print bar
    print ""

def flip_coin(number):
    flip=0
    for i in range(0,number):
        flip=random.randrange(2)
        if (flip==1):
            print "You flipped a heads"
        elif (flip==0):
            print "You flipped a tails"

def test_coin():
    heads=0
    tails=0
    flip=0
    for i in range(0,200):
        flip=random.randrange(2)
        if (flip==0):
            tails+=1
        elif (flip==1):
            heads+=1
    print " "
    print "Coin toss randomness test results:"
    print " "
    print "Heads: "+repr(heads)
    print "Tails: "+repr(tails)
    print " "

def test_dice(value, number):
    roll_max = value*number
    roll_min = number*1
    array  = range(0, roll_max+1)
    for i in range(0, roll_max+1):
        array[i] = 0
    roll=0
    number_of_possible_rolls = roll_max - roll_min + 1
    total_rolls = number_of_possible_rolls * 100
    for i in range(0, total_rolls):
        roll = 0
        for i in range(1, number+1):
            roll+=random.randrange(value)+1
        array[roll] = array[roll] + 1
    for i in range(roll_min, roll_max+1):
        print repr(i)+"s: "+repr(array[i])

# Program loop -- loops until stopped #

stop = 0
prompt = "> " # default prompt

while ( stop == 0 ):
    command = raw_input(prompt)
    #print command
    if (command=="quit") or (command=="exit") or (command=="Q") or (command=="q") or (command=="stop"):
        stop = 1
    elif (command=="about") or (command=="info"):
        print ""
        print about_string
        print ""
    elif (command=="help") or (command=="h") or (command=="H"):
        print ""
        print "Some available commands:\n"
        print ""
        print "  ndx: roll n dXs"
        print "       example: 1d6 or 2d20"
        print "       d6 rolls 1d6"
        print "       n and x may have any postive integer value"
        print ""
        print "  xky: roll x and keep y"
        print "       example: 5k3"
        print ""
        print "  flip coin: flips a standard two-sided coin"
        print ""
        print "  Is this really random?"
        print "    Test it out! Typing 'test 1d6' will show the results of many die rolls."
        print "    You can do this with any positive integers (eg, 'test 2d20' or 'test 7d45')"
        print "    You can also do 'test coin' to see if the coin tosses are fair."
        print ""
    elif (command=="hello") or (command=="hi"):
        print "Hello, chum!"
    elif (command=="flip coin") or (command=="toss coin") or (command=="coin flip") or (command=="coin toss") or (command=="coin") or (command=="flip"):
        flip_coin(1)
    elif (command=="clear") or (command=="cls") or (command=="clr") or (command=="clc") or (command=="c"):
        for i in range(0,100):
            print ""
        print "Type stuff down here, now!\n"
    elif (command=="test coin"):
        test_coin();
    elif (command[0:4]=="test"):
        splitarg = command.split(' ')
        #print "test:         "+splitarg[0]
        #print "die to test:  "+splitarg[1]
        if (len(splitarg) == 1):
            n = 1
            x = 6
        else: 
            splitarg = splitarg[1].split('d')
            if (splitarg[0] == ''):
                n = 1
            else:
                n = int(splitarg[0])
            #print n
            x = int(splitarg[1])
            #print x
        print "\nTesting "+repr(n)+"d"+repr(x)+"\n"
        test_dice(x, n)
        print ""
    elif (command[0:6]=="prompt"):
        splitarg = command.split(' ')
        nargs = len(splitarg)
        if ( nargs == 1 ):
            prompt = "> "
        else:
            prompt = ""
            for i in range(1, nargs):
                prompt += splitarg[i]+" "
    elif (command == "roll"):
        print "\nYou rolled a d6 and got a "+repr(roll(6, 1))+".\n"
    elif (command[0:4]=="roll"):
        splitarg = command.split(' ')
        # default case: no argument given (just "roll")
        if (len(splitarg) == 1):
            nargs = 1
        else:
            splitarg = splitarg[1].split('d')
            if (splitarg[0] == ''):
                n = 1
            else:
                n = int(splitarg[0])
            x = int(splitarg[1])
            if (n == 1):
                print "\nYou rolled a "+repr(roll(x, 1))+"."
            else:
                rolls  = range(0, n)
                for i in range(0, n):
                    rolls[i] = roll(x, 1)
                print ""
                print bar
                print ""
                print "Rolls:  "+repr(rolls)
                rolls = sorted(rolls, reverse=True)
                print ""
                print "Sorted: "+repr(rolls)
                print ""
                print "Sum: "+repr(sum(rolls))+"\n"
                print bar
            print ""
    elif (command[0:3]=="xky"):
        splitarg = command.split(' ')
        nargs = len(splitarg)
        if (nargs < 3):
            print ""
            print "Usage:    N1kN2     or     xky N1 N2"
            print ""
            print "Example:  5k3       or     xky 5 3"
            print ""
        else:
            x = int(splitarg[1])
            y = int(splitarg[2])
            if (y>x):
                print "\nError: y > x\n"
            else:
                xky(x, y)
    else:
        splitarg = command.split(' ')
        nargs = len(splitarg)
        if ( nargs == 0 ):
            nargs = 0
        else:
            if 'k' in splitarg[0]:
                rollcommand = splitarg[0]
                rollcommand = rollcommand.split('k')
                n = len(rollcommand)
                if (n != 2) or (rollcommand[0] == '') or (rollcommand[1] == ''):
                    print ""
                    print "Usage:    N1kN2     or     xky N1 N2"
                    print ""
                    print "Example:  5k3       or     xky 5 3"
                    print ""
                else:
                    x = int(rollcommand[0])
                    y = int(rollcommand[1])
                    if (y>x):
                        print "\nError: y > x\n"
                    else:
                        xky(x,y)
            elif 'd' in splitarg[0]:
                rollcommand = splitarg[0]
                rollcommand = rollcommand.split('d')
                n = len(rollcommand)
                if (n != 2):
                    print ""
                    print "Usage:    N1dN2     or     roll N1dN2"
                    print ""
                    print "Example:  2d20      or     roll 2d20"
                    print ""
                else:
                    if (rollcommand[0] == ''):
                        n = 1
                    else:
                        n = int(rollcommand[0])
                    if (rollcommand[1] == ''):
                        x = 6
                    else:
                        x = int(rollcommand[1])
                    if (n == 1):
                        print "\nYou rolled a "+repr(roll(x, 1))+"."
                    else:
                        rolls  = range(0, n)
                        for i in range(0, n):
                            rolls[i] = roll(x, 1)
                        print ""
                        print bar
                        print ""
                        print "Rolls:  "+repr(rolls)
                        rolls = sorted(rolls, reverse=True)
                        print ""
                        print "Sorted: "+repr(rolls)
                        print ""
                        print "Sum: "+repr(sum(rolls))
                        print ""
                        print bar
                    print ""
    # card? -- would have to do before ELSE{check for k, d}
    # quote?
    # why?
    # fortune?
    # random/random roll


