import os


class Market:
    def __init__(self, filename="product.txt"):
        """Market sınıfı yapıcı metodu."""
        self.filename = filename
        # Dosya mevcut değilse oluştur
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                pass

    def __del__(self):
        """Market sınıfı yıkıcı metodu."""
        print("Program sonlandırıldı ve dosya kapatıldı.")

    def list_products(self):
        """Ürünleri listeler."""
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("Ürün bulunamadı.")
                    return
                print("\n*** Ürün Listesi ***")
                for idx, line in enumerate(lines, start=1):
                    name, category, price, stock = line.strip().split(',')
                    print(f"{idx}) Ürün Adı: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")
        except Exception as e:
            print(f"Hata: {e}")

    def add_product(self):
        """Yeni bir ürün ekler."""
        name = input("Ürün adı: ")
        category = input("Kategori: ")
        price = input("Fiyat: ")
        stock = input("Stok miktarı: ")
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{name},{category},{price},{stock}\n")
            print("Ürün başarıyla eklendi.")
        except Exception as e:
            print(f"Hata: {e}")

    def delete_product(self):
        """Belirtilen ürünü siler."""
        self.list_products()
        try:
            choice = int(input("Silmek istediğiniz ürün numarasını girin: "))
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            if 1 <= choice <= len(lines):
                del lines[choice - 1]
                with open(self.filename, 'w') as file:
                    file.writelines(lines)
                print("Ürün başarıyla silindi.")
            else:
                print("Geçersiz ürün numarası.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
        except Exception as e:
            print(f"Hata: {e}")