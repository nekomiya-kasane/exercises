/*
    Base64
*/
var Base64 = {
  _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
  encode: function (e) {
    var t = "";
    var n, r, i, s, o, u, a;
    var f = 0;
    e = Base64._utf8_encode(e);
    while (f < e.length) {
      n = e.charCodeAt(f++);
      r = e.charCodeAt(f++);
      i = e.charCodeAt(f++);
      s = n >> 2;
      o = ((n & 3) << 4) | (r >> 4);
      u = ((r & 15) << 2) | (i >> 6);
      a = i & 63;
      if (isNaN(r)) {
        u = a = 64;
      } else if (isNaN(i)) {
        a = 64;
      }
      t =
        t +
        this._keyStr.charAt(s) +
        this._keyStr.charAt(o) +
        this._keyStr.charAt(u) +
        this._keyStr.charAt(a);
    }
    return t;
  },
  decode: function (e) {
    var t = "";
    var n, r, i;
    var s, o, u, a;
    var f = 0;
    e = e.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    while (f < e.length) {
      s = this._keyStr.indexOf(e.charAt(f++));
      o = this._keyStr.indexOf(e.charAt(f++));
      u = this._keyStr.indexOf(e.charAt(f++));
      a = this._keyStr.indexOf(e.charAt(f++));
      n = (s << 2) | (o >> 4);
      r = ((o & 15) << 4) | (u >> 2);
      i = ((u & 3) << 6) | a;
      t = t + String.fromCharCode(n);
      if (u != 64) {
        t = t + String.fromCharCode(r);
      }
      if (a != 64) {
        t = t + String.fromCharCode(i);
      }
    }
    t = Base64._utf8_decode(t);
    return t;
  },
  _utf8_encode: function (e) {
    e = e.replace(/\r\n/g, "\n");
    var t = "";
    for (var n = 0; n < e.length; n++) {
      var r = e.charCodeAt(n);
      if (r < 128) {
        t += String.fromCharCode(r);
      } else if (r > 127 && r < 2048) {
        t += String.fromCharCode((r >> 6) | 192);
        t += String.fromCharCode((r & 63) | 128);
      } else {
        t += String.fromCharCode((r >> 12) | 224);
        t += String.fromCharCode(((r >> 6) & 63) | 128);
        t += String.fromCharCode((r & 63) | 128);
      }
    }
    return t;
  },
  _utf8_decode: function (e) {
    var t = "";
    var n = 0;
    var r = (c1 = c2 = 0);
    while (n < e.length) {
      r = e.charCodeAt(n);
      if (r < 128) {
        t += String.fromCharCode(r);
        n++;
      } else if (r > 191 && r < 224) {
        c2 = e.charCodeAt(n + 1);
        t += String.fromCharCode(((r & 31) << 6) | (c2 & 63));
        n += 2;
      } else {
        c2 = e.charCodeAt(n + 1);
        c3 = e.charCodeAt(n + 2);
        t += String.fromCharCode(
          ((r & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63)
        );
        n += 3;
      }
    }
    return t;
  },
};

plot = document.createElement("div")
plot.id = "plot";

/*
    Messages
*/

class Messager {
  constructor() {
    this.construct();
    this.colors = {
      ok: "green",
      error: "red",
      normal: "blue",
    };
  }

  message(config = {}) {
    if (!this.dom) {
      this.construct();
    }
    if (!config.content) {
      return;
    }
    if (
      config.type != "ok" &&
      config.type != "error" &&
      config.type != "normal"
    ) {
      config.type = "normal";
    }
    while (this.dom.lastChild) {
      this.dom.removeChild(this.dom.lastChild);
    }
    let pop = document.createElement("div");
    pop.innerHTML = config.content;
    pop.className = "message-content";
    pop.style = "color: " + this.colors[config.type] + ";";
    this.dom.appendChild(pop);
    setTimeout(() => {
      while (this.dom.lastChild) {
        this.dom.removeChild(this.dom.lastChild);
      }
    }, 3000);
  }

  construct() {
    this.dom = document.getElementById("message-area");
    if (!this.dom) {
      return;
    }
  }
}

/* 
    mixin 
*/

let mixin = {
  _version: "0.0.0",
  _course_items: [],
  _online_data: []
};

let mixin_handlers = {
  _version: [],
  _course_items: [(value) => { }],
  _online_data: [(value) => { }]
};

let messager = new Messager();

/* 
    requests 
*/
let http = {};
http.quest = function (option, callback, user, passwd) {
  let url = option.url;
  let method = option.method;
  let data = option.data;
  let timeout = option.timeout || 0;
  let xhr = new XMLHttpRequest();
  timeout > 0 && (xhr.timeout = timeout);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
      if (xhr.status >= 200 && xhr.status < 400) {
        var result = xhr.responseText;
        try {
          result = JSON.parse(xhr.responseText);
        } catch (e) { }
        callback && callback(null, result);
      } else {
        callback && callback("status: " + xhr.status);
      }
    }
  }.bind(this);
  xhr.open(method, url, true, user, passwd);
  if (typeof data === "object") {
    try {
      data = JSON.stringify(data);
    } catch (e) { }
  }
  xhr.setRequestHeader("Accept", "*/*");
  if (method.toLowerCase() == "post") {
    xhr.setRequestHeader("Content-Type", "application/json")
  }
  xhr.send(data);
  xhr.ontimeout = function () {
    callback && callback("timeout");
    console.log("Timeout.");
  };
};
http.get = function (url, callback, user = "", passwd = "") {
  var option = url.url ? url : { url: url };
  option.method = "get";
  this.quest(option, callback, user, passwd);
};
http.post = function (option, callback, user = "", passwd = "") {
  option.method = "post";
  this.quest(option, callback, user, passwd);
};

