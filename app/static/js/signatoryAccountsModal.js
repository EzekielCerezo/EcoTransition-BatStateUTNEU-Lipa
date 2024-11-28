// Modal and button elements
const addSignatoryModal = document.getElementById("addSignatoryModal");
const addSignatoryButton = document.getElementById("addUserButton");
const closeModalButton = addSignatoryModal.querySelector(".btn-close");

// Show modal when "Add Account" is clicked
addSignatoryButton.addEventListener("click", () => {
	addSignatoryModal.style.display = "block";
});

// Close modal when close button is clicked
closeModalButton.addEventListener("click", () => {
	addSignatoryModal.style.display = "none";
});

// Close modal when clicking outside the modal dialog
window.addEventListener("click", (event) => {
	if (event.target === addSignatoryModal) {
		addSignatoryModal.style.display = "none";
	}
});
