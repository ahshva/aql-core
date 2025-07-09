# المرحلة ٨٧ – إعلان النية بشكل واضح للآخرين

"""
📣 الهدف: تفعيل قدرة النواة على إعلان نيتها بشكل صريح ومفهوم للوحدات الأخرى قبل اتخاذ أي إجراء،
لتفادي التوترات وتحقيق تفاعل مبني على الوضوح والثقة.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.current_intention = None

    def set_intention(self, intention):
        self.current_intention = intention
        print(f"📣 {self.id} تعلن نيتها: '{intention}'")

    def execute_action(self, action):
        if not self.current_intention:
            print(f"⚠️ {self.id} تحذير: لم يتم إعلان نية قبل تنفيذ الفعل '{action}'")
        else:
            print(f"✅ {self.id} تنفذ '{action}' بنية: '{self.current_intention}'")
            self.current_intention = None  # تُمسح النية بعد التنفيذ

# تجربة إعلان نية وتنفيذ فعل
n = Nucleus("N-Intentional-1")

n.set_intention("بناء قناة تواصل جديدة")
n.execute_action("فتح اتصال مع وحدة خارجية")

n.execute_action("حذف وحدة قديمة")  # بدون نية معلنة
