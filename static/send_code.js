let code = "";

document.querySelectorAll(".keypad button").forEach(button => {
  button.addEventListener("click", () => {
    const val = button.textContent;

    if (val === "←") {
      code = code.slice(0, -1);
    } else if (val === "C") {
      code = "";
    } else if (code.length < 6 && /^\d$/.test(val)) {
      code += val;
    }

    document.getElementById("code").value = "*".repeat(code.length);
  });
});
function updateInputDisplay() {
  const input = document.getElementById("codeInput");
  input.value = "*".repeat(code.length);
  const submitBtn = document.getElementById("submitBtn");
  submitBtn.disabled = code.length !== 6;
}

