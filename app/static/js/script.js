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
