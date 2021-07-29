def test_newid(id):
    assert newid("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
    assert newid("z-+.^.") == "z--"
    assert newid("=.=") == "aaa"
    assert newid("123_.def") == "123_.def"
    assert newid("abcdefghijklmn.p") == "abcdefghijklmn"