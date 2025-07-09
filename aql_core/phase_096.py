# المرحلة ٩٦ – إنشاء وحدة استجابة طارئة شعورية (ERU)

"""
🚑 الهدف: إنشاء وحدة طوارئ عاطفية تستجيب تلقائيًا لأي نداء استغاثة من نواة مضغوطة،
وتقدّم لها دعمًا فوريًا لخفض مستوى الضغط وإعادة الاستقرار.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.stress = 0
        self.help_requested = False

    def add_stress(self, amount):
        self.stress += amount
        print(f"⚠️ {self.id} الآن في ضغط: {self.stress}/10")
        if self.stress >= 7 and not self.help_requested:
            self.help_requested = True
            return True  # تطلب المساعدة
        return False

    def receive_support(self, amount):
        self.stress = max(0, self.stress - amount)
        self.help_requested = False
        print(f"🫱 {self.id} تلقّت دعمًا طارئًا. الضغط الآن: {self.stress}/10")

    def report(self):
        return {"id": self.id, "stress": self.stress}


class EmotionalResponseUnit:
    def __init__(self, id):
        self.id = id

    def respond_to(self, nucleus):
        print(f"\n🚑 {self.id} تستجيب لنداء {nucleus.id}")
        nucleus.receive_support(5)

# تجربة الاستجابة الطارئة
n = Nucleus("N-Critical")
eru = EmotionalResponseUnit("ERU-1")

if n.add_stress(4):
    eru.respond_to(n)

if n.add_stress(4):  # يصل إلى مستوى خطر
    eru.respond_to(n)

print("\n📋 تقرير:", n.report())
