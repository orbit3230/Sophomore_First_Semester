from functools import reduce

def main() :
    members= [
        {'mail': 'abc@gmail.com', 'name': 'G. H. Kim', 'gender': 'Male', 'age': 34},
        {'mail': 'agds@hotmail.com', 'name': 'Martiny Glass', 'gender': 'Female', 'age': 49},
        {'mail': 'm.jen@gmail.com', 'name': 'Jim H. Beam', 'gender': 'Female', 'age': 21},
        {'mail': 'kodfmk@gmail.com', 'name': 'Eminem', 'gender': 'Male', 'age': 54},
        {'mail': 'ujomew@gmail.com', 'name': 'Rihana', 'gender': 'Female', 'age': 52}
    ]

    print(f"Sum of members' age is: {reduce(lambda x, y : x + y['age'], members, 0)}")
    print(f"Membes' mail: {list(map(lambda l : l['mail'], members))}")
    print(f"Female Members' list: {list(map(lambda l : l['name'], filter(lambda x : x['gender'] == 'Female', members)))}")
    print(f"Male Members' list: {list(map(lambda l : l['name'], filter(lambda x : x['gender'] == 'Male', members)))}")
    
if __name__ == "__main__" :
    main()