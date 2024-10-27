
    // Função para alternar a exibição da seção de agendas recentes
    function toggleCardsSection(texto) {
        var cardsSection = document.getElementById("cards-section");
        var toggleButton = document.getElementById("toggle-button");
        var agendaList = document.getElementById("agenda-list");

        // Se a seção estiver visível, esconda-a
        if (cardsSection.style.height === "" || cardsSection.style.height === "0px") {
            gsap.to(cardsSection, { height: "auto", duration: 0.5, ease: "power2.out" });
            toggleButton.innerHTML = `▲ ${texto}`;
            agendaList.style.height = '20rem';
        } else {
            gsap.to(cardsSection, { height: 0, duration: 0.5, ease: "power2.in" });
            toggleButton.innerHTML = `▼ ${texto}`;
            agendaList.style.height = 'auto';
        }
    }
 
    
    