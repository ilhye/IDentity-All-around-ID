// Function to create a new notification element
function createNewElement(message) {
  const notificationsContainer = document.getElementById(
    "notifications-container"
  );
  const notificationItem = document.createElement("div");
  notificationItem.className = "notification-item";

  const icon = document.createElement("div");
  icon.className = "icon";

  const details = document.createElement("div");
  details.className = "details";

  const notificationText = document.createElement("p");
  notificationText.textContent = message;

  const timestamp = document.createElement("span");
  timestamp.className = "timestamp";
  const now = new Date();
  timestamp.textContent = `${now.toLocaleTimeString()} ${now.toLocaleDateString()}`;

  details.appendChild(notificationText);
  details.appendChild(timestamp);
  notificationItem.appendChild(icon);
  notificationItem.appendChild(details);

  // Append the new notification to the bottom of the container
  notificationsContainer.appendChild(notificationItem);
}

// Function to display the application submission notification
function showApplicationNotification() {
  createNewElement("Your application is submitted.");
}

// Function to display the reminder notification
function showReminder() {
  createNewElement("Please check your government ID application status.");
}

// Function to set the reminder interval
function setReminder() {
  const frequencySelect = document.getElementById("reminder-frequency");
  const customIntervalInput = document.getElementById("custom-interval");
  let interval;

  if (frequencySelect.value === "custom") {
    interval = parseInt(customIntervalInput.value, 10) * 24 * 60 * 60 * 1000; // Convert days to milliseconds
  } else {
    interval = parseInt(frequencySelect.value, 10) * 24 * 60 * 60 * 1000; // Convert days to milliseconds
  }

  if (isNaN(interval) || interval <= 0) {
    alert("Please enter a valid interval.");
    return;
  }

  // Clear any existing reminders
  clearInterval(window.reminderInterval);

  // Set a new reminder interval
  window.reminderInterval = setInterval(showReminder, interval);

  alert(
    `Reminder set! You will be reminded every ${
      interval / (24 * 60 * 60 * 1000)
    } days.`
  );
  closeReminderModal();
}

// Function to open the reminder modal
function openReminderModal() {
  document.getElementById("reminder-modal").classList.add("open");
  document.getElementById("reminder-modal-overlay").classList.add("open");
}

// Function to close the reminder modal
function closeReminderModal() {
  document.getElementById("reminder-modal").classList.remove("open");
  document.getElementById("reminder-modal-overlay").classList.remove("open");
}

// Function to open the filter modal
function openFilterModal() {
  document.getElementById("filter-modal").classList.add("open");
  document.getElementById("filter-modal-overlay").classList.add("open");
}

// Function to close the filter modal
function closeFilterModal() {
  document.getElementById("filter-modal").classList.remove("open");
  document.getElementById("filter-modal-overlay").classList.remove("open");
}

// Function to apply the selected filter
function applyFilter() {
  const filterOption = document.getElementById("filter-option").value;
  const filterDate = document.getElementById("filter-date").value;
  const notifications = document.querySelectorAll(".notification-item");

  notifications.forEach((notification) => {
    const notificationType = notification.getAttribute("data-type");
    const notificationDate = notification.getAttribute("data-date");

    let shouldShow = true;

    if (filterOption === "date" && filterDate) {
      shouldShow = notificationDate === filterDate;
    } else if (filterOption === "application") {
      shouldShow = notificationType === "application";
    } else if (filterOption === "renewal") {
      shouldShow = notificationType === "renewal";
    }

    notification.style.display = shouldShow ? "flex" : "none";
  });

  closeFilterModal();
}

// Show the application submission notification when the page loads
showApplicationNotification();

// Handle custom interval input visibility
const frequencySelect = document.getElementById("reminder-frequency");
const customIntervalInput = document.getElementById("custom-interval");
frequencySelect.addEventListener("change", function () {
  if (this.value === "custom") {
    customIntervalInput.style.display = "inline-block";
  } else {
    customIntervalInput.style.display = "none";
  }
});

// Handle filter option visibility
const filterOptionSelect = document.getElementById("filter-option");
const filterDateInput = document.getElementById("filter-date");
filterOptionSelect.addEventListener("change", function () {
  if (this.value === "date") {
    filterDateInput.style.display = "inline-block";
  } else {
    filterDateInput.style.display = "none";
  }
});
