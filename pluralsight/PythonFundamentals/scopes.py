count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    count = c


def set_count_correct(c):
    global count
    count = c


show_count()
set_count(5)
show_count()
set_count_correct(5)
show_count()