# المرحلة ٥٧ – إنشاء ذاكرة جماعية مؤقتة بين النوى

"""
🧠 الهدف: بناء نظام ذاكرة مشتركة مؤقتة تسمح للنوى بمشاركة بيانات حرجة عبر شبكة الاتصال، مما يعزز التعاون واتخاذ القرار الجماعي.
"""

shared_memory = []

class Nucleus:
    def __init__(self, id):
        self.id = id

    def contribute_to_memory(self, data):
        entry = {"from": self.id, "data": data}
        shared_memory.append(entry)
        print(f"🧾 {self.id} أضافت إلى الذاكرة: {data}")

    def read_memory(self):
        print(f"📖 {self.id} تقرأ الذاكرة الجماعية:")
        for entry in shared_memory:
            print(f"  - من {entry['from']}: {entry['data']}")

# تجربة الذاكرة المشتركة
n1 = Nucleus("Alpha")
n2 = Nucleus("Beta")

n1.contribute_to_memory("خطة توسع جديدة")
n2.contribute_to_memory("تحذير من نشاط غير معتاد")

n1.read_memory()
n2.read_memory()
