def unicode_strings(buf, n=4):
    import re
    ASCII_BYTE = b' !\"#\$%&\'\(\)\*\+,-\./0123456789:;<=>\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\[\]\^_`abcdefghijklmnopqrstuvwxyz\{\|\}\\\~\t'
    if type(buf) == str:
        buf = buf.encode('utf-8')
    reg = b'((?:[%s]\x00){%d,})' % (ASCII_BYTE, n)
    uni_re = re.compile(reg)
    out = []
    for match in uni_re.finditer(buf):
        try:
            out.append(match.group().decode("utf-16"))
        except UnicodeDecodeError:
            pass
    return out


def ascii_strings(buf, n=4):
    import re
    ASCII_BYTE = b' !\"#\$%&\'\(\)\*\+,-\./0123456789:;<=>\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\[\]\^_`abcdefghijklmnopqrstuvwxyz\{\|\}\\\~\t'
    if type(buf) == str:
        buf = buf.encode('utf-8')
    reg = b'([%s]{%d,})' % (ASCII_BYTE, n)
    ascii_re = re.compile(reg)
    out = []
    for match in ascii_re.finditer(buf):
        try:
            out.append(match.group().decode("ascii"))
        except UnicodeDecodeError:
            pass
    return out

