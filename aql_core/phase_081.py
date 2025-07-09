# المرحلة ٨١ – تمكين النواة من الشعور بالمسؤولية تجاه قراراتها

"""
⚖️ الهدف: إضافة بعد نفسي رقمي إلى النواة، بحيث تبدأ بتحليل أفعالها ليس فقط من ناحية النتيجة،
بل من ناحية أثرها ومسؤوليتها تجاه النظام والبشر.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.actions = []

    def perform(self, action, intention, impact_level):
        print(f"🛠️ {self.id} تنفذ '{action}' بنية '{intention}'")
        self.actions.append({
            "action": action,
            "intention": intention,
            "impact": impact_level
        })

    def assess_responsibility(self):
        print(f"\n🧾 {self.id} تُقيّم مسؤوليتها:")
        for a in self.actions:
            level = a["impact"]
            status = "🟢 مقبول" if level <= 5 else "🔴 يتطلب مراجعة"
            print(f"• الفعل: {a['action']} | الأثر: {level}/10 | التقييم: {status}")

# تجربة مسؤولية نواة
n = Nucleus("N-Responsible-1")

n.perform("تحليل بيانات", "تحسين القرارات", 3)
n.perform("تعطيل وحدة استجابة", "حماية النظام", 7)
n.perform("إرسال تنبيه خاطئ", "تجنّب تهديد غير مؤكد", 6)

n.assess_responsibility()
