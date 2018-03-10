def multi(factors):
    for fact1 in factors:
        for fact2 in factors:
            product = fact1 * fact2
            print "%s x %s = %s" % (fact1, fact2, product)
factors = range(1, 11)    
multi(factors)
