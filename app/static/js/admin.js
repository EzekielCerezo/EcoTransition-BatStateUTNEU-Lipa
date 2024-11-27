document.addEventListener("DOMContentLoaded", () => {
	console.log("Admin UI loaded.");

	// Section mapping for submenu items
	const sectionMapping = {
		organizationAccountsMenu: "organization-accounts",
		signatoryAccountsMenu: "signatory-accounts",
	};

	// Default menu and submenu IDs
	const defaultMenuId = "manageAccountMenu";
	const defaultSubmenuId = "organizationAccountsMenu";

	// Hide all preloaded sections
	const hideAllSections = () => {
		Object.values(sectionMapping).forEach((sectionId) => {
			const section = document.getElementById(sectionId);
			if (section) {
				section.classList.add("d-none");
				console.log(`Section hidden: ${sectionId}`);
			}
		});
	};

	// Activate a specific submenu and display its corresponding section
	const activateSubmenu = (submenuId) => {
		console.log(`Activating submenu: ${submenuId}`);

		// Remove active state from all submenus
		document.querySelectorAll(".submenu-item").forEach((submenu) => submenu.classList.remove("active"));

		// Add active state to the selected submenu
		const activeSubmenu = document.getElementById(submenuId);
		if (activeSubmenu) {
			activeSubmenu.classList.add("active");
			console.log(`Submenu activated: ${submenuId}`);
		}

		// Display the corresponding section
		hideAllSections();
		const sectionId = sectionMapping[submenuId];
		const section = document.getElementById(sectionId);
		if (section) {
			section.classList.remove("d-none");
			console.log(`Section displayed: ${sectionId}`);
		}
	};

	// Activate the main menu and display its submenu
	const activateMenu = (menuId) => {
		console.log(`Activating menu: ${menuId}`);

		// Remove active state from all menus
		document.querySelectorAll(".menu-item").forEach((menu) => menu.classList.remove("active"));

		// Add active state to the selected menu
		const activeMenu = document.getElementById(menuId);
		if (activeMenu) {
			activeMenu.classList.add("active");
			console.log(`Menu activated: ${menuId}`);

			// Display the submenu
			const submenu = document.getElementById(`${menuId}SubMenu`);
			if (submenu) {
				submenu.classList.remove("d-none");
				console.log(`Submenu displayed: ${menuId}SubMenu`);
			}
		}
	};

	// Initialize the default active menu and submenu
	activateMenu(defaultMenuId);
	activateSubmenu(defaultSubmenuId);

	// Event listener for submenu items
	document.querySelectorAll(".submenu-item").forEach((submenu) => {
		submenu.addEventListener("click", () => {
			activateSubmenu(submenu.id);
		});
	});
});
