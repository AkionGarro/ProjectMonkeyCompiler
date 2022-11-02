const interpreterCodeTxt = document.getElementById("interpreterCode");
const lineCounter2 = document.getElementById("lineCounter2");
var msg = document.getElementById("simpleCode");
var msgEnter = document.getElementById("interpreterCode");
var result = "";
var gbText= "";
var lastKey = "";

var parentesisAbiertos = 0;
var saltosIgnorar = 0;
var parentesisUsado = false;

async function showConsoleWithButton() {
    document.getElementById("interpreterCode").value = '';
    result = await eel.getConsoleResult("")();
    resultText = "";
    for (var i = 0; i < result.length; i++) {
        if(String(typeof result[i]) == "object"){
            if(i==0){
                resultText += JSON.stringify(result[i])
            }else{
                resultText += "\n" + JSON.stringify(result[i])
            }
        }else{
            if(i==0){
                resultText = String(result[i]);
            }else{
                resultText += "\n" + String(result[i]);
            }
        }
    }
    document.getElementById("interpreterCode").value = resultText;
    line_counter2();
}

async function showConsoleWithEnter() {
    result = await eel.getConsoleResult("console")();
    resultText = "";
    for (var i = 0; i < result.length; i++) {
        if(String(typeof result[i]) == "object"){
            if(i==0){
                resultText += JSON.stringify(result[i])
            }else{
                resultText += "\n" + JSON.stringify(result[i])
            }
        }else{
            if(i==0){
                resultText = String(result[i]);
            }else{
                resultText += "\n" + String(result[i]);
            }
        }
    }
    console.log("Resultado: ", resultText);
    gbText+="\n"

    if (result != "Syntactic analysis Sucessfull") {
        gbText+=resultText
         gbText+="\n"
    }
    slipText = gbText.split("\n");
    saltosIgnorar = slipText.length - 1;
    console.log("Saltos: ", saltosIgnorar);
    document.getElementById("interpreterCode").value = (gbText);
    gbText=""
    line_counter2();
}

document.getElementById("compileButton").addEventListener("click", async () => {
    console.log("Código: \n", this.msg.value);
    await eel.startInterpreter(this.msg.value);
    showConsoleWithButton();

});


/*Lines Updating*/


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

interpreterCodeTxt.addEventListener('keyup', async function (e) {
    if (e.key === 'Enter'){
       if (parentesisAbiertos > 0) {
            var text = msgEnter.value.toString();
            gbText+= text;
            var count = 0;
            while (count < parentesisAbiertos) {
                document.getElementById("interpreterCode").value+="\t";
                count++;
            }
            gbText=""
            //line_counter2();
        }
    }else if (e.key === 'Backspace') {
        if (lastKey == '{'){
            parentesisAbiertos--;
        }
        lastKey = msgEnter.value.toString().slice(-1);
        console.log("Parentesis abiertos: ", parentesisAbiertos);
    }
});

interpreterCodeTxt.addEventListener('keypress', async function (e) {
     lastKey = e.key;

     if(e.key === '{') {
        parentesisAbiertos++;
        parentesisUsado = true;

     }else if(e.key === '}') {
        if(parentesisAbiertos > 0) {
            parentesisAbiertos--;
        }
     }else if (e.key === 'Enter') {
        if (parentesisAbiertos == 0 && parentesisUsado == false) {

            var text = msgEnter.value.toString();
            gbText+= text;
            console.log("Result: ", result);
            result = "";
            text = text.split("\n").slice(saltosIgnorar, )[0];
            console.log("El texto:", text);

            eel.startInterpreter(text);
            showConsoleWithEnter();
        }else if(parentesisAbiertos==0 && parentesisUsado == true){
            var text = msgEnter.value.toString();
            gbText+= text;
            text = text.split("\n");
            text = text.slice(saltosIgnorar, );
            text = text.join("\n");
            console.log("El texto ->", text);
            eel.startInterpreter(text);
            showConsoleWithEnter();
        }
        console.log("Saltos a ignorar: ", saltosIgnorar);
    }
});