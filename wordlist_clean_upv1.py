def extract_item_values(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        extracted_words = []

        for line in lines:
            if "Item value: " in line:
                # Extract the word after "Item value: "
                parts = line.split("Item value: ", 1)
                if len(parts) > 1:
                    # Get the part after "Item value: "
                    remainder = parts[1].strip()
                    # Check if it is a single line and not empty
                    if remainder and " " not in remainder and "\n" not in remainder:
                        extracted_words.append(remainder)

        # Write the extracted words to the output file
        with open(output_file, 'w') as file:
            for word in extracted_words:
                file.write(f"{word}\n")

        print(f"Extraction complete. Results saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'passwords.txt'  # Replace with your input file name
output_file = 'cleaned_passwords.txt'  # Replace with your desired output file name
extract_item_values(input_file, output_file)
