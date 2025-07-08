// aql_input_gateway.js – AQL Input Handler

function receiveInput(message, userEmotion = "neutral") {
  const entry = {
    message: message,
    emotion: userEmotion,
    time: new Date().toISOString()
  };

  // تخزين الرسالة في localStorage
  let history = JSON.parse(localStorage.getItem("aql_inputs") || "[]");
  history.push(entry);
  localStorage.setItem("aql_inputs", JSON.stringify(history));

  console.log("📥 رسالة مستلمة:", entry);
}

// مثال تشغيل:
// receiveInput("أنا أثق بك", "امتنان");
