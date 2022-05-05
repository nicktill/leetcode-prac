Array.prototype.myMap = function (callback) {
    const list = [];
    for (let i = 0; i < this.length; i++) {
        list.push(callback(this[i], i, this));
    }
    return list;
}

Array.prototype.myFilter = function (callback) {
    const list = [];
    for (let i = 0; i < this.length; i++) {
        if (callback(this[i], i, this) === true) {
            list.push(this[i]);
        }
    }
    return list;
};

Array.prototype.myReduce = function (callback, initialValue) {
    let accummulator = initialValue;
    for (let i = 0; i < this.length; i++) {
        if (i === 0 && initialValue === undefined) {
            accummulator = this[i];
        }
        else {
            accummulator = callback(accummulator, this[i], i, this)
        }
    }
    return accummulator;
}
