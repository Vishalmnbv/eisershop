function handlePayment() {
    const cod = document.getElementById('cod');
    const upi = document.getElementById('upi');
    const card = document.getElementById('card');
    const upiField = document.getElementById('upi-field');
    const cardField = document.getElementById('card-field');
    const upiInput = document.getElementById('upi_id');
    const cardInputs = [
        document.getElementById('cardnumber'),
        document.getElementById('month'),
        document.getElementById('year'),
        document.getElementById('cvv')
    ];
    if (cod.checked) {
        upiField.classList.add('d-none');
        cardField.classList.add('d-none');
        upiInput.removeAttribute('required');
        cardInputs.forEach(input => input.removeAttribute('required'));
    }
    else if (upi.checked) {
        upiField.classList.remove('d-none');
        cardField.classList.add('d-none');
        upiInput.setAttribute('required', 'required');
        cardInputs.forEach(input => input.removeAttribute('required'));
    }
}
function checkPhone() {
    let phoneInput = document.getElementById('number');
    phoneInput.value = phoneInput.value.replace(/[^0-9]/g, ''); // Sirf numbers allow karein
}
function checkUPI() {
    
}
