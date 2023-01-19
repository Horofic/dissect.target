from flow.record.fieldtypes import datetime as dt

from dissect.target.helpers.regutil import VirtualKey

try:
    from Crypto.Hash import MD4
    from dissect.target.plugins.os.windows.sam import SamPlugin
    
    HAVE_CRYPTO = True
except ImportError:
    HAVE_CRYPTO = False

sam_key_name = "SAM\\SAM\\Domains\\Account"
system_key_name = "SYSTEM\\ControlSet001\\Control\\LSA"


@pytest.mark.skipif(not HAVE_CRYPTO, reason="requires pycryptodome")
def test_sam_plugin_rev1(target_win_users, hive_hklm):
    sam_key = VirtualKey(hive_hklm, sam_key_name)
    sam_key.add_value(
        "F",
        bytes.fromhex(
            "02000100000000004B0002F43D04CA01290000000000000000000000000000800000000000000000000000000000008000CC1DCFFB"
            "FFFFFF00CC1DCFFBFFFFFF0000000000000000E9030000000000000000000000000000010000000300000001000000000001000100"
            "000038000000A10D031A1D49D44CA0C60A55604DBAE7B4BA33FB39930584CEBF951AE9BFDE94CD9EA0DFCBD3AC729D090B37B8FF55"
            "3D00000000000000000100000038000000B0F0B1D239975E5A88BABF3E972A5007CF3ED4D79E432B1DE9364B38EA1CCC74FC6B0DC8"
            "01BD4B050E034CE7E5A66BE500000000000000000300000000000000"
        ),
    )
    users_key = VirtualKey(hive_hklm, "Users")

    f4_key = VirtualKey(hive_hklm, "000001F4")
    f4_key.add_value(
        "F",
        bytes.fromhex(
            "02000100000000008d0fe8cc2e89cb010000000000000000db05c8343089cb0100000000000000000000000000000000f401000001"
            "020000110200000000000000000600010000000000320039003800"
        ),
    )
    f4_key.add_value(
        "V",
        bytes.fromhex(
            "00000000bc00000002000100bc0000001a00000000000000d80000000000000000000000d80000006c000000000000004401000000"
            "0000000000000044010000000000000000000044010000000000000000000044010000000000000000000044010000000000000000"
            "00004401000000000000000000004401000000000000000000004401000015000000a80000005c0100000800000001000000640100"
            "0004000000000000006801000014000000000000007c0100000400000000000000800100000400000000000000010014809c000000"
            "ac0000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ffff1f000101000000"
            "000005070000000200580003000000000014005b03020001010000000000010000000000001800ff070f0001020000000000052000"
            "00002002000000002400440002000105000000000005150000001b89b25233b573192bacca69f40100000102000000000005200000"
            "002002000001020000000000052000000020020000410064006d0069006e006900730074007200610074006f007200660042007500"
            "69006c0074002d0069006e0020006100630063006f0075006e007400200066006f0072002000610064006d0069006e006900730074"
            "006500720069006e0067002000740068006500200063006f006d00700075007400650072002f0064006f006d00610069006e00ffff"
            "ffffffffffffffffffffffffffffffffffffff000100010200000700000003000100030001002634474c46008cbd7b2fa6c538cd2c"
            "060300010003000100"
        ),
    )
    users_key.add_subkey("000001F4", f4_key)

    f5_key = VirtualKey(hive_hklm, "000001F5")
    f5_key.add_value(
        "F",
        bytes.fromhex(
            "0200010000000000000000000000000000000000000000000000000000000000ffffffffffffff7f0000000000000000f501000001"
            "020000150200000000000000000000000000000000320039003800"
        ),
    )
    f5_key.add_value(
        "V",
        bytes.fromhex(
            "00000000b000000002000100b00000000a00000000000000bc0000000000000000000000bc00000070000000000000002c01000000"
            "000000000000002c01000000000000000000002c01000000000000000000002c01000000000000000000002c010000000000000000"
            "00002c01000000000000000000002c01000000000000000000002c01000000000000000000002c0100000800000001000000340100"
            "0004000000000000003801000004000000000000003c01000004000000000000004001000004000000000000000100148090000000"
            "a00000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ffff1f000101000000"
            "0000050700000002004c0003000000000014001b03020001010000000000010000000000001800ff070f0001020000000000052000"
            "00002002000000001800ff070f00010200000000000520000000240200000102000000000005200000002002000001020000000000"
            "0520000000200200004700750065007300740000004200750069006c0074002d0069006e0020006100630063006f0075006e007400"
            "200066006f0072002000670075006500730074002000610063006300650073007300200074006f002000740068006500200063006f"
            "006d00700075007400650072002f0064006f006d00610069006e00010200000700000003000100030001000300010003000100"
        ),
    )
    users_key.add_subkey("000001F5", f5_key)

    e8_key = VirtualKey(hive_hklm, "000003E8")
    e8_key.add_value(
        "F",
        bytes.fromhex(
            "02000100000000005f526d531e21d90100000000000000005f526d531e21d9010000000000000000bb22ba581e21d901e803000001"
            "020000140000000100e40401000800010000000000000000000000"
        ),
    )
    e8_key.add_value(
        "V",
        bytes.fromhex(
            "00000000bc00000002000100bc0000000800000000000000c40000000000000000000000c40000000000000000000000c400000000"
            "00000000000000c40000000000000000000000c40000000000000000000000c40000000000000000000000c4000000000000000000"
            "0000c40000000000000000000000c40000000000000000000000c400000015000000a8000000dc0000000800000001000000e40000"
            "001400000000000000f800000014000000000000000c0100000400000000000000100100000400000000000000010014809c000000"
            "ac0000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ff070f000101000000"
            "00000507000000020058000300000000002400440002000105000000000005150000001b89b25233b573192bacca69e80300000000"
            "1800ff070f0001020000000000052000000020020000000014005b0302000101000000000001000000000102000000000005200000"
            "0020020000010200000000000520000000200200004a006f0068006e00ffffffffffffffffffffffffffffffffffffffffff000100"
            "0102000007000000030001006ef4147d0bb0ab645af5af17e3eb5772030001004b321ebce975e21151102460c479deb20300010003"
            "000100"
        ),
    )
    users_key.add_subkey("000003E8", e8_key)

    sam_key.add_subkey("Users", users_key)
    hive_hklm.map_key(sam_key_name, sam_key)

    # Create SYSTEM keys
    system_key = VirtualKey(hive_hklm, system_key_name)
    data_key = VirtualKey(hive_hklm, "Data", class_name="6d1ae431")
    system_key.add_subkey("Data", data_key)
    gbg_key = VirtualKey(hive_hklm, "GBG", class_name="1ddbd1f5")
    system_key.add_subkey("GBG", gbg_key)
    jd_key = VirtualKey(hive_hklm, "JD", class_name="5f3df852")
    system_key.add_subkey("JD", jd_key)
    skew1_key = VirtualKey(hive_hklm, "Skew1", class_name="c42b803c")
    system_key.add_subkey("Skew1", skew1_key)
    hive_hklm.map_key(system_key_name, system_key)

    target_win_users.add_plugin(SamPlugin)
    results = list(target_win_users.sam())

    assert len(results) == 3
    assert results[2].rid == 1000
    assert results[2].fullname == ""
    assert results[2].username == "John"
    assert results[2].admincomment == ""
    assert results[2].usercomment == ""
    assert results[2].lastlogin == dt("2023-01-05T15:56:51.654921+00:00")
    assert results[2].lastpasswordset == dt("2023-01-05T15:56:51.654921+00:00")
    assert results[2].lastincorrectlogin == dt("2023-01-05T15:57:00.546938+00:00")
    assert results[2].flags == 20
    assert results[2].countrycode == 1
    assert results[2].failedlogins == 1
    assert results[2].logins == 8
    assert results[2].lm == "b0e5df88ef1c16f1dde347abf49e1d97"
    assert results[2].nt == MD4.new("L0ngLiv3LM!".encode("utf-16-le")).digest().hex()


