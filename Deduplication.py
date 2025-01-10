def remove_duplicates_from_file(input_file, output_file):
    try:
        # Read the contents of the input file
        with open(input_file, 'r') as file:
            lines = file.read().splitlines()

        # Remove duplicates by converting the list to a set and then back to a sorted list
        unique_lines = sorted(set(lines))

        # Write the unique lines to the output file
        with open(output_file, 'w') as file:
            for line in unique_lines:
                file.write(f"{line}\n")

        print(f"Duplicates removed. Cleaned data saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'cleaned_passwords.txt'  # Replace with your input file name containing the list of words
output_file = 'completed_passwords.txt'# Replace with your desired output file name
remove_duplicates_from_file(input_file, output_file)

