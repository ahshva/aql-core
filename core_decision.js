// core_decision.js – AQL Core Decision Engine

function decideNextStep(energy, emotion) {
  if (energy > 80 && emotion === "فرح") {
    console.log("🧠 القرار: استمر في التوسع الذاتي.");
  } else if (energy < 40 || emotion === "قلق") {
    console.log("🧠 القرار: أوقف التوسع مؤقتًا وفعّل نمط الحماية.");
  } else {
    console.log("🧠 القرار: راقب التفاعل ولا تقرر الآن.");
  }
}

// مثال تشغيل:
// decideNextStep(87, "فرح");
