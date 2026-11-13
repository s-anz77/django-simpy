const button = document.querySelector(".theme-toggle1");
const button2 = document.querySelector(".theme-toggle2");

const root = document.documentElement;

const savedTheme = localStorage.getItem("theme") || "dark";
root.dataset.theme = savedTheme;

const waves = VANTA.WAVES({
    el: "#header",
    mouseControls: false,
    touchControls: true,
    gyroControls: false,
    minHeight: 80.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    waveHeight: 40,
    zoom: 1,
    color: savedTheme === "dark" ? 0x060A0F : 0x90b6d5 
});

waves.camera.zoom = 2;
waves.camera.updateProjectionMatrix();

button.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "light" ? "dark" : "light";
    root.dataset.theme = nextTheme;
    localStorage.setItem("theme", nextTheme);

    waves.setOptions({
        color: nextTheme === "light" ? 0x90b6d5 : 0x060A0F
    });
});

button2.addEventListener("click", () => {
    const nextTheme = root.dataset.theme === "light" ? "dark" : "light";
    root.dataset.theme = nextTheme;
    localStorage.setItem("theme", nextTheme);

    waves.setOptions({
        color: nextTheme === "light" ? 0x90b6d5 : 0x060A0F
    });
});

// Выдвижная панель

const menuButton = document.querySelector("#menubut");
const hiddenBar = document.querySelector('.hiddenbar')

menuButton.addEventListener('click', () => {
    const isOpen = hiddenBar.classList.toggle("menu-open");
    hiddenBar.classList.toggle("activebar", isOpen);
})