from PIL import Image, ImageDraw, ImageFont
import os

def create_logo(text, filename, size=(60, 60), bg_color=(255, 255, 255), text_color=(0, 0, 0)):
    # Create a new image with a white background
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Calculate text size and position
    font_size = 20
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Draw text in the center
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    draw.text((x, y), text, font=font, fill=text_color)
    
    # Save the image
    img.save(filename)
    print(f"Created placeholder logo: {filename}")

# Create companies directory if it doesn't exist
os.makedirs('assets/companies', exist_ok=True)

# Create placeholder logos
logos = {
    'aws-logo.png': 'AWS',
    'disney-logo.png': 'Disney',
    'data-solutions-logo.png': 'DS',
    'airtel-logo.png': 'Airtel'
}

for filename, text in logos.items():
    filepath = os.path.join('assets/companies', filename)
    create_logo(text, filepath) 