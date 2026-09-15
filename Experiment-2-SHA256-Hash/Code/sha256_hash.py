import hashlib


# Function to create SHA-256 hash of a file
def generate_sha256(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    return hashlib.sha256(file_data).hexdigest()


# Create a sample file
with open("sample.txt", "w") as file:
    file.write("This is the original file data.")


# Calculate the initial SHA-256 hash
trusted_hash = generate_sha256("sample.txt")

print("Trusted SHA-256 Hash:", trusted_hash)


# Wait for the user to modify the file
input("\nMake any change in sample.txt, then press Enter to continue...")


# Calculate the hash after the file may have been changed
updated_hash = generate_sha256("sample.txt")

print("Updated SHA-256 Hash: ", updated_hash)


# Compare both hashes
if trusted_hash == updated_hash:
    print("Integrity Check Passed: The file is unchanged.")
else:
    print("Integrity Check Failed: The file has been modified.")
