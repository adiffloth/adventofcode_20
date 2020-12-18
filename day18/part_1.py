lines = [x for x in open('day18/0.in').read().splitlines()]


# Apply order of operations rules on expression with no parens.
def evaluate(expr):
    parts = expr.split()
    output = int(parts[0])
    op = ''
    for part in parts[1:]:
        if part.isnumeric():
            if op == '+':
                output += int(part)
            elif op == '*':
                output *= int(part)
            else:
                raise(ValueError)
        else:
            op = part

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


part_1 = 0
for line in lines:
    part_1 += parse_and_eval(line)

print(part_1)
