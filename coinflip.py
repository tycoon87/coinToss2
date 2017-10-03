import random

def flip(times):
    heads = 0
    tails = 0
    result = ""
    attempt = 0
    for i in range(0, times):
        toss = random.randint(0,1)
        if (toss == 1):
            attempt += 1
            heads += 1
            result = "heads"
            print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} heads(s) so far and {} tails(s) so far".format(attempt, result, heads,tails)
        else:
            attempt += 1
            tails += 1
            result = "tails"
            print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} heads(s) so far and {} tails(s) so far".format(attempt, result, heads,tails)
        if attempt == times:
            print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} heads(s) so far and {} tails(s) so far '\n' Ending the program, thank you!".format(attempt, result, heads,tails)
print flip(500)