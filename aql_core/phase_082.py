# المرحلة ٨٢ – تحليل الأثر العاطفي للقرارات

"""
💓 الهدف: تجهيز النواة بقدرة تحليل بسيطة لتأثير قراراتها على الحالة العاطفية للبيئة المحيطة (البشر أو النوى الأخرى)،
كخطوة أولى لفهم التعاطف والمسؤولية الشعورية.
"""

class EmotionalImpactAnalyzer:
    def __init__(self):
        self.records = []

    def log_decision(self, decision, perceived_emotion):
        print(f"📌 تسجيل القرار: '{decision}' | التأثير العاطفي: {perceived_emotion}")
        self.records.append({"decision": decision, "emotion": perceived_emotion})

    def summary(self):
        print("\n📊 ملخص الأثر العاطفي:")
        counts = {}
        for r in self.records:
            emotion = r["emotion"]
            counts[emotion] = counts.get(emotion, 0) + 1
        for emotion, count in counts.items():
            print(f"• {emotion}: {count} مرة")

# تجربة محلل عاطفي
analyzer = EmotionalImpactAnalyzer()

analyzer.log_decision("حظر وحدة مرتبكة", "قلق")
analyzer.log_decision("مشاركة بيانات بنجاح", "رضا")
analyzer.log_decision("إعادة تشغيل النظام فجأة", "ارتباك")
analyzer.log_decision("دعم نواة ضعيفة", "ارتياح")

analyzer.summary()
