import binascii

string_example = "test"
byte_array_example = b"test"

# Convert string into bytes
print(string_example.encode('utf-8'))

# Convert byte array into string
print(byte_array_example.decode('utf-8'))

# Convert string into hex encoded byte array
print(binascii.hexlify(string_example.encode('utf-8')))

# Convert byte array into hex encoded byte array
print(binascii.hexlify(byte_array_example))

# Convert byte array into hex encoded string
print(binascii.hexlify(byte_array_example).decode('utf-8'))

# Convert hex encoded byte array into ascii byte array
hex_byte_array = b'74657374'
print(binascii.unhexlify(hex_byte_array))

# Convert hex encoded string into ascii byte array
hex_string = '74657374'
print(binascii.unhexlify(hex_string.encode('utf-8')))

# Convert hex encoded string into ascii string
hex_string = '74657374'
print(binascii.unhexlify(hex_string.encode('utf-8')).decode('utf-8'))