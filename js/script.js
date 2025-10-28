// =====================
// Initialize on page load
// =====================

document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    updateFooterYear();
    highlightActiveSection();
});

// =====================
// Navigation & Scrolling
// =====================

function initializeNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                // Calculate offset for fixed sidebar (only on desktop)
                const isMobile = window.innerWidth <= 768;
                const offset = isMobile ? 20 : 100;

                const targetPosition = targetSection.offsetTop - offset;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// =====================
// Active Section Highlighting
// =====================

function highlightActiveSection() {
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.nav-link');

    // Initial highlight
    updateActiveLink();

    // Update on scroll
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        // Debounce scroll event for performance
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(updateActiveLink, 50);
    });

    function updateActiveLink() {
        let currentSection = '';
        const scrollPosition = window.scrollY + 200;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSection = section.getAttribute('id');
            }
        });

        // If at the very top, highlight the first section
        if (window.scrollY < 100) {
            currentSection = sections[0].getAttribute('id');
        }

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + currentSection) {
                link.classList.add('active');
            }
        });
    }
}

// =====================
// Footer Year
// =====================

function updateFooterYear() {
    const yearElement = document.getElementById('year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}

// =====================
// Handle window resize
// =====================

let resizeTimeout;
window.addEventListener('resize', function() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(function() {
        // Recalculate active section on resize
        highlightActiveSection();
    }, 250);
});
