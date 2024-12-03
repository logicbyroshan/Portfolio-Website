const songs = [
    {
        title: "Humble Poet",
        artist: "Bella",
        cover: "assets/Hobbies/Songs/Humble Poet cover.jpg",
        src: "assets/Hobbies/Songs/Humble Poet.mp3",
    },
    {
        title: "Pehli Pehli Baar Jab Pyar Kisi Se Hota Hai",
        artist: "Kumar Sanu",
        cover: "assets/Hobbies/Songs/Pehli Pehli Bar Cover.jpg",
        src: "assets/Hobbies/Songs/Pehli Pehli Baar Jab Jab Pyaar Kisise Hota Hai .mp3",
    },
    {
        title: "Tere Ho Ke",
        artist: "King X Bella",
        cover: "assets/Hobbies/Songs/Tere Hoke cover.jpg",
        src: "assets/Hobbies/Songs/Tere Ho Ke.mp3",
    },
];
let currentIndex = 0;
let isLooping = false;
let isRandom = false;

// DOM Elements
const songTitle = document.getElementById("song-title");
const songArtist = document.getElementById("song-artist");
const songCover = document.getElementById("song-cover");
const audio = new Audio(songs[currentIndex].src);
const playPauseBtn = document.getElementById("play-pause-btn");
const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");
const loopBtn = document.getElementById("loop-btn");
const randomBtn = document.getElementById("random-btn");

// Update Song Info
function updateSong() {
    audio.src = songs[currentIndex].src;
    songTitle.textContent = songs[currentIndex].title;
    songArtist.textContent = songs[currentIndex].artist;
    songCover.src = songs[currentIndex].cover;
    audio.play();
}
// Play/Pause Functionality
playPauseBtn.addEventListener("click", () => {
    const playPauseIcon = playPauseBtn.querySelector("img"); // Assuming the button contains an <img>
    
    if (audio.paused) {
        audio.play();
        playPauseIcon.src = "assets/Icons/pause.png"; // Path to your play icon
    } else {
        audio.pause();
        playPauseIcon.src = "assets/Icons/play.png"; // Path to your pause icon
    }
});


// Next Song
nextBtn.addEventListener("click", () => {
    if (isRandom) {
        currentIndex = Math.floor(Math.random() * songs.length);
    } else {
        currentIndex = (currentIndex + 1) % songs.length;
    }
    updateSong();
});

// Previous Song
prevBtn.addEventListener("click", () => {
    currentIndex = (currentIndex - 1 + songs.length) % songs.length;
    updateSong();
});

// Loop Toggle
loopBtn.addEventListener("click", () => {
    isLooping = !isLooping;
    loopBtn.style.color = isLooping ? "#00FF00" : "white"; // Change color to indicate loop is on
    audio.loop = isLooping;
});

// Random Toggle
randomBtn.addEventListener("click", () => {
    isRandom = !isRandom;
    randomBtn.style.color = isRandom ? "#00FF00" : "white"; // Change color to indicate random is on
});

// Automatically Play Next Song
audio.addEventListener("ended", () => {
    if (!isLooping) {
        nextBtn.click();
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const sliders = document.querySelectorAll(".photo-slider");

    sliders.forEach((slider) => {
        const images = slider.querySelectorAll("img");
        let currentIndex = 0;

        function showNextImage() {
            images[currentIndex].classList.remove("active");
            currentIndex = (currentIndex + 1) % images.length;
            images[currentIndex].classList.add("active");
        }

        // Initialize the first image as active
        images[currentIndex].classList.add("active");

        // Start the slideshow for this slider
        setInterval(showNextImage, 3000);
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const creativeImages = document.querySelectorAll(".creative-product img");
    const diyImages = document.querySelectorAll(".diy-card .creative-product img");
    const clayartImages = document.querySelectorAll(".clayart-card .creative-product img");
    const artisticImages = document.querySelectorAll(".artistic-card .creative-product img");

    let currentCreativeIndex = 0;
    let currentDIYIndex = 0;
    let currentClayartIndex = 0;
    let currentArtisticIndex = 0;

    function showNextImage(images, currentIndex) {
        images[currentIndex].classList.remove("active");
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].classList.add("active");
        return currentIndex;
    }

    // Initialize sliders
    creativeImages[currentCreativeIndex].classList.add("active");
    diyImages[currentDIYIndex].classList.add("active");
    clayartImages[currentClayartIndex].classList.add("active");
    artisticImages[currentArtisticIndex].classList.add("active");

    // Set intervals for each slider
    setInterval(() => {
        currentCreativeIndex = showNextImage(creativeImages, currentCreativeIndex);
    }, 3000);

    setInterval(() => {
        currentDIYIndex = showNextImage(diyImages, currentDIYIndex);
    }, 3000);

    setInterval(() => {
        currentClayartIndex = showNextImage(clayartImages, currentClayartIndex);
    }, 3000);

    setInterval(() => {
        currentArtisticIndex = showNextImage(artisticImages, currentArtisticIndex);
    }, 3000);
});
