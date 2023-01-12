#/**
 #* *Copyright (C), 2023-2024, Sara Echeverria (bl33h)
    # *@author Sara Echeverria, Fabian Juarez, Andres Montoya, Ricardo Mendez, Adrian Rodriguez
    # *FileName: byLetter
    # @version: I
    #- Creation: 11/01/2023
    #- Last modification: 12/01/2023

# Data
words = [ "Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra", "NoSQL", "MongoDB", "Postgres", "Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas", "R", "statistics", "regression", "probability", "machine learning", "decision trees", "libsvm", "C++", "Haskell", "programming languages", "mathematics", "theory", "machine learning", "Mahout", "neural networks", "deep learning", "Big Data", "artificial intelligence", "MapReduce"]

# Empty dict
byLetter = {}

# Default addition cycle
for word in words:
    letter = word[0]
    byLetter.setdefault(letter,[]).append(word)

# By letter addition cycle
from collections import defaultdict
byLetter = defaultdict(list)
for word in words:
    byLetter[word[0]].append(word)

# Final print
print (byLetter)