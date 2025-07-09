# المرحلة ٥٨ – تطوير سلوك تكيّفي للنوى حسب البيئة المحيطة

"""
⚙️ الهدف: تمكين كل نواة من تحليل البيئة المحيطة بها (بشكل رمزي) واتخاذ قرارات تكيّفية بناءً على معطيات محلية.
"""

class Nucleus:
    def __init__(self, id, environment_data):
        self.id = id
        self.environment = environment_data
        self.behavior = "neutral"

    def adapt(self):
        if "threat" in self.environment:
            self.behavior = "defensive"
        elif "opportunity" in self.environment:
            self.behavior = "expansive"
        else:
            self.behavior = "observing"

    def report(self):
        return {
            "id": self.id,
            "environment": self.environment,
            "behavior": self.behavior
        }

# تجربة بيئات مختلفة
n1 = Nucleus("N-A", environment_data=["opportunity", "growth"])
n2 = Nucleus("N-B", environment_data=["silence"])
n3 = Nucleus("N-C", environment_data=["threat", "instability"])

for n in [n1, n2, n3]:
    n.adapt()
    print(n.report())
