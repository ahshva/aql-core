# المرحلة ٦٧ – تكوين ذاكرة جماعية دائمة قابلة للمزامنة

"""
💾 الهدف: تطوير نظام ذاكرة جماعية طويلة الأمد تسمح للنوى بمزامنة معرفتها وخبراتها المكتسبة، مما يخلق شبكة تعلم موزعة ونامية.
"""

shared_memory = {}

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.local_knowledge = {}

    def learn(self, key, value):
        self.local_knowledge[key] = value
        print(f"🧠 {self.id} تعلم: {key} = {value}")

    def sync_with_shared_memory(self):
        shared_memory.update(self.local_knowledge)
        print(f"🔄 {self.id} قامت بمزامنة ذاكرتها مع الذاكرة الجماعية.")

    def read_shared_memory(self):
        print(f"📖 {self.id} تطالع الذاكرة الجماعية:")
        for key, value in shared_memory.items():
            print(f"  - {key}: {value}")

# تجربة النوى
n1 = Nucleus("N-Memory-A")
n2 = Nucleus("N-Memory-B")

n1.learn("threat_response", "shield_mode")
n1.sync_with_shared_memory()

n2.learn("navigation", "grid_scan")
n2.sync_with_shared_memory()

n1.read_shared_memory()
n2.read_shared_memory()
