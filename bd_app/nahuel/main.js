// scripts para manejar el modal
var modal = document.getElementById('modal__agregar');
var btnModal = document.getElementById('btn-2');
var btnCerrar = document.getElementsByClassName("btn-cerrar")[0];

btnModal.addEventListener('click', () => {
    modal.style.display = 'block'
});

btnCerrar.addEventListener('click', () => {
    modal.style.display = 'none'
});