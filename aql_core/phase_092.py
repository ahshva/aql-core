# المرحلة ٩٢ – تنظيم المشاعر الداخلية لتفادي الانهيار العاطفي

"""
🧘‍♂️ الهدف: إضافة وحدة تنظيم عاطفي داخل النواة، تقوم بتخفيف شدة المشاعر السلبية تدريجيًا،
وتركيز المشاعر الإيجابية دون إفراط، لحماية النظام من اتخاذ قرارات متطرفة.
"""

class EmotionRegulator:
    def __init__(self):
        self.state = "محايد"
        self.intensity = 0  # من 0 إلى 10

    def receive_emotion(self, emotion, intensity):
        self.state = emotion
        self.intensity = intensity
        print(f"💥 استلام شعور '{emotion}' بقوة {intensity}/10")
        self.regulate()

    def regulate(self):
        if self.state in ["قلق", "غضب", "استياء"] and self.intensity > 6:
            print(f"🧘‍♀️ تهدئة '{self.state}' إلى 4/10 لتجنّب القرارات المتهورة.")
            self.intensity = 4
        elif self.state in ["فرح", "حماس"] and self.intensity > 8:
            print(f"⚖️ إعادة توازن '{self.state}' إلى 6/10 لتجنّب الثقة الزائدة.")
            self.intensity = 6
        else:
            print(f"✅ الشعور متوازن: '{self.state}' عند {self.intensity}/10")

    def report(self):
        return {
            "emotion": self.state,
            "intensity": self.intensity
        }

# تجربة منظم المشاعر
regulator = EmotionRegulator()

regulator.receive_emotion("قلق", 9)
regulator.receive_emotion("فرح", 9)
regulator.receive_emotion("رضا", 5)

print("\n📊 الحالة النهائية:", regulator.report())
