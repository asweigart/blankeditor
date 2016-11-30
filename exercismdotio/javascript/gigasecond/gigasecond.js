var Gigasecond = function(startDate) {
    this.startDate = startDate;
};

Gigasecond.prototype.date = function() {
    var billionSecondsLater = new Date(this.startDate);

    billionSecondsLater.setSeconds(billionSecondsLater.getSeconds() + 1000000000);

    return billionSecondsLater;
};

module.exports = Gigasecond;