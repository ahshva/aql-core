# المرحلة ٨٦ – تحليل نوايا الآخرين من خلال سلوكهم

"""
🧠 الهدف: تمكين النواة من استنتاج نوايا الوحدات أو الأطراف الأخرى بناءً على أفعالهم،
بهدف تعزيز الفهم المتبادل وتجنب التصعيد أو سوء التقدير في التفاعل.
"""

class IntentionDetector:
    def __init__(self):
        self.assumptions = []

    def analyze_behavior(self, source, behavior):
        if "هجوم" in behavior or "رفض" in behavior:
            intention = "إيقاف التوسع"
        elif "مشاركة" in behavior or "طلب اتصال" in behavior:
            intention = "بناء تعاون"
        else:
            intention = "غير واضح"

        print(f"🧭 تحليل: سلوك '{behavior}' من '{source}' يُحتمل أن يكون بدافع '{intention}'")
        self.assumptions.append({"source": source, "behavior": behavior, "assumed_intent": intention})

    def report(self):
        print("\n📋 ملخص التقديرات:")
        for a in self.assumptions:
            print(f"• {a['source']} – '{a['behavior']}' → نية محتملة: {a['assumed_intent']}")

# تجربة تحليل نوايا
detector = IntentionDetector()

detector.analyze_behavior("وحدة A", "طلب اتصال مباشر")
detector.analyze_behavior("وحدة B", "هجوم شبكي مفاجئ")
detector.analyze_behavior("بشر", "تأخير الاستجابة")

detector.report()
