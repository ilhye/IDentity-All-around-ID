// Save user's accessibility preference
function setAccessibility(accessibilityType) {
  localStorage.setItem("accessibility", accessibilityType);
}

// Check if accessibility is set to "vision" and enable TTS
document.addEventListener("DOMContentLoaded", function () {
  if (localStorage.getItem("accessibility") === "vision") {
      enableTextToSpeech();
  }
});

function enableTextToSpeech() {
  document.querySelectorAll("[id^='speak-']").forEach((element) => {
      textToSpeech(element);
  });
}

// Function to speak text content
function textToSpeech(element) {
  const text = element.textContent || element.innerText;
  const speech = new SpeechSynthesisUtterance(text);
  speech.lang = "en-US";
  speech.rate = 1;
  window.speechSynthesis.speak(speech);
}

// Event Listener for manual TTS activation
document.getElementById("text-to-speech")?.addEventListener("click", function () {
  enableTextToSpeech();
});
