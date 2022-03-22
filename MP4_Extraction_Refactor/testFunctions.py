def testFunc(my_dict = None):

    print(my_dict)

def listPacker(a_list, directory):
    """
    Given a list each element will become a line in a txt file

    a_list = list 
    directory = where to place the file
    """
    #Save a list
    textfile = open(directory, "w")
    for element in a_list:
        textfile.write(element + "\n")
    textfile.close()

def listUnpacker(directory):
    """
    Given a text file will turn each line into a list element

    diectory = directory of .txt file

    returns a list each element being a line from the file
    """
    #load list
    a_file = open(directory, "r")

    list = []
    for line in a_file:
        stripped_line = line.strip()
        list.append(stripped_line)

    a_file.close()
    return list


lists = [[],[],[],[],[]]
DL1 = [1,2,3,4]
DL2 = [4,5,6,7]
DL3 = [7,8,9,10]

lists[0] = DL1
lists[1] = DL2
lists.append(DL3)
print(lists)