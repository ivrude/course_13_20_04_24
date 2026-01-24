console.log("JS LOADED");

document.addEventListener("DOMContentLoaded", () => {

    // плавне зʼявлення сторінки
    document.body.classList.add("fade-in");
    setTimeout(() => {
        document.body.classList.add("show");
    }, 100);

    // підсвітка рядка при + / -
    document.querySelectorAll("a[href*='inc'], a[href*='dec']").forEach(btn => {
        btn.addEventListener("click", () => {
            const row = btn.closest("tr");
            if (!row) return;

            row.classList.add("table-info");
            setTimeout(() => {
                row.classList.remove("table-info");
            }, 600);
        });
    });

    // loading при submit
    document.querySelectorAll("form").forEach(form => {
        form.addEventListener("submit", () => {
            const btn = form.querySelector("button[type=submit]");
            if (btn) {
                btn.innerHTML = "⏳ Зачекайте...";
                btn.disabled = true;
            }
        });
    });

    // fade-in при скролі
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    });

    document.querySelectorAll(".fade-in").forEach(el => observer.observe(el));
});

document.querySelectorAll(".js-loading").forEach(link => {
    link.addEventListener("click", function () {
        this.innerHTML = "⏳ Додаємо...";
        this.classList.add("disabled");
    });
});
