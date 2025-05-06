# Personal Portfolio Website

A modern, responsive, and accessible personal portfolio website built with HTML5, CSS3, and JavaScript. This website is designed to showcase your professional experience, education, skills, and contact information in a clean and organized manner.

## Features

- Responsive design that works on all devices
- Accessible to screen readers and keyboard navigation
- SEO-friendly structure
- Modern and professional design
- Smooth scrolling navigation
- Print-friendly styles
- Timeline-based experience and education sections
- Skills grid layout
- Contact information with social media links

## Setup Instructions

1. Clone this repository to your local machine
2. Replace the placeholder content in `index.html` with your personal information:
   - Update the meta tags with your name and keywords
   - Add your profile picture to the `assets` folder
   - Fill in your professional experience
   - Add your education history
   - List your skills
   - Update contact information and social media links

3. Customize the styling:
   - Modify the color scheme in `styles.css` by updating the CSS variables in the `:root` selector
   - Adjust spacing and layout as needed
   - Add or remove sections as required

4. Deploy to GitHub Pages:
   - Create a new repository on GitHub
   - Push your code to the repository
   - Go to repository settings
   - Under "GitHub Pages" section, select the main branch as the source
   - Your site will be published at `https://[your-username].github.io/[repository-name]`

## Customization

### Colors
The website uses CSS variables for easy color customization. Edit the following variables in `styles.css`:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --text-color: #333;
    --light-bg: #f8f9fa;
}
```

### Profile Picture
1. Add your profile picture to the `assets` folder
2. Update the image source in `index.html`:
```html
<img src="assets/your-image.jpg" alt="Your Name's professional headshot">
```

### Content Sections
The website includes the following sections:
- About
- Experience
- Education
- Skills
- Contact

You can modify these sections in `index.html` to match your needs.

## Accessibility Features

- Semantic HTML structure
- ARIA labels for navigation
- Keyboard navigation support
- Focus indicators
- Screen reader friendly content
- Reduced motion support
- Print-friendly styles

## Browser Support

The website is compatible with:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests! 