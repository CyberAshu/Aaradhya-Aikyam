document.addEventListener("DOMContentLoaded", function() {
    // Intersection Observer for fade-in animation on scroll
    const sections = document.querySelectorAll(".section");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in"); // Add animation class when in view
            } else {
                entry.target.classList.remove("fade-in"); // Optional: remove on exit
            }
        });
    }, {
        threshold: 0.1 // Adjust this threshold as needed
    });

    sections.forEach(section => {
        observer.observe(section); // Observe each section
    });

    // Shrink navbar on scroll
    const header = document.querySelector('header');
    const shrinkOn = 50; // Scroll distance to toggle navbar style

    // Initially set the navbar as solid
    header.classList.remove('transparent');

    window.addEventListener('scroll', function() {
        if (window.scrollY > shrinkOn) {
            header.classList.add('transparent'); // Add transparent class for semi-transparent background
        } else {
            header.classList.remove('transparent'); // Remove transparent class for solid background
        }
    });

    // For the "See More" button functionality
    const toggleBtn = document.getElementById("seeMoreBtn");
    const hiddenItems = document.querySelectorAll(".portfolio-item.hidden");

    if (toggleBtn) {
        toggleBtn.addEventListener("click", function() {
            hiddenItems.forEach(item => {
                item.classList.toggle("hidden");
                if (!item.classList.contains("hidden")) {
                    item.classList.add("fade-in");
                    setTimeout(() => item.classList.remove("fade-in"), 600); // Remove class after animation
                }
            });
            toggleBtn.textContent = toggleBtn.textContent === "See More" ? "See Less" : "See More";
        });
    }

    document.getElementById('menu-toggle').addEventListener('click', function () {
        const navLinks = document.getElementById('nav-links');
        const sidebar = document.getElementById('sidebar');
    
        // Toggle the visibility of the nav-links and sidebar
        navLinks.style.display = (navLinks.style.display === 'block' ? 'none' : 'block');
        sidebar.style.display = (sidebar.style.display === 'block' ? 'none' : 'block');
    });
    

    // Hamburger menu and sidebar functionality
    const menuToggle = document.getElementById("menu-toggle");
    const sidebar = document.getElementById("sidebar");

    if (menuToggle && sidebar) {
        menuToggle.addEventListener("click", () => {
            sidebar.classList.toggle("active");
            menuToggle.classList.toggle("active");
        });

        // Close sidebar when clicking outside of it
        document.addEventListener("click", (event) => {
            if (!sidebar.contains(event.target) && !menuToggle.contains(event.target) && sidebar.classList.contains("active")) {
                sidebar.classList.remove("active");
                menuToggle.classList.remove("active");
            }
        });
    }
});
