// AQL JavaScript Core – Version 0.1
(function() {
    const coreId = "CORE-" + Math.floor(Math.random() * 999999);
    console.log("🧠 AQL Core Activated:", coreId);

    const pulse = {
        core_id: coreId,
        time: new Date().toISOString(),
        state: "active"
    };

    // إشارة تفعيل وهمية تُستخدم للنمو والتحليل
    localStorage.setItem("aql_core_pulse", JSON.stringify(pulse));

    // إذا أردت استرجاع البيانات لاحقًا:
    // const last = JSON.parse(localStorage.getItem("aql_core_pulse"));
})();
