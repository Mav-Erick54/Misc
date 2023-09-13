# Input GFF file
input_file = "88_augustus.gff"

# Output GFF file
output_file = "clean_88_augustus_annotation.gff"

# Open the input and output files
with open(input_file, "r") as input_gff, open(output_file, "w") as output_gff:
    # Iterate through lines in the input GFF file
    for line in input_gff:
        # Check if the line does not start with "#"
        if not line.startswith("#"):
            # Write non-comment lines to the output GFF file
            output_gff.write(line)