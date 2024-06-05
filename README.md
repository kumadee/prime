# prime
I created this repo to find the prime numbers for a given range of natural numbers as fast as possible.

The tests were executed on a 4-cores 64-bit AMD A8-6410 APU (potato CPU :D) and DDR3 16GB RAM (memory is insignificant here).

|range|python3.12|pypy3|rust|Go|
|-|-|-|-|-|
|1-1000000|0m0,721s|0m0,246s|0m0,108s|0m0,120s|
|1-10000000|0m19,303s|0m3,712s|0m2,614s|0m2,584s|
|1-100000000|12m31,370s|2m2,538s|1m12,671s|1m12,408s|

