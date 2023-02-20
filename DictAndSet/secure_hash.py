import hashlib

# print(sorted(hashlib.algorithms_guaranteed))
# print(sorted(hashlib.algorithms_available))

python_program = """for i in range(10):
print(i)
"""
print(python_program)

# for b in python_program.encode('utf8'):
#     print(b, chr(b))    # prints encoded values.

original_hash = hashlib.sha3_256(python_program.encode('utf8'))
# How to generate a hash using hashlib.
print("SHA256: {}".format(original_hash.hexdigest()))
# The hexdigest method produces a hexadecimal representation of the
# secure hash.
# once we have this representation, we can use it to see if the original
# data has been modified through comparison.

python_program += "print('code change')"
print(python_program)

new_hash = hashlib.sha3_256(python_program.encode('utf8'))
print()
print("SHA256:{}".format(new_hash.hexdigest()))

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed.")
else:
    print("The code has been modified")
