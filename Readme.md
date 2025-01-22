# **Flow Log Parser**

## **Description**
This program parses a file containing flow log data and assigns each row to a tag using a lookup table. The lookup table is provided as a CSV file with three columns: 'dstport', 'protocol', and 'tag'. The combination of 'dstport' and 'protocol' specifies the tag that applies to each log entry. The program has two outputs:

1. Match count for each tag.
2. Match count for each 'port/protocol' combination.

## **Assumptions** - This software only supports AWS VPC Flow Log Version 2.
- The lookup table **must be a CSV file** with three columns named 'dstport, protocol, and tag'.
- **Protocol names are matched case-insensitively** (for example, 'TCP == tcp').
- The **program must handle huge files efficiently** (tested with 10MB log files and 10,000 mappings).
- **Only built-in Python libraries** are used (no pandas, Spark, or other dependencies).
- Logs without a matching '(dstport, protocol)' entry in the lookup table will be marked as **"Untagged"**.

---

## **Folder Structure**

```
Illumio/
│── Requirements/
│   ├── flow_logs.txt          # Sample input flow logs
│   ├── flowlog_tagger.py      # Main script for processing logs
│   ├── lookup.csv             # Lookup table for port/protocol mapping
│   ├── output.txt             # Output file with processed results
│   ├── __pycache__/           # (Generated Python cache files)
│── scaled_to_10mb/            # Directory for large test files
│   ├── flowlog_tagger_test.py  # Test script to validate functionality
│   ├── large_flow_logs.txt     # 10MB+ flow log file for scalability testing
│   ├── large_lookup.csv        # 10,000 entry lookup table for testing
│   ├── main.py                 # Alternate script for execution
│   ├── output.txt              # Output file containing final results
│── README.md                   # Instructions and documentation
```

---

## **Usage**

### **Running the Program**
1. Ensure **Python 3.x** is installed on your machine.
2. Place the `lookup.csv` and `flow_logs.txt` files in the same directory as `flowlog_tagger.py`.
3. Run the script using the command:
   ```bash
   python3 flowlog_tagger.py Requirements/flow_logs.txt Requirements/lookup.csv Requirements/output.txt
   ```
4. The output will be written to `output.txt` in the **Requirements/** directory.

### **Verifying the Output**
Check `output.txt` for results. Example output:

```
Tag Counts:
Tag,Count
Untagged,8
email,3
sv_P1,2
sv_P2,1
sv_P4,1

Port/Protocol Combination Counts:
Port,Protocol,Count
22,tcp,1
23,tcp,1
25,tcp,1
80,tcp,1
110,tcp,1
143,tcp,1
443,tcp,1
993,tcp,1
1024,tcp,1
49153,tcp,1
49154,tcp,1
49155,tcp,1
49156,tcp,1
49157,tcp,1
49158,tcp,1
```

---

## **Testing**
A test script `flowlog_tagger_test.py` is included for validating the core functionality.
To run tests:

```bash
python3 scaled_to_10mb/flowlog_tagger_test.py
```

Expected output:

```
Output.txt
```

---

## **Performance & Scalability**
✅ Successfully processed **10MB+ flow logs** (`large_flow_logs.txt`).
✅ Lookup table tested with **10,000 mappings** (`large_lookup.csv`).
✅ Efficient file handling: reads and processes logs **line by line** to avoid memory issues.

---

## **Submission Details**

🔹 **GitHub Repository:** [Insert Your Repository Link Here]\
🔹 **Submission includes:**

- `flowlog_tagger.py` (Main script)
- `flowlog_tagger_test.py` (Test script)
- `large_flow_logs.txt` (10MB test file)
- `large_lookup.csv` (10,000 mappings)
- `output.txt` (Results after execution)
- `README.md` (Documentation and instructions)



