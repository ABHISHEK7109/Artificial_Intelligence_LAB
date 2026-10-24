
# Backward Chaining Algorithm

def backward_chaining(facts, rules, goal):
    facts = set(facts)

    # If goal is already a known fact
    if goal in facts:
        return True

    # Check rules that can prove the goal
    for conditions, conclusion in rules:
        if conclusion == goal:

            # Try to prove every condition
            if all(backward_chaining(facts, rules, condition)
                   for condition in conditions):
                print("Proved:", goal)
                return True

    # Goal could not be proved
    return False


# Initial facts
facts = ["A", "B"]

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

# Goal to prove
goal = "E"

print("Initial facts:", facts)
print("Goal:", goal)

if backward_chaining(facts, rules, goal):
    print("Goal achieved:", goal)
else:
    print("Goal cannot be proved:", goal)
