# المرحلة ٦٩ – بناء نواة القرار الذاتي

"""
🧭 الهدف: إنشاء نوع خاص من النوى لديه قدرة على اتخاذ قرارات مستقلة بناءً على المدخلات، دون انتظار أوامر خارجية،
وهو ما يُعتبر أساس الذكاء الذاتي المستقل داخل نظام AQL.
"""

class DecisionNucleus:
    def __init__(self, id):
        self.id = id
        self.state = "idle"

    def evaluate_inputs(self, inputs):
        if "threat" in inputs:
            self.state = "defend"
        elif "opportunity" in inputs:
            self.state = "expand"
        elif "conflict" in inputs:
            self.state = "negotiate"
        else:
            self.state = "observe"

    def act(self):
        actions = {
            "defend": f"🛡️ {self.id} تُفعّل وضع الدفاع.",
            "expand": f"🚀 {self.id} تبدأ التوسع.",
            "negotiate": f"🤝 {self.id} تدخل في تفاوض.",
            "observe": f"👁️ {self.id} تراقب الوضع.",
            "idle": f"💤 {self.id} في وضع الخمول."
        }
        print(actions.get(self.state, "❓ حالة غير معروفة."))

# تجربة نواة قرار
dn = DecisionNucleus("N-Decision-Core")

# محاكاة حالات مختلفة
test_inputs = [
    ["silence"],
    ["opportunity", "growth"],
    ["conflict", "resistance"],
    ["threat"]
]

for inputs in test_inputs:
    print(f"\n📥 مدخلات: {inputs}")
    dn.evaluate_inputs(inputs)
    dn.act()
