def get_issuer(number: str) -> str:
    if number.startswith('4'):
        return "Visha"
    
    if number.startswith('3'):
        return "Amirican Express"
    
    if number.startswith('5'):
        return "Master Card"