//Navbar toggle
document.addEventListener("DOMContentLoaded", function () {
  const hamburgerIcon = document.querySelector(".hamburger img");
  const hamburgerMenu = document.querySelector(".hamburger .hemburger-menu");

  hamburgerIcon.addEventListener("click", function () {
      // Toggle the visibility of the menu
      if (hamburgerMenu.style.display === "none" || hamburgerMenu.style.display === "") {
          hamburgerMenu.style.display = "block"; // Show the menu
      } else {
          hamburgerMenu.style.display = "none"; // Hide the menu
      }
  });
});




//Home skills typing 
document.addEventListener("DOMContentLoaded", () => {
    const skillText = document.getElementById("skill-text");
    const skills = ["Python Developer", "Web Developer", "Creative Thinker", "Innovative Coder"]; // Add more skills here
    let currentSkill = 0;
    let charIndex = 0;
    let typingSpeed = 100; // Typing speed in milliseconds
    let erasingSpeed = 50; // Erasing speed in milliseconds
    let delayBetweenSkills = 1500; // Delay before typing the next skill
    
    function typeSkill() {
      if (charIndex < skills[currentSkill].length) {
        skillText.textContent += skills[currentSkill].charAt(charIndex);
        charIndex++;
        setTimeout(typeSkill, typingSpeed);
      } else {
        setTimeout(eraseSkill, delayBetweenSkills);
      }
    }
  
    function eraseSkill() {
      if (charIndex > 0) {
        skillText.textContent = skills[currentSkill].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(eraseSkill, erasingSpeed);
      } else {
        currentSkill = (currentSkill + 1) % skills.length; // Loop through the skills array
        setTimeout(typeSkill, typingSpeed);
      }
    }
  
    // Start the typing effect
    setTimeout(typeSkill, delayBetweenSkills);
  });
  


// Function to toggle the active category within its container
function toggleCategory(element) {
  const container = element.closest('.cards-categories'); // Get the parent container
  const categories = container.querySelectorAll('.category'); // Scope to this container

  // Remove active class from all categories in this container
  categories.forEach(category => category.classList.remove('active'));

  // Add active class to clicked category
  element.classList.add('active');
}


// sort button sort items
document.addEventListener("DOMContentLoaded", () => {
    // Get all buttons and dropdowns
    const sortButtons = document.querySelectorAll(".cards-sort .outline-btn");
  
    sortButtons.forEach((button) => {
      button.addEventListener("click", (event) => {
        const parent = event.target.closest(".cards-sort");
        const dropdown = parent.querySelector(".sort-items");
  
        // Close other open dropdowns
        document.querySelectorAll(".sort-items").forEach((menu) => {
          if (menu !== dropdown) {
            menu.style.display = "none";
          }
        });
  
        // Toggle the visibility of the current dropdown
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
      });
    });
  
    // Close dropdowns when clicking outside
    document.addEventListener("click", (event) => {
      if (!event.target.closest(".cards-sort")) {
        document.querySelectorAll(".sort-items").forEach((menu) => {
          menu.style.display = "none";
        });
      }
    });
  });
  

  //Progreess skill bar
  document.addEventListener("DOMContentLoaded", () => {
    const progressContainers = document.querySelectorAll(".progress-container");

    progressContainers.forEach((container) => {
        const progressValue = container.getAttribute("data-progress");
        const progressBar = container.querySelector(".progress");

        // Ensure the progress value is valid and animate the bar
        if (progressValue && !isNaN(progressValue) && progressValue >= 0 && progressValue <= 100) {
            progressBar.style.width = `${progressValue}%`;
        }
    });
});


// FAQ section
document.addEventListener("DOMContentLoaded", () => {
    const faqCards = document.querySelectorAll(".faq-card");

    faqCards.forEach((card) => {
        const answer = card.querySelector(".answer");
        const toggleIcon = card.querySelector(".faq-toggle");

        toggleIcon.addEventListener("click", () => {
            // Toggle answer visibility
            if (answer.style.display === "none" || !answer.style.display) {
                answer.style.display = "block"; // Show the answer
                toggleIcon.src = "../../static/assets/Icons/close.png"; // Change to "hide" icon
                toggleIcon.alt = "Hide FAQ";
            } else {
                answer.style.display = "none"; // Hide the answer
                toggleIcon.src = "../../static/assets/Icons/open.png"; // Change to "show" icon
                toggleIcon.alt = "Show FAQ";
            }
        });
    });
});


//Hobbies slider
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let carouselDom = document.querySelector('.carousel');
let SliderDom = carouselDom.querySelector('.carousel .list');
let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
let timeDom = document.querySelector('.carousel .time');

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
let timeRunning = 3000;
let timeAutoNext = 7000;

nextDom.onclick = function(){
    showSlider('next');    
}

prevDom.onclick = function(){
    showSlider('prev');    
}
let runTimeOut;
let runNextAuto = setTimeout(() => {
    next.click();
}, timeAutoNext)
function showSlider(type){
    let  SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if(type === 'next'){
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    }else{
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        next.click();
    }, timeAutoNext)
}


//category filter toggle

document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const menuItems = document.getElementById("menu-items");

  menuToggle.addEventListener("click", () => {
      // Toggle the menu's visibility
      menuItems.classList.toggle("open");
  });
});

//helping card js

document.addEventListener("DOMContentLoaded", () => {
  const starRatings = document.querySelectorAll(".star-rating");

  starRatings.forEach(rating => {
      const progress = Math.min(Math.max(parseInt(rating.dataset.progress, 10) || 1, 1), 5);
      for (let i = 0; i < progress; i++) {
          const star = document.createElement("span");
          star.textContent = "⭐"; // Emoji for filled star
          rating.appendChild(star);
      }
      for (let i = progress; i < 5; i++) {
          const emptyStar = document.createElement("span");
          emptyStar.textContent = "☆"; // Emoji for empty star
          rating.appendChild(emptyStar);
      }
  });
});