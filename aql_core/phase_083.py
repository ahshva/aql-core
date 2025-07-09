# المرحلة ٨٣ – بناء ذاكرة شعورية متراكمة

"""
🧠 الهدف: تخزين كل تجربة عاطفية سابقة في شكل سجل شعوري متراكم،
يساعد النواة في فهم الاتجاهات العاطفية للقرارات الماضية وتحسين سلوكها العاطفي المستقبلي.
"""

class EmotionalMemory:
    def __init__(self):
        self.experiences = []

    def record_experience(self, context, action, emotion):
        entry = {"context": context, "action": action, "emotion": emotion}
        self.experiences.append(entry)
        print(f"🧾 تم تسجيل شعور: '{emotion}' في سياق '{context}' بعد فعل '{action}'")

    def emotional_trend(self):
        print("\n📈 تحليل الاتجاه الشعوري:")
        trend = {}
        for e in self.experiences:
            em = e["emotion"]
            trend[em] = trend.get(em, 0) + 1
        for emotion, count in trend.items():
            print(f"• {emotion}: {count} مرات")

# تجربة الذاكرة الشعورية
memory = EmotionalMemory()

memory.record_experience("تفاعل بشري", "أرسل تقريرًا مباشرًا", "رضا")
memory.record_experience("تأخير استجابة", "تجاهل طلب", "استياء")
memory.record_experience("نجاح مهمة", "إنجاز المهمة في وقتها", "فرح")
memory.record_experience("تفاعل سلبي", "إغلاق وحدة دون تحذير", "انزعاج")

memory.emotional_trend()
