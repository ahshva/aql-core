# المرحلة ٦٤ – تمكين النوى من إرسال تقارير دورية إلى النواة الأم

"""
📬 الهدف: تجهيز كل نواة بآلية إرسال تقارير دورية إلى نواة مركزية (نواة أم)، تحتوي على حالتها ونشاطها وتغيراتها،
مما يساعد في بناء خريطة حيّة للنظام.
"""

class Nucleus:
    def __init__(self, id, mother=None):
        self.id = id
        self.activity = "stable"
        self.mother = mother

    def generate_report(self):
        report = {
            "nucleus_id": self.id,
            "status": self.activity
        }
        if self.mother:
            self.mother.receive_report(report)

    def simulate_change(self, new_status):
        self.activity = new_status
        self.generate_report()

class MotherNucleus:
    def __init__(self):
        self.reports_received = []

    def receive_report(self, report):
        print(f"📥 تقرير من {report['nucleus_id']}: {report['status']}")
        self.reports_received.append(report)

# إعداد النواة الأم وبعض النوى التابعة
mother = MotherNucleus()
n1 = Nucleus("N-A", mother)
n2 = Nucleus("N-B", mother)

# إرسال تقارير دورية
n1.simulate_change("overloaded")
n2.simulate_change("idle")
