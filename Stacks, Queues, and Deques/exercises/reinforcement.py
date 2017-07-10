
def transfer(S):
    T = []
    for _ in range(len(S)):
        T.append(S.pop())
    return T


def clear_stack(stack):
    if len(stack) == 0:
        return stack
    stack.pop()
    return clear_stack(stack)