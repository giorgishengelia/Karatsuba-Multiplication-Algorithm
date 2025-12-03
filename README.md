# Karatsuba-Multiplication-Algorithm
A high-performance divide-and-conquer algorithm for multiplying large integers.

The Karatsuba algorithm multiplies two numbers faster than classical grade-school multiplication.
Instead of the usual O(n²) time, Karatsuba runs in: 
## O(n<sup>log<sub>2</sub> 8</sup>) ≈ O(n<sup>1.585</sup>)


It achieves this by splitting numbers into halves and reducing the number of required multiplications from 3 → 2.

### Python Algorithm:
![Alt text](assets/Karatsuba.png)

### Output:
![Alt text](assets/Output.png)
