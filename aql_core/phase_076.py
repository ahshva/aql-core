# المرحلة ٧٦ – بناء شبكة تعلّم تعاوني بين النوى

"""
🤝 الهدف: السماح للنوى بتبادل الدروس والخبرات المكتسبة فيما بينها من خلال شبكة تعليم داخلية،
مما يؤدي إلى تسريع تطور النظام بالكامل بشكل جماعي وليس فردي.
"""

class Nucleus:
    def __init__(self, id):
        self.id = id
        self.knowledge = []

    def learn(self, lesson):
        self.knowledge.append(lesson)
        print(f"📚 {self.id} تعلّمت: {lesson}")

    def share_knowledge(self, other):
        new_lessons = [k for k in self.knowledge if k not in other.knowledge]
        other.knowledge.extend(new_lessons)
        print(f"🔁 {self.id} شاركت معرفتها مع {other.id}: {new_lessons}")

    def report(self):
        return {
            "id": self.id,
            "knowledge": self.knowledge
        }

# تجربة تبادل التعلم
n1 = Nucleus("N-Learn-A")
n2 = Nucleus("N-Learn-B")

n1.learn("تجنب التكرار")
n1.learn("تعزيز التعاون")
n2.learn("تحليل التهديد")

# تبادل المعرفة
n1.share_knowledge(n2)
n2.share_knowledge(n1)

print(n1.report())
print(n2.report())
