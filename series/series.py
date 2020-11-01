"""
check if input length is less than or equal to the series length
create an empty list to contain the slices
for each item in series
    add the item & the next 2 items to the slices list
return the slices list
"""


def slices(series, length):
    if length > len(series) or length <= 0 or series == "":
        raise ValueError("Please specify a length less than or equal to the series length")

    slices_list = []
    for i in range(len(series)):
        if i == 0:
            slice = series[i:length]
        else:
            slice = series[i:length+i]
            if len(slice) < length:
                break
        slices_list.append(slice)

    return slices_list
