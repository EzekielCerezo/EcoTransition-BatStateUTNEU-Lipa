document.addEventListener("DOMContentLoaded", () => {
	console.log("JavaScript loaded!");

	// Initialize global variables
	const container = document.getElementById("container");
	const registerBtn = document.getElementById("register");
	const loginBtn = document.getElementById("login");
	const passwordInput = document.getElementById("password");
	const togglePassword = document.getElementById("toggle-password");
	const forgotPasswordModalElement = document.getElementById("forgot-password-modal");

	// Initialize Bootstrap modal instance
	let forgotPasswordModal;
	if (forgotPasswordModalElement) {
		forgotPasswordModal = new bootstrap.Modal(forgotPasswordModalElement);
	}

	// Add event listeners
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

	if (togglePassword && passwordInput) {
		togglePassword.addEventListener("click", () => {
			const isPassword = passwordInput.type === "password";
			passwordInput.type = isPassword ? "text" : "password";
			togglePassword.classList.toggle("fa-eye");
			togglePassword.classList.toggle("fa-eye-slash");
		});
	}
});

// Function to show the forgot password modal
function showForgotPasswordModal() {
	const forgotPasswordModalElement = document.getElementById("forgot-password-modal");
	if (forgotPasswordModalElement) {
		const forgotPasswordModal = new bootstrap.Modal(forgotPasswordModalElement);
		forgotPasswordModal.show();
	}
}

// Function to close the modal
function closeForgotPasswordModal() {
	const forgotPasswordModalElement = document.getElementById("forgot-password-modal");
	if (forgotPasswordModalElement) {
		const forgotPasswordModal = bootstrap.Modal.getInstance(forgotPasswordModalElement);
		if (forgotPasswordModal) {
			forgotPasswordModal.hide();
		}
	}
}
