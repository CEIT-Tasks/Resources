import array

class DataPrinter:
  def print_data(self, data):
    match data:
      case str():
        print(f"Строка: {data}")
      case int():
        print(f"Целое число: {data}")
      case array.array:
        print(f"Массив: {data.tolist()}")
      case _:
        print("Данных нет, или не тот тип данных")