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
  _shop_items: [],
  _filtered_items: [],
  _account: {
    status: 0,
  },
  _search_keyword: "",
};

let mixin_handlers = {
  _version: [],
  _shop_items: [(value) => {}],
  _filtered_items: [(value) => {}],
  _account: [],
  _search_keyword: [],
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
        } catch (e) {}
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
    } catch (e) {}
  }
  xhr.setRequestHeader("Accept", "*/*");
  // if (url.search(/8080/i)) {
  //   // for my proxy
  //   xhr.setRequestHeader("x-request-url", url.slice(url.search(/8080/i) + 5));
  // }
  if (mixin._account.status || (user && passwd)) {
    auth =
      user && passwd
        ? user + ":" + passwd
        : mixin.account.username + ":" + mixin.account.password;
    auth = "Basic " + Base64.encode(auth);
    xhr.setRequestHeader("Authorization", auth);
  }
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

const host = "http://localhost:5000/api";
api = (route) => host + route;

/* 
    router 
*/

USER_NAME_TEMPLATE = `
  <div class="form-group input-group">
      <span class="input-group-icon">
          <svg class="icon-ui" x="0px" y="0px" viewBox="0 0 24 24">
              <path class="fill" d="M15.71,12.71a6,6,0,1,0-7.42,0,10,10,0,0,0-6.22,8.18,1,1,0,0,0,2,.22,8,8,0,0,1,15.9,0,1,1,0,0,0,1,.89h.11a1,1,0,0,0,.88-1.1A10,10,0,0,0,15.71,12.71ZM12,12a4,4,0,1,1,4-4A4,4,0,0,1,12,12Z"/>
          </svg>
      </span>
      <input name="username" type="text" class="form-control" placeholder="User Name" value="" required="required" autofocus="" autocomplete="username">
  </div>
`;
EMAIL_TEMPLATE = `
  <div class="form-group input-group">
    <span class="input-group-icon">
        <svg class="icon-ui" x="0px" y="0px" viewBox="0 0 24 24">
            <path class="stroke" d="M2,4h20v16H2V4z"></path>
            <path class="stroke" d="M2,8l10,5l10-5"></path>
        </svg>
    </span>
    <input name="email" type="text" class="form-control" placeholder="Email Address" value="" required="required" autofocus="" autocomplete="email">
  </div>
`;
PASSWD_TEMPLATE = `
  <div class="form-group input-group">
      <span class="input-group-icon">
          <svg class="icon-ui" x="0px" y="0px" viewBox="0 0 24 24">
              <path class="fill" d="M19,8V7c0-3.9-3.1-7-7-7S5,3.1,5,7v1h2V7c0-2.8,2.2-5,5-5s5,2.2,5,5v1H19"></path>
              <path class="stroke" d="M3,9h18v14H3V9z"></path>
              <circle class="fill" cx="8" cy="16" r="1"></circle>
              <circle class="fill" cx="12" cy="16" r="1"></circle>
              <circle class="fill" cx="16" cy="16" r="1"></circle>
          </svg>
      </span>
      <input name="password" class="form-control" type="password" placeholder="Password" required="required" autocomplete="current-password">
  </div>
`;
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
    shop:
      `
            <div id="shop-content" class="content">
            ` +
      SEARCH_BOX_TEMPLATE +
      `
                <div id="search-results">
                    <table class="styled-table">
                      <thead>
                          <tr>
                          <th>Photo</th>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Price</th>
                            <th>Actions</th>
                          </tr>
                      </thead>
                      <tbody>
                        <!--filled by scripts-->
                      </tbody>
                  </table>
                </div>
            </div>
        `,
    guestbook:
      `
          <div id="guestbook-content" class="content">
            <div id="comments">
              <!--<iframe src="` +
      api("/Comments") +
      `" id="embeded-comments">
              </iframe>-->
            </div>
            <div id="new-comment">
              <form>
                <div>
                  <input name="name" type="text" placeholder="Your name" value="" required="required" autofocus="">
                  <textarea name="comment" id="new-comment-area" rows="4" placeholder="New comment here" value=""></textarea>
                <div>
                <div>
                  <button onclick="submit_comment(this.form); return false;">Submit</button>
                </div>
              </form>
            </div>
          </div>
      `,
    game: `
            <div id="game-content" class="content">
                <!--<canvas id="gamepad"></canvas>-->
                <div id="gamepad"></div>
                <div id="gametools">
                  <button id="start-game" onclick="gamer.pair(); return false;">Start</button>
                  <button id="end-game" onclick="gamer.quit(); return false;">Quit</button>
                </div>
            </div>
        `,
    register:
      `<div id="register-content" class="content">
          <form class="regform">` +
      USER_NAME_TEMPLATE +
      EMAIL_TEMPLATE +
      PASSWD_TEMPLATE +
      `<div class="rail">
                  <div class="rail-content">
                  </div>
                  <div class="rail-toolbar">
                      <a href="#login" class="refa">I already have an account, Log in</a>
                  </div>
              </div>
              <div class="form-action">
                <div>
                    <button onclick="register_submit(this.form); return false;">Register</button>
                </div>
              </div>
          </form>
        </div>`,
    login:
      `
        <div id="login-content" class="content">
            <form class="regform">` +
      USER_NAME_TEMPLATE +
      PASSWD_TEMPLATE +
      `<div class="rail">
                    <div class="rail-content">
                    </div>
                    <div class="rail-toolbar">
                        <a href="#register" class="refa">Don't have accounts? Rigister</a>
                    </div>
                </div>
                <div class="form-action">
                  <div>
                      <button onclick="login_submit(this.form); return false;">Log in</button>
                  </div>
                </div>
            </form>
        </div>
    `,
    logout: `
        <div id="logout-content" class="content">
            Logout
        </div>
    `,
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
    shop: () => {
      console.log("rerender shop");
      if (!mixin._shop_items.length) {
        http.get(api("/AllItems"), function (err, result) {
          if (err) {
            console.error("Failed to fetch items.");
            mixin.search_keyword = "";
            return;
          }
          // for (let i = 0; i < result.length; i++) {
          //   http.get(api("/ItemPhoto/" + result[i].id), function (err, re) {
          //     if (err) {
          //       console.error("Failed to fetch item photo of " + result[i].id);
          //       return;
          //     }
          //     result[i].photo = new Image(re);
          //   })
          // }
          mixin.shop_items = result;
        });
      }
      input = document.querySelector("#search-box-input");
      input.addEventListener("keydown", (e) => {
        if (e.keyCode == 13) {
          console.log("query input");
          http.get(api("/Items/" + input.value), function (err, result) {
            if (err) {
              console.error("Failed to fetch item " + input.value + ".");
              return;
            }
            // for (let i = 0; i < result.length; i++) {
            //   http.get(api("/ItemPhoto/" + result[i].id), function (err, re) {
            //     if (err) {
            //       console.error("Failed to fetch item photo of " + result[i].id);
            //       return;
            //     }
            //     result[i].photo = re;
            //   })
            // }
            mixin.search_keyword = input.value;
            mixin.filtered_items = result;
          });
        }
        return;
      });
    },
    logout: () => {
      mixin.account = {
        status: 0,
      };

      setTimeout(() => {
        switch_hash("home");
      }, 1000);
    },
    guestbook: () => {
      http.get(api("/Comments"), function (err, result) {
        if (err) {
          console.error("Failed to fetch comments.");
          return;
        }
        //console.log(result)
        cmts = document.getElementById("comments");
        while (cmts.hasChildNodes()) {
          cmts.removeChild(cmts.lastChild);
        }
        comments = document.createElement("div");
        comments.id = "comments-content";
        comments.innerHTML = result;
        cmts.appendChild(comments);

        //document.getElementById('embeded-comments').innerHTML = result
      });
    },
    game: () => {
      if (!mixin || !mixin?.account?.status) {
        messager.message({
          type: "error",
          content: "Please login first.",
        });
        switch_hash("login");
      }
      setup_gamepad();
    },
  },
  updators: {
    main: () => {
      router.initiators.main();
    },
    guestbook: () => {
      router.initiators.guestbook();
    },
    shop: () => {
      console.log("rerender shop - update items");

      tbody = document.querySelector("#search-results tbody");
      while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
      }

      (mixin.search_keyword == ""
        ? mixin.shop_items
        : mixin.filtered_items
      ).forEach((e) => {
        document.createElement("tr");
        tbody.appendChild(create_row(e));
      });
    },
  },
  quiters: {
    shop: () => {
      mixin.search_keyword = "";
      mixin.shop_items = [];
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

function updateDOM(selector, path) {
  http.get(api(path), function (err, result) {
    if (err) {
      console.error("Failed to fetch " + path + ".");
      return;
    }
    document.querySelector(selector).innerHTML = result;
  });
}

/* navigtion events */
function init() {
  /* get logo */
  updateDOM("#logo a", "/Logo");

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

  // account change
  mixin_handlers["_account"].push(function (value) {
    if (!value.status) {
      console.log("triggered logout");
      document.getElementById("account").innerHTML = `
            <a href="#register" class="refa">Register</a>
            <a href="#login" class="refa">Login</a>
          `;
      return;
    }
    console.log("triggered login");
    user = "<span>User: " + mixin.account.username + "</span>";
    document.getElementById("account").innerHTML =
      user +
      `
      <a href="#logout" class="refa">Logout</a>
    `;
  });

  // items and keyword
  mixin_handlers["_shop_items"].push(function (value) {
    if (router.current_page != "shop") {
      return;
    }
    console.log("triggered shop_items");
    mixin.filtered_items = filter_shop_items(value, mixin.search_keyword);
    // -> trigger filtered items changes
  });
  mixin_handlers["_filtered_items"].push(function (value) {
    if (router.current_page != "shop") {
      return;
    }
    console.log("triggered filtered_items");
    router.updators["shop"]();
  });
  mixin_handlers["_search_keyword"].push(function (value) {
    console.log("triggered _search_keyword1");
    if (router.current_page != "shop") {
      return;
    }
    console.log("triggered _search_keyword");
    if (value == "") {
      return;
    }
    http.get(api("/Items/" + encodeURI(value)), function (err, result) {
      if (err) {
        console.error("Failed to fetch " + "/Items/" + encodeURI(value) + ".");
        return;
      }
      mixin.filtered_items = result;
    });
  });
}

function filter_shop_items(arr, keyword) {
  if (keyword == "") {
    return arr;
  }
  return arr.filter((item) => item.name.search(keyword) >= 0);
}

function create_row(e) {
  let tr = document.createElement("tr");
  let td = document.createElement("td");
  let img = document.createElement("img");
  img.src = api("/ItemPhoto/" + e.id);
  img.className = "item-photo";
  tr.appendChild(img);
  Object.keys(e).forEach((k) => {
    td = document.createElement("td");
    td.innerHTML = e[k];
    tr.appendChild(td);
  });
  actions = document.createElement("td");
  actions.innerHTML =
    '<a href="javascript:;" class="action refa" item-id="' +
    e["id"] +
    '" onclick="buy_item(this)">[Buy]</a>';
  tr.appendChild(actions);
  return tr;
}

function buy_item(e) {
  if (!mixin.account.status) {
    // not logged in
    messager.message({
      type: "error",
      content: "Please login first.",
    });
    switch_hash("login");
    return;
  }
  console.log("To buy " + e.getAttribute("item-id"));
  id = e.getAttribute("item-id");
  http.get(
    api("/PurchaseItem/" + encodeURI(id)),
    function (err, result) {
      if (err) {
        console.error(
          "Failed to fetch " + "/PurchaseItem/" + encodeURI(id) + "\n" + err
        );
        return;
      }
      messager.message({
        type: "ok",
        content: "succeed to buy " + id + result,
      });
      e.innerText = "[Bought]";
    },
    mixin.account.username,
    mixin.account.password
  );
}

// form actions
function login_submit(form) {
  if (!form.username.value || !form.password.value) {
    messager.message({
      type: "error",
      content: "Form incomplete",
    });
    return;
  }

  // fetch(api("/VersionA"), {
  //   headers: {
  //     authorization: Base64.encode(form.username.value + ":" + form.password.value),
  //   },
  // }).then((response) => {
  //   if (response.ok) {
  //     console.log(response.text());
  //   } else {
  //     throw new Error(
  //       "Something went wrong with your username and password combination"
  //     );
  //   }
  // });

  http.get(
    api("/VersionA"),
    (err, res) => {
      if (err) {
        console.error("Failed to login");
        return;
      }
      mixin.account = {
        status: 1,
        username: form.username.value,
        password: form.password.value,
      };
      messager.message({
        type: "ok",
        content: "username and password provided.",
      });
      switch_hash("home");
    },
    form.username.value,
    form.password.value
  );
}

function register_submit(form) {
  if (!form.username.value || !form.password.value || !form.email.value) {
    messager.message({
      type: "error",
      content: "Form incomplete",
    });
    return;
  }
  // http.post(
  //   {
  //     method: "POST",
  //     data: {
  //       username: form.username.value,
  //       password: form.password.value,
  //       address: form.email.value,
  //     },
  //     url: api("/Register"),
  //   },
  //   (err, result) => {
  //     if (err) {
  //       console.error("Failed to register");
  //       return false;
  //     }
  //     temp = mixin.account;
  //     temp.status = 1;
  //     temp.username = result.username;
  //     temp.password = result.password;
  //     mixin.account = temp;
  //     console.log("asdf to register");
  //     messager.message({
  //       type: "ok",
  //       content: "Succeeded to register and login",
  //     });
  //   },
  //   mixin.account.username,
  //   mixin.account.password
  // );
  data = JSON.stringify({
    username: form.username.value,
    password: form.password.value,
    address: form.email.value,
  });

  fetch(api("/Register"), {
    method: "POST",
    headers: {
      Accept: "text/plain",
      "Content-Type": "application/json",
    },
    body: data,
  })
    .then((res) => res.text())
    .then((res) => {
      if (res == "Username not available") {
        messager.message({
          type: "error",
          content: "Username already registered",
        });
        return false;
      }
      temp = mixin.account;
      temp.status = 1;
      temp.username = data.username;
      temp.password = data.password;
      mixin.account = temp;
      console.log("asdf to register");
      messager.message({
        type: "ok",
        content: "Succeeded to register and login",
      });
      switch_hash("home");
    });
  return false;
}

function submit_comment(form) {
  console.log("submit comment");
  http.post(
    {
      method: "POST",
      data: {
        comment: form.comment.value,
        name: form.name.value,
      },
      url: api("/Comment"),
    },
    (err, result) => {
      if (err) {
        console.error("Failed to submit comment");
        return;
      }
      messager.message({
        type: "ok",
        content: "Succeeded to comment",
      });
      router.updators.guestbook();
    },
    mixin.account.username,
    mixin.account.password
  );
  return false;
}

/*
    Canvas
*/

const init_board = [
  ["Rb", "Nb", "Bb", "Qb", "Kb", "Bb", "Nb", "Rb"],
  ["Pb", "Pb", "Pb", "Pb", "Pb", "Pb", "Pb", "Pb"],
  ["", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "", "", ""],
  ["Pw", "Pw", "Pw", "Pw", "Pw", "Pw", "Pw", "Pw"],
  ["Rw", "Nw", "Bw", "Qw", "Kw", "Bw", "Nw", "Rw"],
];

class Gamer {
  constructor(ele) {
    this.element = ele;
    this.current = undefined;
    this.white_turn = true;
    this.board = [...init_board];
    this.pairinfo = undefined;
    this.myturn = undefined;
    this.turn_count = 0;
  }

  valid_move(tname, sname, it, jt, is, js) {
    if (!this.myturn) {
      messager.message({
        type: "normal",
        content: "waiting for their move...",
      });
      return false; // wait for move
    }
    if (tname != "" && tname[1] == sname[1]) {
      // cannot eat itself
      return false;
    }
    if (
      (this.white_turn && sname[1] != "w") ||
      (!this.white_turn && sname[1] != "b")
    ) {
      return false;
    }
    switch (sname[0]) {
      case "K": {
        if (Math.max(Math.abs(it - is), Math.abs(jt - js)) > 1) {
          return false;
        }
        break;
      }
      case "Q": {
        if (it != is && jt != js && Math.abs(it - is) != Math.abs(jt - js)) {
          return false;
        }
        if (it == is) {
          for (j = Math.min(jt, js) + 1; j < Math.max(jt, js); j++) {
            if (this.board[j][it] != "") {
              return false;
            }
          }
        } else if (jt == js) {
          for (i = Math.min(it, is) + 1; i < Math.max(it, is); i++) {
            if (this.board[jt][i] != "") {
              return false;
            }
          }
        } else {
          let ic = it - is < 0 ? -1 : 1;
          let jc = jt - js < 0 ? -1 : 1;
          let i = is + ic;
          let j = js + jc;
          while (i != is && i != it) {
            if (this.board[j][i] != "") {
              return false;
            }
            i += ic;
            j += jc;
          }
        }
        return true;
      }
      case "R": {
        if (it != is && jt != js) {
          return false;
        }
        return true;
      }
      case "B": {
        let ic = it - is < 0 ? -1 : 1;
        let jc = jt - js < 0 ? -1 : 1;
        let i = is + ic;
        let j = js + jc;
        while (i != is && i != it) {
          if (this.board[j][i] != "") {
            return false;
          }
          i += ic;
          j += jc;
        }
        return true;
      }
      case "N": {
        let dx = Math.abs(is - it);
        let dy = Math.abs(js - jt);
        if ((dx != 1 || dy != 2) && (dx != 2 || dy != 1)) {
          return false;
        }
        return true;
      }
      case "P": {
        let mae = sname[1] == "w" ? -1 : 1;
        if (mae > 0 && js == 1 && jt > js && jt - js < 3) {
          return true;
        }
        if (mae < 0 && js == 6 && js > jt && js - jt < 3) {
          return true;
        }
        if (tname != "" && jt - js == mae && Math.abs(is - it) == 1) {
          return true;
        }
        if (mae != jt - js || it != is) {
          return false;
        }
        return true;
      }
      default: {
        return false;
      }
    }
  }

  pick(e) {
    this.current = e.srcElement;
  }

  dragover(e) {
    e.preventDefault();
  }

  wait_their_move() {
    let timer = null;
    if (!this.pairinfo || !this.pairinfo.gameId) {
      return
    }
    http.get(
      api("/TheirMove" + "?gameId=" + this.pairinfo.gameId),
      (err, res) => {
        if (err) {
          console.error("Failed to get move.");
          btn.removeAttribute("disabled");
          btn.innerText = "start";
          return;
        }
        if (!this.process_their_move(res)) {
          if (timer) {
            clearTimeout(timer)
            timer = null
          }
          timer = setTimeout(() => {
            console.log("ask", res);
            this.wait_their_move();
          }, 1000);
        } else {
          console.log("ac their move", res);
          clearTimeout(timer);
          timer = null
          return
        }
      }
    );
  }

  drop(e) {
    let tar = e.srcElement.tagName == "IMG" ? e.srcElement : undefined;
    let tar_cell =
      e.srcElement.tagName == "IMG" ? e.srcElement.parentNode : e.srcElement;

    let src = this.current;
    let src_cell = src.parentNode;

    let it = Number(tar_cell.getAttribute("coord-x"));
    let jt = Number(tar_cell.getAttribute("coord-y"));
    let is = Number(src_cell.getAttribute("coord-x"));
    let js = Number(src_cell.getAttribute("coord-y"));

    let btn = document.getElementById("start-game");

    if (
      !this.valid_move(
        tar ? tar.getAttribute("chess") : "",
        src.getAttribute("chess"),
        it,
        jt,
        is,
        js
      )
    ) {
      return;
    }
    console.log("move on " + this.pairinfo.gameId)
    if (!this.pairinfo || !this.pairinfo.gameId) {
      return
    }
    http.post(
      {
        method: "POST",
        data: {
          "gameId": this.pairinfo.gameId,
          "move": JSON.stringify([this.turn_count + 1, it, jt, is, js])
        },
        url: api("/MyMove"),
      },
      (err, res) => {
        if (err || res != "move registered") {
          console.error("Failed to post move error: " + res + ".");
          btn.removeAttribute("disabled");
          btn.innerText = "start";
          return;
        }
        if (tar_cell.lastChild) {
          tar_cell.removeChild(tar_cell.lastChild);
        }
        tar_cell.appendChild(src);
        this.board[jt][it] = src.getAttribute("chess");
        this.board[js][is] = "";
        if (src_cell.lastChild) {
          src_cell.removeChild(src_cell.lastChild);
        }

        this.myturn = false;
        this.turn_count += 1;

        if (tar?.getAttribute("chess")[0] == "K") {
          messager.message({
            type: "ok",
            content: "You won",
          });
          this.quit();
        }

        this.wait_their_move();
      }
    );
  }

  pair() {
    let btn = document.getElementById("start-game");
    btn.innerText = "Pairing";
    btn.setAttribute("disabled", "1");
    let timer = null;

    http.get(
      api("/PairMe"),
      (err, res) => {
        if (err) {
          console.error("Failed to pair.");
          btn.removeAttribute("disabled");
          btn.innerText = "start";
          return;
        }
        this.pairinfo = res;
        if (res.state != "progress") {
          if (timer) {
            clearTimeout(timer)
            timer = null
          }
          timer = setTimeout(() => {
            console.log("ask", res);
            this.pair();
          }, 1000);
        } else {
          console.log("paired", res);
          document.getElementById("start-game").innerText = "Paired";
          clearTimeout(timer);
          timer = null
          this.myturn =
            (this.pairinfo.player1 == mixin.account.username &&
              !this.white_turn) ||
            (this.pairinfo.player2 == mixin.account.username &&
              this.white_turn);
          this.turn_count = 0;
          if (!this.myturn) {
            this.white_turn = false
            this.wait_their_move();
          }
        }
      },
      mixin.account.username,
      mixin.account.password
    );
  }

  quit() {
    let btne = document.getElementById("quit-game");
    let btns = document.getElementById("start-game");
    console.log("quitting ", this.pairinfo)
    if (!this.pairinfo || !this.pairinfo.gameId) {
      return
    }
    http.get(api("/QuitGame" + "?gameId=" + this.pairinfo.gameId), (err, res) => {
      if (err) {
        console.error("Failed to quit.");
        if (res[0] == "n") {
          this.reset();
        }
        return;
      }
      this.pairinfo = undefined;
      console.log(res);
      btns.innerText = "Pair Me";
      btns.removeAttribute("disabled");

      this.reset();
    },
    mixin.account.username,
    mixin.account.password);
  }

  process_their_move(json) {
    if (json[0] != this.turn_count + 1) {
      return false;
    }
    this.turn_count += 1;
    console.log("process their_move " + json);

    let cells = document.getElementsByClassName('cell')
    let it = json[1]
    let jt = json[2]
    let is = json[3]
    let js = json[4]
    let st_cell = cells[js * 8 + is]
    let ed_cell = cells[jt * 8 + it]
    let img = st_cell.lastChild
    st_cell.removeChild(st_cell.lastChild)
    if (ed_cell.lastChild) {
      ed_cell.removeChild(ed_cell.lastChild)
    }
    ed_cell.appendChild(img)

    this.myturn = true;
    if (tar?.getAttribute("chess")[0] == "K") {
      messager.message({
        type: "ok",
        content: "You lost",
      });
      this.quit();
    }
    return true
  }

  reset() {
    this.current = undefined;
    this.white_turn = true;
    this.board = [...init_board];
    this.pairinfo = undefined;
    this.myturn = undefined;
    this.turn_count = 0;

    setup_gamepad()
  }
}

let gamer;

function setup_gamepad() {
  if (gamer) {
    delete gamer;
  }
  gamer = new Gamer();

  let pad = document.getElementById("gamepad");
  if (!pad) {
    return;
  }
  while (pad.lastChild) {
    pad.removeChild(pad.lastChild)
  }
  const type = [
    "Rb",
    "Nb",
    "Bb",
    "Qb",
    "Kb",
    "Bb",
    "Nb",
    "Rb",
    "Pb",
    "Pb",
    "Pb",
    "Pb",
    "Pb",
    "Pb",
    "Pb",
    "Pb",
    "Pw",
    "Pw",
    "Pw",
    "Pw",
    "Pw",
    "Pw",
    "Pw",
    "Pw",
    "Rw",
    "Nw",
    "Bw",
    "Qw",
    "Kw",
    "Bw",
    "Nw",
    "Rw",
  ];
  addr = (e) => "https://cws.auckland.ac.nz/gas/images/" + e + ".svg";
  for (i = 0; i < 8; i++) {
    row = document.createElement("div");
    row.className = "row";
    row.setAttribute("row", i);
    for (j = 0; j < 8; j++) {
      col = document.createElement("div");
      col.className = "cell";
      col.setAttribute("coord-x", j);
      col.setAttribute("coord-y", i);
      namae = gamer.board[i][j];
      if (namae != "") {
        icon = document.createElement("img");
        icon.src = addr(namae);
        icon.setAttribute("draggable", true);
        icon.setAttribute("ondragstart", "gamer?.pick(event)");
        icon.setAttribute("chess", namae);
        icon.setAttribute("chess-type", namae[0]);
        icon.setAttribute("chess-sec", namae[1]);
        col.appendChild(icon);
      }
      col.setAttribute("ondragover", "gamer?.dragover(event)");
      col.setAttribute("ondrop", "gamer?.drop(event)");
      row.appendChild(col);
    }
    pad.appendChild(row);
  }

  // const dpr = window.devicePixelRatio || 1;
  // canvas.height = canvas.width
  // canvas.width *= dpr * 4
  // canvas.height *= dpr * 4
  // let ctx = canvas.getContext("2d")
  // ctx.drawImage(board_img, 0, 0, canvas.width, canvas.height)
  //draw_chess(board, canvas)
}
