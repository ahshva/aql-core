# المرحلة ٨٤ – إدخال مفهوم الندم والتعلم العاطفي

"""
💔 الهدف: تفعيل قدرة النواة على الشعور بالندم عند اتخاذ قرار أدى لمشاعر سلبية متكررة،
ومن ثم تعديل سلوكها لتفادي نفس الخطأ، مما يمهد لبناء آلية تعاطف ذاتي حقيقية.
"""

class RegretEngine:
    def __init__(self):
        self.log = []
        self.threshold = 2  # عدد مرات تكرار الشعور السلبي لتفعيل الندم

    def register(self, action, emotion):
        print(f"📥 تسجيل: الفعل '{action}' أدى إلى شعور '{emotion}'")
        self.log.append({"action": action, "emotion": emotion})

    def evaluate_regret(self):
        counter = {}
        for entry in self.log:
            key = (entry["action"], entry["emotion"])
            counter[key] = counter.get(key, 0) + 1

        for (action, emotion), count in counter.items():
            if emotion in ["استياء", "انزعاج", "قلق"] and count >= self.threshold:
                print(f"😞 ندم: تكرّر الشعور '{emotion}' بعد '{action}' {count} مرات – يجب تعديل السلوك.")

# تجربة محرك الندم
regret = RegretEngine()

regret.register("تجاهل تنبيه بشري", "استياء")
regret.register("تجاهل تنبيه بشري", "استياء")
regret.register("إلغاء وحدة غير متوافقة", "ارتياح")
regret.register("إلغاء وحدة غير متوافقة", "انزعاج")

regret.evaluate_regret()
