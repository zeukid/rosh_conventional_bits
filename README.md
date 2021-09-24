# RSA ENCRYPTION
RSA algorithm is asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private key is kept private.

The idea! The idea of RSA is based on the fact that it is difficult to factorize a large integer. The public key consists of two numbers where one number is multiplication of two large prime numbers. And private key is also derived from the same two prime numbers. So if somebody can factorize the large number, the private key is compromised

# Shor's Algorithm
Shor’s algorithm is famous for factoring integers in polynomial time. Since the best-known classical algorithm requires superpolynomial time to factor the product of two primes, the widely used cryptosystem, RSA, relies on factoring being impossible for large enough integers.

Here is a simple implementation of Shor's Algorithm using Conventional bits. This could help in the understanding of the algorithm. I will post the Implementation for Quantum bits later. 

Links:

RSA Encryption: https://www.geeksforgeeks.org/rsa-algorithm-cryptography/

IBM Quantum Computing: https://quantum-computing.ibm.com/

Shor's Algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm
