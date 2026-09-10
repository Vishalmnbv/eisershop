const stars = document.querySelectorAll(".rating-star");
const ratingInput = document.getElementById("rating");
stars.forEach((star) => {
    star.addEventListener("click", function () {
        let value = this.dataset.value;
        ratingInput.value = value;
        stars.forEach((s) => {
            if (s.dataset.value <= value) {
                s.classList.remove("fa-regular");
                s.classList.add("fa-solid", "text-warning");
            }
            else {
                s.classList.remove("fa-solid");
                s.classList.add("fa-regular");
            }
        });
    });
});