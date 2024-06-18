package com.kumadee;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.Collectors;

/**
 * prime
 */
public class Prime {
  public boolean isPrime(long num) {
    long last = (long) Math.floor(Math.sqrt(num)) + 1;
    if (num > 2 && num % 2 == 0) {
      return false;
    }
    for (long i = 3; i <= last; i = i + 2) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }

  public int countPrime(long start, long num, boolean show) {
    int count = 0;
    System.out.println("Start: " + start + ", num: " + num);
    if (start < 3) {
      count = 1;
      start = 3;
    }
    if (start % 2 == 0) {
      start++;
    }
    for (long i = start; i <= num; i = i + 2) {
      if (isPrime(i)) {
        count++;
        if (show) {
          System.out.println(i);
        }
      }
    }
    return count;
  }

  private List<Long[]> createChunks(long num, int numOfChunks) {
    List<Long[]> result = new ArrayList<>();
    long chunkSize = (long) Math.floor(num / numOfChunks);
    for (long i = 0; i < numOfChunks; i++) {
      var start = 0L;
      if (i > 0) {
        start = i * chunkSize;
      }
      var end = (i + 1) * chunkSize;
      if (i + 1 == numOfChunks) {
        end += num % numOfChunks;
      }
      result.add(new Long[] { start, end });
    }
    return result;
  }

  public static void main(String[] args) {
    int maxWorkers = 4;
    Long limit = 1_000L;
    if (args.length > 0) {
      limit = Long.parseLong(args[0]);
    }
    if (args.length > 1) {
      maxWorkers = Integer.parseInt(args[1]);
    }
    Prime p = new Prime();
    var chunks = p.createChunks(limit, maxWorkers);
    var executor = Executors.newVirtualThreadPerTaskExecutor();
    List<Callable<Integer>> tasks = chunks.stream()
        .map(chunk -> (Callable<Integer>) () -> p.countPrime(chunk[0], chunk[1], false))
        .collect(Collectors.toList());
    List<Future<Integer>> results = tasks.stream()
        .map(task -> executor.submit(task))
        .collect(Collectors.toList());

    Integer sum = results.stream()
        .mapToInt(future -> {
          try {
            return future.get();
          } catch (Exception e) {
            e.printStackTrace();
            return 0;
          }
        })
        .sum();
    System.out.println("Total primes for " + limit + " natural numbers is " + sum);
    Map<Long, Integer> primeCounts = new HashMap<Long, Integer>() {
      {
        put(10L, 4);
        put(100L, 25);
        put(1_000L, 168);
        put(10_000L, 1229);
        put(100_000L, 9592);
        put(1_000_000L, 78498);
        put(10_000_000L, 664579);
        put(100_000_000L, 5761455);
      }
    };
    System.out.println("Is number of prime correct? => " + sum.equals(primeCounts.get(limit)));
  }
}
