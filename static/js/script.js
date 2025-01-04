document.addEventListener("DOMContentLoaded", function () {
    const toastElements = document.querySelectorAll('.toast');
    toastElements.forEach(toastElement => {
        const toast = new bootstrap.Toast(toastElement);
        toast.show();
    });
});