lines = [x for x in open('day18/0.in').read().splitlines()]


# Apply order of operations rules on expression with no parens.
def evaluate(expr):
    output = 1
    parts = expr.split()
    while '+' in parts:
        add_idx = parts.index('+')
        sub = int(parts[add_idx - 1]) + int(parts[add_idx + 1])
        parts = parts[:add_idx - 1] + [str(sub)] + parts[add_idx + 2:]
    for part in parts:
        if part.isnumeric():
            output *= int(part)
    return output


# Find innermost parens, call evaluate() on the contents.
# Repeat until all parens are gone, then call evaluate() one final time.
def parse_and_eval(expr):
    while ')' in expr:
        rt_paren_idx = expr.index(')')
        lt_paren_idx = expr[:rt_paren_idx].rfind('(')
        sub = evaluate(expr[lt_paren_idx + 1:rt_paren_idx])
        expr = expr[:lt_paren_idx] + str(sub) + expr[rt_paren_idx + 1:]

    return evaluate(expr)


part_2 = 0
for line in lines:
    part_2 += parse_and_eval(line)

print(part_2)
