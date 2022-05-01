# RSA

- To implement RSA algorithm in Python.
- Ron ***R***ivest & Adi ***S***hamir & Leonard ***A***dleman

##### tags: `110-2` `Dr. Shin-Ming Cheng`

## How to use

- If you want to ***ENCRYPT*** a message using RSA algorithm
	- usage: `py "RSA Encryption.py"`
- If you want to ***DECRYPT*** a message using RSA algorithm
	- usage: `py "RSA Decryption.py"`
- The `RSA Encryption` file will split each character of your plaintext input into bytes through **UTF-8** and **hexadecimal**, then convert to decimal integer
	- Input `"A"` -> `b'A'` -> `0100 0001` -> `65`
	- Input `"AA"` -> `b'AA` -> `0100 0001 0100 0001` -> `16705`

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
		- The encryption of *pt* =  2 is *ct* = <img src="https://render.githubusercontent.com/render/math?math=\color{red}\2^7 \mod 33 = 29">
		- The decryption of *ct* = 29 is *pt* = <img src="https://render.githubusercontent.com/render/math?math=\color{red}\29^3 \mod 33 = 2">

## Example

- *plaintext* = `rsa is good`
- *p* = ```11556895667671057477200219387242513875610589005594481832449286005570409920461121505578566298354611080750154513073654150580136639937876904687126793459819369```
- *q* = ```9789731420840260962289569924638041579833494812169162102854947552459243338614590024836083625245719375467053459789947717068410632082598060778090631475194567```
- *e* = ```19```
- *d* = ```77410829494065078552190250304099125050736735018316234514988441348831176023853312803867671315395348748359328828068606957825082257747811116954200942254866186060027505952608564766237075015065410402961361228729204635363549685334314716847974380602722686199587148098391213644866271307043132151602040909065431421355```

### Encryption

- `py "RSA Encryption.py"`
```

RSA Encryption
---------------
Please enter your plaintext: rsa is good
---------------
Convert input:
    1. Original input: rsa is good
    2. Split into bytes: b'rsa is good'
    3. Convert into decimal: 138362407251297349722402660
---------------
Please enter your prime p: 11556895667671057477200219387242513875610589005594481832449286005570409920461121505578566298354611080750154513073654150580136639937876904687126793459819369
Please enter your prime q: 9789731420840260962289569924638041579833494812169162102854947552459243338614590024836083625245719375467053459789947717068410632082598060778090631475194567
Your N is: 113138904645172037883970365829067951997230612719077573521906183509830180342554841790268134999423971247602095979484887092205889453631416247856139838680189062511282674134361726455828113825651055263796576482555849771303361415911103661873954509376979834006775895197929252775133737380642752081153063469135950168223
---------------
Please enter your public key e: 19
---------------
Ciphertext: 54882345225167460084171140955967992282667377204091588609033122708127178701031330892145313384333633434351416426054905444501627535687406486333900653735405050718476919959313978328014547396916374860709789694961602071336719500773643463363664159608737935223634541379347683781861750996253589715773012484147642400699
```

### Decryption

- `py "RSA Decryption.py"`
```

RSA Decryption
---------------
Please enter your ciphertext: 54882345225167460084171140955967992282667377204091588609033122708127178701031330892145313384333633434351416426054905444501627535687406486333900653735405050718476919959313978328014547396916374860709789694961602071336719500773643463363664159608737935223634541379347683781861750996253589715773012484147642400699
---------------
Please enter your private key d: 77410829494065078552190250304099125050736735018316234514988441348831176023853312803867671315395348748359328828068606957825082257747811116954200942254866186060027505952608564766237075015065410402961361228729204635363549685334314716847974380602722686199587148098391213644866271307043132151602040909065431421355
---------------
Please enter your N: 113138904645172037883970365829067951997230612719077573521906183509830180342554841790268134999423971247602095979484887092205889453631416247856139838680189062511282674134361726455828113825651055263796576482555849771303361415911103661873954509376979834006775895197929252775133737380642752081153063469135950168223
---------------
Plaintext: b'rsa is good'
```
