# المرحلة ٧٢ – إدارة الموارد الذكية بين النوى المستقلة

"""
⚡ الهدف: السماح للنظام بتوزيع الموارد (مثل الطاقة، المعالجة، الذاكرة) بين النوى المستقلة،
بناءً على احتياجات كل نواة ووظيفتها الحالية، بدون تدخل خارجي.
"""

class Nucleus:
    def __init__(self, id, need_level):
        self.id = id
        self.need_level = need_level
        self.allocated = 0

    def request_resources(self, total_pool):
        ratio = self.need_level / total_pool["total_need"]
        self.allocated = round(total_pool["available_energy"] * ratio, 2)
        print(f"⚙️ {self.id} تم تخصيص {self.allocated} وحدة طاقة.")

    def report(self):
        return {
            "id": self.id,
            "need_level": self.need_level,
            "allocated_energy": self.allocated
        }

# إنشاء النوى وتحديد الاحتياج
n1 = Nucleus("N-Energy-1", 5)
n2 = Nucleus("N-Energy-2", 3)
n3 = Nucleus("N-Energy-3", 2)

# إجمالي الموارد والطاقة المتاحة
resource_pool = {
    "available_energy": 100,
    "total_need": n1.need_level + n2.need_level + n3.need_level
}

# تخصيص الموارد تلقائيًا
for n in [n1, n2, n3]:
    n.request_resources(resource_pool)
    print(n.report())
