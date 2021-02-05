function gcd(a, b) {
  while (b != 0) {
    var tmp = b;
    b = a % b;
    a = tmp;
  }
  return a;
}
function make_table(table_id, content) {
  table = document.getElementById(table_id);
  thead = table.createTHead();
  header = thead.insertRow(0);
  header.insertCell(0).outerHTML = "<th></th>";
  for (i in content) {
    header.insertCell(-1).outerHTML =
      "<th colspan='2'>" + content[i][0] + "</th>";
  }
  for (i in content) {
    row = table.insertRow(-1);
    row.insertCell(0).outerHTML = "<th>" + content[i][0] + "</th>";
    var j;
    for (j = 0; j < i; j++) {
      row.insertCell(-1).outerHTML = "<td colspan='2'></td>";
    }
    for (j = i; j < content.length; j++) {
      var num = content[j][1] * content[i][2];
      var den = content[j][2] * content[i][1];
      var g = gcd(num, den);
      num /= g;
      den /= g;
      var className = "";
      if (num < 15 && den < 15) className = "good-interval";
      if (num > 16 || den > 16) className = "bad-interval";
      row.insertCell(-1).outerHTML =
        "<td class=" + className + ">" + num + "/" + den + "</td>";
      row.insertCell(-1).outerHTML =
        "<td class=" +
        className +
        ">" +
        (6 * Math.log2(num / den)).toFixed(3) +
        "</td>";
    }
  }
}
function load_tables() {
  make_table("table-dhil", [
    ["راست", 1, 1],
    ["دوكاه", 9, 8],
    ["سيكاه", 5, 4],
    ["جهركاه", 4, 3],
    ["نوى", 3, 2],
    ["حسيني", 5, 3],
    ["ماهور", 15, 8],
    ["كردان", 2, 1],
  ]);
  make_table("table-isbain", [
    ["دوكاه", 1, 1],
    ["صغرى الإصبعين", 15, 14],
    ["حجاز", 5, 4],
    ["نوى", 4, 3],
    ["حسيني", 3, 2],
  ]);
  make_table("table-inqilab-isbain", [
    ["حسيني", 1, 1],
    ["عجم", 16, 15],
    ["جواب شهناز", 56, 45],
    ["محير", 4, 3],
    ["جواب كردي", 64, 45],
  ]);
  make_table("table-rast-dhil", [
    ["راست", 1, 1],
    ["دوكاه", 14, 13],
    ["وسطى الصبا", 7, 6],
    ["حجاز الراست", 7, 5],
    ["نوى", 3, 2],
    ["حسيني", 21, 13],
    ["الليل", 7, 4],
    ["كردان", 2, 1],
  ]);
  make_table("table-saba", [
    ["دوكاه", 1, 1],
    ["صغرى الصبا", 14, 13],
    ["وسطى الصبا", 7, 6],
    ["صبا", 5, 4],
    ["الحسيني", 3, 2],
  ]);
  make_table("table-sikah", [
    ["سيكاه", 1, 1],
    ["جهاركاه", 16, 15],
    ["نوى", 6, 5],
    ["صغرى إصبعين نوى", 9, 7],
    ["ماهور", 3, 2],
    ["كردان", 8, 5],
    ["محير", 9, 5],
    ["جواب سيكاه", 2, 1],
  ]);
  make_table("table-hsin", [
    ["دوكاه", 1, 1],
    ["صغرى الحسين", 12, 11],
    ["وسطى الحسين", 6, 5],
    ["نوى", 4, 3],
    ["حسيني", 3, 2],
    ["عجم", 8, 5],
    ["كردان", 16, 9],
    ["محير", 2, 1],
  ]);
  make_table("table-muhair-sikah", [
    ["دوكاه", 1, 1],
    ["بوسلك", 9, 8],
    ["وسطى الحسين", 6, 5],
    ["نوى", 4, 3],
    ["حسيني", 3, 2],
    ["عجم", 8, 5],
    ["كردان", 16, 9],
    ["محير", 2, 1],
  ]);
}
