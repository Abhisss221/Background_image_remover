from rembg import remove 
from PIL import Image
input_path = r'C:\Users\Abhishek\OneDrive\Desktop\pythom\test1.jpeg'
output_path = "output.png"
inputp = Image.open(input_path)
output = remove(inputp)
output.save(output_path)