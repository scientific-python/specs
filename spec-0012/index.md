---
title: "SPEC 12 — Formatting mathematical expressions"
number: 12
date: 2024-06-06
author:
  - "Pamphile Roy <roy.pamphile@gmail.com>"
discussion: https://discuss.scientific-python.org/t/spec-12-formatting-mathematical-expressions
endorsed-by:
---

## Description

It is known that the PEP8 and other established styling documents are missing
guidelines about mathematical expressions. This leads to people coming with
their own interpretation and style. Standardizing the way we represent maths
would lead to the same benefits seen with "normal" code. It brings consistency
in the ecosystem improving the collaborative efforts.

This SPEC standardize the formatting of mathematical expressions.

## Implementation

The following rules must be followed.
These rules respect and complement the PEP8 (relevant sections includes
[id20](https://www.python.org/dev/peps/pep-0008/#id20) and
[id20](https://www.python.org/dev/peps/pep-0008/#id28)).

We define a _group_ as a collection of operators having the same priority.
e.g. `a + b + c` is a single group, `a + b * c` is composed of two groups `a`
and `b * c`. A group is also a collection delimited with parenthesis.
`(a + b * c)` is a group. And the whole expression by itself is a
group. 

- There a space before and after `-` and `+`. Except if
  the operator is used to define the sign of the number;

  ```
  a + b
  -a
  ```

- Within a group, if operators with different priorities are used, add whitespace around the operators with the lowest priority(ies).

  ```
  a + b*c
  ```

- There is no space before and after `**`.

  ```
  a**b
  ```

- There is no space before and after operators `*` and `/`. Only exception is if the expression consist of a single operator linking two groups with more than one
 element.

  ```
  a*b
  (a*b) * (c*d)
  ```

- Operators within a group are ordered from the lowest to the highest priority.
  If this is technically an issue (e.g. restriction on the AST), add
  parenthesis or spaces.

  ```
  a/d*b**c
  a*(b**c)/d
  a*b**c / d
  a * b**c / d
  ```

- When splitting an equation, new lines should start with the operator linking
  the previous and next logical block. Single digit on a line are forbidden.

  ```
  (
      a/b
      + c*d
  )
  ```

### Examples

```python
# good
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a + b) * (a - b)
dfdx = sign*(-2*x + 2*y + 2)
result = 2*x**2 + 3*x**(2/3)
y = 4*x**2 + 2*x + 1
c_i1j = (
    1./n**2.
    *np.prod(
        0.5*(2. + abs(z_ij[i1, :]) + abs(z_ij) - abs(z_ij[i1, :] - z_ij)), axis=1
    )
)
```

```python
# bad
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
dfdx = sign * (-2 * x + 2 * y + 2)
result = 2 * x ** 2 + 3 * x ** (2 / 3)
y = 4 * x ** 2 + 2 * x + 1
c_i1j = (
    1.0
    / n ** 2.0
    * np.prod(
        0.5 * (2.0 + abs(z_ij[i1, :]) + abs(z_ij) - abs(z_ij[i1, :] - z_ij)), axis=1
    )
)
```

## Notes

These formatting rules do not make any consideration in terms of performances
nor precision. The scope is limited to styling.
