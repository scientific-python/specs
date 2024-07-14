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

PEP8 and other established styling documents do not include guidelines about
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
referred to as explicit subexpressions of  the whole expression, and `1` and
`i + 1` are explicit subexpressions of the expression `range(1, i + 1)`. `i` and
`1` are "implicit" subexpressions of `i + 1`: they could be written as explicit
subexpressions `(i)` and `(1)` without affecting the order  of operations, but they
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
- `x * y + z` is a compound expression; there are two operators and no explicit
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

The following rules are not imagined to be all encompassing, and there may be
syntactically valid cases in which the following rules would lead to contradictions.
Nonetheless, we expect them to be useful in most cases, and projects that adopt the
SPEC endeavor to use them where practical. These rules are intended to respect and
complement the PEP8 rules (relevant sections includes [id20](https://www.python.org/dev/peps/pep-0008/#id20) 
and [id28](https://www.python.org/dev/peps/pep-0008/#id28)).

0. Unless required by other rules, rely on the implicit order of operations;
   i.e., do not add extraneous parentheses. For example, prefer `u**v + y**z`
   over `(u**v) + (y**z)`, and prefer `x + y + z` over `(x + y) + z`.
1. Always use the `**` operator and unary `+`, `-`, and `~` operators *without*
   surrounding whitespace. For example, prefer `-x**4` over `- (x ** 4)`. 
2. Always surround non-PEMDAS operators with whitespace, and always make the priority of
   non-PEMDAS operators explicit, even if the parentheses are consistent with the
   implicit order of operations. For example, prefer `(x == y) or (w == t)` over
   `x==y or w==t`.[^1]
3. Always surround AS operators with whitespace.
4. Typically surround MD operators with whitespace, except when there are lower-priority 
   operators (namely AS) within the same compound expression or the division operation
   would be written mathematically as a fraction with a horizontal bar.
   For example, prefer `z = -x * y**t` over `z = -x*y**t`, but
   prefer `z = w + x*y**t` over `z = w + x * y**t` due to the presence of the
   lower-priority addition operator. Also, prefer `z = t/v * x/y` over
   `z = t / v * x / y` if this would  be written mathematically as the product of
   two fractions.
5. According to the other rules, only `**`, `*`, `/`, and the unary `+`, `-`, and `~`
   operators can appear in implicit subexpressions without spaces. In such expressions,
   - Include unary operators at the left, and use at most one within an implicit
     subexpression without spaces. 
   - Include `**` operators at the right, and use at most one within an implicit
     subexpression without spaces.
  
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
6. When breaking lines at operators, always include the operator at the beginning
   of the new line rather than at the end of the old line, and use parentheses if
   needed to allow for implicit rather than explicit line breaks. For example, if
   `x + y` must be broken, prefer
   ```python3
   (x
    + y)
   ```
   over
   ```python3
   x + \
   y
   ```
7. If required to satisfy other style requirements, include line breaks between
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
   be placed at the operator with lowest priority. For example, if
   (x + y*z) must be broken, prefer
   ```
   (x
    + y*z)
   ```
   over
   ```
   (x + y
    * z)
   ```
   If there are multiple candidates, include the break at the first opportunity.
9. All preceeding rules may be broken if there is a clear reason to do so. Examples include:
   - They conflict with other style rules. For example, there is not supposed to be
     whitepace surrounding the `**` operator, but one can imagine a chain of `**`
     operations that exhausts the character limit of a line.
   - Domain knowledge suggests a reason. For instance, in the expression
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

[^1]: There is a case for simply eliminating spaces to reinforce the implicit order
      of operations, as in `x==y or w==t`. However, if this were the rule, following
      the rule would require users to remember the full order of operations hierarchy
      and apply it without mistakes. Use of explicit parentheses with non-PEMDAS
      operators leads to simpler rules, is more explicit, and is not uncommon in
      existing code.
