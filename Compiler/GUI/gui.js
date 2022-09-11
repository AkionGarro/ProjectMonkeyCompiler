document.getElementById("btnUploadfile").addEventListener("click", openDialog);

function openDialog() {
  var file = document.getElementById("fileid");
  file.click();
}

function onFileLoad(elementId, event) {
  document.getElementById(elementId).value = event.target.result;
}

function onChooseFile(event, onLoadFileHandler) {
  let input = event.target;
  if (!input.files[0]) return undefined;
  let file = input.files[0];
  let fr = new FileReader();
  fr.onload = onLoadFileHandler;
  fr.readAsText(file);
}

function checkMode(checkBox) {
  bodyCont = document.getElementsByTagName("body")[0];
  header = document.getElementById("headerCont");
  compileButton = document.getElementById("compileButton");
  btnUploadfile = document.getElementById("btnUploadfile");
  simpleCode = document.getElementById("simpleCode");
  interpreter = document.getElementById("interpreterCode");

  if (!checkBox.checked) {
    bodyCont.style.backgroundColor = "white";
    bodyCont.style.color = "black";

    header.style.backgroundColor = "white";
    header.style.color = "black";

    compileButton.style.backgroundColor = "white";
    compileButton.style.color = "black";
    compileButton.style.border.color = "white";

    btnUploadfile.setAttribute("stroke", "black");

    simpleCode.style.backgroundColor = "white";
    simpleCode.style.color = "black";

    interpreter.style.backgroundColor = "white";
    interpreter.style.color = "black";
  } else {
    bodyCont.style.backgroundColor = "#06071d";
    bodyCont.style.color = "white";

    header.style.backgroundColor = "#06071d";
    header.style.color = "white";

    compileButton.style.backgroundColor = "#06071d";
    compileButton.style.color = "white";

    btnUploadfile.setAttribute("stroke", "white");

    simpleCode.style.backgroundColor = "#06071d";
    simpleCode.style.color = "white";

    interpreter.style.backgroundColor = "#06071d";
    interpreter.style.color = "white";
  }
}

var simpleCodeTxt = document.getElementById("simpleCode");
var interpreterCodeTxt = document.getElementById("interpreterCode");
var lineCounter1 = document.getElementById("lineCounter1");
var lineCounter2 = document.getElementById("lineCounter2");

simpleCodeTxt.addEventListener("scroll", () => {
  lineCounter1.scrollTop = simpleCodeTxt.scrollTop;
  lineCounter1.scrollLeft = simpleCodeTxt.scrollLeft;
});

simpleCodeTxt.addEventListener("keydown", (e) => {
  let { keyCode } = e;
  let { value, selectionStart, selectionEnd } = simpleCodeTxt;
  if (keyCode === 9) {
    // TAB = 9
    e.preventDefault();
    simpleCodeTxt.value =
      value.slice(0, selectionStart) + "\t" + value.slice(selectionEnd);
    simpleCodeTxt.setSelectionRange(selectionStart + 2, selectionStart + 2);
  }
});

var lineCountCache1 = 0;
function line_counter1() {
  var lineCount = simpleCodeTxt.value.split("\n").length;
  var outarr = new Array();
  if (lineCountCache1 != lineCount) {
    for (var x = 0; x < lineCount; x++) {
      outarr[x] = x + 1 + ".";
    }
    lineCounter1.value = outarr.join("\n");
  }
  lineCountCache1 = lineCount;
}
simpleCodeTxt.addEventListener("input", () => {
  line_counter1();
});

interpreterCodeTxt.addEventListener("scroll", () => {
  lineCounter2.scrollTop = interpreterCodeTxt.scrollTop;
  lineCounter2.scrollLeft = interpreterCodeTxt.scrollLeft;
});

interpreterCodeTxt.addEventListener("keydown", (e) => {
  let { keyCode } = e;
  let { value, selectionStart, selectionEnd } = interpreterCodeTxt;
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
