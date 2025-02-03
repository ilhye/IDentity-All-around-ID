// Search functionality
const searchInput = document.getElementById("searchInput");
const idCards = document.querySelectorAll(".id-card");

searchInput.addEventListener("input", () => {
  const searchTerm = searchInput.value.toLowerCase();

  idCards.forEach((card) => {
    const name = card.getAttribute("data-name").toLowerCase();
    const age = card.getAttribute("data-age").toLowerCase();
    const tags = Array.from(card.querySelectorAll(".tag")).map((tag) =>
      tag.textContent.toLowerCase()
    );

    // Check if the search term matches the name, age, or any of the tags
    if (
      name.includes(searchTerm) ||
      age.includes(searchTerm) ||
      tags.some((tag) => tag.includes(searchTerm))
    ) {
      card.style.display = "flex";
    } else {
      card.style.display = "none";
    }
  });
});

// Apply button functionality
const applyButtons = document.querySelectorAll(".apply-btn");
const applyModal = document.getElementById("applyModal");
const closeModal = document.querySelectorAll(".close");

let currentCard = null; // To store the ID card that triggered the modal

applyButtons.forEach((button) => {
  button.addEventListener("click", () => {
    currentCard = button.closest(".id-card"); // Store the clicked card
    applyModal.style.display = "flex"; // Show the modal
  });
});

closeModal.forEach((button) => {
  button.addEventListener("click", () => {
    applyModal.style.display = "none";
    checkModal.style.display = "none";
  });
});

document.getElementById("newApplication").addEventListener("click", () => {
  if (currentCard) {
    const newApplicationUrl = currentCard.getAttribute("data-new-application");
    window.open(newApplicationUrl, "_blank"); // Open in a new tab
  }
});

document.getElementById("renewApplication").addEventListener("click", () => {
  if (currentCard) {
    const renewApplicationUrl = currentCard.getAttribute(
      "data-renew-application"
    );
    window.open(renewApplicationUrl, "_blank"); // Open in a new tab
  }
});

// Check availability button functionality
const checkButtons = document.querySelectorAll(".check-btn");
const checkModal = document.getElementById("checkModal");
const availabilityText = document.getElementById("availabilityText");
const requiredDocumentsLink = document.getElementById("requiredDocumentsLink");
const branchesLink = document.getElementById("branchesLink");

checkButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const idName = button.closest(".id-card").getAttribute("data-name");
    if (idName === "National ID (PhilSys ID)") {
      availabilityText.innerHTML =
        "The application process for the National ID (PhilSys ID) is available at designated branches.<br><br>Please refer to the provided link for the required application documents and a list of branches where you can apply.";
      requiredDocumentsLink.href =
        "https://philsys.gov.ph/supporting-documents/";
      branchesLink.href = "https://philsys.gov.ph/registration-center/";
    } else if (idName === "Passport ID") {
      availabilityText.innerHTML =
        "The Passport application process is available onsite once you have completed the scheduled appointment and filled out the application form.<br><br>Please refer to the provided link for the required application documents and a list of branches where you can schedule an appointment.";
      requiredDocumentsLink.href =
        "https://consular.dfa.gov.ph/services/passport/requirements";
      branchesLink.href = "https://filipiknow.net/dfa-branches/";
    } else if (idName === "Postal ID") {
      availabilityText.innerHTML =
        "The Postal ID application process is available onsite, where you can complete payment and have your ID captured after filling out the application form.<br><br>Please refer to the provided link for a list of required application documents and branches where you can make payment and have your ID captured.";
      requiredDocumentsLink.href =
        "https://www.postalidph.com/requirements.html";
      branchesLink.href = "https://www.postalidph.com/where-to-apply.html";
    }
    checkModal.style.display = "flex"; // Show the modal
  });
});

// Close modal when clicking outside of it
window.addEventListener("click", (event) => {
  if (event.target === applyModal) {
    applyModal.style.display = "none";
  }
  if (event.target === checkModal) {
    checkModal.style.display = "none";
  }
});
