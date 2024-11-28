document.querySelectorAll('.faq-card').forEach(card => {
    card.addEventListener('click', () => {
        const answer = card.querySelector('p');
        const showIcon = card.querySelector('.show-faq');
        const hideIcon = card.querySelector('.hide-faq');
        
        if (answer.style.display === 'none' || answer.style.display === '') {
            answer.style.display = 'block'; // Show the answer
            showIcon.style.display = 'none'; // Hide the plus icon
            hideIcon.style.display = 'block'; // Show the minus icon
        } else {
            answer.style.display = 'none'; // Hide the answer
            showIcon.style.display = 'block'; // Show the plus icon
            hideIcon.style.display = 'none'; // Hide the minus icon
        }
    });
});

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

let skillIndex = 0;
let charIndex = 0;
let typingSpeed = 150;  // Speed of typing in milliseconds
let deletingSpeed = 100;  // Speed of deleting
let delayBetweenSkills = 1000;  // Delay before starting to delete
let isDeleting = false;  // Track if we are deleting text

function typeSkill() {
    const currentSkill = skills[skillIndex];
    
    if (!isDeleting) {
        // Typing logic: add one letter at a time
        skillText.textContent = currentSkill.slice(0, charIndex + 1);
        charIndex++;
        
        // If the entire skill is typed out, wait and then start deleting
        if (charIndex === currentSkill.length) {
            setTimeout(() => {
                isDeleting = true;
            }, delayBetweenSkills);  // Wait before starting deletion
        }
    } else {
        // Deleting logic: remove one letter at a time
        skillText.textContent = currentSkill.slice(0, charIndex - 1);
        charIndex--;
        
        // If the skill is fully deleted, move to the next skill
        if (charIndex === 0) {
            isDeleting = false;
            skillIndex = (skillIndex + 1) % skills.length;  // Loop through skills
        }
    }
    
    // Adjust the speed depending on whether we're typing or deleting
    const speed = isDeleting ? deletingSpeed : typingSpeed;
    
    // Recursively call this function after the determined speed
    setTimeout(typeSkill, speed);
}

// Start the typing effect
typeSkill();



const selectBtn = document.querySelector(".dropdown")
const dropBox = document.querySelector(".list")
const arrow = document.querySelector(".arrow")

const options = document.querySelectorAll(".item")
const selectText = document.querySelector(".select")


let isDropBoxVisible = false;

selectBtn.addEventListener("click", ()=> {
    if(!isDropBoxVisible) {
        dropBox.style.display = "block";
        arrow.style.transform = "rotate(180deg)"
    }
    else{
        dropBox.style.display = "none";
        arrow.style.transform = "rotate(0deg)"

    }
    isDropBoxVisible = !isDropBoxVisible;
})

options.forEach((option)=> {
    option.addEventListener("click", () => {
        let selectOption = option.querySelector("span").innerText;
        selectText.innerText = selectOption;
        arrow.style.transform = "rotate(0deg)";

        dropBox.style.display="none";
        isDropBoxVisible = false;

        // console.log(selectOption)
    })

})