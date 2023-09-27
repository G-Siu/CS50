import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")

try:
    output = []
    with open(sys.argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            split_name = row["name"].split(", ")
            output.append({"first": split_name[1], "last": split_name[0], "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"]).writeheader()
    # print(output)
    for row in output:
        writer.writerow(row)
