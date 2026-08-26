/**
 * Antigravity Core Portfolio JavaScript Module
 * Clean, centralized event listeners and interactive controllers
 */

document.addEventListener("DOMContentLoaded", function () {
    // --------------------------------------------------------------------------
    // 1. Mobile Navigation Drawer Controls
    // --------------------------------------------------------------------------
    const mobileToggle = document.getElementById("mobile-toggle");
    const mobileClose = document.getElementById("mobile-close");
    const mobilePanel = document.getElementById("mobile-panel");
    const mobileOverlay = document.getElementById("mobile-overlay");

    window.openMobileNav = function () {
        if (!mobilePanel || !mobileOverlay) return;
        mobilePanel.classList.add("active");
        mobileOverlay.classList.add("active");
        document.body.classList.add("popup-open");
    };

    window.closeMobileNav = function () {
        if (!mobilePanel || !mobileOverlay) return;
        mobilePanel.classList.remove("active");
        mobileOverlay.classList.remove("active");
        document.body.classList.remove("popup-open");
    };

    window.toggleMobileNav = function (e) {
        if (e && e.preventDefault) e.preventDefault();
        if (!mobilePanel) return;
        if (mobilePanel.classList.contains("active")) {
            window.closeMobileNav();
        } else {
            window.openMobileNav();
        }
    };

    if (mobileToggle) {
        mobileToggle.addEventListener("click", window.toggleMobileNav);
    }
    if (mobileClose) {
        mobileClose.addEventListener("click", window.closeMobileNav);
    }
    if (mobileOverlay) {
        mobileOverlay.addEventListener("click", window.closeMobileNav);
    }

    // Auto-close mobile drawer when any link is clicked
    document.querySelectorAll(".mobile-nav-links a").forEach(link => {
        link.addEventListener("click", window.closeMobileNav);
    });

    // --------------------------------------------------------------------------
    // 2. Global Resume PDF Modal Controls
    // --------------------------------------------------------------------------
    window.openPopup = function () {
        const popup = document.getElementById("popup");
        if (popup) {
            popup.style.display = "block";
            document.body.classList.add("popup-open");
        }
    };

    window.closePopup = function () {
        const popup = document.getElementById("popup");
        if (popup) {
            popup.style.display = "none";
            document.body.classList.remove("popup-open");
        }
    };

    // --------------------------------------------------------------------------
    // 3. Skill Popups (Certificates & Video Resources)
    // --------------------------------------------------------------------------
    window.showSkillPopup = function (popupId) {
        const popup = document.getElementById(popupId);
        if (popup) {
            popup.style.display = "block";
            document.body.classList.add("popup-open");
        }
    };

    window.closeSkillPopup = function (popupId) {
        const popup = document.getElementById(popupId);
        if (popup) {
            popup.style.display = "none";
            document.body.classList.remove("popup-open");
        }
    };

    // --------------------------------------------------------------------------
    // 4. Outside-Click and Escape-Key Dismissal Listeners
    // --------------------------------------------------------------------------
    window.addEventListener("click", function (e) {
        // Resume Modal Backdrop Click
        const resumePopup = document.getElementById("popup");
        if (resumePopup && e.target === resumePopup) {
            window.closePopup();
        }

        // Skill Modal Backdrops Click
        document.querySelectorAll(".skill-popup-overlay").forEach(overlay => {
            if (e.target === overlay) {
                window.closeSkillPopup(overlay.id);
            }
        });

        // Custom Sort Dropdown Outside Click
        const sortDropdown = document.getElementById("sortDropdown");
        const sortBtn = document.getElementById("sortBtn") || document.querySelector(".sort-trigger-btn") || document.querySelector(".sort-btn");
        if (sortDropdown && sortBtn && !sortBtn.contains(e.target) && !sortDropdown.contains(e.target)) {
            sortDropdown.style.display = "none";
            sortBtn.classList.remove("active");
        }
    });

    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
            window.closePopup();
            window.closeMobileNav();
            document.querySelectorAll('.skill-popup-overlay[style*="block"]').forEach(p => {
                window.closeSkillPopup(p.id);
            });
            const sortDropdown = document.getElementById("sortDropdown");
            if (sortDropdown) sortDropdown.style.display = "none";
        }
    });

    // --------------------------------------------------------------------------
    // 5. Search & Sort Filter Actions
    // --------------------------------------------------------------------------
    window.toggleSortDropdown = function () {
        const dropdown = document.getElementById("sortDropdown");
        const sortBtn = document.getElementById("sortBtn") || document.querySelector(".sort-trigger-btn") || document.querySelector(".sort-btn");
        if (!dropdown) return;
        const isVisible = dropdown.style.display === "block";
        dropdown.style.display = isVisible ? "none" : "block";
        sortBtn?.classList.toggle("active", !isVisible);
    };

    window.clearSearch = function () {
        const searchInput = document.querySelector(".search-input");
        const form = document.querySelector(".search-form") || searchInput?.closest("form");
        if (searchInput) searchInput.value = "";
        form?.submit();
    };

    // --------------------------------------------------------------------------
    // 6. Typing Effect on Hero Section (Software Engineer only)
    // --------------------------------------------------------------------------
    const skillText = document.getElementById("skill-text");
    if (skillText) {
        const textToType = "Software Engineer";
        let charIndex = 0;
        let isDeleting = false;

        function typeSkill() {
            if (!skillText) return;
            if (!isDeleting && charIndex <= textToType.length) {
                skillText.textContent = textToType.substring(0, charIndex++);
                setTimeout(typeSkill, 90);
            } else if (!isDeleting && charIndex > textToType.length) {
                setTimeout(() => { isDeleting = true; typeSkill(); }, 3000);
            } else if (isDeleting && charIndex >= 0) {
                skillText.textContent = textToType.substring(0, charIndex--);
                setTimeout(typeSkill, 45);
            } else {
                isDeleting = false;
                charIndex = 0;
                setTimeout(typeSkill, 600);
            }
        }

        skillText.textContent = "";
        setTimeout(typeSkill, 400);
    }

    // --------------------------------------------------------------------------
    // 7. Interactive Accordion for FAQs
    // --------------------------------------------------------------------------
    document.querySelectorAll(".faq-card").forEach(card => {
        const answer = card.querySelector(".answer") || card.querySelector(".card-desc");
        const toggleIcon = card.querySelector(".faq-toggle");

        if (!answer || !toggleIcon) return;

        const openIcon = toggleIcon.dataset.openIcon || toggleIcon.src;
        const closeIcon = toggleIcon.dataset.closedIcon || toggleIcon.src;

        card.addEventListener("click", function () {
            const isVisible = answer.classList.toggle("visible");
            card.classList.toggle("active", isVisible);
            
            if (isVisible) {
                toggleIcon.classList.add("rotated");
                if (closeIcon) toggleIcon.src = closeIcon;
            } else {
                toggleIcon.classList.remove("rotated");
                if (openIcon) toggleIcon.src = openIcon;
            }
        });
    });

    // --------------------------------------------------------------------------
    // 8. Progress Bars Initialization
    // --------------------------------------------------------------------------
    document.querySelectorAll(".progress-container").forEach(container => {
        const progressBar = container.querySelector(".progress") || container.querySelector(".skill-progress-fill");
        const progressValue = container.dataset.progress;

        if (progressBar && !isNaN(progressValue) && progressValue >= 0 && progressValue <= 100) {
            progressBar.style.width = `${progressValue}%`;
        }
    });

    // --------------------------------------------------------------------------
    // 9. Mobile Footer Accordion Toggles
    // --------------------------------------------------------------------------
    document.querySelectorAll(".foot-nav-head").forEach(header => {
        header.addEventListener("click", function () {
            const list = this.parentElement.querySelector("ul");
            const toggle = this.querySelector(".dropdown-toggle");
            list?.classList.toggle("active");
            toggle?.classList.toggle("active");
        });
    });

    // --------------------------------------------------------------------------
    // 10. Project Showcase Image Slider
    // --------------------------------------------------------------------------
    let currentSlideIndex = 0;
    
    window.nextSliderSlide = function () {
        const slider = document.querySelector(".hero-image-slider .slider");
        const slides = document.querySelectorAll(".hero-image-slider .slide");
        if (!slider || slides.length <= 1) return;
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        slider.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
    };

    window.prevSliderSlide = function () {
        const slider = document.querySelector(".hero-image-slider .slider");
        const slides = document.querySelectorAll(".hero-image-slider .slide");
        if (!slider || slides.length <= 1) return;
        currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        slider.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
    };
});
