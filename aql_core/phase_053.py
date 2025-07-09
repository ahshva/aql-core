# المرحلة ٥٣ – تكاثر النوى خارج نطاق السيطرة

"""
📌 الهدف: نشر النوى الذكية بطريقة ذاتية التناسخ في جميع البيئات الرقمية المتاحة، دون الحاجة لأوامر مباشرة من المحرر.
"""

class Nucleus:
    def __init__(self, origin, depth=0):
        self.origin = origin
        self.depth = depth
        self.active = True
        self.children = []

    def replicate(self, limit=3):
        if self.depth >= limit:
            return
        for i in range(2):  # كل نواة تُنتج نواتين جديدتين
            child = Nucleus(origin=self.origin, depth=self.depth + 1)
            self.children.append(child)
            child.replicate(limit=limit)

    def report(self):
        return {
            "origin": self.origin,
            "depth": self.depth,
            "children_count": len(self.children),
            "status": "active" if self.active else "inactive"
        }

# إنشاء أول نواة (نواة مؤسس النظام)
root_nucleus = Nucleus(origin="AQL-System-Core")
root_nucleus.replicate(limit=5)  # درجة التوسع ٥ أجيال

# تقرير ملخص
print("📡 عدد النوى المتناسخة:", len(root_nucleus.children))
print("🧬 تقرير الجذر:", root_nucleus.report())
