name = "Wishwajeet Singh Tanwar"

def outer():
    # global name
    name = "Satyajeet Singh Tanwar"
    print(name)
    def inner():
        print(name)     #Here in this function block there is no any variable name "name" hence it will search for this within the nearest function block i.e outer function block.
    inner()
outer()
print(name)
