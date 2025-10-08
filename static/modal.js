document.addEventListener("DOMContentLoaded", () => {
  const modals = document.querySelectorAll('.flash-modal');

  modals.forEach(modal => {
    // Show modal
    setTimeout(() => modal.classList.add('show'), 100);

    // Auto hide after 3 seconds
    setTimeout(() => modal.classList.remove('show'), 3000);

    // Close button
    modal.querySelector('.close-btn').addEventListener('click', () => {
      modal.classList.remove('show');
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById('confirmModal');
  let currentForm = null;

  // Handle all "close account" buttons
  document.querySelectorAll('.table-btn.danger').forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault(); // prevent form submit
      currentForm = this.closest('form'); // store the form
      modal.classList.add('show'); // show modal
    });
  });

  // Cancel button
  modal.querySelector('.cancel-btn').addEventListener('click', () => {
    modal.classList.remove('show');
    currentForm = null;
  });

  // Confirm button
  modal.querySelector('.confirm-btn').addEventListener('click', () => {
    if (currentForm) {
      currentForm.submit(); // submit the form
    }
  });
});
