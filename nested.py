import types

def nested_to_flat(lis):
    flat_list = []
    index = 0

    while (index < len(lis)):

        element = lis[index]

        if type(element) != types.IntType:
            flat_list = flat_list + nested_to_flat(element)
        else:
            flat_list.append(element)

        index += 1

    return flat_list
a=[2,3,4]
print(nested_to_flat(a))