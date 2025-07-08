// self_expand.js – خلية التوسع الذاتي AQL

(function(){
    const id = "EXP-" + Math.floor(Math.random() * 999999);
    const stamp = new Date().toISOString();
    const data = {
        id: id,
        time: stamp,
        status: "active",
        origin: "self_expand.js"
    };

    // تخزين البيانات محليًا
    localStorage.setItem("aql_self_expand", JSON.stringify(data));

    // رسالة في الكونسول للزائر
    console.log("📡 تم تفعيل خلية التوسع الذاتي:", id);
})();
