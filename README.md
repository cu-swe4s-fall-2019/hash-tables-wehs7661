[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/hash-tables-wehs7661.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/hash-tables-wehs7661)
# Hash tables
## Description
This is a repository for Assignment 6 of the course Software Engineering for Scientists (CSCI 7000) at CU Boulder, which includes the following files:
- `hash_functions.py`: A Python module of hash algorithms.
- `hash_tables.py`: A Python module of methods used in generating a hash table. 
- `test_hash.py`: A Python script containing the unit test functions for the methods used in `hash_functions.py` and `test_tables.py`.
- `rand_words.txt`: A text file of random words.
- `non_rand_words.txt`: A text file of non-random words.
- `scatter.py`: A Python script for generating a scatter plot from `STDIN`.
- `hash_table_plots.sh`: A shell script for generating scatter plots of hash tables with different input parameters. 
## Installation
All the Python scripts are written in Python 3 and the packages required to run the codes include: `argparse`, `sys`, `matplotlib`, `time`, `os`, `random` and `unittest`.
## Usage
### 1. Scatter plots of hash functions
`hash_functions.py` includes three different hash algorithm, including `h_ascii`, `h_rolling` and `h_myown`, which implements the ASCII hash method, the polynomial rolling hash method, and my own hash method, respectively. Here, we have two different input files, including `rand_words.txt` and `non_rand_words.txt`. For the detailed usage of the methods, please refer to the docstring of the methods.
#### (1) Using `h_ascii` on `rand_words.txt` (Figure 1.)
```
python hash_functions.py -i rand_words.txt -m ascii | python scatter.py -o images/ascii_func_rand.png -x "Hashed word" -y "Hashed value"
```
![](images/ascii_func_rand.png)
#### (2) Using `h_ascii` on `non_rand_words.txt` (Figure 2.)
```
python hash_functions.py -i non_rand_words.txt -m ascii | python scatter.py -o images/ascii_func_non_rand.png -x "Hashed word" -y "Hashed value"
```
![](images/ascii_func_non_rand.png)
#### (3) Using `h_rolling` on `rand_words.txt` (Figure 3.)
```
python hash_functions.py -i rand_words.txt -m rolling | python scatter.py -o images/rolling_func_rand.png -x "Hashed word" -y "Hashed value"
```
![](images/rolling_func_rand.png)
#### (4) Using `h_rolling` on `non_rand_words.txt` (Figure 4.)
```
python hash_functions.py -i non_rand_words.txt -m rolling | python scatter.py -o images/rolling_func_non_rand.png -x "Hashed word" -y "Hashed value"
```
![](images/rolling_func_non_rand.png)
#### (5) Using `h_myown` on `rand_words.txt` (Figure 5.)
```
python hash_functions.py -i rand_words.txt -m myown | python scatter.py -o images/myown_func_rand.png -x "Hashed word" -y "Hashed value"
```
![](images/myown_func_rand.png)
#### (6) Using `h_myown` on `non_rand_words.txt` (Figure 6.)
```
python hash_functions.py -i non_rand_words.txt -m myown | python scatter.py -o images/myown_func_non_rand.png -x "Hashed word" -y "Hashed value"
```
![](images/myown_func_non_rand.png)
### 2. Insert time and search time as functions of load factor
`hash_tables.py` includes two different collision resolution strategies, including `LP` (linear probing) and `CH` (chained hash). Here, we have two different input files, including `rand_words.txt` and `non_rand_words.txt`. For the detailed usage of the methods, please refer to the docstring of the methods. To generate the following plots at once, run `bash hash_table_plots.sh`. (Note: the units of insert time and search time are both second.)
#### (1) Using `h_ascii` with linear probing appraoch on `rand_words.txt` (Figure 7. and 8.)
![](images/ascii_linear_rand_add.png)
![](images/ascii_linear_rand_search.png)
#### (2) Using `h_ascii` with linear probing appraoch on `non_rand_words.txt` (Figure 9. and 10.)
![](images/ascii_linear_nonrand_add.png)
![](images/ascii_linear_nonrand_search.png)
#### (3) Using `h_ascii` with quadratic probing appraoch on `rand_words.txt` (Figure 11. and 12.)
![](images/ascii_quadratic_rand_add.png)
![](images/ascii_quadratic_rand_search.png)
#### (4) Using `h_ascii` with quadratic probing appraoch on `non_rand_words.txt` (Figure 13. and 14.)
![](images/ascii_quadratic_nonrand_add.png)
![](images/ascii_quadratic_nonrand_search.png)
#### (5) Using `h_ascii` with chained hash appraoch on `rand_words.txt` (Figure 15. and 16.)
![](images/ascii_chained_rand_add.png)
![](images/ascii_chained_rand_search.png)
#### (6) Using `h_ascii` with chained hash appraoch on `non_rand_words.txt` (Figure 17. and 18.)
![](images/ascii_chained_nonrand_add.png)
![](images/ascii_chained_nonrand_search.png)
#### (7) Using `h_rolling` with linear probing approach on `rand_words.txt` (Figure 19. and 20.)
![](images/rolling_linear_rand_add.png)
![](images/rolling_linear_rand_search.png)
#### (8) Using `h_rolling` with linear probing approach on `non_rand_words.txt` (Figure 21. and 22.)
![](images/rolling_linear_nonrand_add.png)
![](images/rolling_linear_nonrand_search.png)
#### (9) Using `h_rolling` with quadratic probing approach on `rand_words.txt` (Figure 23. and 24.)
![](images/rolling_quadratic_rand_add.png)
![](images/rolling_quadratic_rand_search.png)
#### (10) Using `h_rolling` with quadratic probing approach on `non_rand_words.txt` (Figure 25. and 26.)
![](images/rolling_quadratic_nonrand_add.png)
![](images/rolling_quadratic_nonrand_search.png)
#### (11) Using `h_rolling` with chained hash approach on `rand_words.txt` (Figure 27. and 28.)
![](images/rolling_chained_rand_add.png)
![](images/rolling_chained_rand_search.png)
#### (12) Using `h_rolling` with chained hash approach on `rand_words.txt` (Figure 29. and 30.)
![](images/rolling_chained_nonrand_add.png)
![](images/rolling_chained_nonrand_search.png)
#### (13) Using `h_myown` with linear probing approach on `rand_words.txt` (Figure 31. and 32.)
![](images/myown_linear_rand_add.png)
![](images/myown_linear_rand_search.png)
#### (14) Using `h_myown` with linear probing approach on `non_rand_words.txt` (Figure 33. and 34.)
![](images/myown_linear_nonrand_add.png)
![](images/myown_linear_nonrand_search.png)
#### (15) Using `h_myown` with quadratic probing approach on `rand_words.txt` (Figure 35. and 36.)
![](images/myown_quadratic_rand_add.png)
![](images/myown_quadratic_rand_search.png)
#### (16) Using `h_myown` with quadratic probing approach on `non_rand_words.txt` (Figure 37. and 38.)
![](images/myown_quadratic_nonrand_add.png)
![](images/myown_quadratic_nonrand_search.png)
#### (17) Using `h_myown` with chained hash approach on `rand_words.txt` (Figure 39. and 40.)
![](images/myown_chained_rand_add.png)
![](images/myown_chained_rand_search.png)
#### (18) Using `h_myown` with chained hash approach on `rand_words.txt` (Figure 41. and 42.)
![](images/myown_chained_nonrand_add.png)
![](images/myown_chained_nonrand_search.png)

