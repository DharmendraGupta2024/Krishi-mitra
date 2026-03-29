// custom javascript for Krishi Mitra UI

document.addEventListener("DOMContentLoaded", function() {
    // Back to top button logic
    const backToTopBtn = document.getElementById("backToTopBtn");
    
    if (backToTopBtn) {
        window.addEventListener("scroll", function() {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add("show");
            } else {
                backToTopBtn.classList.remove("show");
            }
        });

        backToTopBtn.addEventListener("click", function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }
});