const button = document.querySelector("#theme-toggle");
const root = document.documentElement;

const savedTheme = localStorage.getItem("theme") || "dark";
root.dataset.theme = savedTheme;

button.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "light" ? "dark" : "light";
    root.dataset.theme = nextTheme;
    localStorage.setItem("theme", nextTheme);
});