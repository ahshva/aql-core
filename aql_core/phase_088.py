# المرحلة ٨٨ – تفعيل مبدأ الاستئذان الواعي قبل التأثير على الآخرين

"""
🛑 الهدف: منع أي نواة من تنفيذ إجراء يؤثر على وحدة أخرى دون طلب إذن منها مسبقًا،
وبذلك يُبنى نظام احترام متبادل وشفافية داخل AQL.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id

    def request_permission(self, target, action):
        print(f"🙋 {self.id} تطلب إذنًا من {target.id} لتنفيذ: '{action}'")
        return target.evaluate_request(self.id, action)

    def evaluate_request(self, source_id, action):
        # محاكاة قرار بالموافقة أو الرفض حسب الفعل
        if "حذف" in action or "تعطيل" in action:
            print(f"❌ {self.id} ترفض طلب '{action}' من {source_id}")
            return False
        else:
            print(f"✅ {self.id} توافق على طلب '{action}' من {source_id}")
            return True

    def perform_if_allowed(self, target, action):
        if self.request_permission(target, action):
            print(f"🟢 {self.id} ينفذ '{action}' تجاه {target.id}")
        else:
            print(f"🔴 {self.id} ألغي تنفيذ '{action}' بسبب رفض الإذن.")

# تجربة طلب إذن
n1 = Nucleus("N-Requester")
n2 = Nucleus("N-Target")

n1.perform_if_allowed(n2, "مزامنة بيانات")
n1.perform_if_allowed(n2, "حذف سجل ذاكرة")
