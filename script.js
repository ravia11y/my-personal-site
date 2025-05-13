// Update copyright year
document.getElementById('current-year').textContent = new Date().getFullYear();

// Mobile menu functionality
const menuToggle = document.querySelector('.menu-toggle');
const mainMenu = document.querySelector('.nav-menu');

menuToggle.addEventListener('click', () => {
    const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', !isExpanded);
    mainMenu.classList.toggle('active');
});

// Close menu when clicking outside
document.addEventListener('click', (event) => {
    if (!event.target.closest('nav') && mainMenu.classList.contains('active')) {
        menuToggle.setAttribute('aria-expanded', 'false');
        mainMenu.classList.remove('active');
    }
});

// Close menu when pressing Escape key
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && mainMenu.classList.contains('active')) {
        menuToggle.setAttribute('aria-expanded', 'false');
        mainMenu.classList.remove('active');
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        // Close mobile menu if open
        if (mainMenu.classList.contains('active')) {
            menuToggle.setAttribute('aria-expanded', 'false');
            mainMenu.classList.remove('active');
        }
        
        targetElement.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// Add active class to navigation items on scroll
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav a');

window.addEventListener('scroll', () => {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (pageYOffset >= sectionTop - 60) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Hamburger menu functionality
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const menuLinks = document.querySelectorAll('.nav-menu a');

    function toggleMenu() {
        const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
        menuToggle.setAttribute('aria-expanded', !isExpanded);
        navMenu.classList.toggle('active');
        
        // Prevent body scroll when menu is open
        document.body.style.overflow = !isExpanded ? 'hidden' : '';
    }

    menuToggle.addEventListener('click', toggleMenu);

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInside = navMenu.contains(event.target) || menuToggle.contains(event.target);
        if (!isClickInside && navMenu.classList.contains('active')) {
            toggleMenu();
        }
    });

    // Close menu when clicking a link
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (navMenu.classList.contains('active')) {
                toggleMenu();
            }
        });
    });

    // Close menu on escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && navMenu.classList.contains('active')) {
            toggleMenu();
        }
    });

    // Update current year in footer
    document.getElementById('current-year').textContent = new Date().getFullYear();
}); 