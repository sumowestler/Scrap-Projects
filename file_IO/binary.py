# Thing to keep in mind is that strings and
#
# integers cannot be directly written to a binary file.

# with open("binary", 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))
#   A more concise way to write a basic binary file.

# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#
#         # 'b' must precede the mode to specify binary file status. The bytes function converts our integers to bytes
#         # for storage in the binary file.
#         # the .write method must be used when writing to a binary file.
#
# with open("binary", 'br') as bin_file:
#     for b in bin_file:
#         print(b)

a = 65534  # FF EE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
d = 2998302  # 00 2D C0 1E

with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))  # .t0_bytes method converts larger integers to bytes.
    bin_file.write(b.to_bytes(2, 'big'))  # Above 65535, computer needs 3 bytes to store a value.
    bin_file.write(c.to_bytes(4, 'big'))  # We use even numbers for size, so 4.
    bin_file.write(
        d.to_bytes(4, 'big'))  # Big notation means that the m ost significant parts of the number are encoded first
    bin_file.write(d.to_bytes(4, 'little'))  # Little is the opposite.

# Reading from a binary file.
# .from_bytes method is used to translate a number into an int or string.
# .read
with open('binary2', 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'little')
    print(i)