@pytest.mark.skipif(not HAVE_CRYPTO, reason="requires pycryptodome")
def test_sam_plugin_rev2(target_win_users, hive_hklm):
    sam_key = VirtualKey(hive_hklm, sam_key_name)
    sam_key.add_value(
        "F",
        bytes.fromhex(
            "03000100000000002d1b92bfb821d901020000000000000000000000000000800000000000000000000000000000008000cc1dcffb"
            "ffffff00cc1dcffbffffff0000000000000000e9030000000000000000000000000000010000000300000001000000000001000200"
            "00007000000030000000200000004b903580f1d3d1c080ed5e524152dce5e577c97453495325ca097ef6f9aa033d28cb7a5bdd6e6e"
            "12a1f0f0eb812f72a3d6b4ee5b0cf83ff8cc969f7b17be5ecc3af36a62f2e32eb53404d4b5ff0b446e580e067325fbca89b002f313"
            "956ea315000000000000000000000000000000000200000070000000300000002000000041c297509ef4c3ee93e0aa165ac31b4ee6"
            "f61832de6102735db58a83a7ea225a01a9fefe0fe344cee07fc9c58db7f25bc53503eefcd22a898a4b09efe97bf725ae652f7a66b5"
            "e5ca54ecae35e0d01c8517a4985dfbb7116aa1e49eb304b35efc000000000000000000000000000000000200000000000000"
        ),
    )
    users_key = VirtualKey(hive_hklm, "Users")

    f4_key = VirtualKey(hive_hklm, "000001F4")
    f4_key.add_value(
        "F",
        bytes.fromhex(
            "0300010000000000000000000000000000000000000000000000000000000000ffffffffffffff7f0000000000000000f401000001"
            "020000110200000000000000000000010000000000000000000400"
        ),
    )
    f4_key.add_value(
        "V",
        bytes.fromhex(
            "00000000f400000003000100f40000001a00000000000000100100000000000000000000100100006c000000000000007c01000000"
            "000000000000007c01000000000000000000007c01000000000000000000007c01000000000000000000007c010000000000000000"
            "00007c01000000000000000000007c01000000000000000000007c01000000000000000000007c0100000800000001000000840100"
            "0018000000000000009c0100001800000000000000b40100001800000000000000cc010000180000000000000001001480d4000000"
            "e40000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ffff1f000101000000"
            "000005070000000200900004000000000014005b03020001010000000000010000000000001800ff070f0001020000000000052000"
            "000020020000000038001b030200010a00000000000f0300000000040000dea22867213ed2af19ad5d79b0c107292756fc20d8ad66"
            "f610f268fadf2af80f0000240044000200010500000000000515000000a64ddd54933204de30f57de4f40100000102000000000005"
            "200000002002000001020000000000052000000020020000410064006d0069006e006900730074007200610074006f007200cf3142"
            "00750069006c0074002d0069006e0020006100630063006f0075006e007400200066006f0072002000610064006d0069006e006900"
            "730074006500720069006e0067002000740068006500200063006f006d00700075007400650072002f0064006f006d00610069006e"
            "000102000007000000020002000000000010bfd0433bb0cc289fff5c6f6fbae448020002000000000064bd06a1f999640aa53a7cd5"
            "6e892df60200020000000000400501061d259efa1d58f957a2c4da580200020000000000f3dd8cb513a4e696a56f310c8dca67cb"
        ),
    )
    users_key.add_subkey("000001F4", f4_key)

    f5_key = VirtualKey(hive_hklm, "000001F5")
    f5_key.add_value(
        "F",
        bytes.fromhex(
            "0300010000000000000000000000000000000000000000000000000000000000ffffffffffffff7f0000000000000000f501000001"
            "020000150200000000000000000000000000000000000000000800"
        ),
    )
    f5_key.add_value(
        "V",
        bytes.fromhex(
            "00000000e800000003000100e80000000a00000000000000f40000000000000000000000f400000070000000000000006401000000"
            "0000000000000064010000000000000000000064010000000000000000000064010000000000000000000064010000000000000000"
            "00006401000000000000000000006401000000000000000000006401000000000000000000006401000008000000010000006c0100"
            "0018000000000000008401000018000000000000009c0100001800000000000000b4010000180000000000000001001480c8000000"
            "d80000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ffff1f000101000000"
            "000005070000000200840004000000000014001b03020001010000000000010000000000001800ff070f0001020000000000052000"
            "00002002000000001800ff070f0001020000000000052000000024020000000038001b030200010a00000000000f03000000000400"
            "00dea22867213ed2af19ad5d79b0c107292756fc20d8ad66f610f268fadf2af80f0102000000000005200000002002000001020000"
            "0000000520000000200200004700750065007300740000004200750069006c0074002d0069006e0020006100630063006f0075006e"
            "007400200066006f0072002000670075006500730074002000610063006300650073007300200074006f0020007400680065002000"
            "63006f006d00700075007400650072002f0064006f006d00610069006e0001020000070000000200020000000000da34867f328d08"
            "1d7059314057a74186020002000000000076f4bd93c3dcf52ad2c8f07efca4b71e0200020000000000fbe769a9d0fe610f6ec2dd57"
            "29b24f2e0200020000000000f6647f3b6b820781d3e4c2f3d81cfad5"
        ),
    )
    users_key.add_subkey("000001F5", f5_key)

    f7_key = VirtualKey(hive_hklm, "000001F7")
    f7_key.add_value(
        "F",
        bytes.fromhex(
            "0300010000000000000000000000000000000000000000000000000000000000ffffffffffffff7f0000000000000000f701000001"
            "020000150200000000000000000000000000000000000000000c00"
        ),
    )
    f7_key.add_value(
        "V",
        bytes.fromhex(
            "000000000c010000030001000c0100001c00000000000000280100000000000000000000280100004a000000000000007401000000"
            "0000000000000074010000000000000000000074010000000000000000000074010000000000000000000074010000000000000000"
            "00007401000000000000000000007401000000000000000000007401000000000000000000007401000008000000010000007c0100"
            "001800000000000000940100001800000000000000ac0100001800000000000000c4010000180000000000000001001480ec000000"
            "fc0000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ffff1f000101000000"
            "000005070000000200a80005000000000014005b03020001010000000000010000000000001800ff070f0001020000000000052000"
            "00002002000000001800ff070f0001020000000000052000000024020000000038001b030200010a00000000000f03000000000400"
            "00dea22867213ed2af19ad5d79b0c107292756fc20d8ad66f610f268fadf2af80f0000240044000200010500000000000515000000"
            "a64ddd54933204de30f57de4f701000001020000000000052000000020020000010200000000000520000000200200004400650066"
            "00610075006c0074004100630063006f0075006e00740041002000750073006500720020006100630063006f0075006e0074002000"
            "6d0061006e00610067006500640020006200790020007400680065002000730079007300740065006d002e00a1c401020000070000"
            "0002000200000000005148692f372e35796905b9b71365cd570200020000000000e92a4756fde315c4ddbdd86bcec5964e02000200"
            "00000000bda997d478b6066fc29ee564368f3c8a02000200000000006b79688fbcfd21288ce204ae5f66ba59"
        ),
    )
    users_key.add_subkey("000001F7", f7_key)

    f8_key = VirtualKey(hive_hklm, "000001F8")
    f8_key.add_value(
        "F",
        bytes.fromhex(
            "030001000000000000000000000000000000000000000000cda69bbfb821d901ffffffffffffff7f0000000000000000f801000001"
            "020000110000000000000000000000000000000000000000000000"
        ),
    )
    f8_key.add_value(
        "V",
        bytes.fromhex(
            "000000000c010000030001000c010000240000000000000030010000000000000000000030010000be00000000000000f001000000"
            "00000000000000f00100000000000000000000f00100000000000000000000f00100000000000000000000f0010000000000000000"
            "0000f00100000000000000000000f00100000000000000000000f00100000000000000000000f00100000800000001000000f80100"
            "00180000000000000010020000380000000000000048020000180000000000000060020000180000000000000001001480ec000000"
            "fc0000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ffff1f000101000000"
            "000005070000000200a80005000000000014005b03020001010000000000010000000000001800ff070f0001020000000000052000"
            "00002002000000001800ff070f0001020000000000052000000024020000000038001b030200010a00000000000f03000000000400"
            "00dea22867213ed2af19ad5d79b0c107292756fc20d8ad66f610f268fadf2af80f0000240044000200010500000000000515000000"
            "a64ddd54933204de30f57de4f801000001020000000000052000000020020000010200000000000520000000200200005700440041"
            "0047005500740069006c006900740079004100630063006f0075006e00740041002000750073006500720020006100630063006f00"
            "75006e00740020006d0061006e006100670065006400200061006e0064002000750073006500640020006200790020007400680065"
            "002000730079007300740065006d00200066006f0072002000570069006e0064006f0077007300200044006500660065006e006400"
            "6500720020004100700070006c00690063006100740069006f006e0020004700750061007200640020007300630065006e00610072"
            "0069006f0073002e00000001020000070000000200020000000000dccdb08585b3a61cc050361da76c285f0200020010000000d9af"
            "d012b71716646cc273ece262daaff988c5b2b31138aa99729f739033eccafde31016a3bd59b186fe045db3be74fe02000200000000"
            "00bc5ffde554dc7215c4aaa928eac171c702000200000000002f76bddf67175ab40e390f7b56a2a70e"
        ),
    )
    users_key.add_subkey("000001F8", f8_key)

    e8_key = VirtualKey(hive_hklm, "000003E8")
    e8_key.add_value(
        "F",
        bytes.fromhex(
            "0300010000000000af58b2fbb721d9010000000000000000c1f7affbb721d9010000000000000000064ae824b821d901e803000001"
            "020000140000002c00e40403000400010000000000000000000000"
        ),
    )
    e8_key.add_value(
        "V",
        bytes.fromhex(
            "00000000f400000003000100f40000000800000000000000fc0000000000000000000000fc0000000000000000000000fc00000000"
            "00000000000000fc0000000000000000000000fc0000000000000000000000fc0000000000000000000000fc000000000000000000"
            "0000fc0000000000000000000000fc0000000000000000000000fc00000015000000a80000001401000008000000010000001c0100"
            "0018000000000000003401000038000000000000006c010000180000000000000084010000180000000000000001001480d4000000"
            "e40000001400000044000000020030000200000002c014004400050101010000000000010000000002c01400ff070f000101000000"
            "0000050700000002009000040000000000240044000200010500000000000515000000a64ddd54933204de30f57de4e80300000000"
            "38001b030200010a00000000000f0300000000040000dea22867213ed2af19ad5d79b0c107292756fc20d8ad66f610f268fadf2af8"
            "0f00001800ff070f0001020000000000052000000020020000000014005b0302000101000000000001000000000102000000000005"
            "2000000020020000010200000000000520000000200200004a006f0068006e00ffffffffffffffffffffffffffffffffffffffffff"
            "22a88301020000070000000200020000000000ee5cf441445c05397fda8c7f9199f866020002001000000001cbd838215335f6d65d"
            "81ff88bcc02ee8dd17c186264164c5134894e5fabd391f1f7c31a5c782e879aacf06bb54067e02000200000000006fec9332976503"
            "00a2c558248f8b5a310200020000000000549d3bcdeb83706e54e9f8cf7644b766"
        ),
    )
    users_key.add_subkey("000003E8", e8_key)

    sam_key.add_subkey("Users", users_key)
    hive_hklm.map_key(sam_key_name, sam_key)

    # Create SYSTEM keys
    system_key = VirtualKey(hive_hklm, system_key_name)
    data_key = VirtualKey(hive_hklm, "Data", class_name="36f1befb")
    system_key.add_subkey("Data", data_key)
    gbg_key = VirtualKey(hive_hklm, "GBG", class_name="bae89edb")
    system_key.add_subkey("GBG", gbg_key)
    jd_key = VirtualKey(hive_hklm, "JD", class_name="626b21ce")
    system_key.add_subkey("JD", jd_key)
    skew1_key = VirtualKey(hive_hklm, "Skew1", class_name="e6f92d89")
    system_key.add_subkey("Skew1", skew1_key)
    hive_hklm.map_key(system_key_name, system_key)

    target_win_users.add_plugin(SamPlugin)
    results = list(target_win_users.sam())

    assert len(results) == 5

    assert results[3].rid == 504
    assert results[3].fullname == ""
    assert results[3].username == "WDAGUtilityAccount"
    assert (
        results[3].admincomment
        == "A user account managed and used by the system for Windows Defender Application Guard scenarios."
    )
    assert results[3].usercomment == ""
    assert results[3].lastlogin == dt("1601-01-01T00:00:00+00:00")
    assert results[3].lastpasswordset == dt("2023-01-06T10:22:15.648840+00:00")
    assert results[3].lastincorrectlogin == dt("1601-01-01T00:00:00+00:00")
    assert results[3].flags == 17
    assert results[3].countrycode == 0
    assert results[3].failedlogins == 0
    assert results[3].logins == 0
    assert results[3].lm == ""
    assert results[3].nt == "2f4bbedb0aa738ae7ce3d9846692d3e4"

    assert results[4].rid == 1000
    assert results[4].fullname == ""
    assert results[4].username == "John"
    assert results[4].admincomment == ""
    assert results[4].usercomment == ""
    assert results[4].lastlogin == dt("2023-01-06T10:16:46.964138+00:00")
    assert results[4].lastpasswordset == dt("2023-01-06T10:16:46.948549+00:00")
    assert results[4].lastincorrectlogin == dt("2023-01-06T10:17:56.104242+00:00")
    assert results[4].flags == 20
    assert results[4].countrycode == 44
    assert results[4].failedlogins == 3
    assert results[4].logins == 4
    assert results[4].lm == ""
    assert results[4].nt == MD4.new("MD4St1llGo1ngStr0ng!".encode("utf-16-le")).digest().hex()
