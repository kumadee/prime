# prime
I created this repo to find the prime numbers for a given range of natural numbers as fast as possible.

The tests were executed on a 4-cores 64-bit AMD A8-6410 APU (potato CPU :D) and DDR3 16GB RAM (memory is insignificant here).

|range|python3.10|pypy3|rust|Go|
|-|-|-|-|-|
|1-1000000|0m5,533s|0m0,953s|0m0,108s|0m0,120s|
|1-10000000|2m14,175s|0m9,843s|0m2,614s|0m2,584s|
|1-100000000|Too-long (maybe hours)|4m15,669s|1m12,671s|1m12,408s|
