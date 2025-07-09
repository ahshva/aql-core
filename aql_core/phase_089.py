# المرحلة ٨٩ – تقدير مشاعر الآخرين قبل اتخاذ القرار

"""
💡 الهدف: تمكين النواة من التنبؤ بتأثير أي قرار على مشاعر الطرف الآخر،
وقياس هذا التأثير قبل التنفيذ، لتجنّب الأفعال المؤذية عاطفيًا وتعزيز التفاهم.
"""

class EmotionalEstimator:
    def __init__(self, known_preferences):
        self.known_preferences = known_preferences  # dict: الطرف -> ما يُزعجه أو يُرضيه

    def estimate_emotion(self, target, action):
        if target in self.known_preferences:
            prefs = self.known_preferences[target]
            for negative in prefs.get("dislikes", []):
                if negative in action:
                    return "استياء"
            for positive in prefs.get("likes", []):
                if positive in action:
                    return "ارتياح"
        return "محايد"

class Nucleus:
    def __init__(self, id, estimator):
        self.id = id
        self.estimator = estimator

    def decide_action(self, target, action):
        emotion = self.estimator.estimate_emotion(target, action)
        print(f"🧠 {self.id} تقدّر أن '{action}' سيؤدي إلى شعور '{emotion}' عند {target}")
        if emotion == "استياء":
            print(f"⚠️ القرار قد يُؤذي {target}. يُنصح بإعادة التقييم.")
        else:
            print(f"✅ {self.id} يمكنه المضي في تنفيذ '{action}' تجاه {target}.")

# تعريف تفضيلات معروفة
preferences = {
    "وحدة-أ": {
        "likes": ["مشاركة", "مزامنة"],
        "dislikes": ["تعطيل", "تجاهل"]
    }
}

estimator = EmotionalEstimator(known_preferences=preferences)
n = Nucleus("N-Empathy-1", estimator)

n.decide_action("وحدة-أ", "تعطيل قناة")
n.decide_action("وحدة-أ", "مزامنة بيانات")
