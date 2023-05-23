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

$(".open-btn").on("click", function () {
    $(".sidebar").addClass("active");
});
$(".close-btn").on("click", function () {
    $(".sidebar").removeClass("active");
});
var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});
function showLanguageSelectors() {
    var textarea = document.querySelector('textarea[name="file_content"]');
    var languageSelectors = document.getElementById("languageSelectors");
    if (textarea.value.trim() !== "") {
        languageSelectors.style.display = "block";
    } else {
        languageSelectors.style.display = "none";
    }
}
document.addEventListener("DOMContentLoaded", function () {
    showLanguageSelectors();
});

$(".sidebar ul li").on("click", function () {
    $(".sidebar ul li.active").removeClass("active");
    $(this).addClass("active");
});
$(".open-btn").on("click", function () {
    $(".sidebar").addClass("active");
});
$(".close-btn").on("click", function () {
    $(".sidebar").removeClass("active");
});
function changeFontSize(change) {
    var paragraphs = document.getElementsByTagName("p");
    for (var i = 0; i < paragraphs.length; i++) {
        var currentSize = parseFloat(
            window.getComputedStyle(paragraphs[i]).fontSize
        );
        var newSize = currentSize + parseFloat(change);
        paragraphs[i].style.fontSize = newSize + "px";
    }
}
