def unhex(hex_string):
    import binascii
    if type(hex_string) == str:
        return binascii.unhexlify(hex_string.encode('utf-8'))
    else:
        return binascii.unhexlify(hex_string)

def tohex(data):
    import binascii
    if type(data) == str:
        return binascii.hexlify(data.encode('utf-8'))
    else:
        return binascii.hexlify(data)

example_data = b'\x02\x00\x00\x00\x00\x04\x00\x00\x00test\x01\x04\x00\x00\x00t\x00e\x00s\x00t\x00'   

print("This is hex encoded data: %r" % tohex(example_data))

