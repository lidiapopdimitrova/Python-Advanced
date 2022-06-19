text = input()

symbols = {}

for ch in text:
    if ch in symbols:
        symbols[ch] += 1
    else:
        symbols[ch] = 1

for char, times_found in sorted(symbols.items()):
    print(f"{char}: {times_found} time/s")
