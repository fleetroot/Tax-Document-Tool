"""
The purpose of this is:
    Open a .txt file downloaded from CoreCard
    Remove unnecessary columns
    Add loan charges
    Save as a csv
    Open in Excel

    with open('test.txt', 'r') as f:
        if ip_address not in d:
        d[ip_address] = 0
    if put_request in line:
        d[ip_address] += 1



    if fee in transaction_description:
        int_trans = int(transaction_amount)
        for val in int_trans:
            total_charges += val

    python TaxDoc.py /Users/kfrechette/Downloads/"download (30).txt"

        if loan_fee not in d:
        d[loan_fee] = 0
    if transaction_amount in line:
        d[loan_fee] += 1

          def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

        https://www.youtube.com/watch?v=hJgg1um6-V8
    """

import os, sys, subprocess

def is_number(s):
    """Return whether or not s is a number."""
    try:
        float(s)
        return True
    except ValueError:
        return False

if len(sys.argv) > 1 and os.path.isfile(str(sys.argv[1])):
    infile = open(sys.argv[1], "r")
else:
    if not os.path.isfile("test.txt"):
        raise Exception("Please provide the transaction activity file for this script to parse.")
    infile = open("test.txt", "r")

outfile = open("out.csv", "w")

total_charges = 0

for line in infile.readlines():
    bits = line.split("\t")
    transaction_date = bits[1]
    transaction_description = bits[3]
    transaction_amount = bits[5].replace("\"", "").replace("$", "").replace(",", "")
    # print "transaction amount:", transaction_amount
    current_balance = bits[8]
    loan_fee = "loan charge"

    if is_number(transaction_amount):
        transaction_amount = float(transaction_amount)
        total_charges += transaction_amount
        #print transaction_date, "\t", transaction_description, "\t", transaction_amount, "\t", current_balance

    outfile.write("%s,%s,%s,%s\n" % (transaction_date,
                                     transaction_description,
                                     transaction_amount,
                                     current_balance))

print "Total Loan Charges: $%s" % total_charges
# print "Year-End Balance: ",t


subprocess.call(["open", "out.csv", "-a", "Microsoft Excel"])


