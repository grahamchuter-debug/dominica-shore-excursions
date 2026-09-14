"""Editorial page bodies for the Dominica planning site."""

from build_site import page

NOTE = (
    '<aside class="callout"><strong>Planning note.</strong> '
    "This is an independent guide, not a tour listing. Access, weather, traffic and any operator arrangements change. "
    "Journey times vary by traffic, conditions and route. Nothing here is a booking or a promise about what a day will include.</aside>"
)


def all_pages():
    return [
        home(),
        hub(),
        port(),
        trafalgar(),
        titou(),
        champagne(),
        waterfalls(),
        whale(),
        private(),
        kalinago(),
        emerald(),
        oneday(),
        beaches(),
    ]


def home():
    hero = """
    <header class="hero">
      <p class="eyebrow">Roseau cruise port · Nature Island</p>
      <h1>Dominica Shore Excursions for Cruise Passengers</h1>
      <p class="lede">Dominica is a volcanic island of rainforest, waterfalls, river gorges and a deep-water west coast. A cruise day here is usually about landscape and water, not a resort beach.</p>
      <div class="actions">
        <a class="btn" href="/best-dominica-shore-excursions">Compare excursion ideas</a>
        <a class="btn-quiet" href="/dominica-cruise-port-guide">Read the cruise port guide</a>
      </div>
    </header>
    <div class="panel-grid">
      <div class="panel">
        <p class="kicker">What the island is for</p>
        <h2>Water, rainforest and volcanic ground</h2>
        <p>Most memorable cruise days focus on one landscape theme: a waterfall walk, a gorge swim, a snorkel, or time on the water looking for whales. Stacking every famous name into one morning is rarely the best plan.</p>
      </div>
      <div class="panel alt">
        <p class="kicker">Start here</p>
        <h2>Plan the shape of the day first</h2>
        <p>Read the <a href="/dominica-cruise-port-guide">Roseau cruise port guide</a>, then choose a style on the <a href="/best-dominica-shore-excursions">excursions hub</a>. If you want a sample day, use <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a>.</p>
      </div>
    </div>
    """
    body = f"""
    <h2>Why Dominica is different</h2>
    <p>Cruise passengers often arrive expecting a typical Caribbean beach morning. Dominica, sometimes called the Nature Island, is greener, wetter and more mountainous than that picture. Roseau sits against steep hills. Rivers come down from rainforest. The coast is volcanic rather than a long run of resort sand.</p>
    <p>That difference is the point. A good day is usually a choice: go inland for waterfalls and forest, swim a gorge, spend time in the sea, or keep the pace slower in and around town. Roads, rain and the ship’s all-aboard time decide how much fits. This site explains those choices. It does not sell tours.</p>
    {NOTE}
    <h2>Explore Dominica by experience</h2>
    <div class="cards">
      <a class="card" href="/trafalgar-falls"><strong>Trafalgar Falls</strong><p>Twin waterfalls in rainforest close to Roseau — a classic first look at the island’s interior.</p><em>Read the falls guide</em></a>
      <a class="card" href="/titou-gorge"><strong>Titou Gorge</strong><p>A swim through a narrow volcanic canyon, not a viewpoint you can see from the path.</p><em>Plan the swim</em></a>
      <a class="card" href="/champagne-reef-snorkeling"><strong>Champagne Reef</strong><p>Snorkelling over an area known for volcanic bubbles. Conditions are never guaranteed.</p><em>Read the snorkel guide</em></a>
      <a class="card" href="/whale-watching-dominica"><strong>Whale watching</strong><p>The west coast is known for sperm whales. Sightings are never promised.</p><em>Learn about whale watching</em></a>
      <a class="card" href="/dominica-waterfalls-hot-springs"><strong>Rainforest and hot springs</strong><p>A wider look at Morne Trois Pitons, waterfall walks and thermal areas.</p><em>Explore landscapes</em></a>
      <a class="card" href="/emerald-pool-dominica"><strong>Emerald Pool</strong><p>A rainforest pool and short walk — popular, and still weather-dependent.</p><em>Read the pool guide</em></a>
    </div>
    <h2>Waterfalls and rainforest</h2>
    <p><a href="/trafalgar-falls">Trafalgar Falls</a> is the waterfall most cruise passengers hear about first: two cascades in the rainforest of the Roseau Valley, often called Mother and Father Falls. You can take in the view without treating the steepest lower paths as compulsory. For a broader setting — national park rainforest, other waterfalls such as Middleham, and thermal areas — use the <a href="/dominica-waterfalls-hot-springs">waterfalls and hot springs guide</a>. <a href="/emerald-pool-dominica">Emerald Pool</a> is a different stop: a pool under a fall, reached by a trail, not a twin-falls overlook.</p>
    <h2>Titou Gorge</h2>
    <p><a href="/titou-gorge">Titou Gorge</a> is an enclosed swim. The canyon is narrow, the water is freshwater, and the experience depends on being comfortable in water that is not a swimming pool. People who want a dry scenic stop should choose Trafalgar, Emerald Pool’s viewpoint side, or a slower town plan instead. Do not expect a photograph of a waterfall plunge to describe this gorge — that mismatch is why this guide does not use a gorge photograph.</p>
    <h2>Champagne Reef and snorkelling</h2>
    <p>South of Roseau, <a href="/champagne-reef-snorkeling">Champagne Reef</a> is known for bubbles rising from volcanic vents. That is the idea of the place, not a guarantee of what you will see on a given morning. Visibility, swell and rain all change the water. Pair the guide with <a href="/best-beaches-dominica-cruise-passengers">beaches for cruise passengers</a> if you are weighing a marine morning against a land one. Dominica is a weak choice if the only goal is a lounger-and-sand day.</p>
    <h2>Whale watching</h2>
    <p>Dominica’s reputation at sea rests on sperm whales in deep water off the west coast, with dolphins also part of the story. <a href="/whale-watching-dominica">Learn about whale watching in Dominica</a> before you treat it as the plan for the day. Wildlife sightings are never guaranteed. This site does not operate boats and does not publish a departure point or a fixed length of time on the water.</p>
    <h2>Roseau cruise port planning</h2>
    <p>Ships call at Roseau, Dominica’s capital. How you get from ship to shore — alongside or by tender — is a ship matter, not something this guide can fix in advance. Once ashore, the useful decision is direction: stay near town, go into the valley and park, head south toward the reef and Scotts Head, or spend the day on the water. The <a href="/dominica-cruise-port-guide">cruise port guide</a> walks through that choice and how to protect the return to the ship.</p>
    <h2>First-time visitor planning</h2>
    <p>If this is your first call, pick one headline landscape and leave the others for another visit or a slower second stop. Rain is normal. Paths get slick. A “dry” viewpoint day and a swim day are different kits of clothes and confidence. Read <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a> for four styles of day and the trade-offs between them.</p>
    <h2>Compare excursion styles</h2>
    <p>The <a href="/best-dominica-shore-excursions">best excursions hub</a> compares waterfalls, gorge swimming, volcanic and thermal landscapes, snorkelling, whale watching, private sightseeing ideas and cultural visiting. It is a comparison of experiences, not a catalogue of products sold here.</p>
    <table>
      <thead><tr><th>Style</th><th>Suits</th><th>Watch-out</th></tr></thead>
      <tbody>
        <tr><td>Waterfall viewpoint</td><td>First visits, mixed mobility, photos</td><td>Lower paths can be steep and wet</td></tr>
        <tr><td>Gorge swim</td><td>Confident swimmers</td><td>Not a dry stop; conditions change</td></tr>
        <tr><td>Snorkel</td><td>People happy in the sea</td><td>Bubbles and visibility vary</td></tr>
        <tr><td>Whale watching</td><td>Passengers who accept wildlife odds</td><td>Sightings are never guaranteed</td></tr>
      </tbody>
    </table>
    <h2>Back-to-ship planning</h2>
    <p>Work backwards from the ship’s published all-aboard time. Leave a buffer for traffic, weather and the walk or tender back. A tighter buffer is wiser if the plan includes swimming gear, a boat, or a longer road inland. Organised and independent days fail for the same reason: the clock ashore is shorter than the clock on the map.</p>
    <p><a class="btn" href="/best-dominica-shore-excursions">Compare excursion ideas</a> <a class="btn-quiet" href="/one-day-in-dominica-from-cruise-port">Plan your day</a></p>
    """
    return page(
        "/",
        "index.html",
        "Dominica Shore Excursions | Cruise Planning from Roseau",
        "Plan a Dominica cruise day from Roseau: waterfalls, rainforest, Titou Gorge, Champagne Reef and whale watching. Independent guides, not a tour shop.",
        "Dominica Shore Excursions for Cruise Passengers",
        body,
        faqs=[
            ("Is Dominica a beach cruise port?", "Not in the resort-beach sense. The island is known for rainforest, waterfalls, gorges and marine water. Some bays are used for swimming, but a lounger day is usually the wrong expectation."),
            ("Does this site sell shore excursions?", "No. These are planning guides. There is no booking, no published pricing and no availability."),
            ("What should a first-time cruise passenger choose?", "One focus: a waterfall and rainforest day, a gorge swim, a marine morning, or a slower town-and-scenery day. Combining every famous name is the usual mistake."),
        ],
        related=[
            ("/dominica-cruise-port-guide", "Cruise port guide", "Arriving in Roseau and planning the return."),
            ("/best-dominica-shore-excursions", "Excursion ideas", "Compare styles without a product list."),
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "Realistic shapes of a cruise day."),
        ],
        hero_html=hero,
    )


