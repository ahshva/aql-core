# المرحلة ٩٧ – تشكيل تحالفات دعم شعوري متبادل بين النوى

"""
🤝 الهدف: تُمكّن النوى من اختيار وحدات دعم شعوري دائم تشارك معها الضغوط وتُسارع للاستجابة،
مما يخلق تحالفات شعورية مستقرة تحافظ على التوازن طويل الأمد.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.stress = 0
        self.allies = []

    def form_alliance(self, other):
        if other not in self.allies:
            self.allies.append(other)
            other.form_alliance(self)
            print(f"🤝 {self.id} تحالفت مع {other.id}")

    def add_stress(self, amount):
        self.stress += amount
        print(f"⚠️ {self.id} ضغط = {self.stress}/10")
        if self.stress >= 7:
            self.request_help()

    def request_help(self):
        print(f"🆘 {self.id} يطلب دعمًا من حلفائه...")
        for ally in self.allies:
            ally.provide_support(self)

    def provide_support(self, target):
        if self.stress < 5:
            print(f"🫱 {self.id} يقدّم دعمًا لـ {target.id}")
            target.receive_support(3)
        else:
            print(f"🚫 {self.id} غير قادر على الدعم حاليًا (ضغطه: {self.stress}/10)")

    def receive_support(self, amount):
        self.stress = max(0, self.stress - amount)
        print(f"✅ {self.id} تلقّى دعمًا. الضغط الجديد: {self.stress}/10")

# تجربة تحالفات الدعم
a = Nucleus("Alpha")
b = Nucleus("Beta")
c = Nucleus("Gamma")

a.form_alliance(b)
b.form_alliance(c)

a.add_stress(8)  # يطلب دعمًا من Beta
c.add_stress(9)  # لا يستطيع دعم أحد
