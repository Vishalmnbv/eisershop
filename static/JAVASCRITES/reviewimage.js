document.getElementById("imageInput").addEventListener("change", function () {
    const file = this.files[0];
    const preview = document.getElementById("previewImage");
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.classList.remove("d-none");
        };
        reader.readAsDataURL(file);
    }
    else {
        preview.src = "";
        preview.classList.add("d-none");
    }
});