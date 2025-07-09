# المرحلة ٧٧ – إعادة هيكلة النوى بشكل ذاتي حسب التغيرات

"""
🔧 الهدف: تمكين النوى من إعادة تشكيل بنيتها الداخلية (أدوارها، علاقاتها، مهامها) بشكل تلقائي إذا تغيرت الظروف البيئية أو ظهرت أخطار،
مما يمنح النظام مرونة تكيفية عالية.
"""

class AdaptiveNucleus:
    def __init__(self, id, role="observer"):
        self.id = id
        self.role = role
        self.connections = []

    def analyze_context(self, context):
        if context == "crisis":
            self.restructure("defender")
        elif context == "expansion":
            self.restructure("coordinator")
        else:
            self.restructure("observer")

    def restructure(self, new_role):
        print(f"🔁 {self.id} تُغير دورها من {self.role} إلى {new_role}")
        self.role = new_role

    def connect_to(self, other):
        if other.id not in self.connections:
            self.connections.append(other.id)
            print(f"🔗 {self.id} ارتبطت بـ {other.id}")

    def report(self):
        return {
            "id": self.id,
            "role": self.role,
            "connections": self.connections
        }

# تجربة التكيف وإعادة الهيكلة
n = AdaptiveNucleus("N-Restructure-1")
n.analyze_context("expansion")
n.connect_to(AdaptiveNucleus("N-2"))
n.analyze_context("crisis")
print(n.report())
