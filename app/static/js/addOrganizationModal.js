// Get the modal and the icon button
const addUserModal = document.getElementById("addOrganizationModal");
const addUserIcon = document.getElementById("addUserIcon");

// When the icon is clicked, show the modal
addUserIcon.addEventListener("click", function () {
	addUserModal.style.display = "block"; // Show the modal
});

// Function to close the modal
function closeAddUserForm() {
	addUserModal.style.display = "none";
}

///////////CODE ABOVE IS FOR organizationAccounts.html///////
const btnClose = document.querySelector(".btn-close");

// When the close button is clicked, hide the modal
btnClose.addEventListener("click", function () {
	addUserModal.style.display = "none"; // Hide the modal
});
