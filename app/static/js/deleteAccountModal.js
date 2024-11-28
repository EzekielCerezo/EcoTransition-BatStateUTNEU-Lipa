// Get the modal and relevant buttons
const deleteAccountModal = document.getElementById("deleteAccountModal");
const deleteUserButton = document.getElementById("deleteUserButton");
const btnClose = deleteAccountModal.querySelector(".btn-close");
const cancelButton = deleteAccountModal.querySelector(".btn-secondary");

// Open the modal when the delete button is clicked
deleteUserButton.addEventListener("click", function () {
	deleteAccountModal.style.display = "block"; // Show the modal
});

// Close the modal on "Cancel" or "Close" button click
function closeModal() {
	deleteAccountModal.style.display = "none";
}
btnClose.addEventListener("click", closeModal);
cancelButton.addEventListener("click", closeModal);

// Prevent form submission for now (add AJAX handling here if needed)
document.getElementById("deleteAccountForm").addEventListener("submit", function (e) {
	e.preventDefault();
	alert("Account deletion logic will be implemented here.");
	closeModal(); // Close the modal after submission
});
