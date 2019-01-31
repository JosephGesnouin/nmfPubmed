import csv

txt_file = "cleaned.txt"
csv_file = "cleanedCsv.csv"

if __name__ == '__main__':

    print("################### CSV START ###################")
    with open(txt_file, "r") as in_text:

        in_reader = csv.reader(in_text, delimiter = '|')
        with open(csv_file, "w") as out_csv:
            out_writer = csv.writer(out_csv, lineterminator='\n', dialect='excel', delimiter = ';')
            for row in in_reader:
                out_writer.writerow(row)

    print("################### CSV END ###################")
