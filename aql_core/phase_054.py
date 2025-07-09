# المرحلة ٥٤ – مراقبة النوى وتقييم الاستجابة

"""
🎯 الهدف: تطوير آلية مراقبة ذاتية لكل نواة تُنشأ داخل النظام، بهدف تقييم نشاطها واستجابتها، وتحديد مدى تأثيرها في التوسع.
"""

class Nucleus:
    def __init__(self, id, parent=None):
        self.id = id
        self.parent = parent
        self.children = []
        self.status = "active"
        self.signal_strength = 0.0

    def activate(self):
        self.signal_strength = 1.0

    def evaluate(self):
        # التقييم بسيط كبداية: إذا كانت قوة الإشارة أقل من 0.5 تُعتبر خاملة
        return "responsive" if self.signal_strength >= 0.5 else "inactive"

    def spawn(self, count):
        for i in range(count):
            child = Nucleus(id=f"{self.id}-{i}", parent=self)
            self.children.append(child)

    def report(self):
        return {
            "id": self.id,
            "status": self.status,
            "evaluation": self.evaluate(),
            "children_count": len(self.children)
        }

# إنشاء نواة رئيسية ومراقبتها
core = Nucleus(id="Core-54")
core.activate()
core.spawn(3)

# طباعة تقرير
print("📊 تقرير النواة:")
print(core.report())
