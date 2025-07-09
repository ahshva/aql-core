# المرحلة ٩٨ – إنشاء خريطة شعورية مرئية للنظام

"""
🗺️ الهدف: توليد خريطة تُظهر كل نواة، حالتها الشعورية، وتحالفاتها، في شكل نصي واضح،
لتمكين النظام من تحليل البنية الشعورية وفهم نقاط التوتر أو الدعم الجماعي.
"""

class EmotionalMap:
    def __init__(self):
        self.nuclei = {}

    def add_nucleus(self, nucleus):
        self.nuclei[nucleus.id] = nucleus

    def render_map(self):
        print("\n🧭 خريطة الشعور الجماعي:")
        for nucleus in self.nuclei.values():
            status = f"{nucleus.id} | ضغط: {nucleus.stress}/10 | حلفاء: {[ally.id for ally in nucleus.allies]}"
            print(status)

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.stress = 0
        self.allies = []

    def form_alliance(self, other):
        if other not in self.allies:
            self.allies.append(other)
            other.form_alliance(self)

    def add_stress(self, amount):
        self.stress += amount

# إعداد النوى والخريطة
a = Nucleus("N-Alpha")
b = Nucleus("N-Beta")
c = Nucleus("N-Charlie")
d = Nucleus("N-Delta")

a.form_alliance(b)
b.form_alliance(c)
c.form_alliance(d)

a.add_stress(3)
b.add_stress(6)
c.add_stress(8)
d.add_stress(2)

emap = EmotionalMap()
for n in [a, b, c, d]:
    emap.add_nucleus(n)

emap.render_map()
