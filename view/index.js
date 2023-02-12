const textarea = document.getElementById("textarea");
const submitButton = document.getElementById("submit");
const responseDiv = document.getElementById("response");

submitButton.addEventListener("click", () => {
  const text = textarea.value;

  const data = {
    document: text
  };

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "https://api.gptzero.me/v2/predict/text", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      responseDiv.textContent = this.responseText;
    }
  };
  xhr.send(JSON.stringify(data));
});
