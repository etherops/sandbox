### compare_substring_replace_strategy_perf.py

Strings are immutable in python.  This script looks at 4 different ways to achieve substring replace in python, namely string concatenation, conversation to and back from list, and normal iteration, and generator iteration.

Results:
```
$ ./compare_substring_replace_strategy_perf.py 10000
Testing for string length of 10000
Solving with concatenation
Elapsed time: 2.121925354e-05
Solving with array conversion
Elapsed time: 0.000351905822754
Solving with normal iteration
Elapsed time: 0.00219011306763
Solving with generator iteration
Elapsed time: 0.00143480300903
```

Interesting, string concatenation is the clear winner here!
