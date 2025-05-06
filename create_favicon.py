from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon():
    # Create directory if it doesn't exist
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    # Create favicon (32x32)
    favicon = Image.new('RGBA', (32, 32), (26, 54, 93))  # Using primary color
    draw = ImageDraw.Draw(favicon)
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    # Draw text
    text = "RV"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (32 - text_width) // 2
    y = (32 - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save favicon
    favicon.save('assets/favicon.png')
    
    # Create apple touch icon (180x180)
    apple_icon = Image.new('RGBA', (180, 180), (26, 54, 93))
    draw = ImageDraw.Draw(apple_icon)
    
    try:
        font = ImageFont.truetype("arial.ttf", 100)
    except:
        font = ImageFont.load_default()
    
    # Draw text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (180 - text_width) // 2
    y = (180 - text_height) // 2
    
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # Save apple touch icon
    apple_icon.save('assets/apple-touch-icon.png')

if __name__ == "__main__":
    create_favicon() 