# Revert
Revert calculates combinations from a CSV file (with format value;number) and finds combinations whose sum matches a target value.
It reads data from the CSV file, performs the calculations, and outputs the results to a text file.

## Usage

```shell
root@pocketvince:~/revert# python3 revert.py data.csv 691

Research 691 on data.csv

--- Calculation Completed ---
Running time: 0.55 seconds
Number of tries: 524287
Number of occurrences found: 2

--- Contents of results.txt ---
Result: VL2B7 (521), IKR24 (170)
Result: 46DBD (296), VCCPK (359), 8SPUF (36)
```

## Contributing

Readme generator: https://www.makeareadme.com/