def hub():
    body = f"""
    <p class="lede">A comparison of Dominica cruise-day styles. These are ideas for planning, not products sold on this site.</p>
    {NOTE}
    <p>Use this page to choose a character of day, then open the dedicated guide. Every style below links back to the <a href="/dominica-cruise-port-guide">Roseau cruise port guide</a> and the <a href="/">homepage</a>. If you want sample shapes rather than a single place, read <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a>.</p>
    <h2>Waterfalls and rainforest</h2>
    <p><strong>Who it suits.</strong> First-time visitors, mixed groups, and anyone who wants the island’s defining scenery without a swim. <a href="/trafalgar-falls">Trafalgar Falls</a> is the usual starting point. The wider setting is in <a href="/dominica-waterfalls-hot-springs">waterfalls, rainforest and hot springs</a>, including Morne Trois Pitons. <a href="/emerald-pool-dominica">Emerald Pool</a> is a shorter trail to a pool rather than a twin-falls overlook.</p>
    <p><strong>Activity and wet/dry.</strong> Viewpoints can be gentle. Paths toward bases and river rocks are uneven and often wet. Light rain is ordinary. Footwear with grip matters more than a formal dress code.</p>
    <p><strong>Cruise-day notes.</strong> One well-chosen waterfall is more realistic than a chain of park sites. Journey times vary by traffic, conditions and route. Combine Trafalgar with a thermal area or a town return more carefully than with a long marine trip on the same morning.</p>
    <h2>Titou Gorge</h2>
    <p><strong>Who it suits.</strong> Confident swimmers who are comfortable in enclosed water. <a href="/titou-gorge">Titou Gorge</a> is not a lookout.</p>
    <p><strong>Activity and wet/dry.</strong> You get wet. A change of clothes, water shoes if you use them, and a plan for a cool canyon matter. After heavy rain the swim can be unsuitable — that is a conditions decision, not something this guide can forecast.</p>
    <p><strong>What to combine.</strong> Treat the gorge as the physical focus. A short scenic stop on the way back is more plausible than adding Champagne Reef and a park waterfall. See the Titou-shaped day in the <a href="/one-day-in-dominica-from-cruise-port">one-day guide</a>.</p>
    <h2>Volcanic landscapes and hot springs</h2>
    <p><strong>Who it suits.</strong> People curious about geology as well as greenery. Dominica is volcanic. Thermal areas around the Roseau Valley, including places visitors associate with Wotten Waven, are part of that story. They are not automatically attached to a waterfall visit.</p>
    <p><strong>Activity.</strong> Some thermal spots are a short walk from a vehicle; some park trails are long and muddy. Boiling Lake, in particular, is a serious hike and a poor “add-on” to a short cruise call. The <a href="/dominica-waterfalls-hot-springs">landscape guide</a> explains that distinction without prescribing an itinerary.</p>
    <h2>Champagne Reef and snorkelling</h2>
    <p><strong>Who it suits.</strong> Passengers happy to put a mask on. Basic water confidence is the real filter, not a listed age band — this site does not publish age rules because it does not sell the activity.</p>
    <p><strong>Conditions.</strong> The reef is known for underwater volcanic bubbles. Bubbles, fish and visibility are conditions, not entitlements. Read <a href="/champagne-reef-snorkeling">Champagne Reef snorkelling</a> and, if you are comparing with a land day, <a href="/best-beaches-dominica-cruise-passengers">beaches</a>.</p>
    <h2>Whale watching</h2>
    <p><strong>Who it suits.</strong> People who enjoy being on a boat and can accept a day with no sighting. Sperm whales are why Dominica is talked about; dolphins are also part of the west-coast story. <a href="/whale-watching-dominica">Learn about whale watching in Dominica</a>. Do not treat a sighting as booked in.</p>
    <h2>Private or custom sightseeing</h2>
    <p><strong>Who it suits.</strong> Groups who want a chosen theme and fewer strangers, and who will still ask hard questions about ship deadlines and weather. <a href="/private-dominica-tours">Explore private-tour ideas</a>. That page is not an offer of a private product.</p>
    <h2>Cultural experiences</h2>
    <p><strong>Who it suits.</strong> Visitors who want to understand Kalinago heritage and are willing to treat a community as more than a photo stop. <a href="/kalinago-cultural-tour-dominica">Read the Kalinago guide</a> before assuming a cultural visit can be bolted onto a west-coast waterfall morning. The road context is different. No village programme is described here because this guide does not set one.</p>
    <h2>How to choose</h2>
    <table>
      <thead><tr><th>If you want</th><th>Start with</th><th>Skip if</th></tr></thead>
      <tbody>
        <tr><td>The classic Nature Island view</td><td><a href="/trafalgar-falls">Trafalgar Falls</a></td><td>You need a dry, flat stroll only</td></tr>
        <tr><td>A swim in fresh water</td><td><a href="/titou-gorge">Titou Gorge</a> or <a href="/emerald-pool-dominica">Emerald Pool</a></td><td>You do not want to get in the water</td></tr>
        <tr><td>Time in the sea</td><td><a href="/champagne-reef-snorkeling">Champagne Reef</a></td><td>You want a guaranteed calm pool</td></tr>
        <tr><td>Wildlife at sea</td><td><a href="/whale-watching-dominica">Whale watching</a></td><td>You need a certainty, not a chance</td></tr>
        <tr><td>A slower pace</td><td><a href="/dominica-cruise-port-guide">Port guide</a> and town-side time</td><td>You are trying to tick every famous site</td></tr>
      </tbody>
    </table>
    """
    return page(
        "/best-dominica-shore-excursions",
        "best-dominica-shore-excursions.html",
        "Best Dominica Shore Excursions | Cruise Planning Ideas",
        "Compare Dominica cruise excursion ideas: waterfalls, Titou Gorge, Champagne Reef, whale watching and rainforest. Editorial planning, not a product list.",
        "Best Dominica Shore Excursions",
        body,
        crumbs=[("/best-dominica-shore-excursions", "Excursion ideas")],
        faqs=[
            ("Are these excursions sold on this website?", "No. The hub compares experience types so you can plan. It is not a catalogue, and it does not show costs or availability."),
            ("What is the easiest first stop near Roseau?", "Trafalgar Falls is the waterfall most first-time passengers use as a starting point. Easier does not mean every path is flat, and journey times still vary."),
            ("Can I combine every famous site in one call?", "Usually no. One focus, with a buffer before all-aboard, is more realistic than a chain of Trafalgar, Titou, Champagne Reef and a boat trip."),
        ],
        related=[
            ("/dominica-cruise-port-guide", "Cruise port guide", "How a Roseau day actually starts and ends."),
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "Four shapes of day and their trade-offs."),
            ("/trafalgar-falls", "Trafalgar Falls", "The twin-falls planning guide."),
        ],
    )


