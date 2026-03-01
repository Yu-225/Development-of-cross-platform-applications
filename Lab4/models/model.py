from dataclasses import dataclass
from datetime import datetime, date, time, timedelta
from typing import List


# ------------------------
# ENTITY
# ------------------------

@dataclass
class SleepSession:
    bed_time: time
    wake_time: time
    had_awakenings: int
    awake_minutes: int  # хвилини сумарно
    quality: int  # 1–5

    def to_datetimes(self) -> tuple[datetime, datetime]:
        """Перетворює time → datetime з урахуванням переходу через північ."""
        today = date.today()

        sleep_dt = datetime.combine(today, self.bed_time)
        wake_dt = datetime.combine(today, self.wake_time)

        if wake_dt <= sleep_dt:
            wake_dt += timedelta(days=1)

        return sleep_dt, wake_dt


# ------------------------
# CALCULATOR
# ------------------------

class SleepCalculator:

    @staticmethod
    def calculate_time_in_bed(session: SleepSession) -> timedelta:
        sleep_dt, wake_dt = session.to_datetimes()
        return wake_dt - sleep_dt

    @staticmethod
    def calculate_actual_sleep(session: SleepSession) -> timedelta:
        time_in_bed = SleepCalculator.calculate_time_in_bed(session)
        awakenings = timedelta(minutes=session.awake_minutes)
        return time_in_bed - awakenings

    @staticmethod
    def calculate_efficiency(session: SleepSession) -> float:
        time_in_bed = SleepCalculator.calculate_time_in_bed(session)
        actual_sleep = SleepCalculator.calculate_actual_sleep(session)

        if time_in_bed.total_seconds() == 0:
            return 0.0

        return (actual_sleep / time_in_bed) * 100


# ------------------------
# ANALYZER
# ------------------------

class SleepAnalyzer:

    @staticmethod
    def calculate_score(session: SleepSession) -> int:
        actual_sleep_hours = (
            SleepCalculator.calculate_actual_sleep(session).total_seconds() / 3600
        )
        efficiency = SleepCalculator.calculate_efficiency(session)

        score = 0

        # 50% — тривалість
        if 7 <= actual_sleep_hours <= 9:
            score += 50
        elif 6 <= actual_sleep_hours < 7 or 9 < actual_sleep_hours <= 10:
            score += 30
        else:
            score += 10

        # 30% — ефективність
        if efficiency >= 85:
            score += 30
        elif efficiency >= 75:
            score += 20
        else:
            score += 10

        # 20% — фрагментація
        if session.had_awakenings == 0:
            score += 20
        elif session.had_awakenings <= 2:
            score += 15
        else:
            score += 5

        return score

    @staticmethod
    def generate_recommendations(session: SleepSession) -> List[str]:
        recommendations = []

        actual_sleep = (
            SleepCalculator.calculate_actual_sleep(session).total_seconds() / 3600
        )
        efficiency = SleepCalculator.calculate_efficiency(session)

        if actual_sleep < 7:
            recommendations.append("Збільшити тривалість сну до 7–9 годин.")

        if efficiency < 85:
            recommendations.append("Зменшити нічні пробудження або покращити гігієну сну.")

        if session.had_awakenings > 2:
            recommendations.append("Звернути увагу на причини частих пробуджень.")

        if session.quality <= 2:
            recommendations.append("Проаналізувати рівень стресу або режим дня.")

        if not recommendations:
            recommendations.append("Сон у межах норми. Підтримуйте поточний режим.")

        return recommendations


if __name__ == "__main__":
    session = SleepSession(
        bedtime=time(22, 0),
        wake_time=time(6, 0),
        awakenings_duration=30,
        awakenings_count=1,
        subjective_rating=4,
    )

    print(SleepCalculator.calculate_actual_sleep(session))