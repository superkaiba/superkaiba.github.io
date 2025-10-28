// Minimal script
// No navigation needed since we have a single-page layout

document.addEventListener('DOMContentLoaded', function() {
    // Update footer year if element exists
    const yearElement = document.getElementById('year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
});
