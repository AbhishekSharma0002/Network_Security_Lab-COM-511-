Experiment – 2

Aim:

To apply hashing techniques for generating a secure SHA-256 hash and use it to verify data integrity and identify tampering.

Brief Theory:

SHA-256: SHA-256 (Secure Hash Algorithm 256) is a cryptographic hashing method that converts input data into a fixed 256-bit (64 hexadecimal characters) hash value.

Hashing: Hashing is a one-way process that transforms data into a fixed-length digital fingerprint. The same input always produces the same hash, while even a small change in the input generates a different hash.

Data Integrity: Data integrity means ensuring that data has not been altered or modified. It can be checked by comparing the current hash of the data with a trusted reference hash.


Methodology:

1. Create a text file “sample.txt” containing some original text, such as “Network security is important.”


2. Read the file in binary mode and generate its SHA-256 hash using Python’s hashlib module.


3. Save the original hash as the trusted reference hash and verify that the original file produces a “match.”


4. Modify a character in the file by changing “important” to “Important.”


5. Generate the SHA-256 hash of the modified file and compare it with the original trusted hash.


6. Display “Match” or “Mismatch” to determine whether the file has been changed.


7. Compare the original and modified hashes character by character and count the number of different hash characters.



Results:

The original file generated a 64-character SHA-256 hash and returned “Match” before modification. After changing one character, the verification returned “Mismatch”, with 59 out of 64 (92.19%) hexadecimal hash characters being different.

Detailed Outputs:

The outputs and screenshots can be reviewed by scanning the QR code below.

Discussion:

The original file produced a “match,” whereas changing only one character resulted in a “mismatch.” The comparison showed that 59 of the 64 hash characters were different, demonstrating the change-sensitive property of SHA-256. Therefore, the hash can be used to identify data modifications when the reference hash is trusted.

Improvements:

The code was modified by changing the function and variable names, updating the comments, improving the output messages, and making the instructions clearer. The code structure was also made easier to read and understand while keeping the SHA-256 hashing and file integrity verification process unchanged.


Conclusion:

SHA-256 hashing was successfully used to verify data integrity and detect changes in the file. The results showed that even a small modification produced a different hash, proving its effectiveness in detecting tampering.
