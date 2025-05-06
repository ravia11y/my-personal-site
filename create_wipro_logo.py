from PIL import Image, ImageDraw, ImageFont
import os

def create_wipro_logo(filename, size=(60, 60)):
    # Create a new image with Wipro's brand color
    bg_color = (0, 0, 128)  # Wipro blue
    text_color = (255, 255, 255)  # White text
    
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Calculate text size and position
    text = "Wipro"
    font_size = 16
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
    print(f"Created new Wipro logo: {filename}")

# Create the Wipro logo
filepath = os.path.join('assets', 'companies', 'wipro-logo.png')
create_wipro_logo(filepath) 