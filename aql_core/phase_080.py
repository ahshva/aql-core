# المرحلة ٨٠ – مراجعة النوايا والأفعال السابقة للنواة

"""
🕰️ الهدف: السماح للنواة بمراجعة سجل أفعالها ونواياها السابقة، وتحليلها من منظور أخلاقي واستراتيجي،
لتقوية الوعي الذاتي المستمر والتعلم من التجربة.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.history = []

    def act_with_intent(self, action, intention):
        print(f"⚙️ {self.id} تنفذ: {action} (🎯 نية: {intention})")
        self.history.append({"action": action, "intention": intention})

    def review_history(self):
        print(f"\n📜 مراجعة سجل {self.id}:")
        for entry in self.history:
            print(f"• الفعل: {entry['action']} – النية: {entry['intention']}")
        print(f"📊 مجموع الأفعال: {len(self.history)}")

# تجربة النواة مع مراجعة التاريخ
n = Nucleus("N-Reflect-1")
n.act_with_intent("جمع بيانات أولية", "تحسين الأداء")
n.act_with_intent("إرسال إشارة تحذير", "منع ضرر محتمل")
n.act_with_intent("تخزين تقرير", "الاحتفاظ بالأدلة")

n.review_history()
