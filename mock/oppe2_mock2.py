def is_function(domain, co_domain, fun):
    bool_1 = is_key(domain, fun)
    bool_2 = is_domain(domain, fun)
    bool_3 = is_co_domain(co_domain, fun)

    if bool_1 and bool_2 and bool_3:
        return True
    else:
        return False


def is_key(domain, fun):
    for i in domain:
        if i in fun.keys():
            f = True
        else:
            f = False
            break

    return f


def is_domain(domain, fun):
    for i in fun.keys():
        if i in domain:
            f = True
        else:
            f = False
            break

    return f


def is_co_domain(co_domain, fun):
    for i in fun.values():
        if i in co_domain:
            f = True
        else:
            f = False
            break

    return f
