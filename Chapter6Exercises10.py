#Dorlens Janvier Chapter 6 Exercises 10




def myRange(stop, start=None, step=None):
    if start is None and step is None:
        start, stop = 0, stop
        step = 1
    elif step is None:
        start, stop = stop, start
        step = -1

    result = []
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    elif step < 0:
        while start > stop:
            result.append(start)
            start += step

    return result

# Test 
print(myRange(5))           
print(myRange(1, 5))        
print(myRange(1, 10, 2))    
print(myRange(10, 1, -2))   