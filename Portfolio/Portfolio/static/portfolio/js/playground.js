function dark_light(e) {
  var btn = document.querySelector("#btn");
  var content = document.getElementById("content").style;
  var title = document.getElementById("title").style;
  if (btn.className == "fa-solid fa-sun fa-xl") {
    btn.className = "fa-solid fa-moon fa-xl";
    btn.innerHTML = " Dark";
    btn.style.color = "#000000";
    title.color = "#000000";
    content.color = "#000000";
    content.fontWeight = "bold";
    content.backgroundColor = "#ffffffb9";
  } else {
    btn.className = "fa-solid fa-sun fa-xl";
    title.color = "#ffffff";
    btn.innerHTML = " Light";
    btn.style.color = "#ffffff";
    content.color = "#ffffff";
    content.fontWeight = "bold";
    content.backgroundColor = "#000000b9";
  }
}

function calculate(e) {
  var exp = document.getElementById("exp").value;
  var result = document.getElementById("result");
  var exp_result = eval(exp);
  if (exp_result == undefined) {
    result.innerHTML = "Estava á espera do que?";
  } else {
    result.innerHTML = "Resultado: " + exp_result;
  }
}

function clearExp(e) {
  document.getElementById("exp").value = "";
  document.getElementById("result").innerHTML = "Resultado: 0";
}

function showName(e) {
  var nome = document.getElementById("nome").value;
  var label1 = document.getElementById("nome1");
  var label2 = document.getElementById("nome2");
  var label3 = document.getElementById("nome3");

  if (nome == "" || nome == undefined) {
    label1.innerHTML = "😠";
    label2.innerHTML = "Vá agora a sério, insira um nome";
    label3.innerHTML = "😠";
  } else {
    label1.innerHTML = nome;
    label2.innerHTML = nome;
    label3.innerHTML = nome;
  }
}

function forLabel1(e) {
  var label1 = document.getElementById("nome1");
  var label2 = document.getElementById("nome2");
  var label3 = document.getElementById("nome3");
  var label4 = document.getElementById("nome4");
  var label5 = document.getElementById("nome5");
  var label6 = document.getElementById("nome6");

  if (label2.innerHTML == "🦔") {
    label1.innerHTML = "🦔";
    label2.innerHTML = "";
  } else if (label1.innerHTML == "🦔") {
    label1.innerHTML = "";
    label3.innerHTML = "🦔";
  } else if (label3.innerHTML == "🦔") {
    label5.innerHTML = "🦔";
    label3.innerHTML = "";
  } else if (label5.innerHTML == "🦔") {
    label6.innerHTML = "🦔";
    label5.innerHTML = "";
  } else if (label6.innerHTML == "🦔") {
    label4.innerHTML = "🦔";
    label6.innerHTML = "";
  }
}

function forLabel2(e) {
  var label1 = document.getElementById("nome1");
  var label2 = document.getElementById("nome2");
  var label3 = document.getElementById("nome3");
  var label4 = document.getElementById("nome4");

  if (label4.innerHTML == "🦔") {
    label4.innerHTML = "";
    label1.innerHTML = "🎉";
    label3.innerHTML = "🎉";
    label2.innerHTML = "PARABÉNS, CONSEGUIU CAPTURAR O OURIÇO!!";
  }
}

function clearOurico(e) {
  var label1 = document.getElementById("nome1");
  var label2 = document.getElementById("nome2");
  var label3 = document.getElementById("nome3");
  var label4 = document.getElementById("nome4");
  document.getElementById("nome").value = "";
  label1.innerHTML = "";
  label2.innerHTML = "🦔";
  label3.innerHTML = "";
  label4.innerHTML = "";
}

function dataAtual(e) {
  const today = new Date();
  monName = new Array(
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
  );
  var labelData = document.getElementById("labelData");
  labelData.innerHTML =
    today.getDay() +
    " de " +
    monName[today.getMonth()] +
    ", " +
    today.getFullYear();
}
