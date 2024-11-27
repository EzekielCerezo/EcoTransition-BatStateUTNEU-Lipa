document.addEventListener("DOMContentLoaded", () => {
	console.log("Initializing Signatory UI logic...");

	// Mapping menu items to sections to show
	const sectionMapping = {
		documentsMenu: ["document-list", "document-details"], // Show both sections
		eventCalendarMenu: ["events-calendar", "events-details"], // Show both sections
		eventAnalyticsMenu: ["event-analytics"],
	};

	// Hide all sections
	const hideAllSections = () => {
		Object.keys(sectionMapping).forEach((menuId) => {
			sectionMapping[menuId].forEach((sectionId) => {
				const section = document.getElementById(sectionId);
				if (section) {
					section.classList.add("d-none");
					console.log(`Section hidden: ${sectionId}`);
				}
			});
		});
	};

	// Activate a menu and display the corresponding sections
	const activateMenu = (menuId) => {
		console.log(`Activating menu: ${menuId}`);

		// Remove active state from all menu items
		document.querySelectorAll(".menu-item").forEach((item) => item.classList.remove("active"));

		// Set active state for the clicked menu
		const activeMenu = document.getElementById(menuId);
		if (activeMenu) {
			activeMenu.classList.add("active");
			console.log(`Menu item activated: ${menuId}`);
		}

		// Hide all sections and show the relevant ones
		hideAllSections();
		const activeSections = sectionMapping[menuId];
		if (activeSections) {
			activeSections.forEach((sectionId) => {
				const section = document.getElementById(sectionId);
				if (section) {
					section.classList.remove("d-none");
					console.log(`Section displayed: ${sectionId}`);
				}
			});
		}
	};

	// Default menu to activate on load
	const defaultMenu = "documentsMenu";
	activateMenu(defaultMenu);

	// Add click event listeners to menu items
	document.querySelectorAll(".menu-item").forEach((menu) => {
		menu.addEventListener("click", () => {
			activateMenu(menu.id);
		});
	});
});
