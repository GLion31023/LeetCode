def compress(chars: list[str]) -> int:
    n = len(chars)
    if n == 0:
        return 0

    read, write = 0, 0

    while read < n:
        char = chars[read]
        count = 0

        while read < n and chars[read] == char:
            read += 1
            count += 1

        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(compress(["a", "b", "c"]))
print(compress(["a", "a", "a", "a", "a", "b"]))
print(compress(["a", "a", "a", "a", "b", "a"]))
