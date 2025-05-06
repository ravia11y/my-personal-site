from PIL import Image, ImageDraw, ImageFont
import os

def create_company_logo(text, filename, bg_color, size=(60, 60)):
    # Create a new image with specified background color
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Calculate text size and position
    font_size = 14  # Slightly smaller font for better fit
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
    
    # Add text with white color
    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    
    # Save the image
    img.save(filename)
    print(f"Created logo: {filename}")

# Create companies directory if it doesn't exist
os.makedirs('assets/companies', exist_ok=True)

# Company logos with their brand colors
companies = {
    'aws-logo.png': ('AWS', (255, 153, 0)),  # AWS Orange
    'disney-logo.png': ('Disney', (0, 113, 235)),  # Disney Blue
    'data-solutions-logo.png': ('DS', (41, 128, 185)),  # Blue
    'airtel-logo.png': ('Airtel', (237, 28, 36)),  # Airtel Red
    'wipro-logo.png': ('Wipro', (0, 0, 128))  # Wipro Blue
}

# Create all logos
for filename, (text, color) in companies.items():
    filepath = os.path.join('assets', 'companies', filename)
    create_company_logo(text, filepath, color) 