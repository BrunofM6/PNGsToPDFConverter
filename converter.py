from PIL import Image
from reportlab.pdfgen import canvas

def convert_pngs_to_pdf(image_paths, output_pdf_path):   
    images = [Image.open(image_path) for image_path in image_paths]
    width, height = images[0].size
    
    c = canvas.Canvas(output_pdf_path, pagesize=(width, height))
    
    for image_path in image_paths:
        c.drawImage(image_path, 0, 0, width=width, height=height)
        c.showPage()
    
    c.save()

i = int(input('how many PNG do you wish to convert? '))

image_paths = []
for n in range(i):
    print(f'image number {n + 1}')
    image_path = input('write the image path: ')
    image_paths.append(image_path)

output_pdf_path = 'output.pdf'
convert_pngs_to_pdf(image_paths, output_pdf_path)
