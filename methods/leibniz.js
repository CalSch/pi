// name: Leibniz series
// desc: Calculating pi with the Leibniz series
// url: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

function calcPi(depth) {
    let sum=0;
    for (let i=0;i<depth;i++) {
        let x=1/(i*2+1)
        if (i%2)
            sum-=x;
        else
            sum+=x;
    }

    return sum*4;
}

// console.log(calcPi(5_000_000_000))