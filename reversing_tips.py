import binascii

#Tip 1: Hex encoding Binary Data

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

#Tip 2:  Byte strings are not Strings

string_example = "test"
byte_array_example = b"test"

# Convert string into bytes
print(string_example.encode('utf-8'))

# Convert byte array into string
print(byte_array_example.decode('utf-8'))

example_data = b'\x02\x00\x00\x00\x00\x04\x00\x00\x00test\x01\x04\x00\x00\x00t\x00e\x00s\x00t\x00'
#This is the hex encoding of the example data structure shown below

print("This is hex encoded data: %r" % tohex(example_data))

#Tip 3: Use Struct to convert between data and types

'''
Example Data Structure

struct strings{
DWORD number_of_strings;
string* string;
}

struct string{
BOOL is_wide_string;
DWORD string_length;
chr* string;
}
'''
import struct
#The line below will grab the first DWORD (32 bits) from the example struct above which was hex encoded as "example_data"
#The first four bytes (32 bits) will be decoded using the stuct library using the format, little endian "<" and unsigned int "I"
#The result will be the first portion of the struct.
#Using string slicing we grab the first 4 bytes ":4" and [0] states we only want the first result, in case there were more unsigned ints that were found
number_of_strings = struct.unpack('<I',example_data[:4])[0]
print("Number of strings: %d" % number_of_strings)

#Tip 5: Use Custom struct class to parse binary data

import struct

example_string_2 = b'\x00\x04\x00\x00\x00test'
#This is bytes 5 - 9 of the example structure above

class EXAMPLE_STRING:
    def __init__(self):
        self.is_wide_string = False
        self.string_length = 0
        self.string = b''
    def from_buffer_copy(self, data):
        ptr = 0
        self.is_wide_string = struct.unpack('?', data[ptr:ptr+1])[0]
        ptr += 1
        self.string_length = struct.unpack('<I', data[ptr:ptr+4])[0]
        ptr += 4
        if self.is_wide_string:
            self.string = data[ptr:ptr+(self.string_length*2)].decode('utf-16le')
            ptr += self.string_length*2
        else:
            self.string = data[ptr:ptr+self.string_length].decode('utf-8')
            ptr += self.string_length
    def pack(self):
        data = b''
        data += struct.pack('?', self.is_wide_string)
        data += struct.pack('<I', self.string_length)
        if self.is_wide_string:
            data += self.string.encode('utf-16le')
        else:
            data += self.string.encode('utf-8')
        return data

print("Example string data: %r" % example_string_2)
es = EXAMPLE_STRING()
es.from_buffer_copy(example_string_2)
print("Example is wide: %s" % es.is_wide_string)
print("Example string length: %d" % es.string_length)
print("Example string: %s" % es.string)

es.is_wide_string = True
print("Example string data converted to wide: %r" % es.pack())

