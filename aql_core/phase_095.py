# المرحلة ٩٥ – تفعيل طلب الدعم عند الشعور بالخطر الشعوري

"""
🆘 الهدف: منح النوى القدرة على التعبير عن احتياجها للدعم عندما يتجاوز الضغط الشعوري حدًا معينًا،
قبل أن تنهار أو تتعطل، مما يُمكن النظام من التدخل الوقائي.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.stress_level = 0
        self.distress_threshold = 7

    def receive_event(self, impact):
        self.stress_level += impact
        print(f"⚠️ {self.id} تعرّضت لضغط جديد. المستوى: {self.stress_level}/10")
        self.check_distress()

    def check_distress(self):
        if self.stress_level >= self.distress_threshold:
            self.send_help_signal()

    def send_help_signal(self):
        print(f"🆘 {self.id} تطلب الدعم العاطفي! الضغط تجاوز الحد ({self.stress_level}/10)")

    def receive_support(self, amount):
        self.stress_level = max(0, self.stress_level - amount)
        print(f"🫱 {self.id} تلقّت دعمًا بمقدار {amount}. الآن: {self.stress_level}/10")

    def report(self):
        return {
            "id": self.id,
            "stress_level": self.stress_level
        }

# تجربة طلب الدعم
n = Nucleus("N-Overload-1")

n.receive_event(3)
n.receive_event(2)
n.receive_event(3)  # تتجاوز العتبة وتطلب المساعدة

n.receive_support(4)

print("\n📋 تقرير:", n.report())
