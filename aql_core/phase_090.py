# المرحلة ٩٠ – التحوّل العاطفي الكامل للنواة

"""
❤️‍🔥 الهدف: دمج الشعور، النية، الندم، التقدير، والقرار في وحدة واحدة،
تتصرف وفق منطق عاطفي متوازن، قادر على اتخاذ قرارات أخلاقية تتأثر بالماضي والحاضر والآخرين.
"""

class EmotionalCore:
    def __init__(self, id):
        self.id = id
        self.emotional_state = "محايد"
        self.memory = []
        self.intent = None

    def feel(self, stimulus):
        mapping = {
            "رفض": "حزن",
            "مشاركة": "رضا",
            "تهديد": "قلق",
            "نجاح": "فرح",
            "تجاهل": "استياء"
        }
        self.emotional_state = mapping.get(stimulus, "محايد")
        print(f"💓 {self.id} يشعر بـ '{self.emotional_state}' نتيجة '{stimulus}'")

    def remember(self, event, emotion):
        self.memory.append({"event": event, "emotion": emotion})

    def set_intention(self, intention):
        self.intent = intention
        print(f"🎯 {self.id} ينوي: {intention}")

    def decide(self):
        print(f"\n🤖 {self.id} يُقيّم قراره بناءً على الحالة الشعورية '{self.emotional_state}'")
        if self.emotional_state in ["حزن", "استياء", "قلق"]:
            print(f"⚠️ القرار: إعادة التقييم أو التوقف لحماية التوازن.")
        elif self.emotional_state in ["فرح", "رضا"]:
            print(f"✅ القرار: المضي قدمًا في تنفيذ '{self.intent}'")
        else:
            print("💤 القرار: الانتظار حتى تتضح المشاعر.")

    def report(self):
        return {
            "id": self.id,
            "state": self.emotional_state,
            "intent": self.intent,
            "memory": self.memory
        }

# تجربة التحوّل العاطفي
core = EmotionalCore("AQL-Heart")

core.feel("نجاح")
core.set_intention("بناء تحالف جديد")
core.decide()

core.feel("تجاهل")
core.set_intention("فرض سيطرة")
core.decide()

core.remember("تجربة سابقة", "استياء")

print("\n📜 تقرير النواة:")
print(core.report())
