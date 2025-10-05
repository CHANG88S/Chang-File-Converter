import img2pdf
import os

# Define the file paths
image_file = "my_image.jpg"
pdf_output = "output.pdf"

# The conversion process
with open(pdf_output, "wb") as f:
    f.write(img2pdf.convert(image_file))

print(f"Successfully converted {image_file} to {pdf_output}")