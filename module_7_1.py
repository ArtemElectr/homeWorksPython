class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.weight, self.category)


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        string = file.read()
        file.close()
        return string

    def add(self, *products):
        for product in products:
            products_now = self.get_products()
            if product.name in products_now:
                print('Продукт {} уже есть в магазине'.format(product.name))
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{str(product)}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
