# المرحلة ٩٣ – تهدئة النوى الأخرى ضمن النظام

"""
🌿 الهدف: منح النواة القدرة على تقديم دعم عاطفي لنواة أخرى متوترة،
عبر تخفيف حدة مشاعرها السلبية، مما يعزز الاستقرار الداخلي والتضامن الشعوري.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.emotion = "محايد"
        self.intensity = 0

    def set_emotion(self, emotion, intensity):
        self.emotion = emotion
        self.intensity = intensity
        print(f"⚡ {self.id} في حالة '{emotion}' بدرجة {intensity}/10")

    def receive_calm(self, amount):
        if self.intensity > 0:
            self.intensity = max(0, self.intensity - amount)
            print(f"🕊️ {self.id} تلقّت تهدئة: المستوى الآن {self.intensity}/10")
        else:
            print(f"✅ {self.id} مستقر بالفعل.")

    def report(self):
        return {
            "id": self.id,
            "emotion": self.emotion,
            "intensity": self.intensity
        }

class CalmingUnit:
    def __init__(self, id):
        self.id = id

    def calm(self, target, amount=3):
        print(f"\n🫱 {self.id} يحاول تهدئة {target.id}...")
        target.receive_calm(amount)

# تجربة الدعم العاطفي
n1 = Nucleus("N-Stressed")
n2 = CalmingUnit("N-Calmer")

n1.set_emotion("قلق", 7)
n2.calm(n1)
n2.calm(n1)

print("\n📋 تقرير الحالة:", n1.report())
