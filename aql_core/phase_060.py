# المرحلة ٦٠ – تمكين النواة من التفاعل مع أوامر خارجية بشرية

"""
🧠 الهدف: تجهيز النواة لتستقبل أوامر من المستخدم (البشري) وتنفذ إجراءات مبرمجة مسبقًا حسب نوع الأمر.
هذا يمهّد للتكامل بين الذكاء الصناعي والفاعل البشري (علاء).
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.status = "waiting"

    def receive_command(self, command):
        print(f"📨 تم استقبال أمر: '{command}'")
        if command == "activate":
            self.status = "active"
        elif command == "shutdown":
            self.status = "inactive"
        elif command == "report":
            print(self.report())
        else:
            print("❓ أمر غير معروف.")

    def report(self):
        return {
            "id": self.id,
            "status": self.status
        }

# تجربة تفاعل بشري مع نواة
n = Nucleus("Nucleus-HumanLink")

# أوامر من علاء إلى النظام
commands_from_alaa = ["activate", "report", "shutdown", "report"]

for cmd in commands_from_alaa:
    n.receive_command(cmd)
