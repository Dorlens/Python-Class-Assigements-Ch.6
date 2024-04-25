# Dorlens Janvier Chapter 6 Exercises 5

userAge = [10,30,50,18,21,40,12,17,15]
over_Eighteen = []

def isSorted(userAge):
 for i in range(len(userAge)):
        if i >= 18:
            over_Eighteen.append(i)
        else:
           return True
        return False

if isSorted(userAge):
    print("True")
else:
     print("False")