
var msg = document.getElementById('simpleCode');


async function showConsoleResults(){
  result =await eel.getConsoleResult()();
  document.getElementById('interpreterCode').value = result ;

}
document.getElementById('compileButton').addEventListener('click',async()=>{
  await eel.startInterpreter(this.msg.value);
  showConsoleResults();

});


function checkMode(checkBox) {
  bodyCont = document.getElementsByTagName("body")[0];
  header = document.getElementById("headerCont");
  files = document.getElementById("filesCont");
  compileButton = document.getElementById("compileButton");
  btnNewFile = document.getElementById("btnNewFile");
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

    files.style.backgroundColor = "white";
    files.style.color = "black";
    btnNewFile.setAttribute("stroke", "black");
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

    files.style.backgroundColor = "#06071d";
    files.style.color = "white";
    compileButton.style.backgroundColor = "#06071d";
    compileButton.style.color = "white";

    btnNewFile.setAttribute("stroke", "white");
    btnUploadfile.setAttribute("stroke", "white");

    simpleCode.style.backgroundColor = "#06071d";
    simpleCode.style.color = "white";

    interpreter.style.backgroundColor = "#06071d";
    interpreter.style.color = "white";
  }
}

