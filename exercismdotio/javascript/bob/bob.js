//
// This is only a SKELETON file for the "Bob" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Bob = function() {};

Bob.prototype.hey = function(input) {
    input = input.trim();

    if (input === '') {
        return 'Fine. Be that way!';
    }

    if (input === input.toUpperCase() && input.match(/[A-Za-z\u00C0-\u017F]/)) {
        return 'Whoa, chill out!';
    }

    if (input[input.length - 1] === '?') {
        return 'Sure.';
    }

    return 'Whatever.';
};

module.exports = Bob;