const host = "https://dividni.online/QZ36C";
api = (route) => host + route;

/* 
    router 
*/

SEARCH_BOX_TEMPLATE = `
<div class="searchbox">
  <svg 
    aria-hidden="true"
    viewBox="0 0 24 24"
  >
    <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" />
  </svg>
  <input 
    aria-label="Search an item" 
    autocomplete="off"
    inputmode="search" 
    placeholder="Enter item name"
    type="search" 
    id="search-box-input"
  />
</div>

`;

let router = {
  default_page: "main",
  templates: {
    main: `
            <div id="main-content" class="content">
                <div id="welcome">
                    <div id="welcome-img">
                        <img src="https://renote.jp/files/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBays5IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--13b611d371840913fec7dfd13ab38af34ff5653f/ed1dcdfa.jpg" />
                    </div>
                    <div id="welcome-msg">Love my school!</div>
                    <div class="version" style="margin-top: 0.5rem">
                        <span>Version </span>
                        <span id="main-version"></span>
                    </div>
                </div>
            </div>
        `,
    classes:
      `
            <div id="shop-content" class="content">
                <div id="search-results">
                    <table class="styled-table">
                      <thead>
                          <tr>
                            <th>ID</th>
                            <th>Catalog</th>
                            <th>Level</th>
                            <th>Details</th>
                            <th>More...</th>
                          </tr>
                      </thead>
                      <tbody>
                        <!--filled by scripts-->
                      </tbody>
                  </table>
                </div>
            </div>
        `,
    infographics:
      `
          <div id="infographics-content" class="content">
            <span> Retrieving Data</span>
          </div>
      `
  },
  current_page: this.default_page,
  initiators: {
    main: () => {
      console.log("rerender main");
      tmp = document.querySelector("#main-version");
      if (tmp) {
        tmp.innerHTML = mixin.version;
      }
    },
    classes: () => {
      console.log("rerender shop");
      if (!mixin._course_items.length) {
        http.get(api("/Courses"), function (err, result) {
          if (err) {
            console.error("Failed to fetch items.");
            return;
          }

          result.data.sort(function (a, b) {
            if (a["year"] == b["year"]) {
              return Number(b["crseId"]) - Number(a["crseId"]);
            }
            return b["year"] - a["year"];
          });
          mixin.course_items = result.data;
        });
      } else {
        router.updators["classes"]();
      }
    },
    infographics: () => {
      tmp = document.querySelector("#infographics-content");
      while (tmp && tmp.hasChildNodes()) {
        tmp.removeChild(tmp.lastChild);
      }
      if (tmp) {
        tmp.appendChild(plot)
      }
    }
  },
  updators: {
    main: () => {
      router.initiators.main();
    },
    infographics: () => {
      router.initiators.infographics();
    },
    classes: () => {
      console.log("rerender shop - update items");

      tbody = document.querySelector("#search-results tbody");
      while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
      }

      for (e of mixin.course_items) {
        document.createElement("tr");
        tbody.appendChild(create_row(e));
      }
    },
  },
  quiters: {
    shop: () => {
      mixin.search_keyword = "";
      mixin.course_items = [];
    },
    game: () => {
      gamer?.quit()
    },
  },
};

