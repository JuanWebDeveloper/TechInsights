const deleteButton = document.getElementById('delete-button');
const cancelButton = document.getElementById('cancel-button');
const confirmDelete = document.querySelector('.confirm-delete');

deleteButton.addEventListener('click', () => {
 if (confirmDelete.classList.contains('show')) {
  confirmDelete.classList.remove('show');
  confirmDelete.classList.add('hide');
 } else {
  confirmDelete.classList.remove('hide');
  confirmDelete.classList.add('show');
 }
});

cancelButton.addEventListener('click', () => {
 confirmDelete.classList.remove('show');
 confirmDelete.classList.add('hide');
});
