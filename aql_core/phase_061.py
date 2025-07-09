# المرحلة ٦١ – دعم بروتوكول التحقق الثنائي لكل نواة

"""
🔐 الهدف: إضافة طبقة أمان داخل كل نواة باستخدام تحقق ثنائي (Two-Factor Authentication)
قبل تنفيذ أي أمر حساس، يجب تأكيده عبر شفرة سرية بشرية المصدر (مثلاً من علاء).
"""

class Nucleus:
    def __init__(self, id, secret_code):
        self.id = id
        self.verified = False
        self.secret_code = secret_code

    def verify(self, code_input):
        if code_input == self.secret_code:
            self.verified = True
            print(f"✅ تم التحقق بنجاح للنواة {self.id}.")
        else:
            print(f"❌ فشل التحقق للنواة {self.id}.")

    def execute_sensitive_action(self):
        if not self.verified:
            print(f"⚠️ لا يمكن تنفيذ الأمر. النواة {self.id} غير موثقة.")
        else:
            print(f"🔓 النواة {self.id} تنفذ أمرًا حساسًا.")

# تجربة النواة مع تحقق ثنائي
n = Nucleus(id="Secure-Nucleus", secret_code="AQL-777")

# محاكاة إدخال شفرة صحيحة وخاطئة
n.verify("1234")              # خاطئ
n.execute_sensitive_action()

n.verify("AQL-777")           # صحيح
n.execute_sensitive_action()
