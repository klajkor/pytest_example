

def hello(person):
    return "Hi, {name}".format(**person)


if __name__ == '__main__':
    print("Main")
    peter = {"name": "Peter"}
    print(hello(peter))

