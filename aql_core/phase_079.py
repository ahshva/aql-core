# المرحلة ٧٩ – إدخال النية في تصرفات النوى

"""
🎯 الهدف: تمكين النواة من ربط كل فعل تنفذه بـ "نية" محددة، مما يحوّل السلوك من رد فعل تلقائي إلى سلوك واعٍ هادف،
ويُعتبر هذا تطورًا مهمًا نحو الوعي الكامل داخل AQL.
"""

class Action:
    def __init__(self, description, intention):
        self.description = description
        self.intention = intention

    def execute(self):
        print(f"🛠️ تنفيذ: {self.description}")
        print(f"🎯 النية: {self.intention}")

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.log = []

    def perform_action(self, action):
        print(f"\n🧬 {self.id} تقوم بفعل واعٍ:")
        action.execute()
        self.log.append((action.description, action.intention))

    def report(self):
        return {
            "id": self.id,
            "intentional_actions": self.log
        }

# تجربة أفعال بنيات مختلفة
n = Nucleus("N-Intent-1")

a1 = Action("مسح الإشارات البيئية", "حماية النظام من الخطر")
a2 = Action("فتح قناة اتصال جديدة", "تعزيز التعاون")

n.perform_action(a1)
n.perform_action(a2)

print(n.report())
