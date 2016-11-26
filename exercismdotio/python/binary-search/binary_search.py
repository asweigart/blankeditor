def binary_search(haystack, needle):
    start = 0
    end = len(haystack) - 1

    while start <= end:
        ptr = ((end - start) // 2) + start

        if haystack[ptr] == needle:
            return ptr
        elif start == end:
            raise ValueError
        
        elif needle > haystack[ptr]:
            start = ptr + 1
        elif needle < haystack[ptr]:
            end = ptr - 1
    raise ValueError
