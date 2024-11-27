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
	let forgotPasswordModal = forgotPasswordModalElement ? new bootstrap.Modal(forgotPasswordModalElement) : null;

	// Event listener: Toggle between Sign In and Continue as Guest views
	if (registerBtn) {
		registerBtn.addEventListener("click", () => {
			console.log("Register button clicked");
			container?.classList.add("active");
		});
	}

	if (loginBtn) {
		loginBtn.addEventListener("click", () => {
			console.log("Login button clicked");
			container?.classList.remove("active");
		});
	}

	// Event listener: Toggle password visibility
	if (togglePassword && passwordInput) {
		togglePassword.addEventListener("click", () => {
			const isPassword = passwordInput.type === "password";
			passwordInput.type = isPassword ? "text" : "password";
			togglePassword.classList.toggle("fa-eye");
			togglePassword.classList.toggle("fa-eye-slash");
			console.log("Password visibility toggled:", passwordInput.type);
		});
	}

	// Event listener: "Continue as Guest" form submission
	const guestForm = document.getElementById("guest-form");
	const emailInput = document.getElementById("guest-email");
	const feedback = document.getElementById("guest-error");

	if (guestForm && emailInput && feedback) {
		guestForm.addEventListener("submit", async (event) => {
			event.preventDefault();
			const email = emailInput.value.trim();
			console.log("Guest form submitted with email:", email);

			// Validate email input
			if (!email) {
				displayFeedback(feedback, "Please enter a valid email.", "form-error");
				return;
			}

			// API call to send email to backend
			try {
				const response = await fetch("/auth/guest-continue", {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify({ email }),
				});

				const result = await response.json();
				console.log("API Response:", result);

				if (response.ok && result.message) {
					displayFeedback(feedback, result.message, "form-success");
					emailInput.value = ""; // Clear email input
				} else {
					displayFeedback(feedback, result.error || "An error occurred.", "form-error");
				}
			} catch (error) {
				console.error("Error during API call:", error);
				displayFeedback(feedback, "An error occurred while processing your request.", "form-error");
			}
		});
	}

	// Event listener: Login form submission
	const loginForm = document.querySelector("form[action='/auth/']");
	if (loginForm) {
		loginForm.addEventListener("submit", (event) => {
			console.log("Login form submitted with data:", new FormData(event.target));
		});
	}

	// Event listener: Show forgot password modal
	const showForgotPasswordModal = () => {
		if (forgotPasswordModal) {
			forgotPasswordModal.show();
			console.log("Forgot password modal displayed.");
		}
	};

	const closeForgotPasswordModal = () => {
		if (forgotPasswordModal) {
			forgotPasswordModal.hide();
			console.log("Forgot password modal hidden.");
		}
	};

	// Attach modal-related functions globally
	window.showForgotPasswordModal = showForgotPasswordModal;
	window.closeForgotPasswordModal = closeForgotPasswordModal;
});

// Helper function to display feedback messages
function displayFeedback(element, message, className) {
	element.textContent = message;
	element.className = className;
}
