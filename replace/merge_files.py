#! /usr/bin/python3

filenames = ['file1.txt', 'file2.txt', 'file3.txt']
with open('output_file', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
