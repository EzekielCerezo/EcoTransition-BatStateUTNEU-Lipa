document.addEventListener("DOMContentLoaded", () => {
	console.log("JavaScript loaded!");

	const container = document.getElementById("container");
	const registerBtn = document.getElementById("register");
	const loginBtn = document.getElementById("login");
	const passwordInput = document.getElementById("password");
	const togglePassword = document.getElementById("toggle-password");

	// Ensure buttons exist before adding listeners
	if (registerBtn) {
		registerBtn.addEventListener("click", () => {
			container.classList.add("active");
		});
	}

	if (loginBtn) {
		loginBtn.addEventListener("click", () => {
			container.classList.remove("active");
		});
	}

	togglePassword.addEventListener("click", () => {
		// Toggle input type between 'password' and 'text'
		const isPassword = passwordInput.getAttribute("type") === "password";
		passwordInput.setAttribute("type", isPassword ? "text" : "password");

		// Toggle icon class between 'eye' and 'eye-slash'
		togglePassword.classList.toggle("fa-eye");
		togglePassword.classList.toggle("fa-eye-slash");
	});
});

// Ensure the modal is hidden by default
document.addEventListener("DOMContentLoaded", () => {
	const modal = document.getElementById("forgotPasswordModal");
	if (modal) {
		modal.style.display = "none";
		modal.classList.remove("show");
	}
});

// Function to show the modal
function showModal() {
	const modal = document.getElementById("forgotPasswordModal");
	const backdrop = document.createElement("div");
	backdrop.className = "modal-backdrop fade show";

	// Show the modal
	if (modal) {
		modal.style.display = "block";
		modal.classList.add("show");
	}

	// Append the backdrop to the body
	document.body.appendChild(backdrop);
}

// Function to close the modal
function closeModal() {
	const modal = document.getElementById("forgotPasswordModal");
	const backdrop = document.querySelector(".modal-backdrop");

	// Hide the modal
	if (modal) {
		modal.style.display = "none";
		modal.classList.remove("show");
	}

	// Remove the backdrop
	if (backdrop) {
		backdrop.parentNode.removeChild(backdrop);
	}
}

