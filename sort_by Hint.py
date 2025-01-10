def filter_words_starting_with_n(input_file, output_file):
    try:
        # Read the contents of the input file
        with open(input_file, 'r') as file:
            lines = file.read().splitlines()

        # Filter words that start with 'n' or 'N'
        filtered_words = [line for line in lines if line.lower().startswith('n')]

        # Write the filtered words to the output file
        with open(output_file, 'w') as file:
            for word in filtered_words:
                file.write(f"{word}\n")

        print(f"Words starting with 'n' or 'N' saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'completed_passwords.txt'  # Replace with your input file name containing the list of words
output_file = 'filtered_words.txt'  # Replace with your desired output file name
filter_words_starting_with_n(input_file, output_file)
