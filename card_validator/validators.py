def get_issuer(number: str ) -> str:
    if number.startswith('4'):
        return "Visha"
    
    if number.startswith('37') or number.startswith('56'):
        return "American Express"
    
    if number.startswith('51') or number.startswith('52') or number.startswith('53') or number.startswith(
        '54') or number.startswith('55'):
        return "MasterCard"