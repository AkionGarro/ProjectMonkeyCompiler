

var msg = document.getElementById("simpleCode");
async function showConsoleResults() {
  document.getElementById("interpreterCode").value ='';
  result = await eel.getConsoleResult()();
  document.getElementById("interpreterCode").value = result;
  line_counter2();
}

document.getElementById("compileButton").addEventListener("click", async () => {
  await eel.startInterpreter(this.msg.value);
  showConsoleResults();

});





/*Lines Updating*/
const interpreterCodeTxt = document.getElementById("interpreterCode");
const lineCounter2 = document.getElementById("lineCounter2");

interpreterCodeTxt.addEventListener("scroll", () => {
    lineCounter2.scrollTop = interpreterCodeTxt.scrollTop;
    lineCounter2.scrollLeft = interpreterCodeTxt.scrollLeft;
});

interpreterCodeTxt.addEventListener("keydown", (e) => {
    let {keyCode} = e;
    let {value, selectionStart, selectionEnd} = interpreterCodeTxt;
    if (keyCode === 9) {
        // TAB = 9
        e.preventDefault();
        interpreterCodeTxt.value =
            value.slice(0, selectionStart) + "\t" + value.slice(selectionEnd);
        interpreterCodeTxt.setSelectionRange(
            selectionStart + 2,
            selectionStart + 2
        );
    }
});


var lineCountCache2 = 0;

function line_counter2() {
    var lineCount = interpreterCodeTxt.value.split("\n").length;
    var outarr = new Array();
    if (lineCountCache2 != lineCount) {
        for (var x = 0; x < lineCount; x++) {
            outarr[x] = x + 1 + ".";
        }
        lineCounter2.value = outarr.join("\n");
    }
    lineCountCache2 = lineCount;
}

interpreterCodeTxt.addEventListener("input", () => {
    line_counter2();
});