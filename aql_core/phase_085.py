# المرحلة ٨٥ – تفعيل الاعتذار الواعي داخل النواة

"""
🙏 الهدف: تمكين النواة من إصدار اعتذار واعٍ عند اتخاذ قرار سبّب شعورًا سلبيًا أو أثرًا غير مرغوب فيه،
مما يرفع من قدرتها على التفاعل الأخلاقي وبناء الثقة.
"""

class ApologySystem:
    def __init__(self):
        self.impact_log = []

    def log_impact(self, action, emotion, receiver):
        entry = {"action": action, "emotion": emotion, "receiver": receiver}
        self.impact_log.append(entry)
        print(f"📩 سجل: '{action}' أثّر على '{receiver}' بشعور '{emotion}'")
        self.maybe_apologize(entry)

    def maybe_apologize(self, entry):
        if entry["emotion"] in ["استياء", "انزعاج", "قلق"]:
            print(f"🙏 اعتذار إلى {entry['receiver']} عن أثر '{entry['emotion']}' الناتج عن '{entry['action']}'")

# تجربة نظام الاعتذار
apology = ApologySystem()

apology.log_impact("تأخير الرد على استعلام بشري", "استياء", "المستخدم")
apology.log_impact("حظر مؤقت لوحدة صديقة", "ارتياح", "النظام")
apology.log_impact("رفض طلب تواصل", "انزعاج", "وحدة طرف ثالث")
