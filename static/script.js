var uploadArea = document.getElementById("uploadArea");
var uploadForm = document.getElementById("uploadForm");
var fileInput = document.getElementById("fileInput");

// Manejador de eventos para cuando se arrastra un archivo sobre el área
uploadArea.addEventListener("dragover", function (e) {
    e.preventDefault();
    uploadArea.classList.add("dragover");
});

// Manejador de eventos para cuando se sale del área de arrastre
uploadArea.addEventListener("dragleave", function (e) {
    e.preventDefault();
    uploadArea.classList.remove("dragover");
});

// Manejador de eventos para cuando se suelta el archivo en el área
uploadArea.addEventListener("drop", function (e) {
    e.preventDefault();
    uploadArea.classList.remove("dragover");

    // Obtener el archivo arrastrado
    var file = e.dataTransfer.files[0];
    fileInput.files = e.dataTransfer.files;

    // Enviar el formulario para redirigir al cliente al endpoint en Flask
    uploadForm.submit();
});

// Manejador de eventos para cuando se hace clic en el área para seleccionar un archivo
uploadArea.addEventListener("click", function () {
    fileInput.click();
});

// Manejador de eventos para cuando se selecciona un archivo
fileInput.addEventListener("change", function () {
    // Enviar el formulario para redirigir al cliente al endpoint en Flask
    uploadForm.submit();
});
