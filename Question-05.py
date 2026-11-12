def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))


def bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    total = amount + gst
    return total, gst

total, gst = bill(200, gst_rate=0.05)
print("Total:", total, "GST:", gst)


count = 10                 # global variable

def show_local():
    count = 5              # local variable
    print("Local:", count)

def change_global():
    global count
    count = 20

def outer():
    value = 1
    def inner():
        nonlocal value
        value += 1
    inner()
    print("Nonlocal:", value)

show_local()
change_global()
print("Global:", count)
outer()
