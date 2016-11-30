var DnaTranscriber = function() {};

DnaTranscriber.prototype.toRna = function(dna) {
    rna = '';

    for (var i = 0; i < dna.length; i++) {
        if (dna[i] == 'C') {
            rna += 'G';
        }
        else if (dna[i] == 'G') {
            rna += 'C';
        }
        else if (dna[i] == 'A') {
            rna += 'U';
        }
        else if (dna[i] == 'T') {
            rna += 'A';
        }
    }

    return rna;
};

module.exports = DnaTranscriber;