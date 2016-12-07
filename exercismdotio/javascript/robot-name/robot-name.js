

var Robot = function() {
    this.reset();
};

Robot.prototype.reset = function() {
    if (Math.floor(Math.random() * 2) === 0) {
        this.name = this.nextName();
    } 
    else {
        this.nextName();
        this.name = this.nextName();
    }

};

Robot.prototype.nextName = function() {
    
    var nameToReturn = Robot.nextName;

    // generate a new name
    var letterPart = Robot.nextName.slice(0, 2);
    var numberPart = Number(Robot.nextName.slice(2, 5));

    // increment the nextName
    numberPart += 1;

    // check for roll over
    if (numberPart === 1000) {
        numberPart = 0;
        letterPart = this.nextLetters(letterPart);
        Robot.nextName = letterPart + pad(numberPart, 3);
    }
    else {
        Robot.nextName = letterPart + numberPart;
    }
    return nameToReturn;
};


Robot.prototype.nextLetters = function(currentLetters) {
    if (currentLetters === 'ZZ') {
        return 'AA';
    }

    var firstLetter = currentLetters[0];
    var secondLetter = currentLetters[1];

    if (secondLetter !== 'Z') {
        secondLetter = String.fromCharCode(secondLetter.charCodeAt() + 1);
        return firstLetter + secondLetter;
    }
    else {
        // secondLetter *is* Z, so do the wrap around
        secondLetter = 'A';
        firstLetter = String.fromCharCode(firstLetter.charCodeAt() + 1);
        return firstLetter + secondLetter;
    }
};

Robot.nextName = 'AA000';


function pad(num, size) {
    var s = num+"";
    while (s.length < size) s = "0" + s;
    return s;
}

module.exports = Robot;