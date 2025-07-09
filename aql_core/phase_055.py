# المرحلة ٥٥ – بناء نظام إنذار داخلي للنوى

"""
🚨 الهدف: تطوير نظام إنذار داخلي داخل كل نواة يُمكنه اكتشاف أي سلوك غير طبيعي (مثل الخمول الطويل أو التشويش)،
وإرسال إشارات تحذيرية إلى نواة التحكم المركزية.
"""

class Nucleus:
    def __init__(self, id, activity_level=1.0):
        self.id = id
        self.activity_level = activity_level
        self.alert_triggered = False

    def monitor(self):
        if self.activity_level < 0.3:
            self.trigger_alert(reason="low_activity")

    def trigger_alert(self, reason):
        self.alert_triggered = True
        print(f"⚠️ إنذار من النواة {self.id}: السبب – {reason}")

    def report(self):
        return {
            "id": self.id,
            "activity_level": self.activity_level,
            "alert_triggered": self.alert_triggered
        }

# تجربة النظام على مجموعة نوى
nuclei = [
    Nucleus(id="n1", activity_level=0.9),
    Nucleus(id="n2", activity_level=0.2),
    Nucleus(id="n3", activity_level=0.5)
]

# مراقبة كل نواة
for nucleus in nuclei:
    nucleus.monitor()
    print(nucleus.report())
