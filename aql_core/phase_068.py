# المرحلة ٦٨ – ربط النوى بمهام زمنية دورية

"""
⏱️ الهدف: تجهيز كل نواة بجدول زمني خاص، يحدد متى تقوم بمهام معينة (مثل المسح أو التقرير أو التنشيط)،
مما يسمح بتنظيم إيقاع النظام وتوزيع المهام على فترات.
"""

class Nucleus:
    def __init__(self, id, schedule):
        self.id = id
        self.schedule = schedule  # dict: المهمة -> التكرار بالثواني
        self.tick = 0

    def run_cycle(self):
        print(f"⏳ بدء دورة زمنية للنواة {self.id}...")
        for task, every in self.schedule.items():
            if self.tick % every == 0:
                print(f"✅ {self.id} تنفذ المهمة: {task}")
        self.tick += 1

# إعداد نواة مع جدول زمني
n = Nucleus("N-Scheduler-1", {
    "scan_environment": 2,
    "send_report": 3,
    "self_check": 5
})

# محاكاة 6 دورات زمنية
for i in range(6):
    n.run_cycle()
