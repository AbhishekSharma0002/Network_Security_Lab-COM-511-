# Experiment 5: Analysis of TLS Handshake Using Wireshark

## 1. Aim

To examine and understand the TLS handshake procedure during HTTPS communication using Wireshark.

## 2. Theory

**TLS (Transport Layer Security):** TLS is a security protocol that provides confidentiality, data integrity, and authentication during network communication.

**HTTPS (Hypertext Transfer Protocol Secure):** HTTPS uses TLS to protect data exchanged between a web browser and a web server.

**TLS Handshake:** The TLS handshake is the initial process in which the client and server negotiate security settings, establish cryptographic keys, and authenticate the server before exchanging protected data.

**TLS Key Logging:** TLS key logging saves session secrets in a key log file, allowing supported TLS traffic to be decrypted and analyzed in Wireshark.

## 3. Methodology

### Step 1: Capture HTTPS Traffic

Wireshark was opened, and the active network interface was selected. HTTPS traffic was captured using the display filter `tcp.port == 443` while visiting `https://www.wireshark.org/`. The captured packets were saved in `.pcapng` format for further analysis.

### Step 2: Examine the Client Hello Message

The display filter `tls.handshake.type == 1` was applied to locate Client Hello packets. The offered TLS versions, cipher suites, server name, and key-share details were examined to understand the security options proposed by the client.

### Step 3: Examine the Server Hello Message

The filter `tls.handshake.type == 2` was used to identify Server Hello packets. The negotiated TLS version, selected cipher suite, and key-share information were inspected to understand the security parameters selected by the client and server.

### Step 4: Configure TLS Key Logging

The browser was configured to save TLS session secrets in a key log file. Wireshark was then configured to use this file to decrypt the corresponding captured TLS traffic.

### Step 5: Inspect the Decrypted TLS Handshake

A new HTTPS session was captured and analyzed. Messages such as Encrypted Extensions, Certificate, Certificate Verify, and Finished were examined when available.

### Step 6: Inspect the Server Certificate

The certificate information was examined to understand server identity and authentication. Details such as the issuer, subject, Subject Alternative Name (SAN), public key, validity period, and signature algorithm were reviewed.

### Step 7: Analyze the Handshake and Encrypted Communication

The captured traffic was analyzed to understand how the client and server negotiate security settings and establish an encrypted connection. Decrypted packets were used to inspect handshake messages and certificate-related information.

## 4. Flowchart

```text
Start
  |
  v
Capture HTTPS Traffic Using Wireshark
  |
  v
Identify Client Hello and Server Hello
  |
  v
Configure TLS Key Logging
  |
  v
Inspect Decrypted Handshake Messages
  |
  v
Examine the Server Certificate
  |
  v
Record Observations
  |
  v
End
```

## 5. Results

- The Client Hello message displayed the TLS versions and cipher suites offered by the client, along with key-share information.
- The Server Hello message showed the negotiated TLS version and the selected cipher suite, `TLS_AES_128_GCM_SHA256`, if observed in the capture.
- The handshake analysis helped identify encrypted extensions, certificate information, and authentication-related messages where visible.
- Certificate inspection provided details about the server identity, SAN, validity period, and public key.
- The captured traffic demonstrated the TLS negotiation process used to establish a secure HTTPS connection.
- TLS key logging demonstrated how supported traffic can be decrypted in Wireshark for authorized analysis.

## 6. Discussion

The Client Hello and Server Hello messages demonstrated how the client and server negotiate TLS security parameters. The selected TLS version, cipher suite, and key-share information helped explain how a secure connection is established.

TLS key logging enabled inspection of handshake messages that would otherwise remain encrypted. Examining the server certificate provided information about server authentication, certificate validity, and public-key details. These observations helped explain how TLS protects HTTPS communication through encryption and authentication.

## 7. Improvements

- Automate the analysis of TLS handshake messages and certificate details.
- Test different TLS versions and cipher suites to compare their behavior.
- Include certificate validation checks to identify expired or incorrectly configured certificates.
- Store TLS key log files securely and remove them after authorized analysis.

## 8. Conclusion

The experiment demonstrated how Wireshark can be used to capture and analyze TLS handshakes during HTTPS communication. The Client Hello and Server Hello messages illustrated the negotiation of security parameters, while TLS key logging enabled inspection of decrypted handshake messages when configured correctly. Certificate analysis provided an understanding of server authentication and certificate properties. Overall, the experiment improved understanding of TLS negotiation, encryption, and authentication in secure web communication.
