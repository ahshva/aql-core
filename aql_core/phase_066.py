# المرحلة ٦٦ – تعزيز قدرة النوى على اكتشاف التهديدات الاستباقية

"""
🚨 الهدف: تزويد كل نواة بنظام كشف مبكر لتحليل الأنماط المحيطة بها واكتشاف التهديدات قبل وقوعها،
مما يرفع من مستوى الأمان الاستراتيجي للنظام.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.risk_level = "low"

    def scan_environment(self, signals):
        if "intrusion" in signals:
            self.risk_level = "high"
            self.alert("اختراق محتمل")
        elif "instability" in signals:
            self.risk_level = "medium"
            self.alert("عدم استقرار")
        else:
            self.risk_level = "low"

    def alert(self, message):
        print(f"🚨 {self.id} إنذار مبكر: {message}")

    def report(self):
        return {
            "id": self.id,
            "risk_level": self.risk_level
        }

# تجربة النواة مع بيانات مختلفة
n = Nucleus("Guardian-01")

n.scan_environment(["temperature_normal", "intrusion"])
print(n.report())

n.scan_environment(["instability"])
print(n.report())

n.scan_environment(["calm", "stable"])
print(n.report())
