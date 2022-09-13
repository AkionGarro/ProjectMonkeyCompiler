document.getElementById("btnUploadfile").addEventListener("click", openDialog);

function openDialog() {
    var file = document.getElementById("fileid");
    file.click();
}

function onFileLoad(elementId, event) {
    document.getElementById(elementId).value = event.target.result;
    line_counter1();
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
    linesTextArea1 = document.getElementById("lineCounter1");
    linesTextArea2 = document.getElementById("lineCounter2");

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
        linesTextArea1.style.backgroundColor = "white";
        linesTextArea1.style.color = "black";
        linesTextArea2.style.backgroundColor = "white";
        linesTextArea2.style.color = "black";
        interpreter.style.backgroundColor = "white";
        interpreter.style.color = "black";
    } else {
        bodyCont.style.backgroundColor = "#06071d";
        bodyCont.style.color = "white";

        header.style.backgroundColor = "#06071d";
        header.style.color = "white";

        compileButton.style.backgroundColor = "#06071d";
        compileButton.style.color = "white";

        linesTextArea1.style.backgroundColor = "#06071d";
        linesTextArea1.style.color = "white";
        linesTextArea2.style.backgroundColor = "#06071d";
        linesTextArea2.style.color = "white";

        btnUploadfile.setAttribute("stroke", "white");

        simpleCode.style.backgroundColor = "#06071d";
        simpleCode.style.color = "white";

        interpreter.style.backgroundColor = "#06071d";
        interpreter.style.color = "white";
    }
}

const simpleCodeTxt = document.getElementById("simpleCode");
const lineCounter1 = document.getElementById("lineCounter1");


simpleCodeTxt.addEventListener("scroll", () => {
    lineCounter1.scrollTop = simpleCodeTxt.scrollTop;
    lineCounter1.scrollLeft = simpleCodeTxt.scrollLeft;
});

simpleCodeTxt.addEventListener("keydown", (e) => {
    let {keyCode} = e;
    let {value, selectionStart, selectionEnd} = simpleCodeTxt;
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


