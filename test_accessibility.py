import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def test_accessibility(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    results = {
        'passed': [],
        'failed': [],
        'warnings': []
    }
    
    # Test 1: Check for proper heading hierarchy
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    if not any(h.name == 'h1' for h in headings):
        results['failed'].append('No H1 heading found')
    
    # Test 2: Check images for alt text
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            results['failed'].append(f'Image missing alt text: {img.get("src", "unknown source")}')
    
    # Test 3: Check for proper ARIA labels
    interactive_elements = soup.find_all(['a', 'button', 'input'])
    for element in interactive_elements:
        if not (element.get('aria-label') or element.get('aria-labelledby') or element.get('title')):
            if element.name == 'a' and not element.get_text().strip():
                results['failed'].append(f'Link missing accessible name: {element.get("href", "unknown link")}')
    
    # Test 4: Check for proper form labels
    forms = soup.find_all('form')
    for form in forms:
        inputs = form.find_all('input')
        for input_elem in inputs:
            if input_elem.get('type') not in ['submit', 'button', 'hidden']:
                if not (input_elem.get('id') and form.find('label', {'for': input_elem.get('id')})):
                    results['failed'].append(f'Input missing label: {input_elem.get("name", "unnamed input")}')
    
    # Test 5: Check for proper color contrast (basic check)
    style_tags = soup.find_all('style')
    for style in style_tags:
        if 'color:' in style.string and 'background-color:' in style.string:
            results['warnings'].append('Manual color contrast check needed')
    
    # Test 6: Check for proper language attribute
    if not soup.html.get('lang'):
        results['failed'].append('HTML language attribute missing')
    
    # Test 7: Check for skip links
    skip_links = soup.find_all('a', {'class': 'skip-link'})
    if not skip_links:
        results['warnings'].append('Skip link not found')
    
    # Test 8: Check for proper document structure
    if not soup.find('main'):
        results['failed'].append('Main content area not found')
    if not soup.find('header'):
        results['warnings'].append('Header element not found')
    if not soup.find('footer'):
        results['warnings'].append('Footer element not found')
    
    return results

def print_results(results):
    print("\n=== Accessibility Test Results ===\n")
    
    if results['failed']:
        print("❌ Failed Tests:")
        for test in results['failed']:
            print(f"  - {test}")
    else:
        print("✅ No critical failures found")
    
    if results['warnings']:
        print("\n⚠️ Warnings:")
        for warning in results['warnings']:
            print(f"  - {warning}")
    
    if results['passed']:
        print("\n✅ Passed Tests:")
        for test in results['passed']:
            print(f"  - {test}")

if __name__ == "__main__":
    results = test_accessibility('index.html')
    print_results(results) 