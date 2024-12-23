import csv

CSV_FILE = "monthly_sales.csv"

def read_from_file():
    sales_list = []
    try:
        with open(CSV_FILE) as file:
            for line in file:
                line = line.replace("\n", "")
                month_data = line.split(",")
                sales_list.append(month_data)
    except FileNotFoundError:
        print("Error: Could not find the file '" + CSV_FILE + "'. Please check the file path.")
    return sales_list

def write_to_file(sales_list):
    with open(CSV_FILE, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales_list)