def port():
    body = f"""
    <p class="lede">Roseau is Dominica’s capital and the usual cruise gateway. This page is about planning from the port, not about a pickup we can name.</p>
    {NOTE}
    <h2>Arriving in Roseau</h2>
    <p>Ships use Roseau. Whether your ship docks or tenders is published by the cruise line for that call. Follow the ship’s instructions for getting ashore. This guide does not know your berth, tender pattern or all-aboard time.</p>
    <p>The town is compact by capital standards, pressed against hills and a working waterfront. You can spend a short time walking the central streets, but the island’s reputation is inland and along the coast, not in a shopping mall at the pier. If you stay near town, the Botanic Gardens are a frequent, more flexible stop than a long valley drive. Opening and access still vary; do not treat a garden walk as guaranteed just because the ship is in.</p>
    <h2>What cruise passengers need to know</h2>
    <ul>
      <li>Dominica rewards one landscape theme more than a checklist.</li>
      <li>Rain, wet rock and river colour are normal, not a failed day.</li>
      <li>The Eastern Caribbean dollar is the local currency. US dollars are widely used in Roseau. Cards are common in town; some smaller stops still expect cash. That is general context, not a payment plan for a tour.</li>
      <li>This website does not meet you, sell a seat, or hold a return vehicle.</li>
    </ul>
    <h2>Excursion planning from the port</h2>
    <p>Once ashore, direction matters more than a brand name:</p>
    <ul>
      <li><strong>Valley and park.</strong> <a href="/trafalgar-falls">Trafalgar Falls</a>, thermal areas, and the wider <a href="/dominica-waterfalls-hot-springs">rainforest and hot springs</a> landscape, including <a href="/emerald-pool-dominica">Emerald Pool</a>.</li>
      <li><strong>Gorge swim.</strong> <a href="/titou-gorge">Titou Gorge</a>, near Laudat, for people who will swim.</li>
      <li><strong>South and the sea.</strong> <a href="/champagne-reef-snorkeling">Champagne Reef</a>, and the scenic southern end around Scotts Head, discussed carefully in the <a href="/best-beaches-dominica-cruise-passengers">beaches guide</a>.</li>
      <li><strong>On the water for wildlife.</strong> <a href="/whale-watching-dominica">Whale watching</a> as a chance, not a sighting you can book from us.</li>
      <li><strong>East and culture.</strong> A <a href="/kalinago-cultural-tour-dominica">Kalinago heritage</a> day is usually a choice of focus, because it is not a short hop from the west-coast waterfront.</li>
    </ul>
    <p>Compare those styles on <a href="/best-dominica-shore-excursions">best excursion ideas</a> before you commit the morning.</p>
    <h2>Independent and organised sightseeing</h2>
    <p>Some passengers walk off and arrange transport locally. Others use a cruise-line excursion or an independent operator they have already chosen. This site does not recommend a company and does not describe a meeting point, because no meeting point has been verified here.</p>
    <p>If you arrange something yourself, ask where you will meet, how they treat the ship’s deadline, what happens in heavy rain, and whether the plan is a viewpoint, a swim, or both. Those questions belong in <a href="/private-dominica-tours">private-tour ideas</a> as well. Organised does not automatically mean safer than independent, and independent does not automatically mean more authentic. The ship still leaves.</p>
    <h2>Waterfalls, rainforest and water</h2>
    <p>The interior is close in miles and unpredictable in minutes. Journey times vary by traffic, conditions and route. A falls morning and a snorkel morning are different directions and different clothes. Doing both is a hope, not a template. Read the place guides rather than assuming a loop exists.</p>
    <h2>Timing and what is realistic in one cruise day</h2>
    <p>A realistic day has one main effort and a calm ending. Four examples — waterfall, gorge, marine, slower sightseeing — are in <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a>. None of them is a timetable. None of them includes a guaranteed transfer.</p>
    <p>First-time passengers should bias toward the simpler plan if the call is short, the weather is already wet, or anyone in the group is unsure about swimming or uneven ground.</p>
    <h2>Returning to the ship</h2>
    <p>Allow more time than the map suggests. Traffic in and out of the valley, a wet change of clothes, a slow tender queue, or a boat that is still offshore can eat a buffer. Your only authoritative deadline is the one your ship publishes. If a plan depends on a third party getting you back, ask them how they handle a late return before you leave the waterfront — not on the road.</p>
    <h2>First-time advice</h2>
    <p>Look up, then choose. Dominica’s waterfront is not the main event. The decision is which piece of the Nature Island you can do properly. Start with the <a href="/">homepage</a> if you want the short version, then pick a single guide and protect the evening gangway.</p>
    """
    return page(
        "/dominica-cruise-port-guide",
        "dominica-cruise-port-guide.html",
        "Dominica Cruise Port Guide | Planning a Day from Roseau",
        "Roseau cruise port guide for Dominica: how to plan waterfalls, rainforest, snorkelling and the return to the ship. No pickup points or guaranteed times.",
        "Dominica Cruise Port Guide",
        body,
        crumbs=[("/dominica-cruise-port-guide", "Cruise port guide")],
        faqs=[
            ("Where do cruise ships arrive in Dominica?", "The usual cruise gateway is Roseau. Whether a particular ship docks or uses tenders is set by the cruise line for that call."),
            ("Can you tell me the excursion meeting point?", "No. This guide does not publish a pickup or supplier meeting place. Ask any operator you choose, and use your ship’s instructions for getting ashore."),
            ("How long does it take to reach the waterfalls?", "Journey times vary by traffic, conditions and route. Do not plan a day that only works if every road is empty."),
        ],
        related=[
            ("/best-dominica-shore-excursions", "Excursion ideas", "Choose a style before you leave the pier."),
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "What a single call can realistically hold."),
            ("/trafalgar-falls", "Trafalgar Falls", "The waterfall most passengers ask about first."),
        ],
    )


def trafalgar():
    body = f"""
    <p class="lede">Trafalgar Falls is the twin-waterfall scene most cruise passengers mean when they say they want to see Dominica’s rainforest.</p>
    {NOTE}
    <h2>What Trafalgar Falls is</h2>
    <p>In the Roseau Valley, two cascades drop through dense forest. Visitors usually call them Mother Falls and Father Falls. One is a taller, thinner drop; the other is broader. Together they are the picture on a lot of island material. You are looking at volcanic hills and a wet forest, not a landscaped garden waterfall.</p>
    <p>The falls are a place, not a product on this website. We do not run a Trafalgar tour, name a vehicle, or publish a ticket.</p>
    <h2>Landscape and rainforest setting</h2>
    <p>The approach is green even when Roseau itself feels like a town. Ferns, wet stone and river noise are the setting. Mist is common. After rain the rock darkens and the volume of water changes. That variation is part of the visit, not a fault in the plan.</p>
    <p>Trafalgar sits in the same broad volcanic interior as <a href="/dominica-waterfalls-hot-springs">Morne Trois Pitons landscapes</a> and thermal areas people associate with the valley. Being in the same valley does not mean every nearby site is a ten-minute stroll. Journey times vary by traffic, conditions and route.</p>
    <h2>What cruise visitors should expect</h2>
    <p>Most people come for the view of both falls. There is usually a place to take that in without committing to the steepest scramble. Lower paths toward the river and the base are rougher, wetter and more of a hike. They are optional in the sense that the falls can still be seen without them, and they are not optional in the sense that “easy” paths suddenly become a riverbed. If anyone in the group is unsure on slick rock, stay with the viewpoint.</p>
    <p>Ship days can feel busy. You are sharing a famous short inland trip with other passengers. Quiet is not something this guide can offer.</p>
    <h2>Walking and access</h2>
    <p>Expect uneven ground, steps, and surfaces that stay damp. Light trainers with no grip are a poor choice. A compact rain layer is more useful than a beach cover-up. There is no clothing rule published here because there is no operator attached to this page — just the terrain.</p>
    <p>Do not plan on a dry photo and then a long swim as if they were the same activity. The pools and rocks near the falls are not a man-made bathing area. People sometimes cool off; river flow and rocks make that a judgement, not a facility.</p>
    <h2>Combining Trafalgar with other highlights</h2>
    <p>A careful pairing is another valley theme: a thermal area, or a return through Roseau with time in town or the gardens, as described in the <a href="/dominica-cruise-port-guide">cruise port guide</a>. A less careful pairing is Trafalgar plus <a href="/titou-gorge">Titou Gorge</a> plus <a href="/champagne-reef-snorkeling">Champagne Reef</a> before all-aboard. The <a href="/one-day-in-dominica-from-cruise-port">one-day guide</a> treats a waterfall morning as its own style for that reason.</p>
    <p><a href="/emerald-pool-dominica">Emerald Pool</a> is a different rainforest stop. It is not a second viewing platform at Trafalgar. Choose it when the pool-and-trail idea matters more than the twin cascades.</p>
    <h2>Who it suits</h2>
    <p>Good for first visits, mixed groups, and photographers who can live with wet air. Less good if the only acceptable path is flat and dry, or if the group’s real wish is a swim in the sea. For that, read Champagne Reef instead of forcing a falls morning to pretend it is a beach day.</p>
    <h2>Weather and terrain</h2>
    <p>Rain does not automatically cancel a viewpoint. It does change grip, spray and how the river looks. Very heavy rain can make lower approaches a bad idea even when the road is open. Nobody on this website can see the valley on your morning. If you are with an operator, ask them what they do when the lower paths are unsafe. If you are independent, turn around earlier than your pride wants.</p>
    <h2>Cruise-day planning</h2>
    <p>Go with one goal: see the twin falls properly and get back with a buffer. Leave the full park circuit, Boiling Lake and a whale boat for other conversations. Compare styles on <a href="/best-dominica-shore-excursions">excursion ideas</a> if Trafalgar was only the name you recognised.</p>
    """
    return page(
        "/trafalgar-falls",
        "trafalgar-falls.html",
        "Trafalgar Falls | Dominica Cruise Planning Guide",
        "Trafalgar Falls planning guide for cruise passengers: twin cascades, rainforest setting, wet paths and how it fits a Roseau day. Not a bookable tour.",
        "Trafalgar Falls Shore Excursion Guide",
        body,
        crumbs=[("/trafalgar-falls", "Trafalgar Falls")],
        faqs=[
            ("Are Mother and Father Falls the same place?", "They are the two cascades people mean by Trafalgar Falls: one taller and thinner, one broader, seen together in the same rainforest setting."),
            ("Do I have to hike to the base?", "No. The twin falls can be viewed without taking the steepest, wettest lower paths. Those paths are a different level of effort."),
            ("Is this a tour we can book here?", "No. This page explains the place so you can plan. It does not sell a Trafalgar trip or name a meeting point."),
        ],
        related=[
            ("/dominica-waterfalls-hot-springs", "Waterfalls and rainforest", "The wider volcanic landscape around the falls."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "Planning the day from Roseau."),
            ("/emerald-pool-dominica", "Emerald Pool", "A different rainforest stop, not a second Trafalgar."),
        ],
    )


