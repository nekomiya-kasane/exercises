// class AxesProp {
//     constructor(options) {
//         this.min = options ? (options.min ?? -10) : -10,
//             this.max = options.x ? (options.max ?? 10) : 10,
//             this.tick = options.x ? (options.tick ?? 1) : 1,
//             this.label = options.x ? (options.label ?? 5) : 5,
//             this.name = options.x ? (options.name ?? "x-axis") : "x-axis"
//     }
// }

// let index = 0

// class Plotter {
//     constructor(options) {
//         this.axes = options.axes ?? [true, true, true, true]
//         this.hue = options.hue ?? (() => {
//             color_pool = ["green", "red"]
//             return color_pool[floor(random() * color_pool.length)]
//         })
//         this.x = options.x ? AxesProp(options.x) : AxesProp()
//         this.y = options.y ? AxesProp(options.y) : AxesProp()
//         this.width = options.width ?? 500
//         this.height = options.height ?? 400

//         this.index = index
//         index += 1

//         this.data = []
//     }

//     adddata(data) {
//         this.data.push(data)
//         this.redraw_all()
//     }

//     update() {
//         for (let data of this.data) {
//             if (data.update) {
//                 data.update()
//             }
//         }
//         this.redraw_all()
//     }

//     redraw_all() {
//         ele = this.draw()
//         for (let e of document.getElementsByClassName("svg-plot-" + this.index)) {
//             e.removeChild(e.lastChild);
//             e.appendChild(ele);
//         }
//     }

//     draw() {
//         svg = document.createElement("svg");
//         svg.className = "svg-plot" + this.index

//         // draw frame
//         let hori_padding = 20
//         let vert_padding = 30

//         if (this.axes[0]) { // top
//             document.createElement("line")
//         }
//     }

//     create_line(position1, position2, options) {
//         line = document.createElement("line");
//         line.setAttribute("x1", position1[0]);
//         line.setAttribute("y1", position1[1]);
//         line.setAttribute("x2", position2[0]);
//         line.setAttribute("y2", position2[1]);
//         return line
//     }

//     create_polyline(points, id = "") {
//         poly = document.createElement("polyline");
//         pts = []
//         for (const pt of points) {
//             pts.push(pt.join())
//         }
//         poly.setAttribute("points", pts.join(' '))
//         if (id) {
//             poly.setAttribute("id", id)
//         }
//         return poly;
//     }

//     create_text(position, string, options) {
//         text = document.createElement("text")
//         text.setAttribute("x", position[0])
//         text.setAttribute("y", position[1])
        
//             text.setAttribute("id", id)
//         }
//         text.innerHTML = string
//         return text;
//     }
// }

//plotter = new Plotter()

const received_event = new Event("received")
const svgns = "http://www.w3.org/2000/svg";

dates = []
played = []
completed = []

total_days = 0

timer = null
received = false

days_diff = (date1, date2) => Math.round((date1 - date2) / (1000 * 60 * 60 * 24))

update_data = () => {
    const url = "https://cws.auckland.ac.nz/gas/api/GameLog";
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
            played.push(log.played)
            completed.push(log.completed)
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
}

window.onload = () => {
    update_data()
}

window.addEventListener("received", () => {
    div = document.getElementById("plot")
    div.style.transform = "scale(" + Math.min((window.innerWidth - 20) * 0.9 / 800, (window.innerHeight - 20) * 0.9 / 600) + ")";
    
    // info
    info = document.createElement("div")
    info.setAttribute("id", "info")
    info1 = document.createElement("span")
    info1.setAttribute("id", "info-played")
    info1.innerHTML = "<strong>Played:</strong> " + JSON.stringify(played) + "<br/>"
    info2 = document.createElement("span")
    info2.setAttribute("id", "info-completed")
    info2.innerHTML = "<strong>Completed:</strong> " + JSON.stringify(completed)
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
    plot.style.transform = "scale(" + window.innerWidth * 0.9 / 800 + ")";
}

// Plotter

Node.prototype.appendSVG = function(node_name, node_attr) {
    n = document.createElementNS(svgns, node_name);
    this.appendChild(n);
    if (typeof node_attr !== 'undefined') {
        for (key in node_attr) {
            n.setAttribute(key, node_attr[key]);
        }
    }
    return n;
}

Array.prototype.max = function() {
    return Math.max.apply(null, this);
};
  
Array.prototype.min = function() {
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

function create_polyline(points, options = undefined) {
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

xpos = (x) => { return String((10 + 8 * x / 10) * 8); }
ypos = (y) => { return String((90 - 8 * y / 10) * 6); }

function draw_axes(svg) {
    // axes
    let x_axis = create_line([xpos(0), ypos(0)],[xpos(100), ypos(0)], {
        "marker-end": 'url(#arrowhead)',
        class: "axes"
    })
    let y_axis = create_line([xpos(0), ypos(0)],[xpos(0), ypos(100)], {
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
    mi = Math.min(played.min(), completed.min())
    mx = Math.max(played.max(), completed.max())
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
    legend1 = create_text([xpos(90), ypos(105)], "played", {
        class: "played"
    })
    legend2 = create_text([xpos(90), ypos(100)], "completed", {
        class: "completed"
    })
    svg.appendChild(legend1);
    svg.appendChild(legend2);   

    return [mi, mx, pos]
}

function draw_data(svg, pos_fun) {
    points = []
    for (let i = 0; i < played.length; i ++) {
        pos = pos_fun(days_diff(dates[i], dates[0]), played[i])
        points.push([String(xpos(pos[0])), String(ypos(pos[1]))])
    }
    poly1 = create_polyline(points, {
        class: "played"
    })
    points = []
    for (let i = 0; i < completed.length; i ++) {
        pos = pos_fun(days_diff(dates[i], dates[0]), completed[i])
        points.push([String(xpos(pos[0])), String(ypos(pos[1]))])
    }
    poly2 = create_polyline(points, {
        class: "completed"
    })

    svg.appendChild(poly1)
    svg.appendChild(poly2)
}

function draw_logo(svg) {
    points = []
    for (let i = -1; i < 51; i ++) {
        points.push([
            String(xpos(10 * Math.cos(i / 50 * 3.14159 / 2))), 
            String(ypos(30 * Math.sin(i / 50 * 3.14159 / 2)))
        ])
    }
    points.push([
        String(xpos(0)), String(ypos(-0.6))
    ])
    prop = {style: 'stroke: black; stroke-width: 0.4rem; stroke-linecap: "round";fill: none;' }
    poly1 = create_polyline(points, prop)
    svg.appendChild(poly1)
    points = []
    for (let i = 56; i < 101; i ++) {
        points.push([
            String(xpos(10 * Math.cos(i / 50 * 3.14159 / 2))), 
            String(ypos(30 * Math.sin(i / 50 * 3.14159 / 2)))
        ])
    }
    points.push([String(xpos(-2)), String(ypos(0))])
    points.push([String(xpos(-2)), String(ypos(12))])
    points.push([String(xpos(-5)), String(ypos(12))])
    poly2 = create_polyline(points, prop)
    svg.appendChild(poly2)

    theta = Math.asin(12 / 30)
    line4 = create_line([xpos(0), ypos(12)],[
        xpos(10 * Math.cos(theta)), ypos(30 * Math.sin(theta))
    ], prop)
    svg.appendChild(line4)
}