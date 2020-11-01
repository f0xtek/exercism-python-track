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
