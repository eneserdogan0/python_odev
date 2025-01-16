import os
from Market import Market


def main():
    market = Market()

    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        try:
            choice = int(input("Seçiminizi yapın: "))
            if choice == 1:
                market.list_products()
            elif choice == 2:
                market.add_product()
            elif choice == 3:
                market.delete_product()
            elif choice == 4:
                print("Çıkış yapılıyor...")
                break
            else:
                print("Lütfen 1 ile 4 arasında bir seçim yapın.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
