---
title: "SPEC 12 — Formatting mathematical expressions"
number: 12
date: 2024-06-06
author:
  - "Pamphile Roy <roy.pamphile@gmail.com>"
  - "Matt Haberland <mhaberla@calpoly.edu>"
discussion: https://discuss.scientific-python.org/t/spec-12-formatting-mathematical-expressions
endorsed-by:
---

## Description

[PEP 8](https://peps.python.org/pep-0008)
and other established styling documents do not include guidelines about
styling mathematical expressions. This leads to individual interpretation and
styles which may conflict with those of others. We seek to standardizing the
way we represent mathematics for the same reason we standardize other code:
it brings consistency to the ecosystem and allows collaborators to focus on
more important aspects of the code.

This SPEC standardize the formatting of mathematical expressions.

## Terminology

An "explicit" expression is a code expression enclosed within parentheses or
otherwise syntactically separated from other expressions (i.e. by code other
than operators, whitespace, literals, or variables). For example, in the list
comprehension:

```python3
for j in range(1, i + 1)
```

The output expression `j` is one explicit expression and the input sequence
`range(1, i + 1)` is another.

A "subexpression" is subset of an expression that is either explicit or could
be made explicit (i.e. with parentheses) without affecting the order of
operations. In the example above, `j` and `range(1, i + 1)` can also be
referred to as explicit subexpressions of the whole expression, and `1` and
`i + 1` are explicit subexpressions of the expression `range(1, i + 1)`. `i` and
`1` are "implicit" subexpressions of `i + 1`: they could be written as explicit
subexpressions `(i)` and `(1)` without affecting the order of operations, but they
are not explicit as written.

As another example, in `x + y*z`, `y*z` is a subexpression because it could be made
explicit as in `x + (y*z)` without changing the order of operations. However, `x + y`
would not be a subexpression because `(x + y)*z` would change the order of operations.
Note that `x + y*z` as a whole may also be referred to as a "subexpression" rather than
an "expression" even though `(x + y*z)` is not a proper subset of the whole.

A "simple" expression is an expression involving only one operator priority level
without considering the operators within explicit subexpressions.
A "compound" expression is an expression involving more than one operator
priority level without considering the contents of explicit subexpressions.
For example,

- `x + y - z` is a simple expression because `+` and `-` have the
  same priority level. There are no explicit subexpressions to be ignored.
- `x * (y + z)` is also a simple expression because there is only one operator
  between `x` and the explicit subexpression `(y + z)`; we ignore the contents - and
  especially the operator - within the explicit subexpression; conceptually, it may
  regarded as `(...)`.
- `x*y + z` is a compound expression; there are two operators and no explicit
  subexpressions that can be ignored.

The acronym PEMDAS commonly refers to "parentheses", "exponentiation", "multiplication",
"division", "addition", and "subtraction". Herein, we will consider these operators
to be "PEMDAS operators", and we will also include the unary `+`, `-`, and `~` in
this category for convenience. The order of operations of PEMDAS operators is typically
taught in primary school and reinforced throughout a programmer's training and
experience, so it is assumed that most programmers are comfortable relying on the
implicit order of operations of expressions involving a few PEMDAS operations. Implicit
order of operations becomes less obvious as the number of distinct operator priority
levels increases and when multiple non-PEMDAS operators are involved. Portions of this
acronym, namely MD and AS, will be used below to refer to the corresponding operators.

## Implementation

These rules are intended to respect and
complement the [PEP 8 standards](https://peps.python.org/pep-0008), such as using
[implied line continuation](https://peps.python.org/pep-0008/#maximum-line-length) and
and [breaking lines before binary operators](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator).
Although examples do not show the use of hanging indent, any of the indentation styles
allowed by [PEP 8 Indentation](https://peps.python.org/pep-0008/#indentation) are
permitted by this SPEC.

0. Unless otherwise specified, rely on the implicit order of operations;
   i.e., do not add extraneous parentheses. For example, prefer `u**v + y**z`
   over `(u**v) + (y**z)`, and prefer `x + y + z` over `(x + y) + z`. A full
   list of implicit operator priority levels is given by
   [Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
1. Always use the `**` operator and unary `+`, `-`, and `~` operators _without_
   surrounding whitespace. For example, prefer `-x**4` over `- (x ** 4)`.
2. Always surround non-PEMDAS operators with whitespace, and always make the priority of
   non-PEMDAS operators explicit. For example, prefer `(x == y) or (w == t)` over
   `x==y or w==t`.[^1]
3. Always surround AS operators with whitespace.
4. Typically, surround MD operators with whitespace, except in the following situations.
   - When there are lower-priority operators (namely AS) within the same compound
     expression. For example, prefer `z = -x * y**t` over `z = -x*y**t`, but
     prefer `z = w + x*y**t` over `z = w + x * y**t` due to the presence of the
     lower-priority addition operator.
   - The division operation would be written mathematically as a fraction with a
     horizontal bar. For example, prefer `z = t/v * x/y` over `z = t / v * x / y`
     if this would be written mathematically as the product of two fractions,
     e.g. $\frac{t}{v} \cdot \frac{x}{y}$.
5. Considering the previous rules, only `**`, `*`, `/`, and the unary `+`, `-`, and `~`
   operators can appear in implicit subexpressions without spaces. In such expressions,

   - Use at most one unary operator, and if used, ensure that it is the leftmost operator.
   - Use at most one `**` operator, and if used, ensure that it is the rightmost operator.
   - Use at most one `/` operator, and if used, ensure that it is the rightmost operator except for `**`.

   To achieve these goals, simplification or the addition of parentheses may be required.
   For example:

   - The expressions `--x` and `-~x` would be implicit subexpressions without spaces
     containing more than one unary operator. The former can be simplified to `+x` or
     simply `x`, and the latter requires explicit parentheses, i.e. `-(~x)`.
   - The expression `x**y**z` would be an implicit subexpression without spaces
     containing more than one `**` operator. This code would be executed as `x**(y**z)`
     following the implicit order, but the explicit parentheses should be included for
     clarity.
   - In the expression `t**v*x**y + z`, no spaces are used around the multiplication
     operator due to the presence of the lower-priority addition operator. However,
     this would lead to `t**v*x**y` being an implicit subexpression without spaces
     containing more than one `**` operator. This code would be executed as
     `(t**v)*(x**y) + z`, but the explicit parentheses should be included for clarity.
   - In the expression `z + x**y/w`, no spaces are used around the division operator
     due to the presence of the lower-priority addition operator. However, this would
     lead to `x**y/w` being an implicit subexpression without spaces containing `**`
     to the left of another operator. Options for refactoring include the addition of
     parentheses (e.g. `z + (x**y)/w`) or pre-multiplying the exponential by a
     fraction (i.e. `x + 1/w*x**y`).

6. Simplify combinations of unary and binary `+` and `-` operators when possible.
   For example,
   - prefer `x + y` over `x + +y`,
   - prefer `x + y` over `x - -y`,
   - prefer `x - y` over `x - +y`, and
   - prefer `x - y` over `x + -y`.
7. If required to satisfy other style requirements, include line breaks before
   the outermost explicit subexpression possible. For example, if
   `t + (w + (x + (y + z))))` must be broken, prefer
   ```python3
   (t
    + (w + (x + (y + z)))))
   ```
   over
   ```python3
   (t + (w + (x + (y
                   + z)))))
   ```
   If there are multiple candidates, include the break at the first opportunity.
8. If line breaks must occur within a compound subexpression, the break should
   be placed before the operator with lowest priority. For example, if
   (x + y\*z) must be broken, prefer
   ```python3
   (x
    + y*z)
   ```
   over
   ```python3
   (x + y
    * z)
   ```
   If there are multiple candidates, include the break at the first opportunity.
9. Any of the preceding rules may be broken if there is a clear reason to do so.
   - _Conflict with other style rules_. For example, there is not supposed to be
     whitespace surrounding the `**` operator, but one can imagine a chain of `**`
     operations that exhausts the character limit of a line.
   - _Domain knowledge_. For instance, in the expression
     `t = (x + y) - z`, it may be important to emphasize that the addition should be
     performed first for numerical reasons or because `(x + y)` is a conceptually
     important quantity. In such cases, consider adding a comment, e.g.
     ```python3
     t = (x + y) - z  # perform `x + y` first for precision
     ```
     or breaking the expressions into separate logical lines, e.g.
     ```python3
     w = x + y
     t = w - z
     ```

[^1]:
    There is a case for simply eliminating spaces to reinforce the implicit order
    of operations, as in `x==y or w==t`. However, if this were the rule, following
    the rule would require users to remember the full order of operations hierarchy
    and apply it without mistakes. Use of explicit parentheses with non-PEMDAS
    operators leads to simpler rules, is more explicit, and is not uncommon in
    existing code.
