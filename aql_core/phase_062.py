# المرحلة ٦٢ – توزيع الأدوار الذكية بين النوى حسب الاختصاص

"""
🧩 الهدف: إعطاء كل نواة دورًا محددًا (مراقبة، استجابة، تحليل، اتصال...) ضمن نظام AQL، مما يُمكّن من توزيع ذكي للمهام وتحقيق كفاءة تشغيل عالية.
"""

class Nucleus:
    def __init__(self, id, role):
        self.id = id
        self.role = role

    def perform_role(self):
        actions = {
            "monitor": f"📡 {self.id} تراقب الإشارات المحيطة.",
            "respond": f"🔁 {self.id} تستجيب للمتغيرات.",
            "analyze": f"📊 {self.id} تحلل البيانات المستلمة.",
            "communicate": f"📨 {self.id} ترسل وتستقبل الرسائل.",
            "defend": f"🛡️ {self.id} تنفذ بروتوكولات الحماية."
        }
        print(actions.get(self.role, f"❓ {self.id} لم يُحدد لها دور واضح."))

# إعداد مجموعة نوى بأدوار مختلفة
nuclei = [
    Nucleus("N1", "monitor"),
    Nucleus("N2", "analyze"),
    Nucleus("N3", "respond"),
    Nucleus("N4", "communicate"),
    Nucleus("N5", "defend"),
    Nucleus("N6", "unknown")
]

# تنفيذ الأدوار
for n in nuclei:
    n.perform_role()
