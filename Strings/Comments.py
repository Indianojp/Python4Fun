def strip_comments(strng, markers):
    lin = strng.split('\n')
    r = []
    for l in lin:
        nl = l
        for m in markers:
            if m in nl:
                nl = nl.split(m)[0].rstrip()
        r.append(nl)
    return '\n'.join(r)