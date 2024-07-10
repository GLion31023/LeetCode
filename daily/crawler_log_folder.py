def min_operations(logs: list[str]) -> int:
    depth = 0

    for log in logs:
        if log == "../":
            if depth > 0:
                depth -= 1
        elif log == "./":
            continue
        else:
            depth += 1

    return depth


print(min_operations(["d1/", "d2/", "../", "d21/", "./"]))
print(min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(min_operations(["d1/", "../", "../", "../"]))
