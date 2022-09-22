#
# LeetCode
#
# Problem - 204
# URL - https://leetcode.com/problems/count-primes/
#

class Solution:
  def countPrimes(self, n: int) -> int:
    if n < 3:
      return 0
    
    eratosthenesSieve = [True] * n
    eratosthenesSieve[0] = False
    eratosthenesSieve[1] = False
    
    for i in range(2, n):
      if eratosthenesSieve[i]:
        eratosthenesSieve[i * i: n: i] = [0] * (1 + (n - i * i - 1) // i)
    
    return sum(eratosthenesSieve)