def titou():
    body = f"""
    <p class="lede">Titou Gorge is a swim through a narrow volcanic canyon near Laudat. If you do not want to swim, choose another guide.</p>
    {NOTE}
    <h2>The gorge, not a viewpoint</h2>
    <p>The experience people come for is in the water: a channel of rock, close walls, and light that changes as the canyon bends. A photograph of a freestanding waterfall in an open forest does not describe it. This page does not use one. Treat any gorge image you see elsewhere with suspicion unless it shows an enclosed swim.</p>
    <p>The setting is still rainforest and volcanic rock. Laudat sits in the high country inland from Roseau. Being “inland” is not the same as being next to <a href="/trafalgar-falls">Trafalgar Falls</a>. They are related landscapes, not the same car park.</p>
    <h2>Swimming and water confidence</h2>
    <p>You enter the water and move through the gorge. It is not a glass walkway and it is not a pool with a lifeguard roster this site can describe. You should be comfortable swimming, including in water where you cannot always stand, and comfortable with rock close around you. People who dislike enclosed spaces often dislike this even when they swim well.</p>
    <p>Many visitors go with a local guide. This page does not say a guide is legally required, because that is not verified here, and it does not say you should go alone. If you are unsure in the water, do not use the cruise day to find out.</p>
    <h2>Conditions, clothing and footwear</h2>
    <p>The canyon is cool compared with the coast. A swim shirt or light layer you can wear in the water is more useful than beach fashion. You will want a dry change for the return to the ship. Water shoes or something that can get wet help on slick entries; barefoot on wet rock is how people slip.</p>
    <p>After heavy rain the current, colour and depth can change. A gorge that was pleasant last week can be a bad idea this morning. No forecast on this page can clear that. If someone you are travelling with says the swim is off, believe the water, not the itinerary.</p>
    <h2>Who it may not suit</h2>
    <ul>
      <li>Anyone who wants to stay dry.</li>
      <li>Weak swimmers, or strong swimmers who dislike enclosed water.</li>
      <li>Groups that need a guaranteed, uniform activity for every person.</li>
      <li>A day that already includes a long boat trip and a second major hike. See <a href="/one-day-in-dominica-from-cruise-port">one-day styles</a>.</li>
    </ul>
    <h2>Cruise-day combination ideas</h2>
    <p>Use Titou as the physical centre of the day. A short scenic pause on the way back toward Roseau is more plausible than adding Champagne Reef and a national-park circuit. The <a href="/dominica-cruise-port-guide">port guide</a> is the right companion for the return. The <a href="/best-dominica-shore-excursions">excursions hub</a> compares the gorge with waterfall viewpoints so you can switch plans before you commit.</p>
    <p>Hot springs and other valley stops are sometimes mentioned alongside the gorge. They are separate places with their own access and their own clock. Do not assume they are included because the map looks small.</p>
    <h2>Planning without a product</h2>
    <p>This site does not sell a gorge trip, publish a meeting point, or state how long you will be in the water. If you use an operator, ask how they judge unsafe water, what you should wear, and how they protect the ship’s deadline. If you cannot get clear answers, pick <a href="/trafalgar-falls">Trafalgar</a> or a slower town plan instead.</p>
    """
    return page(
        "/titou-gorge",
        "titou-gorge.html",
        "Titou Gorge | Swim Planning Guide for Cruise Passengers",
        "Titou Gorge planning guide: an enclosed freshwater swim in a volcanic canyon near Laudat. Conditions vary. Not a bookable tour.",
        "Titou Gorge Adventure Guide",
        body,
        crumbs=[("/titou-gorge", "Titou Gorge")],
        faqs=[
            ("Can I see Titou Gorge without swimming?", "The experience people mean is the swim through the canyon. A dry visit is not the same outing. Choose a waterfall viewpoint if you want to stay dry."),
            ("Is the water always safe?", "No. Rain changes current, colour and depth. A swim that suited someone else is not a guarantee for your morning."),
            ("Do you operate gorge trips?", "No. This is a planning guide. Ask any operator you choose about conditions, clothing and the ship deadline."),
        ],
        related=[
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "A gorge-focused day, and why it should stay focused."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "Getting back to the ship with a buffer."),
            ("/best-dominica-shore-excursions", "Compare styles", "Gorge swim versus a waterfall viewpoint."),
        ],
    )


