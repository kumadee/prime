# prime

I created this repo to find the prime numbers for a given range of natural numbers as fast as possible.

The tests were executed on a 4-cores 64-bit AMD A8-6410 APU (potato CPU :D) and DDR3 16GB RAM (memory is insignificant here).
> The thread count is 4 for all cases.

|range|python3.12|pypy3|rust|Go|JDK21|
|-|-|-|-|-|-|
|1-1000000|0m3,932s|0m2,334s|0m0,108s|0m0,120s|0m0,444s|
|1-10000000|0m56,782s|0m5,939s|0m2,614s|0m2,584s|0m3,384s|
|1-100000000|26m54,584s|1m45,155s|1m12,671s|1m12,408s|1m23,678s|

Upon increasing the green threads or virtual threads following results were observed.

## 10 million numbers

|threads|Go|JDK21|
|-|-|-|
|10|0m2,341s|0m2,977s|
|20|0m2,363s|0m2,880s|
|50|0m2,342s|0m2,996s|
|100|0m2,397s|0m3,102s|

## 100 million numbers

|threads|Go|JDK21|
|-|-|-|
|10|1m5,148s|1m21,588s|
|20|1m3,827s|1m14,762s|
|50|1m3,412s|1m8,593s|
|100|1m3,442s|1m5,847s|
