// Uses the Web Speech API to convert text to speech
function textToSpeech() {
  const speak = document.getElementById("text-to-speech"); // Get the button element
  const sentence = document.querySelectorAll('*[id^="speak"]'); // Get all elements with an id that starts with "speak"
  const synth = window.speechSynthesis; // Get the speech synthesis object

  // Trigger the click event automatically
  setTimeout(() => {
    speak.click();
  }, 1000); // Wait for 1 second before triggering the click

  for (let i = 0; i < sentence.length; i++) { // Loop through all the elements
    const utterance = new SpeechSynthesisUtterance(sentence[i].textContent);
    synth.speak(utterance);
  }
}

textToSpeech(); // Call the function