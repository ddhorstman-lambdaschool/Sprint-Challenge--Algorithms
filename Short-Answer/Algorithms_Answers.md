#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) If n is 10, we go to 1000 by 100s, so runtime is 10 cycles
   If n is 2, we go to 8 by 4s, so runtime is 2 cycles
   Therefore **O(n)**

b) Outer loop has a runtime of *O(n)*. Inner loop has a runtime of *O(n/2)*.
   Dropping constants, **O(n^2)**


c) `bunnyEars` is called exactly `n` times. So **O(n)**

## Exercise II
This problem is essentially a fancier binary search.
Just like binary search

  function check_breakage(starting floor, ending floor):
    starting floor is `0` if not specified
    ending floor is `n` if not specified

    if `start` and `end` are the same floor:
      if the egg breaks `check_breakage` for the floor below
      if the egg doesn't break we've found the highest floor
    otherwise:
      test the floor midway between `start` and `end`
      if the egg breaks:
        `check_breakage` for the range `start` -> midpoint
      if the egg doesn't break:
        `check_breakage` for the range midpoint -> `end`
