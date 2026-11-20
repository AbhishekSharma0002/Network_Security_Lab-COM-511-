### Experiment 9: Configuration and Analysis of IPsec VPN in Tunnel Mode

### 1\. Aim / Objective

To establish an IKEv2 tunnel between two hosts, test secure communication, and examine the encapsulated packets.

### 2\. Requirements

* Two Kali Linux virtual machines (Gateway A and Gateway B).

* strongSwan IPsec software.

* Terminal with administrator access.

* Network connectivity between both gateways.

* Wireshark or other packet analysis tools.

### 3\. Theory

* IPsec: A set of protocols that secures IP communication through encryption, authentication, and data integrity.

* Tunnel Mode: Protects the entire original IP packet by encapsulating it inside a new IP packet.

* IKEv2: Establishes secure communication by authenticating peers and exchanging encryption keys.

* ESP: Provides encryption, integrity, and replay protection for transmitted data.

* Pre-Shared Key (PSK): A shared secret used to authenticate both VPN gateways.

* strongSwan: An open-source tool used to configure and manage IPsec VPN connections.

### 4\. Procedure

Step 1: Configure IP Addresses

Two Kali Linux virtual machines are set up as Gateway A and Gateway B. Their outer IP addresses are `192.168.229.128` and `192.168.229.129`. The inner tunnel addresses `10.10.1.1/32` and `10.20.1.1/32` are assigned through loopback interfaces.

IP Address Configuration

Step 2: Test Network Connectivity

The connection between both gateways is tested using the ping command to ensure that they can communicate over the outer network.

Outer Network Connectivity

Step 3: Check strongSwan Configuration

The loaded strongSwan settings are examined using the `swanctl` utility. Connection details, peer identities, authentication methods, and tunnel settings are verified.

strongSwan Configuration Verification

Step 4: Check IKE SA and CHILD SA

The VPN connection is started from Gateway A. The following command is used to check the established security associations:

```bash
sudo swanctl --list-sas
```

The output confirms the VPN connection and negotiated security settings.

Established Security Associations

Step 5: Examine IPsec XFRM States

The installed IPsec states are viewed using:

```bash
sudo ip xfrm state
```

This displays the SPI, encryption algorithm, and other security parameters.

IPsec XFRM States

Step 6: Examine IPsec Policies

The configured IPsec policies are checked using:

```bash
sudo ip xfrm policy
```

These policies determine which network traffic must pass through IPsec protection.

IPsec XFRM Policies

Step 7: Test Protected Communication

Secure communication between the inner tunnel addresses is tested with:

```bash
ping -I 10.10.1.1 10.20.1.1
```

Successful replies confirm that packets are travelling through the VPN tunnel.

Protected IPsec Communication

Step 8: Check IPsec Traffic Counters

The IPsec traffic counters are examined to monitor transmitted packets and bytes. Increasing counter values indicate successful processing of tunnel traffic.

IPsec Traffic Counters

### 5\. Improvement

An incorrect pre-shared key was temporarily configured on one gateway to test authentication. The connection failed because the keys did not match. After restoring the correct key, the VPN tunnel was established successfully. This verified PSK-based authentication.

### 6\. Files Included

* Commands.sh: Contains the commands used in the experiment with brief explanations.

* Outputs/ss1.png – ss8.png: Includes screenshots of IP configuration, connectivity, VPN setup, security associations, XFRM states and policies, protected communication, and traffic counters.

### 7\. Result

* IKEv2 and IPsec CHILD Security Associations were successfully established.

* The negotiated ESP encryption algorithm was AES-GCM-16-256.

* Inner-network ping received 4 out of 4 replies with 0% packet loss.

* IPsec counters showed 4 packets and 336 bytes transferred in both directions.

* Incorrect PSK authentication was rejected, while the correct key successfully re-established the tunnel.

Detailed results are available in the screenshots through the QR code provided in the lab manual.

### 8\. Conclusion

The experiment successfully demonstrated a site-to-site IPsec VPN using IKEv2 and ESP in tunnel mode. Secure communication was achieved through encryption and pre-shared key authentication between the two gateways.
