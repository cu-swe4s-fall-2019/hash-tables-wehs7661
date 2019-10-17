# Hash tables

## Description
This is a repository for Assignment 6 of the course Software Engineering for Scientists (CSCI 7000) at CU Boulder, which includes the following files:
- `hash_functions.py`: A Python module of hash algorithms.
- `hash_tables.py`: A Python module of methods used in generating a hash table. 
- `test_hash.py`: A Python script containing the unit test functions for the methods used in `hash_functions.py` and `test_tables.py`.
- `rand_words.txt`: A text file of random words.
- `non_rand_words.txt`: A text file of non-random words.
- `scatter.py`: A Python script for generating a scatter plot from `STDIN`.

## Installation
All the Python scripts are written in Python 3 and the packages required to run the codes include: `argparse`, `sys`, `matplotlib`, `time`, `os`, `random` and `unittest`.

## Usage
### 1. Scatter plots of hash functions
`hash_functions.py` includes two different hash algorithm, including `h_ascii` and `h_rolling`, which implements the ASCII hash method and the polynomial rolling hash method, respectively. Here, we have two different input files, including `rand_words.txt` and `non_rand_words.txt`.
#### (1) Using `h_ascii` on `rand_words.txt`
```
python hash_functions.py 
```



#### (2) Using `h_ascii` on `non_rand_words.txt`
#### (3) Using `h_rolling` on `rand_words.txt`
#### (4) Using `h_rolling` on `non_rand_words.txt`





![](images/ascii_hash_function_non_rand.png)



## Changes made upon the starter code of Assignment 6
- Developed codes for hash algorithm and collision resolution strategies in `hash_functions.py` and `hash_tables.py`.
- Developed `scatter.py` to generate a scatter plot from `STDIN`.
- Added `rand_words.txt` and `non_rand_words.txt`.
- Developed unit tests for all the methods in `hash_functions.py` and `hash_tables.py`, including `test_hash_ascii`, `test_hahs_rolling`, `test_linear_probing` and `test_chained_hash`.
- Developed functional tests for `hash_functions.py`, `hash_tables.py` and `scatter.py`.
- Modified `.travis.yml` to pass TravisCI.

