
#Brian Herrera
#Chapter08 Monthly Sales
#09/26/2024
#Create a program that displays 12 months of sales data, calculates the total
#average monthly sales from a csv file, allows the user to edit sales for any
#month and will be written to the csv file. and also adding try and except
#hanlding 




import FileIO as IO

VALID_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def display_menu():
    print("Options:")
    print("view  - View monthly sales")
    print("year  - View yearly sales total and average")
    print("edit  - Edit monthly sales")
    print("leave - Exit program")

def print_sales(sales_list):
    for month_data in sales_list:
        print(month_data[0] + "\t" + str(month_data[1]))
    print()

def yearly_sales(sales_list):
    total = 0
    for month in sales_list:
        try:
            total += int(month[1])
        except ValueError:
            print("Warning: Invalid sales value for " + month[0] + ". Using 0 for calculation.")
            total += 0

    average = round(total / len(sales_list), 2)
    print("yearly total: " + str(total))
    print("monthly average: " + str(average))

def edit_sales(sales_list):
    month_input = input("Enter the three-letter month abbreviation to edit: ")

    if month_input not in VALID_MONTHS:
        print("Invalid month. Please enter a valid three-letter abbreviation")
        return sales_list

    for month in sales_list:
        if month[0] == month_input:
            new_sales = input("Sales Amount: ")
            month[1] = new_sales
            print("Sales amount for " + month_input + " was changed.")
            break
    else:
        print("Month not found. Try again.")

    return sales_list

def main():
    sales_list = IO.read_from_file()

    if not sales_list:
        print("Error: No data available to proceed. Exiting program.")
        return

    while True:
        display_menu()
        command = input("Enter option choice: ")

        if command == 'view':
            print_sales(sales_list)
        elif command == 'year':
            yearly_sales(sales_list)
        elif command == 'edit':
            sales_list = edit_sales(sales_list)
            IO.write_to_file(sales_list)
        elif command == 'leave':
            break
        else:
            print("Invalid option. Please try again.")

    print("Bye")

if __name__ == "__main__":
    main()
