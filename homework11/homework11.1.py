def geometric_prog(min,q,len_num):
    import pdb; pdb.set_trace()
    for i in range(min,len_num + 1):
        result = min * (q ** i)
        yield result
generator = geometric_prog(1,2,10)
for value in generator:
    print(value)