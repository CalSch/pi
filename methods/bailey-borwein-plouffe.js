// name: Bailey-Borwein-Plouffe
// desc: Calculating pi with the Bailey-Borwein-Plouffe formula
// url: https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

function sumFunc(k) {
    return (1/16**k) * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6));
}
function calcPi(depth) {
    let sum=0;
    for (let i=0;i<depth;i++) {
        sum+=sumFunc(i);
    }

    return sum;
}

// console.log(calcPi(100))
