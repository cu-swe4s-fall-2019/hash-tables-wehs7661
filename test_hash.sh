#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle hash_functions.py
assert_no_stdout
run test_style pycodestyle hash_tables.py
assert_no_stdout
run test_style pycodestyle test_hash.py
assert_no_stdout
run test_style pycodestyle scatter.py
assert_no_stdout

run test_hash_func1 python hash_functions.py -i rand_words.txt -m ascii
assert_exit_code 0
run test_hash_func2 python hash_functions.py -i non_rand_words.txt -m ascii
assert_exit_code 0
run test_hash_func3 python hash_functions.py -i rand_words.txt -m rolling
assert_exit_code 0
run test_hash_func4 python hash_functions.py -i non_rand_words.txt -m rolling
assert_exit_code 0

run bad_input1 python hash_functions.py -i AAA.txt -m ascii
assert_exit_code 1
assert_stdout
run bad_input2 python hash_functions.py -i rand_words.txt -m AAA
assert_exit_code 1
assert_stdout
run bad_input3 python hash_tables.py -n 1000 -a rolling -s LP -i AAA.txt -k 100
assert_exit_code 1
assert_stdout
run bad_input4 python hash_tables.py -n 1000 -a rolling -s AAA -i rand_words.txt -k 100
assert_exit_code 1
assert_stdout
run bad_input5 python hash_tables.py -n 1000 -a AAA -s LP -i rand_words.txt -k 100
assert_exit_code 1
assert_stdout