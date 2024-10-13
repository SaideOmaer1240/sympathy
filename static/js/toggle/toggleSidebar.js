function toggleSidebar() {
    var sidebar = document.querySelector(".sidebar");
    var menuTextItems = document.querySelectorAll('.menu-text');
    if (sidebar.classList.contains("-translate-x-full")) {
        gsap.to(sidebar, { x: 0, duration: 0.5, ease: "power2.out" });
        sidebar.classList.remove("-translate-x-full");
        // Exibir o texto
        menuTextItems.forEach(item => item.classList.remove('hidden'));
    } else {
        gsap.to(sidebar, { x: -256, duration: 0.5, ease: "power2.in" });
        sidebar.classList.add("-translate-x-full");
        // Ocultar o texto
        menuTextItems.forEach(item => item.classList.add('hidden'));
    }
}

 

// Fechar o menu ao clicar em qualquer link
document.querySelectorAll('.sidebar-link').forEach(link => {
    link.addEventListener('click', () => {
        var sidebar = document.querySelector(".sidebar");
        var menuTextItems = document.querySelectorAll('.menu-text');
        if (!sidebar.classList.contains("-translate-x-full")) {
            gsap.to(sidebar, { x: -256, duration: 0.5, ease: "power2.in" });
            sidebar.classList.add("-translate-x-full");
            // Ocultar o texto
            menuTextItems.forEach(item => item.classList.add('hidden'));
        }
    });
});