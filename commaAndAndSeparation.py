spam = ["apples", "bananas", "tofu", "cats" ]
print(*spam[:-1], sep=", ", end=" and " + spam[-1])