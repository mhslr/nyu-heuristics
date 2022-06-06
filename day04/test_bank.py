from bank import Bank


def check(v1, v2):
    assert abs(v1 - v2) < 1e-5


def test_bank():
    bk = Bank({})
    bk.open_account("alice", 10000, 2)
    bk.open_account("bob", 0, 3.14)
    assert len(bk.accounts) == 2
    assert not bk.transfer_usd("alice", "bob", 20000)
    assert bk.transfer_usd("alice", "bob", 3000)
    assert bk.transfer_btc("bob", "alice", 0.32)
    assert not bk.transfer_btc("bob", "alice", 32)
    check(bk.accounts["alice"].usd_balance, 7000)
    check(bk.accounts["alice"].btc_balance, 2.304)
    check(bk.accounts["bob"].usd_balance, 3000)
    check(bk.accounts["bob"].btc_balance, 2.82)

    assert bk.invest("alice", 2000)
    assert not bk.panic("alice", 2000)
    assert bk.panic("alice", 1.37)
    check(bk.accounts["alice"].usd_balance, 45680.177)
