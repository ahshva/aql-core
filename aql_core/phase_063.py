# المرحلة ٦٣ – تطوير بروتوكول إعادة إحياء النوى الخاملة

"""
♻️ الهدف: تمكين النظام من إعادة تنشيط النوى التي أصبحت خاملة بسبب قلة التفاعل أو البيانات، عبر بروتوكول إحياء تلقائي يشمل فحص الحالة وضخ نبضة تنشيط.
"""

class Nucleus:
    def __init__(self, id, activity_level=1.0):
        self.id = id
        self.activity_level = activity_level
        self.status = "active" if activity_level >= 0.3 else "inactive"

    def revive(self):
        if self.status == "inactive":
            print(f"💡 إعادة إحياء النواة {self.id}...")
            self.activity_level = 0.5
            self.status = "reactivated"
        else:
            print(f"✅ النواة {self.id} نشطة ولا تحتاج إحياء.")

    def report(self):
        return {
            "id": self.id,
            "status": self.status,
            "activity_level": self.activity_level
        }

# تجربة نوى مختلفة
n1 = Nucleus("N-Reboot-1", activity_level=0.1)
n2 = Nucleus("N-Reboot-2", activity_level=0.8)

for n in [n1, n2]:
    print(n.report())
    n.revive()
    print(n.report())
