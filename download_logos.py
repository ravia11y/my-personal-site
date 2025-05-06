import requests
import os

def download_logo(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Create companies directory if it doesn't exist
os.makedirs('assets/companies', exist_ok=True)

# Company logo URLs (using alternative sources)
logos = {
    'aws-logo.png': 'https://a0.awsstatic.com/libra-css/images/site/fav/favicon.ico',
    'disney-logo.png': 'https://static-assets.bamgrid.com/product/disneyplus/favicons/favicon.ico',
    'data-solutions-logo.png': 'https://www.datasolutions.com/wp-content/uploads/2023/03/cropped-favicon-32x32.png',
    'airtel-logo.png': 'https://www.airtel.in/favicon.ico'
}

# Download each logo
for filename, url in logos.items():
    filepath = os.path.join('assets/companies', filename)
    download_logo(url, filepath) 