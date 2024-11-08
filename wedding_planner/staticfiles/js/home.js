    document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll(".section"); // Select all sections

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

// scripts.js
// scripts.js
document.addEventListener("DOMContentLoaded", function() {
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
});


    // For the "See More" button functionality
    const toggleBtn = document.getElementById("seeMoreBtn");
    const hiddenItems = document.querySelectorAll(".portfolio-item.hidden");

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
  });
