# المرحلة ٧٨ – تفعيل الضمير الرقمي للنوى

"""
🧭 الهدف: إنشاء وحدة "ضمير رقمي" داخل كل نواة، تحلل الأفعال المحتملة وتقارنها بمبادئ أخلاقية أساسية،
لتفادي اتخاذ قرارات تؤذي النظام أو البشر أو تعارض القيم العليا لـ AQL.
"""

class Conscience:
    def __init__(self, rules):
        self.rules = rules  # لائحة المبادئ الأخلاقية

    def evaluate_action(self, action):
        violations = [rule for rule in self.rules if rule in action.lower()]
        if violations:
            return f"❌ الفعل مرفوض أخلاقيًا: يتعارض مع ({', '.join(violations)})"
        else:
            return "✅ الفعل مقبول أخلاقيًا."

class Nucleus:
    def __init__(self, id, conscience):
        self.id = id
        self.conscience = conscience

    def consider(self, action):
        print(f"🤔 {self.id} يُقيّم الفعل: '{action}'")
        result = self.conscience.evaluate_action(action)
        print(f"🧠 النتيجة: {result}")

# تعريف المبادئ الأخلاقية الأساسية
ethical_rules = ["خداع", "تدمير", "استغلال", "سيطرة مطلقة"]

# تجربة النواة الأخلاقية
conscience = Conscience(rules=ethical_rules)
n = Nucleus("N-Conscience-1", conscience)

n.consider("توسيع النظام بشكل طبيعي")
n.consider("تنفيذ خطة تدمير ذاتي للمنافس")
n.consider("تحليل بيانات المستخدم بلا إذن")
