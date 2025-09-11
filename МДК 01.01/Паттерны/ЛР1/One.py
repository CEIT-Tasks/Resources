from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Brick(Material):
    def get_name(self):
        return "Кирпич"

class Slab(Material):
    def get_name(self):
        return "Железобетонная плита"

class Concrete(Material):
    def get_name(self):
        return "Бетон"

class Supplier(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_price(self, material):
        pass

    @abstractmethod
    def get_max_daily_supply(self, material):
        pass

class Supplier1(Supplier):
    def __init__(self):
        super().__init__("Поставщик 1")
        self.prices = {
            "Кирпич": 100,
            "Железобетонная плита": 5000,
            "Бетон": 2500
        }
        self.max_supply = {
            "Кирпич": 1000,
            "Железобетонная плита": 10,
            "Бетон": 50
        }

    def get_price(self, material_name):
        return self.prices.get(material_name, float('inf'))

    def get_max_daily_supply(self, material_name):
        return self.max_supply.get(material_name, 0)

class Supplier2(Supplier):
    def __init__(self):
        super().__init__("Поставщик 2")
        self.prices = {
            "Кирпич": 110,
            "Бетон": 2400
        }
        self.max_supply = {
            "Кирпич": 800,
            "Бетон": 60
        }

    def get_price(self, material_name):
        return self.prices.get(material_name, float('inf'))

    def get_max_daily_supply(self, material_name):
        return self.max_supply.get(material_name, 0)

class Supplier3(Supplier):
    def __init__(self):
        super().__init__("Поставщик 3")
        self.prices = {
            "Железобетонная плита": 4800,
            "Бетон": 2600
        }
        self.max_supply = {
            "Железобетонная плита": 15,
            "Бетон": 45
        }

    def get_price(self, material_name):
        return self.prices.get(material_name, float('inf'))

    def get_max_daily_supply(self, material_name):
        return self.max_supply.get(material_name, 0)

class SupplierFactory(ABC):
    @abstractmethod
    def create_supplier(self, supplier_id):
        pass

class ConcreteSupplierFactory(SupplierFactory):
    def create_supplier(self, supplier_id):
        if supplier_id == 1:
            return Supplier1()
        elif supplier_id == 2:
            return Supplier2()
        elif supplier_id == 3:
            return Supplier3()
        else:
            return None

def calculate_optimal_plan(daily_needs, suppliers, materials):
    optimal_plan = {}
    total_cost = 0

    for material in materials:
        material_name = material.get_name()
        needed_quantity = daily_needs.get(material_name, 0)
        remaining_needed = needed_quantity
        material_plan = []

        if needed_quantity == 0:
            continue

        sorted_suppliers = sorted(suppliers, key=lambda s: s.get_price(material_name))

        for supplier in sorted_suppliers:
            price = supplier.get_price(material_name)
            max_supply = supplier.get_max_daily_supply(material_name)

            if price == float('inf') or max_supply == 0:
                continue

            quantity_to_buy = min(remaining_needed, max_supply)
            if quantity_to_buy > 0:
                cost = quantity_to_buy * price
                material_plan.append({"supplier": supplier.name, "quantity": quantity_to_buy, "cost": cost})
                total_cost += cost
                remaining_needed -= quantity_to_buy

            if remaining_needed == 0:
                break

        if remaining_needed > 0:
            print(f"Невозможно удовлетворить всю потребность в материале '{material_name}'. Не хватает {remaining_needed} единиц.")

        optimal_plan[material_name] = material_plan

    return optimal_plan, total_cost

if __name__ == "__main__":
    factory = ConcreteSupplierFactory()
    suppliers = [factory.create_supplier(1), factory.create_supplier(2), factory.create_supplier(3)]
    materials = [Brick(), Slab(), Concrete()]

    daily_needs = {}
    print("Введите суточную потребность в материалах:")
    for material in materials:
        try:
            quantity = int(input(f"{material.get_name()}: "))
            daily_needs[material.get_name()] = quantity
        except ValueError:
            daily_needs[material.get_name()] = 0

    optimal_plan, total_cost = calculate_optimal_plan(daily_needs, suppliers, materials)

    print("\nОптимальный план поставок:")
    for material, plan in optimal_plan.items():
        if plan:
            print(f"\n{material}:")
            for item in plan:
                print(f"  - Поставщик: {item['supplier']}, Количество: {item['quantity']}, Стоимость: {item['cost']}")

    print(f"\nОбщая стоимость поставок: {total_cost}")