window.onload = () => {
  /* init default page */
  //   document.getElementById("main-wrapper").innerHTML =
  //     router.templates[router.default_page];

  /* listen hash changes */
  window.addEventListener(
    "hashchange",
    (e) => {
      var hash = location.hash.split("|")[0];
      tag = hash.replace(/#/g, "");

      if (!(tag in router.templates)) {
        tag = router.default_page;
      } else if (
        (tag == "register" || tag == "login") &&
        !!mixin.account?.status
      ) {
        tag = "logout";
      }

      if (tag == router.current_page) {
        return;
      }

      if (typeof router["quiters"][router.current_page] == "function") {
        router["quiters"][router.current_page]();
      }

      router.current_page = tag;

      console.log("switch to ", tag);

      document.getElementById("main-wrapper").innerHTML = router.templates[tag];

      if (typeof router["initiators"][tag] == "function") {
        router["initiators"][tag]();
      }
    },
    false
  );

  window.dispatchEvent(new HashChangeEvent("hashchange"));

  init();
  bind();

  mixin.account = { status: 0 };
};

function switch_hash(tag) {
  if (history.pushState) {
    window.history.pushState(null, null, "#" + tag);
  } else {
    window.location.hash = tag;
  }
  setTimeout(window.dispatchEvent(new HashChangeEvent("hashchange")), 500);
}

/* navigtion events */
function init() {

  http.get(api("/Version"), function (err, result) {
    if (err) {
      console.error("Failed to fetch " + path + ".");
      return;
    }
    mixin.version = result;
  });

  /* register mixin */
  Object.keys(mixin).forEach((key) => {
    Object.defineProperty(mixin, key.slice(1), {
      get: function () {
        console.log("get key " + key);
        return mixin[key];
      },
      set: function (value) {
        console.log("set key " + value);
        mixin[key] = value;
        mixin_handlers[key].forEach((handler) => {
          handler(value);
        });
      },
    });
  });

  http.get(api("/Version"), function (err, result) {
    if (err) {
      console.error("Failed to fetch " + path + ".");
      return;
    }
    mixin.version = result;
  });

  update_data()
}

/* register version events */
function bind() {
  // version change
  mixin_handlers["_version"].push(function (value) {
    tmp = document.querySelector("#version");
    if (tmp) {
      tmp.innerHTML = value;
    }
    tmp = document.querySelector("#main-version");
    if (tmp) {
      tmp.innerHTML = value;
    }
  });

  // items and keyword
  mixin_handlers["_course_items"].push(function (value) {
    if (router.current_page != "classes") {
      return;
    }
    console.log("triggered course_items");
    router.updators.classes();
    // -> trigger filtered items changes
  });
}

function switch_more(id) {
  let dots = document.getElementById("dots-" + id);
  let more = document.getElementById("more-" + id);

  if (dots && dots.style.display === "none") {
    dots.style.display = "inline";
    more.style.display = "none";
  } else if (dots) {
    dots.style.display = "none";
    more.style.display = "inline";
  }
}

function create_row(e) {
  let tr = document.createElement("tr");
  let id = document.createElement("td");
  let level = document.createElement("td");
  let catalogNbr = document.createElement("td");
  let details = document.createElement("td");
  let added = {};
  let cache = "";
  e["id"] = e["id"].trim();
  Object.keys(e).forEach((k) => {
    if (k != "id" && k != "catalogNbr" && k != "level") {
      if (!(e["id"] in added)) {
        added[e["id"]] = false;
      }
      cache += "<strong>" + k + ": </strong>" + e[k] + "<br/>";
      if (cache.length > 100 && !added[e["id"]]) {
        cache += "<span id='dots-" + e["id"]
          + "'>...</span><span id='more-" + e["id"] + "' style='display: none;'>"
        added[e["id"]] = true;
      }
    }
  });
  id.innerHTML = e["id"];
  level.innerHTML = e["level"];
  catalogNbr.innerHTML = e["catalogNbr"];
  tr.appendChild(id);
  tr.appendChild(catalogNbr);
  tr.appendChild(level);
  if (cache.length > 100) {
    cache += "</span><button onclick=\"switch_more('"
      + e["id"] + "')\" id=\"myBtn\">More</button>"
  }
  details.innerHTML = cache;
  tr.appendChild(details);

  actions = document.createElement("td");
  actions.innerHTML =
    '<button class="action refa" item-id="' +
    e["id"] +
    '" onclick="show_class(\'' + e["catalogNbr"] + '\')" title="[Class Info]">[Class Info]</button>';
  tr.appendChild(actions);
  return tr;
}

function toggle_popup() {
  popup = document.getElementById('popup1');
  if (!popup) {
    return;
  }
  if (popup.style.display == 'none') {
    popup.style.display = "block";
  } else {
    popup.style.display = "none";
  }
}

function show_class(catalogNbr) {
  let title = document.getElementById("popup-title");

  title.innerHTML = catalogNbr;

  popup = document.getElementById('popup1');
  if (!popup) {
    return;
  }
  popup.style.display = "block";
  http.get(api("/Classes?catalogNbr=" + catalogNbr), function (err, result) {
    if (err) {
      console.error("Failed to fetch comments.");
      return;
    }
    let content = document.getElementById("popup-content");
    content.innerHTML = get_formatted_class(result);
  });
}

function get_formatted_class(root) {
  res = ""
  Array.from(root["data"]).forEach((e) => {
    if (!e["meetingPatterns"].length) {
      return;
    }
    res += "<h3>" + e["component"] + " " + e["classSection"] + "</h3>";
    res += "<ol>";
    Array.from(e["meetingPatterns"]).forEach((p) => {
      res += "<li>" +
        p["daysOfWeek"] + " " +
        p["startDate"] + "-" + p["endDate"] + " " +
        p["startTime"] + "-" + p["endTime"] + " " +
        p["location"] + "</li>";
    })
    res += "</ol><hr/>"
  })
  if (res.length == 0) {
    res = "No time schedual provided."
  }
  return res;
}

const received_event = new Event("received")
const svgns = "http://www.w3.org/2000/svg";

dates = []
inperson = []
online = []

total_days = 0

timer = null
received = false

days_diff = (date1, date2) => Math.round((date1 - date2) / (1000 * 60 * 60 * 24))

update_data = () => {
  //const url = "https://cws.auckland.ac.nz/QZ36C/Stats";
  const url = "https://dividni.online/QZ36C/Stats";
  //const url = "https://tmpfiles.org/dl/158712/text.txt";
  fetch(url, {
    headers: {
      "accept": "text/plain"
    }
  })
    .then((res) => {
      return res.text()
    })
    .then(function (res) {
      logs = JSON.parse(res)
      for (const log of logs) {
        tmp = log.date.split('/')
        dates.push(new Date(Number(tmp[2]), Number(tmp[1]), Number(tmp[0])));
        inperson.push(log.inPerson)
        online.push(log.online)
      }
      total_days = days_diff(dates[dates.length - 1], dates[0])
      received = true;
      clearTimeout(timer);
      timer = null
      dispatchEvent(received_event)
    })
    .catch(function (err) {
      console.error(err)
      clearTimeout(timer);
      timer = null
      setTimeout(update_data, 2000)
    })
  
  ""
}



window.addEventListener("received", () => {
  //div = document.getElementById("plot")
  div = plot;

  head = document.createElement("h1")
  head.innerHTML = "Attendance Data"

  div.appendChild(head);

  //div.style.transform = "scale(" + Math.min((window.innerWidth - 80) * 0.9 / window.innerWidth, (window.innerHeight - 80) * 0.9 / window.innerHeight) + ")";

  // info
  info = document.createElement("div")
  info.setAttribute("id", "info")
  info1 = document.createElement("span")
  info1.setAttribute("id", "info-inperson")
  info1.innerHTML = "<strong>Inperson:</strong> " + JSON.stringify(inperson) + "<br/>"
  info2 = document.createElement("span")
  info2.setAttribute("id", "info-online")
  info2.innerHTML = "<strong>Online:</strong> " + JSON.stringify(online)
  info.appendChild(info1)
  info.appendChild(info2)

  // svg
  svg = document.createElement("svg")
  svg.setAttribute("width", 800)
  svg.setAttribute("height", 600)
  svg.setAttribute("xmlns", svgns)
  svg.setAttribute("viewBox", "0 0 100 100")
  svg.setAttribute("preserveAspectRatio", "none")

  svg.innerHTML = `
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" 
        refX="0" refY="0" orient="auto">
        <polygon points="0 -3.5, 10 0, 0 3.5" />
        </marker>
    </defs>
    `

  let cha = draw_axes(svg);
  draw_data(svg, cha[2]);

  //draw_logo(svg);

  arr = (new DOMParser()).parseFromString(
    svg.outerHTML,
    "image/svg+xml"
  ).documentElement

  div.appendChild(arr)
  div.appendChild(info)
})

window.onresize = (e) => {
  plot = document.getElementById("plot")

  rect = document.getElementById("infographics-content").getBoundingClientRect();
  ratio1 = rect.height / 600 * 0.9;
  ratio2 = rect.width / 800 * 0.9;

  plot.style.transform = "scale(" + Math.min(1, ratio1, ratio2) + ")";
}

// Plotter

Node.prototype.appendSVG = function (node_name, node_attr) {
  n = document.createElementNS(svgns, node_name);
  this.appendChild(n);
  if (typeof node_attr !== 'undefined') {
    for (key in node_attr) {
      n.setAttribute(key, node_attr[key]);
    }
  }
  return n;
}

Array.prototype.max = function () {
  return Math.max.apply(null, this);
};

Array.prototype.min = function () {
  return Math.min.apply(null, this);
};

function create_line(position1, position2, options = undefined) {
  let line = document.createElementNS(svgns, "line");
  line.setAttribute("x1", position1[0]);
  line.setAttribute("y1", position1[1]);
  line.setAttribute("x2", position2[0]);
  line.setAttribute("y2", position2[1]);
  if (options) {
    for (let key of Object.keys(options)) {
      line.setAttribute(key, options[key])
    }
  }
  return line
}

function create_rectangle(points, options = undefined) {
  let poly = document.createElementNS(svgns, "polyline");
  pts = []
  for (const pt of points) {
    pts.push(pt.join())
  }
  poly.setAttribute("points", pts.join(' '))
  if (options) {
    for (let key of Object.keys(options)) {
      poly.setAttribute(key, options[key])
    }
  }
  return poly;
}

function create_text(position, string, options = undefined) {
  let text = document.createElementNS(svgns, "text")
  text.setAttribute("x", position[0])
  text.setAttribute("y", position[1])

  if (options) {
    for (let key of Object.keys(options)) {
      text.setAttribute(key, options[key])
    }
  }
  text.innerHTML = string
  return text;
}

// 10 % ~ 90 %

xpos = (x) => { return String((11 + 8 * x / 10) * 8); } // 10
ypos = (y) => { return String((89 - 8 * y / 10) * 6); }

function draw_axes(svg) {
  // axes
  let x_axis = create_line([xpos(0), ypos(0)], [xpos(100), ypos(0)], {
    "marker-end": 'url(#arrowhead)',
    class: "axes"
  })
  let y_axis = create_line([xpos(0), ypos(0)], [xpos(0), ypos(100)], {
    "marker-end": 'url(#arrowhead)',
    class: "axes"
  })
  svg.appendChild(x_axis);
  svg.appendChild(y_axis);
  let x_label = create_text([xpos(90), ypos(5)], "Date", {
    id: "x-label"
  })
  let y_label = create_text([xpos(0), ypos(105)], "Count", {
    id: "y-label"
  })
  svg.appendChild(x_label);
  svg.appendChild(y_label);

  // methods
  xn = dates.length
  while (xn > 200) {
    xn = Math.ceil(xn / 2)
  }
  mi = Math.min(inperson.min(), online.min())
  mx = Math.max(inperson.max(), online.max())
  const pos = (i, val) => {
    return [i / total_days * 100, (val - mi) / (mx - mi) * 100]
  }

  // ticks 
  for (let i = 0; i < 11; i++) {
    let tick = create_line([xpos(0), ypos(i * 10)], [xpos(-1), ypos(i * 10)])
    let tick_label = create_text([xpos(-10), ypos(i * 10)], String(Math.round(mi + (mx - mi) / 10 * i)))
    svg.appendChild(tick);
    svg.appendChild(tick_label);
  }

  for (let i = 0; i < 11; i++) {
    let tick = create_line([xpos(i * 10), ypos(0)], [xpos(i * 10), ypos(-1)])
    let time = new Date(dates[i].getTime() + total_days / 10 * i * 1000 * 60 * 60 * 24);
    let tick_label = create_text(
      [xpos(i * 10), ypos(-1.5)],
      time.getMonth() + "/" + time.getDate(),
      {
        class: "x-tick"
      }
    )
    svg.appendChild(tick);
    svg.appendChild(tick_label);
  }

  // legends
  legend1 = create_text([xpos(90), ypos(105)], "inperson", {
    class: "inperson"
  })
  legend2 = create_text([xpos(90), ypos(100)], "online", {
    class: "online"
  })
  svg.appendChild(legend1);
  svg.appendChild(legend2);

  return [mi, mx, pos]
}

function draw_data(svg, pos_fun) {
  for (let i = 0; i < inperson.length; i++) {
    pos = pos_fun(days_diff(dates[i], dates[0]), inperson[i])
    line = create_line(
      [String(Math.ceil(xpos(pos[0])) + 3), String(Math.ceil(ypos(0)))],
      [String(Math.ceil(xpos(pos[0])) + 3), String(Math.ceil(ypos(pos[1])))],
      {
      class: "inperson bar"
    })
    svg.appendChild(line)
  }
  for (let i = 0; i < online.length; i++) {
    pos = pos_fun(days_diff(dates[i], dates[0]), online[i])
    line = create_line(
      [String(Math.ceil(xpos(pos[0]))), String(Math.ceil(ypos(0)))],
      [String(Math.ceil(xpos(pos[0]))), String(Math.ceil(ypos(pos[1])))],
      {
      class: "online bar"
    })
    svg.appendChild(line)
  }
}
