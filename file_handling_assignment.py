
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, World!\n")
            file.write("The answer to life is God.\n")
            file.write("Python is fun!\n")
        print("File created and data written successfully.")
    except PermissionError:
        print("Permission denied: Unable to create or write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Create file operation finished.")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("File not found: 'my_file.txt' does not exist.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Read file operation finished.")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending more data...\n")
            file.write("The year is 2024.\n")
            file.write("Learning is a lifelong journey.\n")
        print("Data appended successfully.")
    except FileNotFoundError:
        print("File not found: 'my_file.txt' does not exist.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Append to file operation finished.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file() 
