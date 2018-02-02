"""
The purpose of this is:
    Open a .txt file downloaded from CoreCard
    Remove unnecessary columns
    Sum and print loan charges
    Save as a csv
    Open in Excel
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
    current_balance = bits[8]
    loan_fee = "590 = Loan Charge"
    if loan_fee in line and is_number(transaction_amount):
        transaction_amount = float(transaction_amount)
        total_charges += transaction_amount

    outfile.write("%s,%s,$%s,%s\n" % (transaction_date,
                                       transaction_description,
                                       transaction_amount,
                                       current_balance,))
outfile.write("Total Loan Charges:, $%s" % (total_charges))

subprocess.call(["open", "out.csv", "-a", "Microsoft Excel"])


