let icon3 = document.getElementById('icon3');
let psw = document.getElementById('psw');
icon3.onclick = function () {
    if (psw.type == 'password') {
        psw.type = 'text';
        icon3.classList = 'fa-solid fa-eye';
    }
    else {
        psw.type = 'password';
        icon3.classList = 'fa-solid fa-eye-slash';
    };
};