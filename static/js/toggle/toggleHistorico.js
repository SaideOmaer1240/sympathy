function toggleCardsSection(section) {
    const historicoList = document.getElementById('historico-list');

    if (section === 'historico') {
        if (historicoList.classList.contains('hidden')) {
            historicoList.classList.remove('hidden');  // Remove a classe para mostrar
        } else {
            historicoList.classList.add('hidden');  // Adiciona a classe para ocultar
        }
    }
}
