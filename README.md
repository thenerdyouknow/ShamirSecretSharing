# ShamirSecretSharing
A Python implementation of Shamir's Secret Sharing Protocol

(March 12th,2019, 1:12 A.M.)
Implements encryption and decryption of Shamir's Secret Sharing protocol using Python class ShamirSecret.

Share Splitting :

To split,first create an object with the plaintext, the threshold value, and the total number of shares.

```
example_object = ShamirSecret(plaintext,threshold,total_number_of_shares)
```

This converts each letter in your string to ASCII values, appends them all together and the converts the resultant to an integer.
This integer is considered the secret that we operate on.(This can get big for huge strings but Python handles big integers fairly well)

Running 

```
shares = example_object.compute_shares()
```
gets you the shares.(These are in the form of tuples in a list)

The secret is split using the procedure mentioned on the Wikipedia page : https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing

Decryption :

Running 
```
recovered_secret = example_object.reconstructing_secret(list_with_threshold_number_of_shares)
```
gets you the original plaintext back.
