
document.querySelectorAll('.alert').forEach((el, index) => {
    setTimeout(() => {
        el.style.animation = "slideOut 0.3s ease forwards";

        setTimeout(() => {
            el.remove();
        }, 300);

    }, 3000 + (index * 200)); // stagger effect
});