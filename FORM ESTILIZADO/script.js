document.addEventListener("DOMContentLoaded", function() {

    const form = document.getElementById("form");

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        alert("Enviado com sucesso!");
    });
    
});