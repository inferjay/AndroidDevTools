Array.prototype.randomDiffElement = function (last) {
    if (this.length == 0) {
        return;
    } else if (this.length == 1) {
        return this[0];
    } else {
        var num = 0;
        do {
            num = Math.floor(Math.random() * this.length);
        } while (Array.isArray(last) ? last.includes(this[num]) : this[num] == last);
        return this[num];
    }
};
var isShow = function isShow(value) {
    return value && value.isshow;
};
var now = new Date().getTime();
var isExpired = function (item) {
    let start = Date.parse(item.start_time);
    let end = Date.parse(item.end_time);
    return item && start <= now && now <= end;
};