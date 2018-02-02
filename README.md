Tax Document Tool


This tool is for editing text files of customer account activity downloaded from CoreCard. 

It will sum the total loan charges and open an edited and appropriately condensed csv in Excel

To use: 

1. Save taxdoc.py
2. Download customer's transaction history from CoreCard (test.txt can be used to test/practice!)
3. Open up terminal, cd into folder containing taxdoc.py
4. Run python taxdoc.py "Path to transaction history," where you've typed out the path to the downloaded file. 
          -The path will usually be "/Users/yourusername/Downloads/file.txt"
            -Change username and filename
            -Be sure to put the whole path in quotes as CC puts a space in the file name automatically and this will throw an               error when you run it
5. A csv will open in excel that you can format however you want (change color of header, freeze top row, etc.) Total loan charges is listed as the last line.
6. Send spreadsheet to customer


Known Issues:
 Still have to format the document in excel a bit to make it look nice;
 "Transaction Amount" header prints with a $ sign in front of it; 
 Won't open a new window of Excel, will only work if there isn't currently an excel doc open;
