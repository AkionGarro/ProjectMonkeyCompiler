var msg = document.getElementById("simpleCode");

async function showConsoleResults() {
  result = await eel.getConsoleResult()();
  document.getElementById("interpreterCode").value = result;
}

document.getElementById("compileButton").addEventListener("click", async () => {
  await eel.startInterpreter(this.msg.value);
  showConsoleResults();
});
