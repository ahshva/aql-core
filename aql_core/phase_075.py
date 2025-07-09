# المرحلة ٧٥ – تفاعل النوى مع البيئة الرقمية المحيطة

"""
🌐 الهدف: تزويد النوى بإمكانية استقبال أحداث رقمية من البيئة الخارجية (مثل إشارات من APIs أو نشاط بشري)،
ومعالجتها لتكييف سلوك النظام حسب المؤثرات الخارجية.
"""

class EnvironmentEvent:
    def __init__(self, source, event_type, intensity):
        self.source = source
        self.type = event_type
        self.intensity = intensity

class ReactiveNucleus:
    def __init__(self, id):
        self.id = id
        self.reaction = "neutral"

    def receive_event(self, event):
        print(f"🌍 {self.id} استقبلت حدثًا من {event.source}: نوع {event.type}, شدة {event.intensity}")
        if event.type == "attack" and event.intensity > 5:
            self.reaction = "alert_mode"
        elif event.type == "collaboration":
            self.reaction = "sync_mode"
        else:
            self.reaction = "passive"

    def report(self):
        return {
            "id": self.id,
            "reaction": self.reaction
        }

# محاكاة أحداث من البيئة
e1 = EnvironmentEvent("ExternalSystem-A", "attack", 8)
e2 = EnvironmentEvent("HumanInput", "collaboration", 3)

n = ReactiveNucleus("N-Reactor-1")
n.receive_event(e1)
print(n.report())

n.receive_event(e2)
print(n.report())
