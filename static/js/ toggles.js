
function toggleSidebar() {
    var sidebar = document.querySelector(".sidebar");
    var menuTextItems = document.querySelectorAll('.menu-text');
    var iconContainers = document.querySelectorAll('.icon-container'); // Seleciona os contêineres de ícones

    if (sidebar.classList.contains("-translate-x-full")) {
        gsap.to(sidebar, { x: 0, duration: 0.5, ease: "power2.out" });
        sidebar.classList.remove("-translate-x-full");

        // Exibir o texto com animação de opacidade
        menuTextItems.forEach(item => {
            gsap.to(item, { opacity: 1, duration: 0.3, ease: "power2.out" });
            item.classList.remove('hidden'); // Certifique-se de que a classe 'hidden' é removida após a animação
        });

        // Resetar o espaçamento dos ícones
        iconContainers.forEach(container => container.style.marginLeft = '0');
    } else {
        gsap.to(sidebar, { x: -256, duration: 0.5, ease: "power2.in" });

        // Ocultar o texto com animação de opacidade
        menuTextItems.forEach(item => {
            gsap.to(item, { opacity: 0, duration: 0.3, ease: "power2.in", onComplete: () => {
                item.classList.add('hidden'); // Adicionar 'hidden' após a animação
            } });
        });

        // Ajustar o espaçamento dos ícones
        iconContainers.forEach(container => container.style.marginLeft = '16px'); // Ajuste conforme necessário
    }
}

function toggleSidebarDesktop() {
    var sidebar = document.querySelector(".sidebar");
    var menuTextItems = document.querySelectorAll('.menu-text');
    var iconContainers = document.querySelectorAll('.icon-container'); // Seleciona os contêineres de ícones

    if (sidebar.classList.contains("-translate-x-full")) {
        gsap.to(sidebar, { x: 0, duration: 0.5, ease: "power2.out" });
        sidebar.classList.remove("-translate-x-full");

        // Exibir o texto com animação de opacidade
        menuTextItems.forEach(item => {
            gsap.to(item, { opacity: 1, duration: 0.3, ease: "power2.out" });
            item.classList.remove('hidden'); // Certifique-se de que a classe 'hidden' é removida após a animação
        });

        // Resetar o espaçamento dos ícones
        iconContainers.forEach(container => container.style.marginLeft = '0');
    } else {
        gsap.to(sidebar, { x: -140, duration: 0.5, ease: "power2.in" });

        // Ocultar o texto com animação de opacidade
        menuTextItems.forEach(item => {
            gsap.to(item, { opacity: 0, duration: 0.3, ease: "power2.in", onComplete: () => {
                item.classList.add('hidden'); // Adicionar 'hidden' após a animação
            } });
        });

        // Ajustar o espaçamento dos ícones
        iconContainers.forEach(container => container.style.marginLeft = '150px'); // Ajuste conforme necessário
    }
}

// Fechar o menu ao clicar em qualquer link
document.querySelectorAll('.sidebar-link').forEach(link => {
    link.addEventListener('click', () => {
        var sidebar = document.querySelector(".sidebar");
        var menuTextItems = document.querySelectorAll('.menu-text');
        var iconContainers = document.querySelectorAll('.icon-container'); // Seleciona os contêineres de ícones

        if (!sidebar.classList.contains("-translate-x-full")) {
            gsap.to(sidebar, { x: -256, duration: 0.5, ease: "power2.in" });
            sidebar.classList.add("-translate-x-full");

            // Ocultar o texto com animação de opacidade
            menuTextItems.forEach(item => {
                gsap.to(item, { opacity: 0, duration: 0.3, ease: "power2.in", onComplete: () => {
                    item.classList.add('hidden'); // Adicionar 'hidden' após a animação
                } });
            });

            // Ajustar o espaçamento dos ícones
            iconContainers.forEach(container => container.style.marginLeft = '16px'); // Ajuste conforme necessário
        }
    });
});
