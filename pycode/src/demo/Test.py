from ListStudy import fib


class Test:
    origin_kws = "1#a#1,2#b#2,3#c#c"
    print(origin_kws)
    if origin_kws is None:
        print('none input!')

    kws_list = origin_kws.split(',')
    print(kws_list)
    return_list = []
    for kws in kws_list:
        kw = kws.split('#')
        print(kw)
        if kw is None or kw[0] == '9999999':
            continue
        else:
            return_list.append(kw[1])
    print('return_list is: %s' % ','.join(return_list))

    print(fib(6))
