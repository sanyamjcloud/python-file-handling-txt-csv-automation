import csv

# -----------------------------
# TEXT FILE OPERATIONS
# -----------------------------

try:
    # 1 & 2. Create text file and write user data
    with open("data.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

    # 3. Read file contents
    with open("data.txt", "r") as file:
        print("\nFile Contents:")
        print(file.read())

    # 4. Append data to file
    with open("data.txt", "a") as file:
        file.write("Status: Learning Python File Handling\n")

    # Read again after appending
    with open("data.txt", "r") as file:
        print("\nUpdated File Contents:")
        print(file.read())

except FileNotFoundError:
    print("File not found error occurred.")
except IOError:
    print("Input/Output error occurred.")
except Exception as e:
    print("An unexpected error occurred:", e)


# -----------------------------
# CSV FILE OPERATIONS
# -----------------------------

try:
    # 6 & 7. Create CSV file and write multiple rows
    with open("students.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Name", "Course"])
        writer.writerow([1, "Sanyam", "Python"])
        writer.writerow([2, "Aman", "Linux"])
        writer.writerow([3, "Ravi", "Cloud Computing"])

    # 8. Read CSV data
    print("\nCSV File Contents:")
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

except Exception as e:
    print("CSV file error:", e)
