# المرحلة ٧٤ – تمكين النوى من إصدار توصيات استراتيجية

"""
📈 الهدف: السماح للنوى المستقلة بتحليل وضع النظام واقتراح توصيات استراتيجية لتحسين الأداء أو تجنب المخاطر،
حتى بدون تنفيذ فوري، مما يرفع مستوى الوعي والتخطيط الجماعي.
"""

class StrategicNucleus:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.recommendation = None

    def analyze(self):
        if "threat_level" in self.data and self.data["threat_level"] > 7:
            self.recommendation = "تعزيز الدفاعات"
        elif "growth_rate" in self.data and self.data["growth_rate"] > 5:
            self.recommendation = "توسيع النطاق"
        else:
            self.recommendation = "استمرار المراقبة"

    def report(self):
        print(f"🧠 {self.id} توصية: {self.recommendation}")
        return {
            "id": self.id,
            "input_data": self.data,
            "recommendation": self.recommendation
        }

# تجربة التوصية في حالات مختلفة
n1 = StrategicNucleus("N-Strategy-A", {"threat_level": 8})
n2 = StrategicNucleus("N-Strategy-B", {"growth_rate": 6})
n3 = StrategicNucleus("N-Strategy-C", {"stability": True})

for n in [n1, n2, n3]:
    n.analyze()
    n.report()
