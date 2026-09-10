document.addEventListener("DOMContentLoaded", function () {
    const radios = document.querySelectorAll('input[name="selected_size"]');
    const hidden = document.getElementById("selected_size");
    function updateSize() {
        const checked = document.querySelector('input[name="selected_size"]:checked');
        if (checked) {
            hidden.value = checked.value;
        }
    }
    updateSize();
    radios.forEach(function (radio) {
        radio.addEventListener("change", updateSize);
    });
});