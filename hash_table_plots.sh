for M in $(seq 1000 1000 10000); 
do
    # Using `h_ascii` with linear probing/quadratic probing/chained hash appraoch on `rand_words.txt`/`non_rand_words.txt`
    python hash_tables.py -n 10000 -a ascii -s LP -i rand_words.txt -k $M > txt/test_ascii_linear_rand.$M.txt
    python hash_tables.py -n 10000 -a ascii -s LP -i non_rand_words.txt -k $M > txt/test_ascii_linear_non_rand.$M.txt
    python hash_tables.py -n 10000 -a ascii -s QP -i rand_words.txt -k $M > txt/test_ascii_quadratic_rand.$M.txt
    python hash_tables.py -n 10000 -a ascii -s QP -i non_rand_words.txt -k $M > txt/test_ascii_quadratic_non_rand.$M.txt
    python hash_tables.py -n 10000 -a ascii -s CH -i rand_words.txt -k $M > txt/test_ascii_chained_rand.$M.txt
    python hash_tables.py -n 10000 -a ascii -s CH -i non_rand_words.txt -k $M > txt/test_ascii_chained_non_rand.$M.txt

    # Using `h_ascii` with linear probing/quadratic probing chained hash appraoch on `rand_words.txt`/`non_rand_words.txt`
    python hash_tables.py -n 10000 -a rolling -s LP -i rand_words.txt -k $M > txt/test_rolling_linear_rand.$M.txt
    python hash_tables.py -n 10000 -a rolling -s LP -i non_rand_words.txt -k $M > txt/test_rolling_linear_non_rand.$M.txt
    python hash_tables.py -n 10000 -a rolling -s QP -i rand_words.txt -k $M > txt/test_rolling_quadratic_rand.$M.txt
    python hash_tables.py -n 10000 -a rolling -s QP -i non_rand_words.txt -k $M > txt/test_rolling_quadratic_non_rand.$M.txt
    python hash_tables.py -n 10000 -a rolling -s CH -i rand_words.txt -k $M > txt/test_rolling_chained_rand.$M.txt
    python hash_tables.py -n 10000 -a rolling -s CH -i non_rand_words.txt -k $M > txt/test_rolling_chained_non_rand.$M.txt

    # Using `h_myown` with linear probing/quadratic probing chained hash appraoch on `rand_words.txt`/`non_rand_words.txt`
    python hash_tables.py -n 10000 -a myown -s LP -i rand_words.txt -k $M > txt/test_myown_linear_rand.$M.txt
    python hash_tables.py -n 10000 -a myown -s LP -i non_rand_words.txt -k $M > txt/test_myown_linear_non_rand.$M.txt
    python hash_tables.py -n 10000 -a myown -s QP -i rand_words.txt -k $M > txt/test_myown_quadratic_rand.$M.txt
    python hash_tables.py -n 10000 -a myown -s QP -i non_rand_words.txt -k $M > txt/test_myown_quadratic_non_rand.$M.txt
    python hash_tables.py -n 10000 -a myown -s CH -i rand_words.txt -k $M > txt/test_myown_chained_rand.$M.txt
    python hash_tables.py -n 10000 -a myown -s CH -i non_rand_words.txt -k $M > txt/test_myown_chained_non_rand.$M.txt
done

# Using h_ascii
grep insert txt/test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_linear_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_linear_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_ascii_linear_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_linear_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_ascii_linear_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_linear_nonrand_search.png -x "Load Factor" -y "Search Time"

grep insert txt/test_ascii_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_quadratic_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_ascii_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_quadratic_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_ascii_quadratic_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_quadratic_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_ascii_quadratic_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_quadratic_nonrand_search.png -x "Load Factor" -y "Search Time"

grep insert txt/test_ascii_chained_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_chained_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_ascii_chained_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_chained_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_ascii_chained_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_chained_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_ascii_chained_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/ascii_chained_nonrand_search.png -x "Load Factor" -y "Search Time"

# Using h_rolling
grep insert txt/test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_linear_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_linear_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_rolling_linear_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_linear_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_rolling_linear_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_linear_nonrand_search.png -x "Load Factor" -y "Search Time"

grep insert txt/test_rolling_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_quadratic_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_rolling_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_quadratic_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_rolling_quadratic_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_quadratic_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_rolling_quadratic_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_quadratic_nonrand_search.png -x "Load Factor" -y "Search Time"

grep insert txt/test_rolling_chained_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_chained_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_rolling_chained_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_chained_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_rolling_chained_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_chained_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_rolling_chained_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/rolling_chained_nonrand_search.png -x "Load Factor" -y "Search Time"

# Using h_myown
grep insert txt/test_myown_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_linear_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_myown_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_linear_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_myown_linear_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_linear_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_myown_linear_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_linear_nonrand_search.png -x "Load Factor" -y "Search Time"

grep insert txt/test_myown_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_quadratic_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_myown_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_quadratic_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_myown_quadratic_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_quadratic_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_myown_quadratic_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_quadratic_nonrand_search.png -x "Load Factor" -y "Search Time"

grep insert txt/test_myown_chained_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_chained_rand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_myown_chained_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_chained_rand_search.png -x "Load Factor" -y "Search Time"
grep insert txt/test_myown_chained_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_chained_nonrand_add.png -x "Load Factor" -y "Insert Time"
grep search txt/test_myown_chained_non_rand.*.txt | cut -d " " -f2,3 | python scatter.py -o images/myown_chained_nonrand_search.png -x "Load Factor" -y "Search Time"
