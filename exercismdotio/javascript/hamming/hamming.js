var Hamming = function() {};

Hamming.prototype.compute = function(string1, string2) {
    if (string1.length !== string2.length) {
        throw new Error('DNA strands must be of equal length.');
    }

    var hammingDistance = 0;
    for (var i = 0; i < string1.length; i++) {
        if (string1[i] !== string2[i]) {
            hammingDistance++;
        }
    }

    return hammingDistance;
};

module.exports = Hamming;