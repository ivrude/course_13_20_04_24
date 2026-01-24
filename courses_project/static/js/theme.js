document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector(".tdnn");
    const moon = document.querySelector(".moon");

    // ініціалізація з localStorage
    if (localStorage.getItem("theme") === "light") {
        document.body.classList.add("light");
        toggle.classList.add("day");
        moon.classList.add("sun");
    }

    toggle.addEventListener("click", () => {
        document.body.classList.toggle("light");
        toggle.classList.toggle("day");
        moon.classList.toggle("sun");

        // зберегти вибір користувача
        const theme = document.body.classList.contains("light") ? "light" : "dark";
        localStorage.setItem("theme", theme);
    });
});
