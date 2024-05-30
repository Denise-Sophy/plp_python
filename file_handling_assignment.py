try:
  # Create "my_file.txt" in write mode and write initial content
  with open("my_file.txt", "w") as file:
    file.write("Name: Denise Sophy Mutayi.\n")
    file.write("My age is: 65\n")
    file.write("And I want to become a software developer.\n")
  print("File creation and writing successful!")

  # Read the file content (optional, can be removed if already verified)
  with open("my_file.txt", "r") as file:
    content = file.read()
    print("\nInitial content of the file:")
    print(content)

  # Open the file in append mode and write additional lines
  with open("my_file.txt", "a") as file:
    file.write("\nAdditional achievements:\n")
    file.write("- Learned basic Python concepts.\n")
    file.write("- Completed file handling exercises successfully.\n")
  print("\nAppending successful!")

except FileNotFoundError:
  print("Error: File 'my_file.txt' not found. Creating a new one.")

except PermissionError:
  print("Error: Insufficient permissions to write to the file.")

finally:
  print("\nScript execution completed.")