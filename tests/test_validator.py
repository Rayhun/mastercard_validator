from card_validator.validators import get_issuer

def test_get_issuer_visa():
    assert get_issuer("4456 4567 7654 4567") == "Visha"

def test_get_issuer_master():
    assert get_issuer("5456 4567 7654 4567") == "MasterCard"
    assert not get_issuer("5665 6567 6547 9876") == "MasterCard"

def test_get_issuer_american_express():
    assert get_issuer("378 2822 4631 0005") == "American Express"
    assert get_issuer("5610 5910 8101 8250") == "American Express"