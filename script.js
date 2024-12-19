// Modal öğelerini seç
const modal = document.getElementById("image-modal");
const modalImg = document.getElementById("modal-image");
const captionText = document.getElementById("caption");
const closeModal = document.querySelector(".close");

// Tüm zoom yapılabilir resimleri seç
const images = document.querySelectorAll(".zoomable");

// Resimlere tıklama olayını bağla
images.forEach(image => {
    image.addEventListener("click", () => {
        modal.style.display = "block";
        modalImg.src = image.src;
        captionText.innerText = image.alt;
    });
});

// Kapatma simgesine tıklanınca modalı gizle
closeModal.addEventListener("click", () => {
    modal.style.display = "none";
});
