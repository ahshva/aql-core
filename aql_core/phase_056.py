# المرحلة ٥٦ – توصيل النوى ببعضها عبر شبكة إشارات داخلية

"""
🌐 الهدف: إنشاء شبكة داخلية تسمح للنوى بالتواصل فيما بينها من خلال إرسال واستقبال إشارات، لتنسيق القرارات وتحقيق وعي جماعي بسيط.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.connections = []
        self.inbox = []

    def connect(self, other):
        if other not in self.connections:
            self.connections.append(other)
            other.connect(self)

    def send_signal(self, message):
        for conn in self.connections:
            conn.receive_signal(f"من {self.id}: {message}")

    def receive_signal(self, message):
        self.inbox.append(message)

    def report(self):
        return {
            "id": self.id,
            "connections": [c.id for c in self.connections],
            "messages_received": self.inbox
        }

# إعداد النوى وتوصيلها
n1 = Nucleus("N1")
n2 = Nucleus("N2")
n3 = Nucleus("N3")

n1.connect(n2)
n2.connect(n3)

# إرسال إشارات
n1.send_signal("استعد للتوسع")
n3.send_signal("مؤكد – جاهز")

# طباعة التقارير
for n in [n1, n2, n3]:
    print(n.report())
