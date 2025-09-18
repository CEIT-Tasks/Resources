import json
import os

## Установите пакет googletrans через pip, если он не установлен:
# pip install googletrans==4.0.0-rc1
from googletrans import Translator

class TextTransformer:
    """
    Базовый класс для преобразования текста.
    """
    def __init__(self, name):
        self.name = name

    def transform(self, text):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")

    def reverse_transform(self, text):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")


class TranslationTransformer(TextTransformer):
    """
    Класс для перевода текста.
    """
    def __init__(self, dest_lang='en'):
        super().__init__("translate")
        self.translator = Translator()
        self.dest_lang = dest_lang
        self.src_lang = None

    def transform(self, text):
        """Переводит текст по словам, сохраняя исходный язык для обратного преобразования."""
        try:
            words = text.split()
            translated_words = []
            for word in words:
                # Определяем исходный язык первого слова, чтобы использовать его для обратного перевода
                if self.src_lang is None:
                    detected = self.translator.detect(word)
                    self.src_lang = detected.lang
                translated = self.translator.translate(word, dest=self.dest_lang)
                translated_words.append(translated.text)
            return ' '.join(translated_words)
        except Exception as e:
            print(f"Ошибка при переводе: {e}")
            return text

    def reverse_transform(self, text):
        """Возвращает переведенный текст обратно на исходный язык."""
        if self.src_lang is None:
            print("Не удалось определить исходный язык для обратного перевода.")
            return text
        try:
            words = text.split()
            original_words = []
            for word in words:
                translated = self.translator.translate(word, dest=self.src_lang)
                original_words.append(translated.text)
            return ' '.join(original_words)
        except Exception as e:
            print(f"Ошибка при обратном переводе: {e}")
            return text

    def to_json(self):
        return {"name": self.name, "dest_lang": self.dest_lang, "src_lang": self.src_lang}

    @staticmethod
    def from_json(data):
        transformer = TranslationTransformer(data.get("dest_lang"))
        transformer.src_lang = data.get("src_lang")
        return transformer


class PermutationTransformer(TextTransformer):
    """
    Класс для шифрования методом перестановки слов по заданной схеме.
    """
    def __init__(self, scheme=None):
        super().__init__("encrypt")
        self.scheme = scheme
        self.inverse_scheme = None

    def transform(self, text):
        """Шифрует текст, переставляя слова по заданной схеме."""
        words = text.split()
        
        # Если схема не задана, создаем ее на основе длины текста
        if not self.scheme:
            self.scheme = list(range(len(words)))
            import random
            random.shuffle(self.scheme)
            
        # Проверяем, соответствует ли схема длине текста
        if len(self.scheme) != len(words):
            print("Схема перестановки не соответствует количеству слов. Пропускаем шифрование.")
            return text
        
        # Генерируем обратную схему, если ее нет
        if not self.inverse_scheme:
            self.inverse_scheme = [0] * len(self.scheme)
            for i, j in enumerate(self.scheme):
                self.inverse_scheme[j] = i

        encrypted_words = [None] * len(words)
        for i, j in enumerate(self.scheme):
            encrypted_words[j] = words[i]
        
        return ' '.join(encrypted_words)

    def reverse_transform(self, text):
        """Расшифровывает текст, используя обратную схему."""
        if not self.inverse_scheme:
            print("Обратная схема не найдена. Невозможно расшифровать.")
            return text

        words = text.split()
        if len(self.inverse_scheme) != len(words):
            print("Схема не соответствует количеству слов в тексте. Пропускаем расшифровку.")
            return text

        decrypted_words = [None] * len(words)
        for i, j in enumerate(self.inverse_scheme):
            decrypted_words[j] = words[i]

        return ' '.join(decrypted_words)
        
    def to_json(self):
        return {"name": self.name, "scheme": self.scheme, "inverse_scheme": self.inverse_scheme}

    @staticmethod
    def from_json(data):
        transformer = PermutationTransformer(data.get("scheme"))
        transformer.inverse_scheme = data.get("inverse_scheme")
        return transformer

class TextFileProcessor:
    """
    Класс-тестовое приложение для записи и чтения данных с преобразованиями.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.transformer_map = {
            "translate": TranslationTransformer,
            "encrypt": PermutationTransformer
        }

    def write_with_transformations(self, text, transformations_list):
        """Записывает текст в файл, применяя заданную последовательность преобразований."""
        print(f"Исходный текст: {text}")
        
        operations_data = []
        current_text = text
        for op_name in transformations_list:
            if op_name not in self.transformer_map:
                print(f"Неизвестное преобразование: {op_name}. Пропускаем.")
                continue

            # Создаем экземпляр класса для преобразования
            transformer = self.transformer_map[op_name]()
            current_text = transformer.transform(current_text)
            operations_data.append(transformer.to_json())
            print(f"Текст после '{op_name}': {current_text}")

        # Формируем структуру данных для сохранения в файл
        file_content = {
            "data": current_text,
            "operations": operations_data
        }

        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(file_content, f, ensure_ascii=False, indent=2)

        print(f"\nДанные успешно записаны в файл: {self.file_path}")

    def read_with_transformations(self):
        """Считывает данные из файла и применяет обратные преобразования."""
        if not os.path.exists(self.file_path):
            print(f"Файл не найден: {self.file_path}")
            return None

        with open(self.file_path, 'r', encoding='utf-8') as f:
            file_content = json.load(f)

        encoded_text = file_content.get("data")
        operations_data = file_content.get("operations")

        print(f"\nСчитываем данные из файла: {self.file_path}")
        print(f"Закодированный текст: {encoded_text}")
        print(f"Последовательность операций: {[op['name'] for op in operations_data]}")
        
        # Применяем обратные преобразования в обратном порядке
        current_text = encoded_text
        for op_data in reversed(operations_data):
            op_name = op_data["name"]
            
            if op_name == "translate":
                transformer = TranslationTransformer.from_json(op_data)
            elif op_name == "encrypt":
                transformer = PermutationTransformer.from_json(op_data)
            else:
                print(f"Неизвестная операция в файле: {op_name}. Невозможно расшифровать.")
                continue

            current_text = transformer.reverse_transform(current_text)
            print(f"Текст после обратного '{op_name}': {current_text}")

        print("\nОбработка завершена.")
        return current_text

if __name__ == "__main__":
    file_path = "output.json"
    initial_text = "Пример текста для демонстрации работы программы с разными преобразованиями."
    
    # Создаем экземпляр тестового приложения
    processor = TextFileProcessor(file_path)

    # Задаем последовательность преобразований (сначала шифрование, потом перевод)
    transformations_to_apply = ["encrypt", "translate"]
    
    # 1. Запись в файл с преобразованиями
    processor.write_with_transformations(initial_text, transformations_to_apply)

    # 2. Чтение из файла с обратными преобразованиями
    decoded_text = processor.read_with_transformations()

    print(f"\nКонечный результат (восстановленный текст): {decoded_text}")
    print(f"Проверка: текст полностью восстановлен? {initial_text == decoded_text}")