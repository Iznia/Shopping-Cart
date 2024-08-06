import unittest

from iznia_azyati_app import ShoppingCart, CartItem

# Kelas TestShoppingCart bertujuan untuk menguji fungsi Add Item, Remove Item, Calculate Total, dan Display Item.
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    # Mengecek function add_item
    def test_add_item(self):
        self.cart.add_item("Kemeja", 55000)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].nama, "Kemeja")
        self.assertEqual(self.cart.items[0].harga, 55000)
    
    # Mengecek function remove_item
    def test_remove_item(self):
        self.cart.add_item("Kemeja", 55000)
        self.cart.remove_item("Kemeja")
        self.assertEqual(len(self.cart.items), 0)
    
    # Mengecek function total price
    def test_total_price(self):
        self.cart.add_item("Kemeja", 55000)
        self.cart.add_item("Celana Pendek", 70000)
        total = self.cart.total_price()
        self.assertEqual(total, 125000)

    

if __name__ == "__main__":
    unittest.main()
    

