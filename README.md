# prime

I created this repo to find the prime numbers for a given range of natural numbers as fast as possible.

The tests were executed on a 4-cores 64-bit AMD A8-6410 APU (potato CPU :D) and DDR3 16GB RAM (memory is insignificant here).

|range|python3.12|pypy3|rust|Go|JDK21|
|-|-|-|-|-|
|1-1000000|0m3,932s|0m2,334s|0m0,108s|0m0,120s|0m0,444s|
|1-10000000|0m56,782s|0m5,939s|0m2,614s|0m2,584s|0m3,384s|
|1-100000000|26m54,584s|1m45,155s|1m12,671s|1m12,408s|1m23,678s|
