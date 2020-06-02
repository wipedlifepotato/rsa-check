# Updates
```
>>> ((ord('x')**e % n)**e % n) **d %n == ord('x')**e %n
! ((m^e mod n)^e mod n)^d = (m^e % n)
  (m^e mod n)^d  mod n = m
! todo: get mechanism to get keys from encrypted message:
'
Crypted
[380606, 255726, 151325, 380606]
Decrypted
['t', 'e', 's', 't']
{'public': (78341, 402617), 'private': (461, 402617)}
{'p': 457, 'q': 881, 'phi': 401280}
'

if we dont know private key, p and q, phi; 

! very small keysPair:
{'e': 7, 'd': 3, 'n': 33, 'phi': 20, 'p': 3, 'q': 11}

!
>>> ((((2**e)**e) % n)**d % n)**d % n
( ((m^e)^e mod N) mod N )^d mod N = m

m^(e*d) mod N = m
>>> (2**(e*d)) % n
2

>>> 2**(e**2 * d**2) % n
2L

>>> 2**(e**4 * d**4) % n
2L

m^(e^z * d^z) mod N = m

!
for not primary: 
>>> 1024/2**2 == 1024 >>2
True
>>> 1024*2**2 == 1024 <<2
True

! 

>>> (m**(e*3) % n)**(d*3) % d == m
True -> IS PRIMARY KEY

>>> (m**(e*4) % n)**(d*4) % d == m
False -> IS NOT PRIMARY KEY!

>>> (m**(e*109) % n)**(d*109) % d == m
True -> IS PRIMARY KEY(109)








```
