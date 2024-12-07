// FAQ Toggle
document.querySelectorAll('.faq-card').forEach(card => {
    card.addEventListener('click', () => {
        const answer = card.querySelector('p');
        const showIcon = card.querySelector('.show-faq');
        const hideIcon = card.querySelector('.hide-faq');

        if (answer && showIcon && hideIcon) {
            if (answer.style.display === 'none' || answer.style.display === '') {
                answer.style.display = 'block'; // Show the answer
                showIcon.style.display = 'none'; // Hide the plus icon
                hideIcon.style.display = 'block'; // Show the minus icon
            } else {
                answer.style.display = 'none'; // Hide the answer
                showIcon.style.display = 'block'; // Show the plus icon
                hideIcon.style.display = 'none'; // Hide the minus icon
            }
        }
    });
});

// Typing Effect for Skills
const skills = [
    "Python Developer",
    "Web Developer",
    "Machine Learning Enthusiast",
    "Data Scientist",
    "AI Engineer",
    "Frontend Developer",
    "Backend Developer"
];

const skillText = document.getElementById("skill-text");

if (skillText) {
    let skillIndex = 0;
    let charIndex = 0;
    let typingSpeed = 150;  // Speed of typing in milliseconds
    let deletingSpeed = 100;  // Speed of deleting
    let delayBetweenSkills = 1000;  // Delay before starting to delete
    let isDeleting = false;  // Track if we are deleting text

    function typeSkill() {
        const currentSkill = skills[skillIndex];

        if (!isDeleting) {
            skillText.textContent = currentSkill.slice(0, charIndex + 1);
            charIndex++;
            if (charIndex === currentSkill.length) {
                setTimeout(() => isDeleting = true, delayBetweenSkills);
            }
        } else {
            skillText.textContent = currentSkill.slice(0, charIndex - 1);
            charIndex--;
            if (charIndex === 0) {
                isDeleting = false;
                skillIndex = (skillIndex + 1) % skills.length;
            }
        }

        const speed = isDeleting ? deletingSpeed : typingSpeed;
        setTimeout(typeSkill, speed);
    }

    typeSkill();
}

// Dropdown Toggle
const selectBtn = document.querySelector(".dropdown");
const dropBox = document.querySelector(".list");
const arrow = document.querySelector(".arrow");
const options = document.querySelectorAll(".item");
const selectText = document.querySelector(".select");

if (selectBtn && dropBox && arrow && options.length && selectText) {
    let isDropBoxVisible = false;

    selectBtn.addEventListener("click", () => {
        if (!isDropBoxVisible) {
            dropBox.style.display = "block";
            arrow.style.transform = "rotate(180deg)";
        } else {
            dropBox.style.display = "none";
            arrow.style.transform = "rotate(0deg)";
        }
        isDropBoxVisible = !isDropBoxVisible;
    });

    options.forEach(option => {
        option.addEventListener("click", () => {
            const selectOption = option.querySelector("span").innerText;
            selectText.innerText = selectOption;
            arrow.style.transform = "rotate(0deg)";
            dropBox.style.display = "none";
            isDropBoxVisible = false;
        });
    });
}
