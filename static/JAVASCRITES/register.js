let icon1 = document.getElementById('icon1')
let password = document.getElementById('password')
icon1.onclick = function () {
    if (password.type == 'password') {
        password.type = 'text';
        icon1.classList = 'fa-solid fa-eye';
    }
    else {
        password.type = 'password';
        icon1.classList = 'fa-solid fa-eye-slash';
    };
};
let icon2 = document.getElementById('icon2')
let conformpassword = document.getElementById('conformpassword')
icon2.onclick = function () {
    if (conformpassword.type == 'password') {
        conformpassword.type = 'text';
        icon2.classList = 'fa-solid fa-eye';
    }
    else {
        conformpassword.type = 'password';
        icon2.classList = 'fa-solid fa-eye-slash';
    };
};

function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById('preview');
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
    }
}