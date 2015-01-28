from random import randint
from montecarlo import montecarlo

def flip_coin(g):
    if randint(0, 1) == 0:
        return True
    return False

mc = montecarlo(flip_coin)
result = mc.run()
print "Result returned: " + str(result)