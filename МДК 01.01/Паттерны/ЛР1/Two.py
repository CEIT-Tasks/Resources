from abc import ABC, abstractmethod

class Body(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Engine(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Gearbox(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Wheels(ABC):
    @abstractmethod
    def get_description(self):
        pass

class SedanBody(Body):
    def get_description(self):
        return "Кузов: Седан"

class CoupeBody(Body):
    def get_description(self):
        return "Кузов: Купе"

class V8Engine(Engine):
    def get_description(self):
        return "Двигатель: V8"

class V12Engine(Engine):
    def get_description(self):
        return "Двигатель: V12"

class I6Engine(Engine):
    def get_description(self):
        return "Двигатель: I6"

class AutomaticGearbox(Gearbox):
    def get_description(self):
        return "Коробка передач: Автоматическая"

class ManualGearbox(Gearbox):
    def get_description(self):
        return "Коробка передач: Механическая"

class RFTWheels(Wheels):
    def get_description(self):
        return "Диски/шины: Run-flat"

class PerformanceWheels(Wheels):
    def get_description(self):
        return "Диски/шины: Performance"

class CarFactory(ABC):
    @abstractmethod
    def create_body(self, model):
        pass

    @abstractmethod
    def create_engine(self, model):
        pass

    @abstractmethod
    def create_gearbox(self, model):
        pass

    @abstractmethod
    def create_wheels(self, model):
        pass

class BMWFactory(CarFactory):
    def create_body(self, model):
        if model == "3 Series":
            return SedanBody()
        if model == "8 Series":
            return CoupeBody()
        if model == "M5":
            return SedanBody()
        return None

    def create_engine(self, model):
        if model == "3 Series":
            return I6Engine()
        if model == "8 Series":
            return V8Engine()
        if model == "M5":
            return V8Engine()
        return None

    def create_gearbox(self, model):
        if model == "3 Series":
            return AutomaticGearbox()
        if model == "8 Series":
            return AutomaticGearbox()
        if model == "M5":
            return AutomaticGearbox()
        return None

    def create_wheels(self, model):
        if model == "3 Series":
            return RFTWheels()
        if model == "8 Series":
            return RFTWheels()
        if model == "M5":
            return PerformanceWheels()
        return None

class CarModel:
    def __init__(self, name, body, engine, gearbox, wheels):
        self.name = name
        self.body = body
        self.engine = engine
        self.gearbox = gearbox
        self.wheels = wheels

    def get_description(self):
        return f"""
        <h2>Модель: {self.name}</h2>
        <ul>
            <li>{self.body.get_description()}</li>
            <li>{self.engine.get_description()}</li>
            <li>{self.gearbox.get_description()}</li>
            <li>{self.wheels.get_description()}</li>
        </ul>
        """

def assemble_and_describe_models(factory):
    models = ["3 Series", "8 Series", "M5"]
    car_models = []
    
    for model_name in models:
        body = factory.create_body(model_name)
        engine = factory.create_engine(model_name)
        gearbox = factory.create_gearbox(model_name)
        wheels = factory.create_wheels(model_name)
        if all([body, engine, gearbox, wheels]):
            car_models.append(CarModel(model_name, body, engine, gearbox, wheels))

    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Модели автомобилей</title>
        <style>
            body { font-family: sans-serif; line-height: 1.6; padding: 20px; }
            .container { max-width: 800px; margin: auto; background: #f4f4f4; padding: 20px; border-radius: 8px; }
            h1 { color: #333; text-align: center; }
            h2 { color: #555; }
            ul { list-style: none; padding: 0; }
            li { background: #e2e2e2; margin-bottom: 10px; padding: 10px; border-radius: 4px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Каталог автомобилей</h1>
    """
    
    for car in car_models:
        html_content += car.get_description()

    html_content += """
        </div>
    </body>
    </html>
    """

    with open("car_models.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print("HTML-файл 'car_models.html' успешно сгенерирован.")

if __name__ == "__main__":
    bmw_factory = BMWFactory()
    assemble_and_describe_models(bmw_factory)
