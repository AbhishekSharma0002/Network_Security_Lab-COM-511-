#!/bin/bash

# Experiment 4: Practical TLS Client–Server Communication
# This file contains the commands used to test a local TLS
# server and client using the generated self-signed X.509 certificate.


# --------------------------------------------------
# 1. Start the local TLS server
# --------------------------------------------------
# Starts a TLS server on port 4433 using the generated
# X.509 certificate and its corresponding private key.
# The server provides a simple web response for testing.
openssl s_server -accept 4433 \
-cert certificate.crt \
-key private.key \
-www


# --------------------------------------------------
# 2. Connect to the TLS server using a client
# --------------------------------------------------
# Establishes a TLS connection to the local server.
# The -CAfile option explicitly trusts the self-signed
# certificate for this local testing environment.
openssl s_client -connect 127.0.0.1:4433 \
-CAfile certificate.crt


# --------------------------------------------------
# 3. Test TLS connection and certificate verification
# --------------------------------------------------
# Connects to the local TLS server and verifies that
# the server certificate is trusted using certificate.crt.
openssl s_client -connect 127.0.0.1:4433 \
-CAfile certificate.crt \
-verify_return_error


# --------------------------------------------------
# 4. Display the TLS communication result
# --------------------------------------------------
# If the TLS handshake succeeds, the certificate is
# successfully used to establish secure communication.
echo "TLS client-server communication test completed."
