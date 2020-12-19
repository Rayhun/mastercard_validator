from card_validator.validators import get_issuer

def test_get_issuer_visa():
    assert get_issuer("4456 4567 7654 4567") == "Visha"