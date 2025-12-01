const button = document.getElementById('color-theme');
const body = document.body;

button.addEventListener('click', () => {
  if (body.classList.contains('dark-mode')) {
    button.textContent = 'Light Mode';
    body.classList.remove('dark-mode');
    body.classList.add('light-mode');
  } else {
    button.textContent = 'Dark Mode';
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');
  }
});