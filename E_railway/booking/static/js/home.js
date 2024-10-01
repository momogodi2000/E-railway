// JavaScript for responsive adjustments and UI interactions

document.addEventListener('DOMContentLoaded', function () {
    // Navbar toggle
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function () {
        navbarCollapse.classList.toggle('show');
    });

    // Scroll to top button (example functionality, add button in HTML if needed)
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.innerText = '↑';
    scrollTopBtn.classList.add('btn', 'btn-primary', 'scroll-top-btn');
    document.body.appendChild(scrollTopBtn);

    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            scrollTopBtn.style.display = 'block';
        } else {
            scrollTopBtn.style.display = 'none';
        }
    });

    scrollTopBtn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
