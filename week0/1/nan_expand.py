def nan_expand(times):
    nan = ""
    if times != 0:
        while times != 0:
            nan = nan + "Not a "
            times -= 1
        nan = nan + "NaN"
    return nan
print(nan_expand(1))