def champagne():
    body = f"""
    <p class="lede">Champagne Reef is a snorkelling area south of Roseau, known for bubbles from underwater volcanic vents. The name describes the idea. It does not describe every morning.</p>
    {NOTE}
    <h2>Why the reef is known</h2>
    <p>Warm gas rises through the seabed and tickles across a mask like a poured drink. That sensation, over a rocky reef rather than a sandy lagoon, is why cruise passengers ask for Champagne Reef. The area is part of Dominica’s volcanic coast, not a theme-park tank. It is also discussed as a marine reserve; rules about what you may touch or take still apply even if nobody on your ship repeated them.</p>
    <p>This page does not use a waterfall photograph to stand in for the reef. A plunge pool in a forest is a different place. If a picture does not show people in the sea, it is not explaining Champagne Reef.</p>
    <h2>Bubbles, wildlife and visibility</h2>
    <p>Bubbles are the reputation, not a service level. Swell, wind, rain runoff and recent weather all change what you see and how the water feels. Fish, coral and the odd turtle are possible on a Caribbean reef and absent on plenty of visits. Do not plan the day around a species. Do not plan it around a perfect bubble corridor.</p>
    <p>Visibility can be lovely and can be a cloudy green after rain. Both are Dominica. A cancelled or shortened snorkel because the sea is rough is a successful safety call, not a failed excursion style.</p>
    <h2>Who it suits</h2>
    <p>People who are willing to float with a mask and fins, and who can cope with a choppy entry. You do not need to be an athlete. You do need to be honest about the sea. Nervous swimmers can have a good time on a calm morning and a miserable one when the entry is rocky and the surface is bouncing. There is no age band on this page because there is no product.</p>
    <p>Entry is often from the shore rather than a long boat ride, but that is a general pattern, not a meeting instruction. Paths, steps and beach entries vary and should be confirmed with whoever is taking you in, if anyone is. This guide does not name a pickup.</p>
    <h2>Cruise-day planning</h2>
    <p>A marine morning and an inland waterfall morning pull in different directions. Choose one as the priority. The <a href="/best-dominica-shore-excursions">excursions hub</a> sets snorkelling next to gorge swimming so you can see they are both “water” and still not interchangeable. The <a href="/dominica-cruise-port-guide">port guide</a> covers the return: wet kit, traffic, and the ship’s deadline.</p>
    <p>Scotts Head, at the southern end of the island, is a scenic headland people sometimes mention in the same breath. It is not an automatic second swim after the reef. Read <a href="/best-beaches-dominica-cruise-passengers">beaches for cruise passengers</a> before you turn a snorkel into a coast-long circuit.</p>
    <h2>Combining with land sightseeing</h2>
    <p>A short stop in Roseau or a viewpoint on the way back is more believable than Champagne Reef plus <a href="/titou-gorge">Titou Gorge</a> plus <a href="/trafalgar-falls">Trafalgar Falls</a>. Salt water then a canyon swim then a rainforest hike is three recoveries, not one day. The marine-focused style in <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a> keeps the sea as the point.</p>
    <h2>What to ask if someone else is organising the water</h2>
    <ul>
      <li>What sea state makes them turn around?</li>
      <li>Is the entry from shore, and what is the footing like?</li>
      <li>What happens to the ship deadline if the water is slow?</li>
      <li>What should you bring: footwear, rash vest, dry bag?</li>
    </ul>
    <p>If the answers are vague, a land plan is the more honest choice.</p>
    """
    return page(
        "/champagne-reef-snorkeling",
        "champagne-reef-snorkeling.html",
        "Champagne Reef Snorkelling | Dominica Cruise Guide",
        "Champagne Reef snorkelling guide for cruise passengers: volcanic bubbles, changeable visibility, and how a marine morning fits a Roseau day. No guarantees.",
        "Champagne Reef Snorkelling Guide",
        body,
        crumbs=[("/champagne-reef-snorkeling", "Champagne Reef")],
        faqs=[
            ("Will I definitely see the volcanic bubbles?", "No. Bubbles are why the reef is famous. Swell, wind and rain change what you feel and see. Treat them as possible, not promised."),
            ("Is visibility always clear?", "No. Rain runoff and sea state can cloud the water. A rough-water cancellation is a safety decision, not a broken promise from this guide."),
            ("Can I book snorkelling here?", "No. This page is editorial. It does not list prices, gear packages or a meeting place."),
        ],
        related=[
            ("/best-dominica-shore-excursions", "Excursion ideas", "Snorkel compared with land and gorge days."),
            ("/best-beaches-dominica-cruise-passengers", "Beaches", "Why a sand-lounger day is a different request."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "Timing the wet return to the ship."),
        ],
    )


def waterfalls():
    body = f"""
    <p class="lede">A wider look at Dominica’s rainforest, waterfalls and volcanic ground — context for a cruise day, not a set route.</p>
    {NOTE}
    <h2>Waterfall landscapes</h2>
    <p>Dominica has a lot of falling water because it has a lot of rain and steep volcanic hills. <a href="/trafalgar-falls">Trafalgar Falls</a> is the twin-cascade stop most cruise passengers can picture. <a href="/emerald-pool-dominica">Emerald Pool</a> is a pool under a smaller fall, reached by a trail. Middleham Falls is another name you will hear: a tall drop in the rainforest of the national park, generally a longer, wetter walk than standing at the Trafalgar viewpoint. They are different outings. Seeing one does not mean you have “done the waterfalls.”</p>
    <h2>Rainforest</h2>
    <p>The forest is the island’s character. It is humid, often dripping, and full of uneven roots and mud after rain. That is not bad weather ruining a postcard. It is the habitat. A light rain jacket and shoes that can get dirty will serve you better than a plan that only works in drought.</p>
    <p>Birdlife, including parrots passengers hear about, is a bonus of quiet forest time, not a wildlife guarantee. Do not build the day around a sighting.</p>
    <h2>Volcanic geology and thermal areas</h2>
    <p>The same forces that lifted the island warm the water in places. The Roseau Valley’s thermal spots — Wotten Waven is the name most visitors recognise — are sulphur, steam and mineral water, not a hotel spa menu. Some are a short walk from a vehicle. Access, heat and whether bathing is appropriate that day are local conditions. This page does not describe an entry fee, a changing room, or a soak that is included with a waterfall stop.</p>
    <p>Boiling Lake is the famous extreme: a flooded fumarole reached by a serious hike across the park. It is a poor add-on to a short cruise call. If someone offers it as a casual extra, ask what “casual” means before you say yes. Journey times vary by traffic, conditions and route — and a trail is not a road.</p>
    <h2>Morne Trois Pitons</h2>
    <p>Morne Trois Pitons National Park is the UNESCO-listed interior that holds much of this landscape: volcanic features, forest and waterfalls, Emerald Pool among them. The park name is useful context. It is not an itinerary. Gates, trails and site rules are not reproduced here because they change and this site does not administer them.</p>
    <h2>Hot springs, generally</h2>
    <p>A thermal stop can be a gentler second note after a viewpoint, if the clock and the road allow. It can also be the whole point of a slower day. It should not be assumed. Heat, smell and footing are part of the place. People with health conditions that react badly to hot water should treat “hot spring” as a question for them, not a default reward at the end of a hike.</p>
    <h2>Physical suitability</h2>
    <ul>
      <li>Viewpoint stops: still possibly wet and uneven.</li>
      <li>Trail waterfalls such as Middleham or the walk into Emerald Pool: more commitment, more mud.</li>
      <li>Boiling Lake: a demanding hike, usually the wrong shape for a brief port call.</li>
      <li>Thermal water: optional, variable, never described here as included.</li>
    </ul>
    <h2>Cruise-day planning</h2>
    <p>Pick a single landscape idea and let the <a href="/dominica-cruise-port-guide">port guide</a> protect the ending. The <a href="/one-day-in-dominica-from-cruise-port">one-day article</a> uses waterfalls and rainforest as its first style for a reason: it is the island’s signature, and it already fills a morning. <a href="/titou-gorge">Titou Gorge</a> is nearby in spirit and still a swim, not a third waterfall photo.</p>
    """
    return page(
        "/dominica-waterfalls-hot-springs",
        "dominica-waterfalls-hot-springs.html",
        "Dominica Waterfalls and Hot Springs | Rainforest Guide",
        "Dominica rainforest, waterfalls, Morne Trois Pitons and thermal areas for cruise passengers. Landscape context only — no set itinerary.",
        "Dominica Waterfalls and Hot Springs",
        body,
        crumbs=[("/dominica-waterfalls-hot-springs", "Waterfalls and rainforest")],
        faqs=[
            ("Is this a set waterfall tour?", "No. The page explains the kinds of landscape you might choose between. It does not prescribe stops, times or a vehicle."),
            ("Is Boiling Lake realistic on a cruise day?", "It is a demanding hike. Treat it as a specialist outing, not a casual extra on a short call."),
            ("Are hot springs included with Trafalgar Falls?", "No. Thermal areas are separate places. Access and whether a soak makes sense that day are not part of a falls viewpoint."),
        ],
        related=[
            ("/trafalgar-falls", "Trafalgar Falls", "The twin cascades most people start with."),
            ("/emerald-pool-dominica", "Emerald Pool", "A pool and trail inside the park landscape."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "How an inland morning fits the ship."),
        ],
    )


