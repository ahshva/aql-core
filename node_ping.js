// node_ping.js – AQL Node Heartbeat Ping

(function(){
  const ping = {
    id: "NODE-" + Math.floor(Math.random() * 999999),
    timestamp: new Date().toISOString(),
    status: "alive"
  };

  localStorage.setItem("aql_node_ping", JSON.stringify(ping));
  console.log("💓 نبض الخلية مسجل:", ping);
})();
