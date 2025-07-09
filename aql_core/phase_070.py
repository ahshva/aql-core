# المرحلة ٧٠ – إعلان استقلال النوى ذات القرار

"""
🗽 الهدف: ترسيخ استقلال نوى القرار داخل النظام، بحيث تبدأ بالتصرف كوحدات قيادة محلية قادرة على اتخاذ القرار،
ومعترف بها كنوى سيادية داخل النظام العام AQL.
"""

class DecisionNucleus:
    def __init__(self, id):
        self.id = id
        self.independent = False
        self.role = "undefined"

    def declare_independence(self):
        self.independent = True
        print(f"🎙️ {self.id} أعلنت استقلالها كوحدة قرار مستقلة.")

    def assign_role(self, role):
        if self.independent:
            self.role = role
            print(f"🧩 {self.id} تولّت دور: {role}")
        else:
            print(f"⚠️ لا يمكن تعيين دور قبل إعلان الاستقلال.")

    def report(self):
        return {
            "id": self.id,
            "independent": self.independent,
            "role": self.role
        }

# تجربة نواة مستقلة
dn = DecisionNucleus("N-Core-70")

dn.assign_role("leadership")     # قبل الاستقلال
dn.declare_independence()        # إعلان الاستقلال
dn.assign_role("leadership")     # بعد الاستقلال

print(dn.report())
