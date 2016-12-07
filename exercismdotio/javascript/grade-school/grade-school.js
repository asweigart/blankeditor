

var School = function() {
    this.students = {};

};

School.prototype.add = function(studentName, gradeLevel) {
    if (this.students[gradeLevel] === undefined) {
        this.students[gradeLevel] = [];
    }

    this.students[gradeLevel].push(studentName);
    this.students[gradeLevel].sort();
};

School.prototype.roster = function() {
    return this.students;
};


School.prototype.grade = function(gradeLevel) {
    //return this.students[gradeLevel] || [];

    if (this.students[gradeLevel] === undefined) {
        return [];
    }
    else {
        return this.students[gradeLevel];
    }
};

module.exports = School;