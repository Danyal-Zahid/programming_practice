def find_repeated_sequences(s, k):
    if len(s) < k:
        return set()
    result = set()
    _map = {}
    i = j = 0
    window = ""
    while True:
        if i == 0:
            while j < k:
                window += s[j]
                j += 1
            _map[window] = 1
            i += 1
        else:
            if j >= len(s) or j - i != k - 1:
                break
            window = s[i:j] + s[j]
            if window in _map:
                _map[window] += 1
            else:
                _map[window] = 1
            i += 1
            j += 1
    for key in _map:
        if _map[key] > 1:
            result.add(key)
    return result

print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 8))

