const button = document.querySelector("#theme-toggle");
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
    // WAVES' `zoom` option adjusts mouse parallax, not the initial framing.
    zoom: 1,
    color: savedTheme === "light" ? 0x90b6d5 : 0x060A0F
});

// Tighten the camera framing on initial load without changing canvas resolution.
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