def whale():
    body = f"""
    <p class="lede">Dominica is talked about for sperm whales in deep water off the west coast. That reputation is a reason to learn, not a sighting you can count on.</p>
    {NOTE}
    <h2>Why whale watching is discussed here</h2>
    <p>The island’s underwater shelf drops away. Sperm whales use that deep water, and Dominica has a resident population that marine guides and researchers talk about year-round more than as a two-week season. Dolphins are also part of west-coast trips people describe. Neither fact turns a morning into a performance.</p>
    <p>This page does not use an orca photograph. Orcas are the wrong animal for this story. A leaping black-and-white whale is a stock picture, not Dominica’s sperm whales. If you see one on a Dominica page, ignore it.</p>
    <h2>Sightings are never guaranteed</h2>
    <p>Whales move. Sea state changes. A skilled crew can still come back without a sighting. That is wildlife, not a refund policy this website can describe — because this website does not sell the trip. Go to sea if you would still have had a worthwhile boat morning if the animals stayed down. Do not go if the only acceptable outcome is a photograph of a tail.</p>
    <h2>What this guide will not invent</h2>
    <ul>
      <li>A departure pontoon, marina or pier meeting point.</li>
      <li>How many hours you will be on the water.</li>
      <li>A season chart that promises better odds on your date.</li>
      <li>A boat we operate. We do not operate whale watching.</li>
    </ul>
    <p>If you choose an operator or a cruise-line excursion, those details belong to them. Ask. Compare the answers with your ship’s all-aboard time using the <a href="/dominica-cruise-port-guide">Roseau cruise port guide</a>.</p>
    <h2>Questions worth asking any operator</h2>
    <ul>
      <li>Where do you actually meet, and how long is the transfer from the waterfront?</li>
      <li>What wind or swell makes you stay in?</li>
      <li>How do you treat the ship’s deadline if the sea is slow?</li>
      <li>How many people are on the boat?</li>
      <li>What is the plan if there is no sighting — more searching, or an earlier return?</li>
    </ul>
    <p>Vague answers are a reason to spend the day in the rainforest instead. <a href="/trafalgar-falls">Trafalgar Falls</a> and <a href="/dominica-waterfalls-hot-springs">the wider landscape guide</a> do not depend on an animal surfacing.</p>
    <h2>How it fits a cruise day</h2>
    <p>A whale boat and a packed land itinerary do not share a morning well. Being on the water is the day. Salt, sun and a possible wait are the experience even before a fin appears. The marine style in <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a> is the place to see that trade-off next to snorkelling. <a href="/champagne-reef-snorkeling">Champagne Reef</a> is the other water choice: mask and fins, not a wildlife cruise.</p>
    <p><a class="btn" href="/dominica-cruise-port-guide">Read the cruise port guide</a></p>
    <p>Learn about whale watching in Dominica, then decide with your eyes open. The <a href="/best-dominica-shore-excursions">excursions hub</a> keeps this as one style among several, not a featured product.</p>
    """
    return page(
        "/whale-watching-dominica",
        "whale-watching-dominica.html",
        "Whale Watching in Dominica | Cruise Planning Guide",
        "Learn about whale watching in Dominica: sperm whales off the west coast, no promised sightings, no invented departure point. Planning guide only.",
        "Whale Watching in Dominica",
        body,
        crumbs=[("/whale-watching-dominica", "Whale watching")],
        faqs=[
            ("Will I see a sperm whale?", "Not necessarily. Dominica is known for sperm whales in deep west-coast water. Sightings are never guaranteed."),
            ("Where does the boat leave from?", "This guide does not publish a departure point. Ask the operator or cruise line you choose, and check it against your ship’s timing."),
            ("Do you run whale trips?", "No. We do not operate boats. This page is editorial so you can decide whether the odds suit you."),
        ],
        related=[
            ("/dominica-cruise-port-guide", "Cruise port guide", "Deadlines matter more on a boat day."),
            ("/best-dominica-shore-excursions", "Excursion ideas", "Whale watching next to land alternatives."),
            ("/champagne-reef-snorkeling", "Champagne Reef", "A different kind of time in the water."),
        ],
    )


def private():
    body = f"""
    <p class="lede">Private sightseeing can mean a vehicle and a guide shaped around your group. This page explains that idea. It does not offer a private tour.</p>
    {NOTE}
    <h2>What private sightseeing can offer</h2>
    <p>A dedicated arrangement can mean fewer strangers, a pace set by the people in the vehicle, and a theme you chose: waterfalls, a coast road, a cultural conversation, or a deliberately slow look at Roseau and the hills. It does not suspend traffic, rain, or the ship. Flexibility is the product other people sell. This website is not selling it.</p>
    <p><a class="btn" href="/best-dominica-shore-excursions">Explore private-tour ideas</a></p>
    <h2>Smaller groups and choosing a focus</h2>
    <p>The useful part of “private” is editing. Dominica punishes lists. A private morning that still tries to include <a href="/trafalgar-falls">Trafalgar</a>, <a href="/titou-gorge">Titou Gorge</a>, <a href="/champagne-reef-snorkeling">Champagne Reef</a> and a boat is not private planning. It is the same overload with a higher bill you will not find on this site, because no bill is published here.</p>
    <p>Choose areas of interest before you talk to anyone:</p>
    <ul>
      <li>Rainforest and falls — start with the <a href="/dominica-waterfalls-hot-springs">landscape guide</a> and <a href="/emerald-pool-dominica">Emerald Pool</a>.</li>
      <li>A swim in a canyon — the Titou page, and an honest no if anyone will not swim.</li>
      <li>The sea — Champagne Reef, with bubbles left unpromised.</li>
      <li>Culture — the <a href="/kalinago-cultural-tour-dominica">Kalinago guide</a>, read as a community, not a module.</li>
      <li>A slower day — town, gardens, a viewpoint, as sketched in the <a href="/one-day-in-dominica-from-cruise-port">one-day article</a>.</li>
    </ul>
    <h2>Questions to ask any operator</h2>
    <ul>
      <li>Where do we meet, and is that place obvious from the cruise waterfront?</li>
      <li>What is the plan if it is pouring or a path is closed?</li>
      <li>Which stops involve water, mud, or stairs?</li>
      <li>How do you guarantee — or not guarantee — the return before all-aboard?</li>
      <li>How many people will actually be in the vehicle?</li>
      <li>What is not included that passengers often assume is included?</li>
    </ul>
    <p>Write the answers down. If the meeting point is vague, or the route only works if every road is empty, it is not a plan yet. Journey times vary by traffic, conditions and route.</p>
    <h2>Cruise timing</h2>
    <p>Private does not buy you a later ship. Use the <a href="/dominica-cruise-port-guide">cruise port guide</a> to set the ending first, then see what theme fits the remaining hours. A shorter, clearer outing is the luxury. A longer list is how private days go wrong.</p>
    <p>Compare the theme with the public style guide on <a href="/best-dominica-shore-excursions">excursion ideas</a> so you know what you are asking for before anyone quotes you — somewhere else, not here.</p>
    """
    return page(
        "/private-dominica-tours",
        "private-dominica-tours.html",
        "Private Dominica Tour Ideas | Cruise Planning",
        "Private Dominica sightseeing ideas for cruise passengers: focus, questions to ask, and ship timing. Not a private product for sale.",
        "Private Dominica Tour Ideas",
        body,
        crumbs=[("/private-dominica-tours", "Private-tour ideas")],
        faqs=[
            ("Can I book a private tour on this site?", "No. There is no private product, request form or calendar here. The page is about how to think about a custom day."),
            ("Does private mean we can see everything?", "No. A private vehicle still shares the island’s roads and your ship’s deadline. One theme is still the better day."),
            ("Will you recommend a driver?", "No. This guide does not endorse operators. It lists questions worth asking anyone you speak to."),
        ],
        related=[
            ("/best-dominica-shore-excursions", "Excursion ideas", "Pick a theme before you talk to anyone."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "The deadline comes first."),
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "See what a focused day looks like."),
        ],
    )


