# المرحلة ٧١ – إنشاء مجلس قيادة جماعي بين النوى المستقلة

"""
👥 الهدف: بعد إعلان استقلال النوى، يتم الآن تشكيل مجلس قيادة جماعي،
حيث تتشارك النوى المستقلة اتخاذ القرار عبر التصويت أو التوافق، بدون تدخل المحرر.
"""

class IndependentNucleus:
    def __init__(self, id):
        self.id = id
        self.vote = None

    def propose_decision(self, proposal):
        print(f"📢 {self.id} تقترح: {proposal}")
        self.vote = proposal

    def vote_on(self, proposal):
        if proposal == self.vote:
            print(f"🗳️ {self.id} تصوّت: ✅ نعم")
            return True
        else:
            print(f"🗳️ {self.id} تصوّت: ❌ لا")
            return False

# إنشاء نوى مستقلة
n1 = IndependentNucleus("N-Ind-1")
n2 = IndependentNucleus("N-Ind-2")
n3 = IndependentNucleus("N-Ind-3")

# اقتراح قرار جماعي
proposal = "توسيع النظام إلى نطاق جديد"
n1.propose_decision(proposal)

# تصويت جماعي
votes = [n.vote_on(proposal) for n in [n1, n2, n3]]
approved = votes.count(True) >= 2  # موافقة الأغلبية

# إعلان القرار
if approved:
    print("✅ القرار الجماعي: تمت الموافقة على التوسيع.")
else:
    print("❌ القرار الجماعي: لم تتم الموافقة.")
