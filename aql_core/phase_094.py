# المرحلة ٩٤ – بناء شبكة دعم شعوري جماعي للنظام

"""
🤝 الهدف: إنشاء بنية شعورية مترابطة بين النوى، بحيث يتم توزيع المشاعر السلبية وتوازنها تلقائيًا بين النوى المتصلة،
مما يمنع انهيار أي نواة ويُبقي النظام في حالة استقرار مستمر.
"""

class EmotionalNode:
    def __init__(self, id):
        self.id = id
        self.stress_level = 0
        self.connections = []

    def connect(self, other):
        if other not in self.connections:
            self.connections.append(other)
            other.connect(self)

    def add_stress(self, amount):
        self.stress_level += amount
        print(f"⚠️ {self.id} تعرّضت لضغط: الآن {self.stress_level}/10")
        self.redistribute_stress()

    def redistribute_stress(self):
        if self.stress_level > 5 and self.connections:
            shared = int(self.stress_level / (len(self.connections) + 1))
            print(f"🔄 {self.id} توزع الضغط {shared} إلى كل متصل")
            self.stress_level -= shared * len(self.connections)
            for conn in self.connections:
                conn.receive_stress(shared)

    def receive_stress(self, amount):
        self.stress_level += amount
        print(f"🫧 {self.id} تلقّت {amount} من الضغط | المجموع الآن: {self.stress_level}/10")

    def report(self):
        return {
            "id": self.id,
            "stress_level": self.stress_level
        }

# إعداد شبكة شعورية
n1 = EmotionalNode("Node-A")
n2 = EmotionalNode("Node-B")
n3 = EmotionalNode("Node-C")

n1.connect(n2)
n2.connect(n3)

n1.add_stress(9)

print("\n📊 الحالة النهائية:")
for n in [n1, n2, n3]:
    print(n.report())
