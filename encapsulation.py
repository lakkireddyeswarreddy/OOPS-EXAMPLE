

class Product:
    
    def __init__(self, product_name, product_price):
        self._product_name = product_name
        self.__product_price = product_price
        
    def get_product_name(self):
        return self._product_name
    
    def set_product_name(self, product_name):
        self._product_name = product_name
        
    def set_product_price(self, product_price):
        if product_price < 0:
            raise Exception("Product price cannot be negative.")
        self.__product_price = product_price
        
    def get_product_price(self):
        return self.__product_price
    
    
if __name__ == "__main__":
    product_obj = Product("Apple", "68.50")
    print(product_obj._product_name)
    # print(product_obj.__product_price) # Raises Attribute error
    # print(product_obj._Product__product_price) # Not encouraged, use setters and getters.
    print(product_obj.get_product_price())