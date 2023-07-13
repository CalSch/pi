// name: Simon Plouffe formula
// desc: The infinite sum of an equation that's too long to put here
// url: https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Digit_extraction_methods

function factorial(n) {
    let prod=1;
    for (let i=2;i<n+1;i++) {
        prod*=i;
    }
    return prod
}
function sumFunc(n) {
    return (n * 2**n * factorial(n)**2) / (factorial(2 * n));
}
function calcPi(depth) {
    let sum=-3;
    for (let i=0;i<depth;i++) {
        sum+=sumFunc(i);
    }

    return sum;
}

// console.log(calcPi(40))