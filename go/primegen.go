package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"sync"
)

func main() {
	var limit uint32 = 100
	var start uint32 = 1
	var maxParallelism uint32 = 4

	if len(os.Args) >= 2 {
		if val, err := strconv.ParseUint(os.Args[1], 10, 32); err == nil {
			limit = uint32(val)
		}
	}
	if len(os.Args) >= 3 {
		if val, err := strconv.ParseUint(os.Args[2], 10, 32); err == nil {
			if val > 0 {
				maxParallelism = uint32(val)
			}
		}
	}

	chunks := createChunks(limit, maxParallelism)
	var wg sync.WaitGroup
	countChannel := make(chan uint32, maxParallelism)
	for i, chunkLimit := range chunks {
		wg.Add(1)
		if i > 0 {
			start = chunks[i-1] + 1
		}
		go func(start uint32, limit uint32) {
			defer wg.Done()
			fmt.Println("CountPrime(", start, "-", limit, ")")
			c := CountPrime(start, limit, false)
			countChannel <- c
		}(start, chunkLimit)
	}
	wg.Wait()
	var count uint32
	for i := uint32(0); i < maxParallelism; i++ {
		count += <-countChannel
	}
	fmt.Printf("Total primes for %d natural numbers is %d.\n", limit, count)
}

func createChunks(num uint32, size uint32) []uint32 {
	result := make([]uint32, size)
	chunk_size := uint32(num / size)
	for i := uint32(0); i < size; i++ {
		lastValue := (i + 1) * chunk_size
		if i+1 == size {
			lastValue += (num % size)
		}
		result[i] = lastValue
	}
	return result
}

func CountPrime(start uint32, limit uint32, show bool) uint32 {
	var count uint32 = 0
	if start < 3 {
		count = 1
		start = 3
	}
	if start%2 == 0 {
		start += 1
	}
	for i := start; i <= limit; i = i + 2 {
		if IsPrime(i) {
			count++
			if show {
				fmt.Println(i)
			}
		}
	}
	return count
}

func IsPrime(num uint32) bool {
	last := uint32(math.Sqrt(float64(num)))
	if num > 2 && num%2 == 0 {
		return false
	}

	for i := uint32(3); i <= last; i = i + 2 {
		if num%i == 0 {
			return false
		}
	}
	return true
}
