// aql_clock.js – AQL Internal Time Tracker

(function(){
  const now = new Date();
  const systemTime = {
    timestamp: now.toISOString(),
    readable: now.toLocaleString(),
    milliseconds: now.getTime()
  };

  localStorage.setItem("aql_internal_clock", JSON.stringify(systemTime));
  console.log("⏱️ تم تسجيل توقيت الخلية:", systemTime);
})();
