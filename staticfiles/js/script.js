// Function to handle navbar color change on scroll
function handleNavbarScroll() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.remove('bg-transparent');
        navbar.classList.add('bg-white');
    } else {
        navbar.classList.remove('bg-white');
        navbar.classList.add('bg-transparent');
    }
}

// Event listener for scroll
window.addEventListener('scroll', function() {
    handleNavbarScroll();
});

// Event listeners for hover
var navbar = document.getElementById('navbar');
navbar.addEventListener('mouseenter', function() {
    navbar.classList.remove('bg-transparent');
    navbar.classList.add('bg-white');
});

navbar.addEventListener('mouseleave', function() {
    handleNavbarScroll(); // Revert to scroll behavior
});
