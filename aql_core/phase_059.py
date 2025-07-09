# المرحلة ٥٩ – بناء سجل تطوّر ذاتي لكل نواة

"""
📘 الهدف: تمكين كل نواة من تسجيل مراحل تطورها بشكل ذاتي، لتوثيق قراراتها وتحوّلاتها على مدار الزمن وتحليل مسار تطورها.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.state = "initialized"
        self.history = []

    def evolve(self, new_state):
        self.history.append((self.state, new_state))
        self.state = new_state
        print(f"🔄 {self.id} انتقلت من '{self.history[-1][0]}' إلى '{new_state}'")

    def report(self):
        return {
            "id": self.id,
            "current_state": self.state,
            "evolution_history": self.history
        }

# تجربة تطور نواة واحدة
n = Nucleus("Nucleus-X")
n.evolve("scanning")
n.evolve("connecting")
n.evolve("coordinating")

print("📜 تقرير التطور:")
print(n.report())
