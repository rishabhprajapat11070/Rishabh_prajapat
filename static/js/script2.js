// Fade-in Reveal Logic
const revealElements = document.querySelectorAll('.reveal');

const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, {
    threshold: 0.1
});

revealElements.forEach(el => {
    scrollObserver.observe(el);
});

// Trigger Hero animation immediately
window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        document.querySelector('section.h-screen .reveal').classList.add('active');
    }, 100);
});

// Navigation Link Smooth Scroll Offset
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        const navHeight = 52;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;

        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    });
});

window.addEventListener('DOMContentLoaded', () => {
    const title = document.querySelector('.reveal-title');
    const description = document.querySelector('.hero-description');
    const group = document.querySelector('.reveal-group');

    // 1. Show Title (100ms)
    setTimeout(() => {
        title.classList.add('reveal-active');
    }, 100);

    // 2. Show Description (400ms)
    setTimeout(() => {
        description.classList.add('reveal-active');
    }, 400);

    // 3. Show Buttons & Socials (700ms)
    setTimeout(() => {
        group.classList.add('reveal-active');
    }, 700);
});