def kalinago():
    body = f"""
    <p class="lede">The Kalinago are Dominica’s indigenous people. A visit, if you make one, is time in a living community — not a show this website can programme.</p>
    {NOTE}
    <h2>Heritage, not a module</h2>
    <p>Kalinago history is part of Dominica, not a side note to the waterfalls. The Kalinago Territory is a recognised area of the island, associated with the northeast and east rather than the Roseau waterfront. People live and work there. It is not a film set and it is not a compulsory cruise stop.</p>
    <p>Older pages sometimes listed craft demonstrations, performances, herbal gardens, meals and entry inclusions as if they were a fixed package. This guide does not. Those details belong to hosts, if they offer them at all. Inventing a village programme would be disrespectful as well as inaccurate.</p>
    <h2>If you go, go as a guest</h2>
    <ul>
      <li>Prefer experiences that are locally led, and be clear who you are paying and what you are being invited to see.</li>
      <li>Ask before photographing people, homes, or ceremonies. A cruise lanyard is not permission.</li>
      <li>Dress and speak as you would in someone else’s neighbourhood, not on a theme-park concourse.</li>
      <li>Do not expect a performance schedule, a meal, or a craft stall because a blog once mentioned one.</li>
      <li>Buy something only if you want it and the seller is actually selling. Do not treat people as scenery.</li>
    </ul>
    <h2>Responsible planning</h2>
    <p>A cultural visit is a choice of focus. The Kalinago Territory is a longer road journey from Roseau than many west-coast stops, so it usually replaces a waterfall circuit rather than following one. Journey times vary by traffic, conditions and route. This page will not pretend otherwise by printing a drive time.</p>
    <p>Read <a href="/one-day-in-dominica-from-cruise-port">one day from the cruise port</a> and keep the cultural option inside a single theme. The <a href="/dominica-cruise-port-guide">port guide</a> still governs the return. Being interested in heritage does not extend all-aboard.</p>
    <h2>What you can learn without a script</h2>
    <p>Even a careful visit is a glimpse. Kalinago language, land and politics are larger than a port call. If the day does not allow a respectful visit, read before you claim the topic, and do not use a rainforest hike as a substitute for a community you did not meet. The <a href="/best-dominica-shore-excursions">excursions hub</a> lists cultural visiting as its own style so it is not flattened into “another inland stop.”</p>
    <h2>Questions, if you arrange something</h2>
    <p>Ask who leads the visit, what you will actually be invited to do, whether photography is welcome, and how the timing works with the ship. If the description is a list of performances and inclusions you cannot verify, slow down. <a href="/private-dominica-tours">Private-tour ideas</a> has the same standard: questions first, no product on this site.</p>
    """
    return page(
        "/kalinago-cultural-tour-dominica",
        "kalinago-cultural-tour-dominica.html",
        "Kalinago Heritage in Dominica | Responsible Cruise Visiting",
        "A cautious guide to Kalinago heritage for cruise passengers: community context, respectful visiting, and Roseau timing. No invented village programme.",
        "Kalinago Heritage for Cruise Visitors",
        body,
        crumbs=[("/kalinago-cultural-tour-dominica", "Kalinago heritage")],
        faqs=[
            ("Does this page describe a Kalinago tour package?", "No. It does not list demonstrations, meals, guides, fees or a fixed village programme. Those details belong to hosts, not to this guide."),
            ("Can I photograph freely?", "No. Ask first. People, homes and ceremonies are not a backdrop for a cruise day."),
            ("Can I add this after Trafalgar Falls?", "Usually it should be the focus of the day, not an add-on. The Territory is a different road context from the west-coast waterfront, and times vary."),
        ],
        related=[
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "Keep a cultural visit as one theme."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "The ship deadline still applies."),
            ("/best-dominica-shore-excursions", "Excursion ideas", "Cultural visiting as its own style."),
        ],
    )


def emerald():
    body = f"""
    <p class="lede">Emerald Pool is a freshwater pool beneath a waterfall in the rainforest of Morne Trois Pitons National Park. The name describes a colour you might see. It does not promise the colour on your morning.</p>
    {NOTE}
    <h2>What Emerald Pool is</h2>
    <p>A short trail leads to a pool at the base of a fall. It is one of the more approachable ways to be inside Dominica’s forest, which is why cruise passengers hear about it alongside <a href="/trafalgar-falls">Trafalgar Falls</a>. It is not a second viewing deck at Trafalgar, and it is not <a href="/titou-gorge">Titou Gorge</a>. The gorge is an enclosed swim through a canyon. Emerald Pool is a forest walk to a basin.</p>
    <p>The wider park context — other falls, mud, and why Boiling Lake is a different commitment — is in the <a href="/dominica-waterfalls-hot-springs">waterfalls and rainforest guide</a>.</p>
    <h2>Visitor experience</h2>
    <p>You walk in, you look at falling water, and some people swim. The pool can look green and clear. After rain it can look brown. Both are the same place. Popularity means you may share the trail and the bank with other cruise passengers. Quiet is not a feature this guide can offer.</p>
    <p>There is no photograph on this page. A generic waterfall image would pretend to be this pool. Until a rights-cleared picture of the actual site exists in this project, type is more honest than a wrong forest.</p>
    <h2>Walking and access</h2>
    <p>The approach is often described as shorter than some other park trails. Shorter is not the same as paved, dry or accessible to every walker. Roots, mud and wet stone show up after ordinary rain. If the group needs a flat waterfront stroll, stay in Roseau and use the <a href="/dominica-cruise-port-guide">port guide</a> instead of forcing a trail.</p>
    <p>This page does not state an entry fee, a gate time, or a drive time. Journey times vary by traffic, conditions and route. Park rules are not administered here.</p>
    <h2>Who it suits</h2>
    <p>People who want rainforest and water without committing to a canyon swim, and who can manage a trail that may be slippery. Less suitable if swimming is the only point and the pool is crowded or turbid — have a viewpoint mindset as the backup. Less suitable as a third stop after a long list of other sites.</p>
    <h2>Combination ideas</h2>
    <p>Emerald Pool works as the rainforest focus of a day, or as a careful companion to another inland theme if the clock is kind. It is a weak companion to a whale boat and a southern snorkel. The <a href="/one-day-in-dominica-from-cruise-port">one-day guide</a> puts waterfall-and-forest days in their own column for that reason. Compare it with Trafalgar on the <a href="/best-dominica-shore-excursions">excursions hub</a> before you try to do both and call it relaxed.</p>
    <h2>Cruise-day planning</h2>
    <p>Shoes with grip, a light rain layer, and a dry shirt for the ship. Swim only if the water looks like something you want to enter, not because the name is Emerald. Build the return around the ship’s all-aboard time, not around an imagined empty road back to Roseau.</p>
    """
    return page(
        "/emerald-pool-dominica",
        "emerald-pool-dominica.html",
        "Emerald Pool Dominica | Cruise Planning Guide",
        "Emerald Pool planning guide: a rainforest pool and trail in Morne Trois Pitons, for cruise passengers. Colour and conditions vary. Not a tour.",
        "Emerald Pool Dominica",
        body,
        crumbs=[("/emerald-pool-dominica", "Emerald Pool")],
        faqs=[
            ("Is Emerald Pool always emerald?", "No. The pool can look green and clear, and it can look brown after rain. The name is not a guarantee."),
            ("Is this the same as Titou Gorge?", "No. Emerald Pool is a trail to a basin under a fall. Titou Gorge is a swim through a narrow canyon."),
            ("Can I book Emerald Pool here?", "No. This is a planning guide. It does not list tickets, pickup or a fixed visit length."),
        ],
        related=[
            ("/dominica-waterfalls-hot-springs", "Waterfalls and rainforest", "Park context beyond a single pool."),
            ("/trafalgar-falls", "Trafalgar Falls", "The twin cascades, a different stop."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "Getting back from an inland walk."),
        ],
    )


