from services.directory import directory

if __name__ == "__main__":
    add, find_by, search_by, count, list, remove_by = directory()
    
    add({"name":"Krishna", "phone": 1234})
    add({"name":"Mohan", "phone": 2345})
    add({"name":"Koyya", "phone": 3456})
    print(list())
    print(count())
    print(find_by(1))
    print(search_by("Koyyas"))
    remove_by(1)
    print(list())