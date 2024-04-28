import numpy as np
### Categorical variable with 4 categories to be converted to numeric data
exercises_bases = ["A", "G", "C", "U", "G", "C", "C"]

### Full list of RNA nucleotide bases
full_bases = ["G", "U", "C", "A"]

### map each base to an integer
mapping = {}
for x in range(len(full_bases)):
  mapping[full_bases[x]] = x

one_hot_encode = []

for c in exercises_bases:
  arr = list(np.zeros(len(full_bases), dtype = int))
  arr[mapping[c]] = 1
  one_hot_encode.append(arr)

print(one_hot_encode)
