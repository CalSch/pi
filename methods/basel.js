// name: Basel Problem
// desc: The infinite sum of 1/(num<sup>2</sup>)
// url: https://en.wikipedia.org/wiki/Basel_problem
function calcPi(depth) {
    let sum=0;
    for (let i=1;i<depth;i++) {
        sum += 1/(i**2);
    }

    return Math.sqrt(6*sum);
}
