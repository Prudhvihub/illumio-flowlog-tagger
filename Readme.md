# illumio-flowlog-tagger
 Assesment

Description

This Python script processes AWS VPC Flow Logs (Version 2 only) and assigns tags based on a lookup table provided in a CSV file. It then generates summary reports of:

Tag Counts: The number of occurrences of each assigned tag.

Port/Protocol Combination Counts: The number of occurrences of each destination port and protocol combination.

Requirements & Assumptions

✅ The program supports only AWS VPC Flow Log Version 2.
✅ The lookup table must be a CSV file with three columns: dstport, protocol, tag.
✅ Matching is case-insensitive for protocol names (e.g., TCP == tcp).
✅ The program must handle large files efficiently (tested with 10MB logs and 10,000 mappings).
✅ Only built-in Python libraries are used (no pandas, Spark, or external dependencies).
✅ Logs that do not have a matching (dstport, protocol) entry in the lookup table will be tagged as "Untagged".


Illumio/
│── Requirements/
│   ├── flow_logs.txt          # Sample input flow logs
│   ├── flowlog_tagger.py      # Main script for processing logs
│   ├── lookup.csv             # Lookup table for port/protocol mapping
│   ├── output.txt             # Output file with processed results
│──__pycache__/           # (Generated Python cache files)
│── scaled_to_10mb/            # Directory for large test files
│   ├── flowlog_tagger_test.py  # Test script to validate functionality
│   ├── large_flow_logs.txt     # 10MB+ flow log file for scalability testing
│   ├── large_lookup.csv        # 10,000 entry lookup table for testing
│   ├── main.py                 # Alternate script for execution
│   ├── output.txt              # Output file containing final results

README.md                   # Instructions and documentation

How to Run the Script

Step 1: Install Python (if not installed)

Ensure you have Python 3.x installed on your machine. You can check by running:
python3 --version
Step 2: Clone the Repository
git clone https://github.com/YOUR_USERNAME/illumio-flowlog-tagger.git
cd illumio-flowlog-tagger
Step 3: Run the Script
python3 Requiremtns/flowlog_tagger.py flow_logs.txt lookup.csv output.txt
✅ This will generate output.txt containing Tag Counts and Port/Protocol Counts.

Step 4: Verify the Output

Check output.txt for results. Example output:
Tag Counts:
Tag,Count
sv_P2,1
sv_P1,2
email,3
Untagged,9

Port/Protocol Combination Counts:
Port,Protocol,Count
22,tcp,1
25,tcp,1
443,tcp,1

Testing the Script

A test script flowlog_tagger_test.py is included for validating the core functionality.
To run tests:
python3 flowlog_tagger_test.py

Performance & Scalability

✅ Successfully processed 10MB+ flow logs (large_flow_logs.txt).
✅ Lookup table tested with 10,000 mappings (large_lookup.csv).
✅ Efficient file handling: reads and processes logs line by line to avoid memory issues.

Submission Details

🔹 GitHub Repository: [Insert Your Repository Link Here]🔹 Submission includes:

flowlog_tagger.py (Main script)

flowlog_tagger_test.py (Test script)

large_flow_logs.txt (10MB test file)

large_lookup.csv (10,000 mappings)

output.txt (Results after execution)

README.md (Documentation and instructions)



