# Triangle

Write a program that can tell you if a triangle is equilateral, isosceles, or scalene.

The program should raise an error if the triangle cannot exist.

## Hint

The triangle inequality theorem states:
z ≤ x + y
where x,y, and z are the lengths of the sides of a triangle. In other words, the
sum of the lengths of any two sides of a triangle always exceeds or is equal to
the length of the third side.

A corollary to the triangle inequality theorem is there are two classes of
triangles--degenerate and non-degenerate. If the sum of the lengths of any two
sides of a triangle is greater than the length of the third side, that triangle
is two dimensional, has area, and belongs to the non-degenerate class. In
mathematics, a degenerate case is a limiting case in which an element of a class
of objects is qualitatively different from the rest of the class and hence
belongs to another, usually simpler, class. The degenerate case of the triangle
inequality theorem is when the sum of the lengths of any two sides of a triangle
is equal to the length of the third side. A triangle with such qualities is
qualitatively different from all the triangles in the non-degenerate class since
it is one dimensional, looks like a straight line, and has no area. Such
triangles are called degenerate triangles and they belong to the degenerate
class.

## Dig Deeper

This exercise does not test for degenerate triangles. Feel free to add your own
tests to check for degenerate triangles.

### Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `exercism/python/<exerciseName>` directory.

For example, if you're submitting `bob.py` for the Bob exercise, the submit command would be something like `exercism submit <path_to_exercism_dir>/python/bob/bob.py`.


For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

The Ruby Koans triangle project, parts 1 & 2 [http://rubykoans.com](http://rubykoans.com)

## Submitting Incomplete Problems
It's possible to submit an incomplete solution so you can see how others have completed the exercise.

