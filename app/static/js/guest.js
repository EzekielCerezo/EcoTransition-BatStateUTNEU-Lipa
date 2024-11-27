document.addEventListener("DOMContentLoaded", () => {
	console.log("Initializing Guest UI logic...");

	// Section mappings for menus
	const sectionMapping = {
		documentsMenu: ["document-list", "document-details"], // Maps menu to sections
	};

	// Reference the document entries container
	const documentEntriesContainer = document.getElementById("document-entries");

	/**
	 * Function to hide all sections by adding the "d-none" class.
	 */
	const hideAllSections = () => {
		console.log("Hiding all sections...");
		Object.values(sectionMapping).forEach((sectionIds) => {
			sectionIds.forEach((sectionId) => {
				const section = document.getElementById(sectionId);
				if (section) {
					section.classList.add("d-none");
					console.log(`Section hidden: ${sectionId}`);
				}
			});
		});
	};

	/**
	 * Function to activate a specific menu and its associated sections.
	 * @param {string} menuId - The ID of the menu to activate.
	 */
	const activateMenu = (menuId) => {
		console.log(`Activating menu: ${menuId}`);

		// Deactivate all menu items
		document.querySelectorAll(".menu-item").forEach((item) => item.classList.remove("active"));

		// Activate the clicked menu
		const activeMenu = document.getElementById(menuId);
		if (activeMenu) {
			activeMenu.classList.add("active");
			console.log(`Menu item activated: ${menuId}`);
		}

		// Hide all sections and display the linked sections
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

	// Tab functionality
	const tabs = document.querySelectorAll(".tab");
	const defaultTabId = "tab-all";

	/**
	 * Function to dynamically load a template and inject data into it.
	 * @param {string} templatePath - The name of the template file (e.g., "documentContainer").
	 * @param {Object} data - The data to inject into the template.
	 * @returns {Promise<string>} - The resolved HTML string.
	 */
	const loadTemplate = async (templatePath, data = {}) => {
		try {
			const response = await fetch(`/guest/api/render-template/${templatePath}`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(data),
			});

			if (!response.ok) {
				throw new Error(`Error rendering template: ${response.status}`);
			}

			return await response.text();
		} catch (error) {
			console.error("Error loading template:", error);
			return `<div>Error loading template: ${templatePath}</div>`;
		}
	};

	/**
	 * Fetches uploaded documents dynamically from the backend.
	 * @returns {Promise<Array>} - A promise resolving to the list of uploaded documents.
	 */
	const fetchUploadedDocuments = async () => {
		try {
			const response = await fetch("/guest/api/documents");
			if (!response.ok) {
				throw new Error(`Error fetching documents: ${response.statusText}`);
			}
			const documents = await response.json();
			console.log("Fetched uploaded documents:", documents);
			return documents;
		} catch (error) {
			console.error("Error fetching uploaded documents:", error);
			return []; // Return an empty array in case of error
		}
	};

	const formatDeadline = (rawDate) => {
		const date = new Date(rawDate);
		const month = date.toLocaleString("en-US", { month: "short" }).toUpperCase();
		const day = String(date.getDate()).padStart(2, "0"); // Ensure 2-digit day
		const year = date.getFullYear();
		return `${month} ${day}, ${year}`;
	};

	/**
	 * Renders document entries based on the active tab.
	 * @param {string} tabId - The ID of the active tab.
	 */
	const renderDocumentEntries = async (tabId) => {
		const uploadedDocuments = await fetchUploadedDocuments();
		const filteredDocuments = uploadedDocuments.filter((doc) => {
			if (tabId === "tab-all") return true;
			if (tabId === "tab-in-progress") return doc.status === "IN PROGRESS";
			if (tabId === "tab-completed") return doc.status === "APPROVED";
			return false;
		});

		documentEntriesContainer.innerHTML = ""; // Clear existing entries

		if (filteredDocuments.length === 0) {
			const noDocumentsHTML = await loadTemplate("noDocument");
			documentEntriesContainer.innerHTML = noDocumentsHTML;
		} else {
			for (const doc of filteredDocuments) {
				console.log("Rendering document:", doc); // Debug log
				const documentHTML = await loadTemplate("documentContainer", {
					title: doc.title,
					status: doc.status, // Original status for display text
					css_status: doc.status.toLowerCase().replace(" ", "-"), // For CSS classes
					color: doc.color, // Add color for circle and border
					uploader: doc.uploader,
					deadline: formatDeadline(doc.deadline),
				});
				documentEntriesContainer.insertAdjacentHTML("beforeend", documentHTML);
			}
		}
	};

	/**
	 * Function to set the active tab and handle tab switching.
	 * @param {HTMLElement} tab - The tab element to activate.
	 */
	const setActiveTab = (tab) => {
		console.log(`Switching to tab: ${tab.id}`);

		// Deactivate all tabs
		tabs.forEach((t) => t.classList.remove("active"));
		console.log("All tabs deactivated.");

		// Activate the clicked tab
		tab.classList.add("active");
		console.log(`Tab activated: ${tab.id}`);

		// Render document entries for the active tab
		renderDocumentEntries(tab.id);
	};

	// Add click event listeners to tabs
	tabs.forEach((tab) => {
		tab.addEventListener("click", () => {
			console.log(`Tab clicked: ${tab.id}`);
			setActiveTab(tab);
		});
	});

	// Initialize the default tab
	const defaultTab = document.getElementById(defaultTabId);
	if (defaultTab) {
		console.log("Setting default tab to 'ALL'...");
		setActiveTab(defaultTab);
	}

	// Initialize the default view
	console.log("Initializing default view for 'Documents Menu'...");
	activateMenu("documentsMenu");
});
