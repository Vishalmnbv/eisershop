let icon4 = document.getElementById('icon4')
let new_password = document.getElementById('new_password')
icon4.onclick = function () {
    if (new_password.type == 'password') {
        new_password.type = 'text';
        icon4.classList = 'fa-solid fa-eye';
    }
    else {
        new_password.type = 'password';
        icon4.classList = 'fa-solid fa-eye-slash';
    };
};
let icon5 = document.getElementById('icon5')
let confirm_password = document.getElementById('confirm_password')
icon5.onclick = function () {
    if (confirm_password.type == 'password') {
        confirm_password.type = 'text';
        icon5.classList = 'fa-solid fa-eye';
    }
    else {
        confirm_password.type = 'password';
        icon5.classList = 'fa-solid fa-eye-slash';
    };
};