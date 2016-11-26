from random import randint

N = 1000

def simulate(N):
    K = 0       # number of correct guesses, after swap
    b = 0       # number of correct initial guesses
    loose = 0   # number of guesses that were incorrect both before and after swapping (should be zero if num_doors = 3)

    num_doors = 3
    options = [x for x in range(1, num_doors+1)]
    print options

    for n in range(N):

        # make this generic-ish: change options to change number of doors
        #options = [1,2,3]       # could remame to "doors"
        #num_doors = len(options)

        # choose a door randint(3) to hold the prize
        prize = randint(1,num_doors)

        # place a bet on a door randint(3)
        bet = randint(1,num_doors)

        # show a door
        # can't be prizedoor or betdoor
        #   - randomly show one of the doors, if prize==bet door
        #   - else show the only door that isn't prize or bet door
        remain = [d for d in options if  (d!=prize and d!=bet)]

        # this is overkill, but want to do a more generic version, allowing for more than 3 doors
        show = remain[randint(0, len(remain)-1)]
        #print prize, bet, remain, show

        # Now switch bet to the door that is NOT bet and is NOT shown
        #   (can bypass by simply incrementing if initial bet was NOT == Prize, logically its the same because out of 3 doors, its equivaleny)
        # if bet NOW == prize increment k
        # generic solution for more than 3 doors, overkill for only 3 doors
        new_options = [d for d in options if (d!=bet and d!=show)]
        new_bet = new_options[randint(0, len(new_options)-1)]
        #print new_options, new_bet, bet, remain, prize, show

        if bet == prize:
            b += 1
        elif new_bet==prize:
            K += 1
        else:
            loose += 1


    print "Number of Doors: ", num_doors
    print "Percentage Initial Guess was Correct: ", 100.0 * float(b)/float(N)
    print "Percentage Swapped Guess was Correct: ", 100.0 * float(K)/float(N)
    print "Percentage neither guess was correct: ", 100.0 * float(loose)/float(N), "  (should be zero if only 3 doors)"

    # hypothesis is that K/N will be 2/3, on 3 doors.
    return float(K) / float(N)
    
# TODO: let user choose number of doors
# todo: let user set number of iterations
print simulate(N)