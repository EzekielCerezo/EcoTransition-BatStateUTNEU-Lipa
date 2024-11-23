document.addEventListener("DOMContentLoaded", () => {
	console.log("JavaScript loaded!");
});

document.addEventListener("DOMContentLoaded", () => {
	const tabs = document.querySelectorAll(".tab");

	tabs.forEach((tab) => {
		tab.addEventListener("click", () => {
			// Remove 'active' class from all tabs
			tabs.forEach((t) => t.classList.remove("active"));

			// Add 'active' class to the clicked tab
			tab.classList.add("active");
		});
	});
});
document.addEventListener("DOMContentLoaded", () => {
	const tabs = document.querySelectorAll(".tab");
	const underline = document.getElementById("underline");

	tabs.forEach((tab) => {
		tab.addEventListener("click", () => {
			// Remove active class from all tabs
			tabs.forEach((t) => t.classList.remove("active"));
			tab.classList.add("active");

			// Get the width and position of the clicked tab
			const tabRect = tab.getBoundingClientRect();
			const containerRect = tab.parentElement.getBoundingClientRect();

			// Calculate the position and width for the underline
			const width = tabRect.width;
			const left = tabRect.left - containerRect.left;

			// Apply the calculated width and position to the underline
			underline.style.width = `${width}px`;
			underline.style.left = `${left}px`;
		});
	});
});
