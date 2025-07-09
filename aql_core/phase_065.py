# المرحلة ٦٥ – تمكين النوى من بناء تحالفات ذكية داخل النظام

"""
🤝 الهدف: إعطاء النوى القدرة على تقييم نوى أخرى وبناء تحالفات معها بناءً على مدى توافق الأهداف،
مما يخلق شبكات فرعية أكثر تماسكًا وتنسيقًا داخل النظام العام.
"""

class Nucleus:
    def __init__(self, id, objective):
        self.id = id
        self.objective = objective
        self.allies = []

    def evaluate_and_ally(self, other):
        if self.objective == other.objective:
            self.allies.append(other.id)
            print(f"✅ {self.id} تحالفت مع {other.id} (هدف مشترك: {self.objective})")
        else:
            print(f"❌ {self.id} لم يتحالف مع {other.id} (اختلاف بالأهداف)")

    def report(self):
        return {
            "id": self.id,
            "objective": self.objective,
            "allies": self.allies
        }

# إنشاء نوى وتحالفها بناءً على الأهداف
n1 = Nucleus("N-01", "defense")
n2 = Nucleus("N-02", "defense")
n3 = Nucleus("N-03", "expansion")

n1.evaluate_and_ally(n2)
n1.evaluate_and_ally(n3)

print(n1.report())
