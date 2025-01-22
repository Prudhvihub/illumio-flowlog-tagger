#!/usr/bin/env python3


import sys
import csv
import os

PROTOCOL_MAP = {
    '1':  'icmp',
    '6':  'tcp',
    '17': 'udp',
}

def load_lookup_table(lookup_file):
    """
    Loads the lookup CSV with columns: dstport,protocol,tag
    Returns a dict of {(port, protocol) : tag} in case-insensitive manner.
    """
    table = {}
    with open(lookup_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            port_str = row['dstport'].strip()
            protocol_str = row['protocol'].strip().lower()
            tag_str = row['tag'].strip()
            table[(port_str, protocol_str)] = tag_str
    return table

def parse_flow_log_line(line):
    """
    Parses a single line of the AWS VPC Flow Log (version 2).
    Returns a dictionary with relevant fields if valid, else None.
    """
    parts = line.strip().split()
    if len(parts) != 14:
        return None
    version, account_id, eni_id, srcaddr, dstaddr, srcport, dstport, protocol, \
        packets, bytes_, start, end, action, log_status = parts
    if version != '2':
        return None
    return {
        'dstport': dstport,
        'protocol': protocol
    }

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 flowlog_tagger.py <flow_log_file> <lookup_csv_file> <output_file>")
        sys.exit(1)

    flow_log_file = sys.argv[1]
    lookup_csv_file = sys.argv[2]
    output_file = sys.argv[3]

    lookup_table = load_lookup_table(lookup_csv_file)
    tag_counts = {}
    port_protocol_counts = {}
    untagged_label = "Untagged"

    with open(flow_log_file, 'r') as flogs:
        for line in flogs:
            record = parse_flow_log_line(line)
            if record is None:
                continue
            proto_num = record['protocol']
            protocol_str = PROTOCOL_MAP.get(proto_num, proto_num).lower()
            dst_port_str = record['dstport']
            key = (dst_port_str, protocol_str)
            tag = lookup_table.get(key, untagged_label)
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            port_protocol_counts[key] = port_protocol_counts.get(key, 0) + 1

    with open(output_file, 'w') as out:
        out.write("Tag Counts:\n")
        out.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            out.write(f"{tag},{count}\n")
        out.write("\nPort/Protocol Combination Counts:\n")
        out.write("Port,Protocol,Count\n")
        for (port, proto), count in sorted(port_protocol_counts.items(), key=lambda x: (int(x[0][0]), x[0][1])):
            out.write(f"{port},{proto},{count}\n")
    print(f"Results written to: {output_file}")

if __name__ == "__main__":
    main()
