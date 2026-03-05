from datetime import datetime

from models.model import SleepSession, SleepCalculator, SleepAnalyzer
from views.view import ViewApp

class ControllerApp:
    def __init__(self, root):
        self.data = {}

        self.view = ViewApp(root, self.handle_input, options=["1", "2", "3", "4", "5"])
        self.view.pack(fill="both", expand=True)
    
    # Обробка змін у полях 
    def handle_input(self, name, value):
        self.data[name] = value

        if self.is_ready():
            self.process()   
        
        if name == "had_awakenings":
            self.view.toggle_awake_field(value)
    
    # перевірка повноти даних
    def is_ready(self):
        required_fields = {
            "bed_time",
            "wake_time",
            "had_awakenings",
            "quality",
        }
        print(self.data.keys())
        return required_fields.issubset(self.data.keys())

    # логіка
    def process(self):
        session = SleepSession(
            bed_time = self.parse_time(self.data["bed_time"]),
            wake_time = self.parse_time(self.data["wake_time"]),
            had_awakenings = 0 if self.data["had_awakenings"] == 'Ні' else 1,
            awake_minutes = self.data.get("awake_minutes", 0),
            quality = int(self.data["quality"]),
        )

        time_in_bed = SleepCalculator.calculate_time_in_bed(session)
        actual_sleep = SleepCalculator.calculate_actual_sleep(session)
        efficiency = SleepCalculator.calculate_efficiency(session)

        score = SleepAnalyzer.calculate_score(session)
        recommendations = SleepAnalyzer.generate_recommendations(session)

        result_text = (
            f"Час у ліжку: {time_in_bed}\n"
            f"Чистий сон: {actual_sleep}\n"
            f"Ефективність: {efficiency:.2f}%\n"
            f"Оцінка: {score}/100\n\n"
            "Рекомендації:\n"
            + "\n".join(recommendations)
        )

        self.view.update_label(result_text)
        
    # перетворення часу
    @staticmethod
    def parse_time(value: str):
        return datetime.strptime(value, "%H:%M").time()