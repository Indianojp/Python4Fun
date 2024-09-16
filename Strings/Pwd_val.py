def password(st):
    return (
        len(st)>7
        and any(c.isupper() for c in st)
        and any(c.islower() for c in st)
        and any(c.isdecimal() for c in st)
    )