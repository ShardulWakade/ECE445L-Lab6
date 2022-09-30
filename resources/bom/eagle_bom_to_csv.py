#!/usr/bin/python3

import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("eagle_csv", type=str, help="name of the Eagle BOM file")
    parser.add_argument("new_csv", type=str, help="name of the file to save the new csv to")
    args = parser.parse_args()

    file_name = args.eagle_csv
    new_file_name = args.new_csv

    with open(file_name, "r") as old_csv:
        reader = csv.reader(old_csv, delimiter=";")
        with open(new_file_name, "w+", newline="") as new_csv:
            writer = csv.writer(new_csv, delimiter=",")
            for line in reader:
                writer.writerow(line)

if __name__ == "__main__":
    main()