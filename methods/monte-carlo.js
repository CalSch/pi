// name: Monte Carlo method
// desc: Calculating pi by making many random points in a square, and finding if they are inside a circle<br>The ratio of circle points to total points should be close to 4 pi

function calcPi(points) {
    let totalPoints=0;
    let pointsInCircle=0;

    for (let i=0;i<points;i++) {
        let x=Math.random();
        let y=Math.random();
        let inCircle=Math.hypot(x,y)<1;
        totalPoints++;
        pointsInCircle+=inCircle;
    }

    return pointsInCircle/totalPoints*4
}