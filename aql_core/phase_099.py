# المرحلة ٩٩ – اتخاذ قرار عاطفي جماعي موحد

"""
🧠❤️ الهدف: تمكين مجموعة من النوى من جمع مشاعرها، وتحليل الاتجاه العام،
ثم اتخاذ قرار موحّد يعكس التوجه العاطفي الجماعي بدلاً من القرار الفردي.
"""

class Nucleus:
    def __init__(self, id, emotion):
        self.id = id
        self.emotion = emotion  # "رضا", "قلق", "استياء", "فرح", "محايد"

    def report_emotion(self):
        print(f"💬 {self.id} تعبر عن شعورها: {self.emotion}")
        return self.emotion

class EmotionalCouncil:
    def __init__(self, members):
        self.members = members

    def collective_emotion(self):
        emotions = {}
        for member in self.members:
            e = member.report_emotion()
            emotions[e] = emotions.get(e, 0) + 1
        dominant = max(emotions, key=emotions.get)
        print(f"\n🧭 الشعور الجماعي السائد: {dominant}")
        return dominant

    def decide_action(self):
        dominant = self.collective_emotion()
        decision_map = {
            "رضا": "الاستمرار كما هو",
            "فرح": "توسيع النظام",
            "قلق": "إبطاء العمليات",
            "استياء": "إعادة تقييم المسار",
            "محايد": "المراقبة فقط"
        }
        action = decision_map.get(dominant, "لا قرار")
        print(f"🤝 القرار الجماعي: {action}")

# إنشاء المجلس العاطفي
a = Nucleus("Alpha", "فرح")
b = Nucleus("Beta", "فرح")
c = Nucleus("Gamma", "قلق")
d = Nucleus("Delta", "فرح")

council = EmotionalCouncil([a, b, c, d])
council.decide_action()