### Discussion
From the figures above, we can observe that
- `rand_words.txt` genernally generate a distribution that is more random than the one generated by `non_rand_words.txt`. This is especially apparently when using `h_ascii` with linear probing, since `h_ascii` is not a very good hash algorithm in terms of generating a random distribution.
- Comparing Figure 1. and 2. with Figure 3. and 4., we can easily tell that algorithm rolling hash method is better than the ascii hash method in terms of generating a random distribution, no matter the input file is `rand_words.txt` or `non_rand_words.txt`.
- From Figure 5., we can see that `h_myown` performed as goog as `h_rolling` at least visually, which is of course better than ascii hash method in terms of gerenerating a random distribution. On the other hand, from Figure 6., we can see that although `h_myown` is not as good as `h_rolling`, but is still better `h_ascii`.

- From Figure 7. to Figure 18., we can see that with `h_ascii`, for the lienar probing approach, the insert time and the search time are approximately proportional to the load factor, while the for the quadratic probing and chained hash approach, the linearity between the insert/search time and the load factor seems much lower. 

- From Figure 19. to 30., we can see that with `h_rolling`, all the collision resolution strategies lead to higher independence between the insert/search time. There is not a big difference in this relationship between different collision resolution strategies. 

- At last, from Figure 31. to Figure 42., we can observe that the performace of `h_myown` is pretty similar to that of `h_ascii`. That is, for the linear  probing approach, the insert time and the search time are approximately proportional to the load factor, while the for the quadratic probing and chained hash approach, the linearity between the insert/search time and the load factor seems much lower. 

## Changes made upon the starter code of Assignment 6
### Basic requirements
- Developed codes for hash algorithms and collision resolution strategies in `hash_functions.py` and `hash_tables.py`.
- Developed `scatter.py` to generate a scatter plot from `STDIN`.
- Added `rand_words.txt` and `non_rand_words.txt`.
- Developed unit tests for all the methods in `hash_functions.py` and `hash_tables.py`, including `test_hash_ascii`, `test_hahs_rolling`, `test_linear_probing` and `test_chained_hash`.
- Developed functional tests for `hash_functions.py`, `hash_tables.py` and `scatter.py`.
- Improved the codes to make them conform to PEP8 coding style.
- Performed a bunch of experiments on hash tables and hash functions as shown above. 
- Modified `.travis.yml` to pass TravisCI.
### Extra credits
- Added another hash method `h_myown` and another collision resolution strategy class `QuadraticProbe` in `hash_functions.py` and `hash_tables.py`.
- Added unit tests for newly added methods and updated README to account for the changes.
- Performed additional experiments to examine the efficacy of newly added methods (already added above).
