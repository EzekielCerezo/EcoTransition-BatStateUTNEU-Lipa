document.addEventListener("DOMContentLoaded", () => {
	const calendarDates = document.getElementById("calendarDates");
	const monthYear = document.getElementById("monthYear");

	const today = new Date();
	let currentMonth = today.getMonth(); // 0-indexed (January is 0)
	let currentYear = today.getFullYear();

	// Render the calendar for a given month and year
	function renderCalendar(month, year) {
		// Clear previous dates
		calendarDates.innerHTML = "";

		// Set the month and year in the header
		const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
		monthYear.textContent = `${monthNames[month]} ${year}`;

		// Get the first day of the month
		const firstDay = new Date(year, month, 1).getDay();

		// Get the number of days in the month
		const daysInMonth = new Date(year, month + 1, 0).getDate();

		// Get the number of days in the previous month
		const daysInPrevMonth = new Date(year, month, 0).getDate();

		// Fill in the blank spaces for the days of the previous month
		for (let i = firstDay - 1; i >= 0; i--) {
			const dateElem = document.createElement("div");
			dateElem.className = "date inactive";
			dateElem.textContent = daysInPrevMonth - i;
			calendarDates.appendChild(dateElem);
		}

		// Fill in the days of the current month
		for (let day = 1; day <= daysInMonth; day++) {
			const dateElem = document.createElement("div");
			dateElem.className = "date";
			dateElem.textContent = day;

			// Highlight today's date
			if (day === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
				dateElem.classList.add("active");
			}

			calendarDates.appendChild(dateElem);
		}

		// Fill in the blank spaces for the next month
		const remainingDays = 42 - (firstDay + daysInMonth); // Total slots in 6 rows of 7 columns
		for (let i = 1; i <= remainingDays; i++) {
			const dateElem = document.createElement("div");
			dateElem.className = "date inactive";
			dateElem.textContent = i;
			calendarDates.appendChild(dateElem);
		}
	}

	// Navigation buttons
	document.querySelector(".prev-month").addEventListener("click", () => {
		currentMonth -= 1;
		if (currentMonth < 0) {
			currentMonth = 11;
			currentYear -= 1;
		}
		renderCalendar(currentMonth, currentYear);
	});

	document.querySelector(".next-month").addEventListener("click", () => {
		currentMonth += 1;
		if (currentMonth > 11) {
			currentMonth = 0;
			currentYear += 1;
		}
		renderCalendar(currentMonth, currentYear);
	});

	// Initial render
	renderCalendar(currentMonth, currentYear);
});
