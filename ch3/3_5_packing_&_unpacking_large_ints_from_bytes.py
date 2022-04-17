"""
3.5. Packing and Unpacking Large Integers from Bytes

Problem
    You have a byte string, and you need to unpack it into an integer value. Alternatively,
    you need to convert a large integer back into a byte string.

Solution
    Suppose your program needs to work with a 16-element byte string that holds a 128-
    bit integer value. For example:
"""
import struct

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'


def pack_unpack_bytes_to_int():
    print(len(data))  # 16
    print(int.from_bytes(data, "little"))  # 69120565665751139577663547927094891008
    print(int.from_bytes(data, "big"))  # 94522842520747284487117727783387188
    print("*"*20)


def pack_unpack_int_to_bytes():
    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, "big"))  # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(x.to_bytes(16, "little"))  # b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'
    print("*" * 20)


def pack_unpack_w_struct():
    """
    Discussion

    Converting large integer values to and from byte strings is not a common operation.
    However, it sometimes arises in certain application domains, such as cryptography or
    networking. For instance, IPv6 network addresses are represented as 128-bit integers.
    If you are writing code that needs to pull such values out of a data record, you might
    face this problem.

    As an alternative to this recipe, you might be inclined to unpack values using the struct
    module, as described in Recipe 6.11. This works, but the size of integers that can be
    unpacked with struct is limited. Thus, you would need to unpack multiple values and
    combine them to create the final value. For example:

    """
    hi, lo = struct.unpack(">QQ", data)
    print((hi << 64) + lo)  # 94522842520747284487117727783387188

    def big_little(num, b, num_type):
        return num.to_bytes(b, num_type)

    x = 0x01020304
    print(big_little(x, 4, "big"))  # b'\x01\x02\x03\x04'
    print("*" * 20)


def pack_large_num_to_bytes():
    x = 532 ** 23
    print(x)
    print(x.bit_length())  # 209

    n_bytes, rem = divmod(x.bit_length(), 8)
    n_bytes += 1 if rem else None

    print(x.to_bytes(n_bytes, "little"))  # b'\x00\x00\x00\x00\x00@[\xb7-\xce\x1c\x10?\xf92\x1fC\x07^\x08\xa43\x0e\xcf\x015\x01'


if __name__ == "__main__":
    pack_unpack_bytes_to_int()
    pack_unpack_int_to_bytes()
    pack_unpack_w_struct()
    pack_large_num_to_bytes()
