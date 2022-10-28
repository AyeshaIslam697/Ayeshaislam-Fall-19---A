import numpy as np
from scipy import stat

print("Qno. 1: Find the mean of this particular dataset")

ayesha_1 = [99, 86 , 87 , 88 , 384 , 86 , 103 , 87 , 94 , 78 , 77 , 85 , 86]
me = np.mean(ayesha_1)
print(me)


print("Qno. 2: Find the median of the dataset of odd value?")

ayesha_2 = [77, 78, 85,86,86,86,87,34,88,94,99,103,111]

med = np.median(ayesha_2)
print(med)

# even value

_ayesha = [77, 78, 85,86,86,86,87,87,88,94,99,103]

even = np.median(_ayesha)
print(even)

print("Qno. 3: Find the mode of the dataset, hence we use Hamza_1 dataset")

sp = stat.mod(ayesha_1)
print(sp)



print("How to do standard derivation in python?")

ayesha_islam = [99, 86 , 7 , 33 , 11 , 80 , 999 , 833]
st = np.std(ayesha_islam)
print(st)

print("How to find a variance? Use a same list ")

v = np.var(ayesha_islam)
print(v)



