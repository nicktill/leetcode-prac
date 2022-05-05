
//AlgoExpert, Front-End Expert 
Array.prototype.myMap = function (callback) {
    const list = [];
    for (let i = 0; i < this.length(); i++) {
        let value = callback(this[i], i, this)
        list.push(value);
    }
}

Array.prototype.myFilter = function (callback) {
    // Write your code here.
}

Array.prototype.myReduce = function (callback, initialValue) {
    // Write your code here.
}
