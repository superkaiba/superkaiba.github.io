// Scroll Animations and Parallax Effects
(function() {
    'use strict';
    
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Stagger animations for children
                const children = entry.target.querySelectorAll('.animate-child');
                children.forEach((child, index) => {
                    setTimeout(() => {
                        child.classList.add('visible');
                    }, index * 100);
                });
            }
        });
    }, observerOptions);
    
    // Initialize scroll animations
    function initScrollAnimations() {
        // Add animation classes to elements
        const animateElements = [
            '.post-header',
            '.profile',
            '.card',
            '.project',
            '.news',
            '.social',
            'article > h2',
            'article > h3',
            'article > p',
            'article > ul',
            'article > ol',
            '.research-info-panel'
        ];
        
        animateElements.forEach(selector => {
            document.querySelectorAll(selector).forEach(el => {
                if (!el.classList.contains('animate-on-scroll')) {
                    el.classList.add('animate-on-scroll');
                    observer.observe(el);
                }
            });
        });
    }
    
    // Parallax effect
    let ticking = false;
    function updateParallax() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.parallax');
        
        parallaxElements.forEach(el => {
            const speed = el.dataset.speed || 0.5;
            const yPos = -(scrolled * speed);
            el.style.transform = `translateY(${yPos}px)`;
        });
        
        // Update neural network background opacity based on scroll
        const neuralBg = document.getElementById('neural-network-bg');
        if (neuralBg) {
            const opacity = Math.max(0.05, 0.15 - scrolled * 0.0001);
            neuralBg.style.opacity = opacity;
        }
        
        ticking = false;
    }
    
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(updateParallax);
            ticking = true;
        }
    }
    
    // Smooth scroll for anchor links
    function smoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault();
                    
                    const headerOffset = 80;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                    
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
    
    // Progress indicator
    function initProgressIndicator() {
        const progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress';
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, var(--global-theme-color), var(--global-hover-color));
            z-index: 9999;
            transition: width 0.1s ease;
        `;
        document.body.appendChild(progressBar);
        
        function updateProgress() {
            const windowHeight = window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight - windowHeight;
            const scrolled = window.scrollY;
            const progress = (scrolled / documentHeight) * 100;
            progressBar.style.width = progress + '%';
        }
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
    }
    
    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        .animate-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .animate-on-scroll.visible {
            opacity: 1;
            transform: translateY(0);
        }
        
        .animate-child {
            opacity: 0;
            transform: translateX(-20px);
            transition: opacity 0.4s ease, transform 0.4s ease;
        }
        
        .animate-child.visible {
            opacity: 1;
            transform: translateX(0);
        }
        
        /* Parallax container */
        .parallax-container {
            position: relative;
            overflow: hidden;
        }
        
        /* Hover lift effect */
        .hover-lift {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .hover-lift:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(107, 70, 193, 0.2);
        }
        
        /* Reveal animation */
        @keyframes reveal {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        .reveal {
            animation: reveal 0.6s ease-out;
        }
    `;
    document.head.appendChild(style);
    
    // Initialize everything when DOM is ready
    function init() {
        initScrollAnimations();
        smoothScroll();
        initProgressIndicator();
        
        // Add parallax data attributes
        const profileImage = document.querySelector('.profile');
        if (profileImage) {
            profileImage.classList.add('parallax');
            profileImage.dataset.speed = '0.3';
        }
        
        // Listen for scroll events
        window.addEventListener('scroll', requestTick);
        
        // Reinitialize on page navigation (for single-page apps)
        if (window.MutationObserver) {
            const observer = new MutationObserver(() => {
                initScrollAnimations();
            });
            
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        }
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();