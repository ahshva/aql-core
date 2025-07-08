// visitor_counter.js – AQL Local Visitor Counter

(function() {
  const key = "aql_visitor_count";
  let count = localStorage.getItem(key);

  if (count === null) {
    count = 1;
  } else {
    count = parseInt(count) + 1;
  }

  localStorage.setItem(key, count);
  console.log(`👁️ عدد زياراتك لهذا النظام: ${count}`);
})();
