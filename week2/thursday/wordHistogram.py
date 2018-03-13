tally = {}
def wordHistogram(paragraph):
    words = paragraph.split()
    for word in words:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1
    print tally
def findTopThree(hist):
    sortedList = sorted(hist, key=hist.get)[::-1]
    print sortedList [0:3]
            
                
    
    

wordHistogram('to be or not to be not to')
findTopThree(tally)