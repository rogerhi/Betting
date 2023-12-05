 Path to the input and output files
input_file_path = 'path_to_your_input_file.txt'
output_file_path = 'path_to_your_output_file.txt'

# Open the input file and the output file
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Read each line from the input file
    for line in input_file:
        # Check if 'Hawthorn' is in the line
        if 'Hawthorn' in line:
            # Write the line to the output file
            output_file.write(line)