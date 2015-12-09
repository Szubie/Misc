Invalid_values =  [4, 8]
invalid_values_list = [1, 2 ,4 ,6 ,8]

print invalid_values_list
for item in invalid_values_list:
    print "Examining ", item
    if item not in Invalid_values:
        print "item removed, list shifted 1 space!"
        invalid_values_list.remove(item)
print invalid_values_list

"""What do we learn from this madness? That it's not a good idea to alter a list as we are iterating over it, as this causes things like this to happen. Instead, we ought to have a third list to append the results to."""