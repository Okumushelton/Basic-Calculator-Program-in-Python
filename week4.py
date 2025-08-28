try:
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    # Try opening the file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify content (e.g., make it uppercase)
    modified = content.upper()

    # Write to a new file
    with open("modified_output.txt", "w") as outfile:
        outfile.write(modified)

    print("Modified content written to 'modified_output.txt' successfully.")

except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read or write file.")