let argEl = document.getElementById("arg");
let logEl = document.getElementById("log");

function run() {
    let arg = parseInt(argEl.value);

    logEl.innerHTML+=`
Running calcPi(${arg})...
`;

    let start = Date.now();
    let result = calcPi(arg);
    let end = Date.now();

    let duration = end-start;

    logEl.innerHTML+=`Pi: ${result}
Took ${duration}ms
`;
}