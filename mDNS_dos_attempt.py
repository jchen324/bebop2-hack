from scapy.all import *
from scapy.layers.dns import DNS, DNSQR

# Define the source and destination for the mDNS packet
ip = IP(
    dst="224.0.0.251", src="192.168.42.68"
)  # mDNS uses the 224.0.0.251 multicast address

# Define the UDP layer
udp = UDP(dport=5353, sport=5353)  # mDNS uses port 5353 for both source and destination

# Define a DNS query record (DNSQR) for each service you're querying
# This example shows just a couple; your actual requirement seems to include many more
qnames = [
    "_arsdk-ff3._udp.local",
    "_arsdk-0901._udp.local",
    "_arsdk-0902._udp.local",
    "_arsdk-0903._udp.local",
    "_arsdk-0905._udp.local",
    "_arsdk-0906._udp.local",
    "_arsdk-090c._udp.local",
    "_arsdk-090d._udp.local",
    "_arsdk-090e._udp.local",
    "_arsdk-0911._udp.local",
    "_arsdk-0913._udp.local",
    "_arsdk-0914._udp.local",
    "_arsdk-0916._udp.local",
    "_arsdk-0900._udp.local",
    "_arsdk-0907._udp.local",
    "_arsdk-0909._udp.local",
    "_arsdk-090a._udp.local",
    "_arsdk-090b._udp.local",
    "_arsdk-0910._udp.local",
    "_arsdk-090f._udp.local",
    "_arsdk-0915._udp.local",
    "_arsdk-0912._udp.local",
    "_arsdk-0917._udp.local",
    "Bebop2-403537._arsdk-090c._udp.local",
]


# Method 1
# Create the DNS query layer with multiple questions
dns = DNS(qdcount=len(qnames))
dns.qd = [DNSQR(qname=qname, qtype="PTR") for qname in qnames]


# Method 2
# # Define a DNS query record (DNSQR) for each service you're querying
# dns_queries = [DNSQR(qname=qname, qtype='PTR', qclass='IN') for qname in qnames]

# # Combine the DNS queries into a single DNS layer, marking it as a query (opcode QUERY)
# # and specifying it as a multicast query (rd=0) with the "QM" question type.
# dns = DNS(rd=0, qr=0, qd=dns_queries)


# Combine all layers into a single packet
packet = ip / udp / dns

# Optionally, display the packet
packet.show()

# Sending the packet, uncomment the line below to send
while True:
    send(packet)
    sleep(1)
