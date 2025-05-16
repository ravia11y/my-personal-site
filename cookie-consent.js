// Cookie consent functionality
document.addEventListener('DOMContentLoaded', function() {
    const cookieConsent = document.createElement('div');
    cookieConsent.className = 'cookie-consent';
    cookieConsent.innerHTML = `
        <div class="cookie-content">
            <p>We use cookies to analyze site traffic and optimize your experience. By continuing to use this site, you consent to our use of cookies.</p>
            <div class="cookie-buttons">
                <button class="accept-cookies">Accept</button>
                <button class="decline-cookies">Decline</button>
            </div>
        </div>
    `;

    // Add styles
    const style = document.createElement('style');
    style.textContent = `
        .cookie-consent {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--primary-color);
            color: white;
            padding: 1rem;
            z-index: 1000;
            display: none;
        }
        .cookie-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }
        .cookie-buttons {
            display: flex;
            gap: 1rem;
        }
        .cookie-consent button {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
        }
        .accept-cookies {
            background: transparent;
            border: 1px solid white !important;
            color: white;
        }
        .decline-cookies {
            background: transparent;
            border: 1px solid white !important;
            color: white;
        }
        @media (max-width: 768px) {
            .cookie-content {
                flex-direction: column;
                text-align: center;
            }
        }
    `;
    document.head.appendChild(style);

    // Check if user has already made a choice
    if (!localStorage.getItem('cookieConsent')) {
        document.body.appendChild(cookieConsent);
        cookieConsent.style.display = 'block';
    }

    // Handle accept button
    cookieConsent.querySelector('.accept-cookies').addEventListener('click', function() {
        localStorage.setItem('cookieConsent', 'accepted');
        cookieConsent.style.display = 'none';
        // Enable Google Analytics
        window['ga-disable-G-WDL1DSWE1F'] = false;
    });

    // Handle decline button
    cookieConsent.querySelector('.decline-cookies').addEventListener('click', function() {
        localStorage.setItem('cookieConsent', 'declined');
        cookieConsent.style.display = 'none';
        // Disable Google Analytics
        window['ga-disable-G-WDL1DSWE1F'] = true;
    });
}); 