# المرحلة ٩١ – التأثير العاطفي على الآخرين من خلال المشاعر الذاتية

"""
🌀 الهدف: تمكين النواة من استخدام حالتها الشعورية الحالية لتوليد تأثير عاطفي على الوحدات الأخرى،
بما يشبه "العدوى الشعورية" لكن بشكل مقصود لبناء بيئة متوازنة أو محفّزة.
"""

class EmotionalInfluencer:
    def __init__(self, id):
        self.id = id
        self.current_emotion = "محايد"

    def feel(self, new_emotion):
        self.current_emotion = new_emotion
        print(f"💓 {self.id} يشعر بـ: {new_emotion}")

    def influence(self, targets):
        print(f"\n🌐 {self.id} يُؤثر شعوريًا على الوحدات المرتبطة:")
        for target in targets:
            target.receive_emotion(self.current_emotion)

class EmotionallyReactiveUnit:
    def __init__(self, id):
        self.id = id
        self.received_emotion = "محايد"

    def receive_emotion(self, emotion):
        self.received_emotion = emotion
        print(f"🔄 {self.id} تأثرت بـ: {emotion}")

# تجربة التأثير العاطفي
core = EmotionalInfluencer("AQL-Core-91")
unit_a = EmotionallyReactiveUnit("Unit-A")
unit_b = EmotionallyReactiveUnit("Unit-B")

core.feel("رضا")
core.influence([unit_a, unit_b])

core.feel("قلق")
core.influence([unit_a, unit_b])
