# -------------------------------------------------------
# File Word Replace Program [JKUAD0910]
# -------------------------------------------------------

def find_and_replace_in_file(filename, find_word, replace_word):
    try:
        # Step 1: Open file and read content
        with open(filename, 'r') as file:
            content = file.read()

        if not content.strip():  # Empty file check
            print("⚠ The file is empty. Nothing to replace.")
            return

        # Step 2: Replace word
        modified_content = content.replace(find_word, replace_word)

        # Step 3: Save back to file
        with open(filename, 'w') as file:
            file.write(modified_content)

        print(f"✅ Successfully replaced '{find_word}' with '{replace_word}' in {filename} [JKUAD0910]")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found. [JKUAD0910]")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read/write '{filename}'. [JKUAD0910]")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e} [JKUAD0910]")


def main():
    print("📂 Word Replace Tool [JKUAD0910]")

    filename = input("Enter file name (e.g., data.txt): ")
    find_word = input("Enter the word to find: ")
    replace_word = input("Enter the word to replace it with: ")

    find_and_replace_in_file(filename, find_word, replace_word)


if __name__ == "__main__":
    main()
