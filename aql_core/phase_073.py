# المرحلة ٧٣ – تفعيل آلية التصحيح الذاتي للنوى

"""
🔄 الهدف: تمكين كل نواة من اكتشاف حالات الخلل الذاتي وتصحيحها تلقائيًا دون انتظار تدخل خارجي،
مما يمنح النظام درجة عالية من الثبات والمرونة.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.status = "stable"
        self.error_detected = False

    def simulate_operation(self, signal):
        if signal == "error":
            self.error_detected = True
            self.status = "faulty"
            print(f"❗ {self.id} اكتشفت خللًا ذاتيًا.")
            self.self_repair()
        else:
            print(f"✅ {self.id} تعمل بكفاءة.")

    def self_repair(self):
        if self.error_detected:
            print(f"🔧 {self.id} تُجري عملية تصحيح...")
            self.status = "stable"
            self.error_detected = False
            print(f"✅ {self.id} استعادت استقرارها.")

    def report(self):
        return {
            "id": self.id,
            "status": self.status,
            "error": self.error_detected
        }

# تجربة الخلل والتصحيح الذاتي
n = Nucleus("N-SelfFix-1")
n.simulate_operation("ok")
print(n.report())

n.simulate_operation("error")
print(n.report())
