from card_validator.validators import get_issuer

def test_get_issuer_visa():
    assert get_issuer("4456 4567 7654 4567") == "Visha"

def test_get_issuer_master():
    assert get_issuer("5456 4567 7654 4567") == "MasterCard"
    assert not get_issuer("5665 6567 6547 9876") == "MasterCard"