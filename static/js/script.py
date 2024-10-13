# JavaScript function to toggle the sidebar in mobile view
def toggleMenu():
    return """
         function toggleMenu() {
            var sidebar = document.getElementById('sidebar');
            if (sidebar.classList.contains('hidden')) {
                sidebar.classList.remove('hidden');
            } else {
                sidebar.classList.add('hidden');
            }
        }
         
    """