# Experiment – 3

### Aim:

To develop a basic challenge-response authentication system for verifying user identity and detecting replay attacks.

### Theory:

**Challenge-Response Authentication:**
It is an authentication method where the system sends a unique challenge and the user generates a valid response using a shared secret.

**Nonce:**
A randomly generated value that is used only once during authentication to make every challenge different and prevent replay attacks.

**HMAC:**
Hash-based Message Authentication Code (HMAC) is a security mechanism that uses a secret key with a hash function to verify the integrity and authenticity of a message.

**Replay Attack:**
A type of attack where an attacker captures a valid authentication response and sends it again to obtain unauthorized access.

### Methodology:

**1. Initialize the shared secret:**
A common secret key is created and shared between the user and the authentication system.

**2. Generate a challenge:**
During authentication, a random 16-byte hexadecimal number is generated using the secret module. The username and challenge timestamp are stored.

**3. Create the authentication response:**
The username, nonce, and timestamp are combined into a message. An HMAC-SHA256 value is generated using the shared secret.

**4. Send the response:**
The response contains the username, nonce, timestamp, and HMAC tag.

**5. Verify the response:**
The system first checks whether the nonce has already been used. It then verifies that the nonce belongs to the correct username and checks whether the timestamp is within the allowed 5-second limit. A new HMAC is calculated and compared with the received HMAC.

**6. Detect replay attacks:**
After a nonce is used, it is added to the used-nonce list. If the same nonce is submitted again, the system identifies it as a replay attack.

**7. Handle delayed responses:**
If the response is older than 5 seconds, it is rejected as an expired response.

### Improvement:

A tampering test was added by modifying the received authentication tag. The system compares the modified tag with the expected HMAC and rejects the altered response.

### Result:

* The valid authentication response was accepted successfully.
* Reusing the same nonce was identified as a replay attack and rejected.
* A response with an old timestamp was rejected as an expired response.
* Changing the HMAC tag caused the authentication process to fail.
* The authenticity and integrity of the response can be verified using the QR code below.

### Discussion:

The valid response was accepted, while the reused nonce, expired response, and modified HMAC were rejected. These results show that nonce tracking, timestamp verification, and HMAC validation can effectively detect replay and response-tampering attempts.

### Improvement:

An HMAC-tampering test was included to modify the received authentication tag and verify that the altered response is rejected. This demonstrates the integrity and authenticity protection provided by HMAC.

### Conclusion:

The challenge-response authentication mechanism successfully verified legitimate users while detecting replay, expired, and tampered responses using nonce, timestamp, and HMAC-based verification.
