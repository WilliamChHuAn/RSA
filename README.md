# RSA

- To implement RSA algorithm in Python.
- Ron ***R***ivest & Adi ***S***hamir & Leonard ***A***dleman

##### tags: `110-2` `Dr. Shin-Ming Cheng`

## How to use

- If you want to know how to use
	- usage: `py RSA.py -h`
- If you want to ***ENCRYPT*** a message using RSA algorithm
	- usage: `py RSA.py -e <plaintext>`
- If you want to ***DECRYPT*** a message using RSA algorithm
	- usage: `py RSA.py -d <ciphertext>`
- This file will regard all of your input (text & key) as **hexadecimal**

## Details

- [Reference](https://www.cs.utexas.edu/~mitra/honors/soln.html)
	1. Generate *N* and *φ(n)*
		- Choose *p* = 3 and *q* = 11
		- Compute *N* = *p* x *q* = 3 x 11 = 33
		- Compute *φ(n)* = (*p* - 1) x (*q* - 1) = 2 x 10 = 20
	2. Generate *e* and *d*
		- Choose *e* such that 1 < *e* < *φ(n)* and *e* and *φ(n)* are coprime.
		- Compute a value for *d* such that (*d* x *e*) % *φ(n)* = 1.
	   	- e.g. 
	   		- Public key is (*e*, *n*) => (7, 33)
	    	- Private key is (*d*, *n*) => (3, 33)
	3. Encrypt / Decrypt
		- The encryption of *pt* =  2 is *ct* = <img src="https://render.githubusercontent.com/render/math?math=2^{7}"> % 33 = *29*
		- The decryption of *ct* = 29 is *pt* = <img src="https://render.githubusercontent.com/render/math?math=29^{3}"> % 33 = *2*

## Example

