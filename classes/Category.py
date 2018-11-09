class Category:
    pass
    id = 1
    name = "Бензин"
    hash = "Некий #"

    id = 2
    name = "Продукты"
    hash = "Некий #"

    id = 3
    name = "Хобби и привычки"
    hash = "Некий #"

    def set(self, id, name, hash)
        self.id = id
        self.name = name
        self.hash = hash
        return (id, name)



