
async function populate_radar() {
    const urlParams = new URLSearchParams(window.location.search)
    quadrants = [
            {name: urlParams.has('br') ? urlParams.get('br'):'?br'},
            {name: urlParams.has('bl') ? urlParams.get('bl'):'?bl'},
            {name: urlParams.has('tl') ? urlParams.get('tl'):"?tl"},
            {name: urlParams.has('tr') ? urlParams.get('tr'):"?tr"}
        ]
    db = await (await fetch('./deploy/db.json')).json()
    console.log(db)

    radar_visualization({
        svg_id: "radar",
        width: 1450,
        height: 1000,
        colors: {
            background: "#fff",
            grid: "#bbb",
            inactive: "#ddd"
        },
        title: "My Radar",
        quadrants: quadrants,
        rings: [
            {name: "INNER", color: "#93c47d"},
            {name: "SECOND", color: "#b7e1cd"},
            {name: "THIRD", color: "#fce8b2"},
            {name: "OUTER", color: "#f4c7c3"}
        ],
        print_layout: true,
        entries: db
    })
}