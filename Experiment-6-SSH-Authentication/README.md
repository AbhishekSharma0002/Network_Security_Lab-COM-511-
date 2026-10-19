### Experiment 6: SSH Remote Access and Authentication

### 1\. Aim

To establish secure remote access to a server using SSH and understand password-based and key-based authentication.

### 2\. Theory

* SSH (Secure Shell): A network protocol that enables secure remote access to another computer through an encrypted connection.

* Remote Login: A method of accessing and controlling a computer from another system over a network.

* SSH Client: A program used to initiate a secure connection with a remote server.

* SSH Server: A service that accepts SSH connection requests and provides remote access.

* Host Key Verification: A security mechanism that helps the client confirm the identity of the remote server and detect possible man-in-the-middle (MITM) attacks.

* Password Authentication: A method in which the user enters a password to verify their identity.

* Public-Key Authentication: A method that uses a public and private key pair to authenticate a user without sending the private key to the server.

### 3\. Procedure

* Install and configure the SSH service on the server.

* Open the terminal on the client machine and initiate an SSH connection to the remote server.

* Enter the server's IP address or hostname to establish the connection.

* Verify the server's host key when prompted by SSH.

* Enter the username and password if password authentication is enabled.

* After successful authentication, access the remote server through the terminal.

* Generate an SSH key pair on the client if public-key authentication is required.

* Copy the public key to the remote server and configure the appropriate permissions.

* Connect to the server again and verify that key-based authentication works.

* Test host-key verification by changing the server's host key in a controlled environment and observing the warning displayed by SSH.

### 4\. Implementation and Commands

The SSH service was configured on the server, and the client was used to connect remotely.

* Install SSH: The OpenSSH package was installed wherever required.

* Start the SSH service: The SSH service was enabled and started on the server.

* Connect to the server: The following command was used to establish a remote connection.

```bash
ssh username@server_ip
```

\- Generate SSH keys: A public and private key pair was created using:

```bash
ssh-keygen -t ed25519
```

\- Copy the public key: The public key was transferred to the server using:

```bash
ssh-copy-id username@server_ip
```

\- Verify the connection: The SSH client was used to confirm successful authentication and remote access.

### 5\. Authentication Methods

A. Password-based authentication

The user enters a password to prove their identity. The server checks the credentials and grants access if they are valid.

B. Public-key authentication

The client uses a private key to prove its identity, while the corresponding public key is stored on the server. This method provides secure authentication without requiring the user to enter a password for every connection.

C. Host-key verification

SSH checks the server's host key against the previously stored key. If the key changes unexpectedly, SSH displays a warning because the server's identity may have changed or a potential MITM attack may be occurring.

### 6\. Testing and Observation

* The SSH client successfully connected to the remote server after valid authentication.

* Password authentication was tested by entering the correct login credentials.

* Public-key authentication was checked after configuring the key pair on the client and server.

* Host-key verification was tested by changing the server's host key in a controlled environment.

* SSH displayed a warning about the changed host key and prevented normal verification from proceeding until the issue was investigated.

### 7\. Discussion

SSH provides secure remote administration by encrypting communication between the client and server. Password authentication verifies the user's credentials, whereas public-key authentication uses cryptographic keys to establish identity.

Host-key verification is important because it confirms that the client is communicating with the intended server. If the stored host key changes, the warning may indicate a legitimate server rebuild or key rotation, but it could also signal a possible man-in-the-middle attack. Therefore, the changed key should be verified independently before reconnecting.

### 8\. Improvements

The experiment can be improved by testing both password-based and public-key authentication and comparing their security and ease of use. SSH host-key verification can also be tested by changing the server's host key in a controlled environment. The client should display a warning when the key does not match the previously stored key. Verifying the new key independently before reconnecting helps prevent potential man-in-the-middle attacks and improves the security of remote access.

### 9\. Conclusion

The experiment demonstrated secure remote access using SSH and explained the working of password-based and public-key authentication. It also verified the importance of server host-key checking in identifying changes to server identity and detecting potential security threats.

Note: Perform the host-key change test only in a controlled lab environment. A changed key should be verified before removing the warning or accepting the new key.