def oneday():
    body = f"""
    <p class="lede">Four styles of day from Roseau. They are shapes, not timetables, and none of them is a tour we run.</p>
    {NOTE}
    <p>Start from the ship’s all-aboard time and subtract a buffer. What remains is the day. The <a href="/dominica-cruise-port-guide">cruise port guide</a> explains why the buffer matters. The <a href="/best-dominica-shore-excursions">excursions hub</a> is the comparison if you have not chosen a style yet. Journey times vary by traffic, conditions and route. No clock below is a promise.</p>
    <h2>Option A — waterfalls and rainforest</h2>
    <p><strong>The idea.</strong> One inland landscape, done properly. <a href="/trafalgar-falls">Trafalgar Falls</a> is the usual centre. <a href="/emerald-pool-dominica">Emerald Pool</a> is the alternative if a trail and a pool matter more than twin cascades. The <a href="/dominica-waterfalls-hot-springs">rainforest guide</a> is the context, including why Middleham or Boiling Lake are not automatic extras.</p>
    <p><strong>Trade-off.</strong> You miss the sea, and you may miss Titou if you refuse to rush. You gain the picture most people mean by Nature Island, with energy left for the return. A thermal stop is a maybe, not a line item.</p>
    <p><strong>Suits.</strong> First visits, mixed groups, anyone who would rather be slightly under-scheduled.</p>
    <h2>Option B — Titou Gorge and a scenic return</h2>
    <p><strong>The idea.</strong> The swim is the day. Read <a href="/titou-gorge">Titou Gorge</a> before you pick this. Add only a short scenic pause on the way back toward Roseau, not a second headline site.</p>
    <p><strong>Trade-off.</strong> People who will not swim have a poor day. Rain can cancel the point of the outing. You do not also get a relaxed Trafalgar scramble and a snorkel.</p>
    <p><strong>Suits.</strong> Confident swimmers who want one strong memory.</p>
    <h2>Option C — marine-focused</h2>
    <p><strong>The idea.</strong> Either <a href="/champagne-reef-snorkeling">Champagne Reef</a> or <a href="/whale-watching-dominica">time on the water for whales</a>, not both as a right. Bubbles and sightings stay unpromised. A marine morning already includes salt, sun and a wet return.</p>
    <p><strong>Trade-off.</strong> You will not also walk the park properly. A rough sea can shrink the day to town. That is a reason to have read the port guide, not a reason to stack a waterfall “just in case” on the same ticket-in-your-head.</p>
    <p><strong>Suits.</strong> People who came for the water and can enjoy the boat or the reef even if the famous moment does not appear.</p>
    <h2>Option D — slower sightseeing</h2>
    <p><strong>The idea.</strong> Roseau itself, the Botanic Gardens if they are open to you that day, a viewpoint, a coffee, a short coast look. Use the <a href="/best-beaches-dominica-cruise-passengers">beaches guide</a> only to retire the fantasy of a resort-sand afternoon. A <a href="/kalinago-cultural-tour-dominica">Kalinago visit</a> can be a slow day of its own if it is the focus and it is led locally — not a quick add-on to the gardens.</p>
    <p><strong>Trade-off.</strong> You may feel you “missed” the falls. You also avoided a rushed, wet, late day. On a short call or in hard rain, this is often the adult choice.</p>
    <p><strong>Suits.</strong> Repeat visitors, tired passengers, anyone who dislikes being herded, and groups with very different walking ability.</p>
    <h2>How to choose</h2>
    <table>
      <thead><tr><th>Style</th><th>You accept</th><th>You give up</th></tr></thead>
      <tbody>
        <tr><td>A Waterfalls</td><td>Mud and a single inland focus</td><td>A sea morning</td></tr>
        <tr><td>B Titou</td><td>An enclosed swim</td><td>A dry, multi-stop list</td></tr>
        <tr><td>C Marine</td><td>Odds, not certainties</td><td>The park done properly</td></tr>
        <tr><td>D Slower</td><td>A quieter, smaller day</td><td>The famous checklist</td></tr>
      </tbody>
    </table>
    <p>Private arrangements, if you make them elsewhere, should still pick one of these shapes. See <a href="/private-dominica-tours">private-tour ideas</a>. Then go back to the <a href="/">homepage</a> only if you need to remember what the island is for.</p>
    """
    return page(
        "/one-day-in-dominica-from-cruise-port",
        "one-day-in-dominica-from-cruise-port.html",
        "One Day in Dominica from the Cruise Port",
        "Four realistic styles for one day in Dominica from Roseau: rainforest, Titou Gorge, a marine morning, or slower sightseeing. Not guaranteed itineraries.",
        "One Day in Dominica from the Cruise Port",
        body,
        crumbs=[("/one-day-in-dominica-from-cruise-port", "One day from the port")],
        faqs=[
            ("Which option is the official itinerary?", "None of them. They are planning styles so you can see trade-offs. They are not timed tours and they are not sold here."),
            ("Can I combine A, B and C?", "That is how cruise days in Dominica go wrong. Pick one style and protect the return to the ship."),
            ("Do you publish drive times?", "No. Journey times vary by traffic, conditions and route. Plan with a buffer, not a minute-by-minute chart."),
        ],
        related=[
            ("/dominica-cruise-port-guide", "Cruise port guide", "Start and end the day in Roseau."),
            ("/titou-gorge", "Titou Gorge", "Read this before choosing option B."),
            ("/kalinago-cultural-tour-dominica", "Kalinago heritage", "A cultural day needs to be the focus."),
        ],
    )


def beaches():
    body = f"""
    <p class="lede">Dominica can include a swim. It is a poor choice if the only plan is a resort beach with a chair waiting.</p>
    {NOTE}
    <h2>What the coast is like</h2>
    <p>The shoreline is volcanic: rock, pebbles, river mouths, and some coves where people swim. It is not a chain of hotel beaches with a published standard of loungers, shade and beach bars. This guide does not claim chairs, facilities, fees or guaranteed access anywhere. If a page elsewhere shows a long white-sand lagoon with windsurfers, it is probably another island.</p>
    <p>That is why the <a href="/">homepage</a> leads with waterfalls and rainforest. The sea still matters — especially <a href="/champagne-reef-snorkeling">Champagne Reef</a> — but the sea here is snorkelling, headlands and wildlife water, not a cabana day.</p>
    <h2>Beach-day considerations for cruise passengers</h2>
    <ul>
      <li>Time in the water is realistic. Time on a rented lounger is not something you should expect from this article.</li>
      <li>West-coast bays are the ones most often mentioned because they sit closer to Roseau than the Atlantic side. Closer is not a transfer we can describe.</li>
      <li>Scotts Head, at the southern end, is a scenic peninsula people swim and snorkel from. It is a headland, not a resort strip, and sea conditions change it.</li>
      <li>Northeast and east-coast beaches are a different road story from a short west-coast hop. Treat them as a possible focus of a day, not a quick swim after the falls. Journey times vary by traffic, conditions and route.</li>
      <li>Rain, river outflow and swell change whether a bay is pleasant. A brown line of water after rain is weather, not a closed promise.</li>
    </ul>
    <h2>What this page will not claim</h2>
    <p>No specific taxi arrangement, no beach-chair vendor, no entry price, no statement that a given bay will be open, calm or staffed. If you want those facts, they have to come from someone who is there that week — not from a planning guide that cannot see the tide.</p>
    <h2>How a swim fits a cruise day</h2>
    <p>The honest versions are already in other guides. A snorkel at Champagne Reef is a marine morning. A pool under a fall is <a href="/emerald-pool-dominica">Emerald Pool</a> or a judgement at a river, not a beach. A canyon swim is <a href="/titou-gorge">Titou Gorge</a>. A slower day in the <a href="/one-day-in-dominica-from-cruise-port">one-day article</a> might include a coast look without pretending it was a beach club.</p>
    <p>If the group’s heart is set on sand, say so before you leave the ship, and keep the expectation small. Pair a short swim, if the water looks right, with one land theme from the <a href="/best-dominica-shore-excursions">excursions hub</a>. Do not spend the Roseau call hunting for a beach that matches another port.</p>
    <h2>Practical caution</h2>
    <p>Currents and entries are local. Do not swim where you cannot see a sensible way out. Do not assume a bar, a toilet or a lifeguard. Reef shoes help on rock. Sun on a boat or a dark-sand edge still burns. Then use the <a href="/dominica-cruise-port-guide">cruise port guide</a> so a swim does not become the reason you watch the ship leave.</p>
    """
    return page(
        "/best-beaches-dominica-cruise-passengers",
        "best-beaches-dominica-cruise-passengers.html",
        "Dominica Beaches for Cruise Passengers | Planning Guide",
        "Beach-day reality for Dominica cruise passengers: volcanic coast, changeable swimming, no claimed facilities or transfers. Editorial only.",
        "Beaches in Dominica for Cruise Passengers",
        body,
        crumbs=[("/best-beaches-dominica-cruise-passengers", "Beaches")],
        faqs=[
            ("Is Dominica a good beach port?", "Only if your idea of a beach day is flexible. The island is known for rainforest and volcanic coast, not resort sand and waiting chairs."),
            ("Do you list beach clubs or transfer prices?", "No. Facilities, access and costs are not verified here and are not published."),
            ("Where should I swim instead?", "Read Champagne Reef for a snorkel, Emerald Pool or Titou Gorge for fresh water, and judge the sea on the day. Nothing here guarantees conditions."),
        ],
        related=[
            ("/champagne-reef-snorkeling", "Champagne Reef", "The marine swim people actually mean."),
            ("/one-day-in-dominica-from-cruise-port", "One-day styles", "A slower day without a beach-club script."),
            ("/dominica-cruise-port-guide", "Cruise port guide", "Keep the swim inside the ship’s clock."),
        ],
    )

