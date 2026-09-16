import hashlib
import secrets
import hmac

# Shared secret key
secret_key = "mysecret"

# Store previously used challenges
used_challenges = set()

# Generate a new challenge
challenge = secrets.token_hex(8)

print("Server Challenge:", challenge)

# Client generates response
response = hashlib.sha256(
    (challenge + secret_key).encode()
).hexdigest()

print("Client Response:", response)

# Server verifies the response
expected_response = hashlib.sha256(
    (challenge + secret_key).encode()
).hexdigest()

if hmac.compare_digest(response, expected_response):
    print("Authentication Successful")
    
    # Mark challenge as used
    used_challenges.add(challenge)
else:
    print("Authentication Failed")

# Replay attack simulation
print("\nReplay Attack Simulation")

# Try to use the same challenge again
if challenge in used_challenges:
    print("Replay Attack Detected")
else:
    print("No Replay Attack Detected")
