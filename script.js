/* =========================================================================
   BAL GANESH MITRA MANDAL — SITE SCRIPT
   File map:
     1. SITE CONFIGURATION   — edit mandal info, hero image, agaman, location
     2. DAILY SCHEDULE       — edit/add utsav days & events
     3. MEMORIES             — add photos & reels here
     4. PEOPLE               — edit team members
     5. AUCTION_CONFIG       — laddu auction settings
     6. DONATION_CONFIG      — UPI donation settings
     7. Utilities
     8. Renderers / interactions (navbar, hero, countdown, timeline,
        memories + lightbox, first-year, people, events, location, social,
        auction, donation, footer, scroll reveal)
     9. Init
   Everything above section 7 is meant to be edited. Nothing below section 6
   needs to change for day-to-day updates.
   ========================================================================= */

/* ============================================================
   1. SITE CONFIGURATION — EDIT ONLY THIS SECTION
   ============================================================ */
const SITE_CONFIG = {
  mandalName: "Bal Ganesh Mitra Mandal",
  year: 2026,

  // Path to the main hero photo of Bappa. Drop your image at this path
  // (e.g. an "assets" folder next to index.html) or change the path here.
  heroImage: "assets/hero.jpg",
  heroImageAlt: "Bal Ganesh Mitra Mandal — Bappa",

  // Group photo shown in the "Our First Year" section.
  groupPhoto: "assets/group-photo.jpg",
  groupPhotoAlt: "Bal Ganesh Mitra Mandal — the team",

  // Bappa's arrival — drives the live countdown. 24-hour "HH:MM" time.
  agaman: {
    date: "2026-09-13",
    time: "18:00",
    label: "Bappa Aagman",
    note: "Sham ko"
  },

  location: {
    name: "Bal Ganesh Mitra Mandal",
    address: "", // e.g. "Near XYZ Chowk, Hyderabad" — shown under the name
    mapsUrl: ""  // paste a Google Maps link here to activate "Get Directions"
  },

  social: {
    instagram: "", // paste your Instagram profile/reel URL here
    // Optional: a small grid of reel/photo previews under the Instagram button.
    // Each item: { media: "assets/social/reel1.jpg", url: "https://instagram.com/..." }
    reels: []
  }
};

/* ============================================================
   2. DAILY SCHEDULE — EDIT / ADD UTSAV EVENTS HERE
   Used for both the Utsav Journey timeline and the Events section.
   Fields:
     id       — unique short string
     date     — "YYYY-MM-DD"
     time     — "HH:MM" (24-hour)
     title    — event name
     description — short emotional line
     image    — path to a photo, or "" for a placeholder
     category — "aagman" | "aarti" | "prasadam" | "cultural" | "visarjan" | "general"
     visible  — true to show it, false to keep it hidden until you're ready
   Only Bappa Aagman (Sun 13 Sep 2026, evening) and Annam Prasadam (a
   Wednesday) were confirmed in the brief — the rest are placeholder
   templates with visible:false so nothing invented appears on the live site.
   ============================================================ */
const DAILY_SCHEDULE = [
  {
    id: "aagman",
    date: "2026-09-13",
    time: "18:00",
    title: "Bappa Aagman",
    description: "Pehli dastak, pehli khushi.",
    image: "",
    category: "aagman",
    visible: true
  },
  {
    id: "annam-prasadam",
    // Exact date wasn't specified beyond "Wednesday" — this defaults to the
    // Wednesday of Utsav week. Please confirm/edit before publishing.
    date: "2026-09-16",
    time: "13:00",
    title: "Annam Prasadam",
    description: "Prasad ka swaad, Bappa ka aashirwad.",
    image: "",
    category: "prasadam",
    visible: true
  },
  // ---- Placeholder templates below — set visible:true once confirmed ----
  {
    id: "daily-aarti-2",
    date: "2026-09-14",
    time: "19:00",
    title: "Daily Aarti",
    description: "Har subah Bappa ke naam.",
    image: "",
    category: "aarti",
    visible: false
  },
  {
    id: "cultural-program",
    date: "2026-09-18",
    time: "19:30",
    title: "Cultural Program",
    description: "Sur, taal aur Bappa ke naam ek shaam.",
    image: "",
    category: "cultural",
    visible: false
  },
  {
    id: "visarjan",
    date: "2026-09-21",
    time: "16:00",
    title: "Visarjan",
    description: "Phir milenge, agle baras.",
    image: "",
    category: "visarjan",
    visible: false
  }
];

/* ============================================================
   3. MEMORIES — ADD PHOTOS & REELS HERE
   Fields:
     type     — "photo" | "video"
     category — "photos" | "reels" | "aarti" | "events" | "bts"
     date     — display string, e.g. "13 Sep 2026"
     title    — short title
     caption  — short emotional line
     media    — path to image/video, or "" for an "Add Photo" placeholder
     visible  — true to show it
   ============================================================ */
const MEMORIES = [
  {
    type: "photo",
    category: "aagman",
    displayCategory: "events",
    date: "13 Sep 2026",
    title: "Bappa Aagman",
    caption: "Shuruaat chhoti ho sakti hai, yaadein nahi.",
    media: "",
    visible: true
  }
];

/* ============================================================
   4. OUR PEOPLE — EDIT TEAM MEMBERS HERE
   Group people under whichever categories apply. Do not invent real
   names — replace "Member Name" with actual names when ready, and set
   visible:false to hide anyone not ready to be shown yet.
   ============================================================ */
const PEOPLE = [
  {
    group: "Mandal Members",
    members: [
      { name: "Member Name", role: "Mandal Member", image: "", visible: true },
      { name: "Member Name", role: "Mandal Member", image: "", visible: true }
    ]
  },
  {
    group: "Decoration Team",
    members: [
      { name: "Member Name", role: "Decoration", image: "", visible: true }
    ]
  },
  {
    group: "Aarti Team",
    members: [
      { name: "Member Name", role: "Aarti", image: "", visible: true }
    ]
  },
  {
    group: "Prasadam Team",
    members: [
      { name: "Member Name", role: "Prasadam", image: "", visible: true }
    ]
  },
  {
    group: "Volunteers",
    members: [
      { name: "Member Name", role: "Volunteer", image: "", visible: true },
      { name: "Member Name", role: "Volunteer", image: "", visible: true }
    ]
  }
];

/* ============================================================
   5. LADDU AUCTION — EDIT HERE
   Set enabled:true to make the section appear automatically near the
   end of the site. No bidding backend is wired up — this is a frontend
   display only; connect a real backend later using this same config shape.
   ============================================================ */
const AUCTION_CONFIG = {
  enabled: false,
  title: "Laddu Auction",
  startingBid: 100,
  currentBid: 0,
  endDate: "", // "YYYY-MM-DD HH:MM"
  description: ""
};

/* ============================================================
   6. DONATION — EDIT HERE
   Set enabled:true to make the donation section appear automatically.
   Only upiId is required for the QR code and payment link to work.
   ============================================================ */
const DONATION_CONFIG = {
  enabled: false,
  upiId: "",              // e.g. "mandalname@upi"
  merchantName: "Bal Ganesh Mitra Mandal",
  phoneNumber: "",         // used to build the payment reference/note
  notePrefix: "DN"
};

/* ============================================================
   7. UTILITIES
   ============================================================ */
function qs(sel, ctx){ return (ctx || document).querySelector(sel); }
function qsa(sel, ctx){ return Array.from((ctx || document).querySelectorAll(sel)); }
function pad2(n){ return String(n).padStart(2, "0"); }

function escapeHtml(str){
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

/** Returns an <img> tag if a path is given, otherwise a tasteful "Add Photo" placeholder. */
function mediaOrPlaceholder(path, alt, label){
  if (path && String(path).trim() !== "") {
    return `<img src="${escapeHtml(path)}" alt="${escapeHtml(alt || "")}" loading="lazy" />`;
  }
  return `<div class="media-placeholder">${escapeHtml(label || "Add Photo")}</div>`;
}

function eventDateTime(ev){
  return new Date(`${ev.date}T${ev.time || "00:00"}:00`);
}

function isSameDay(a, b){
  return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
}

function getEventStatus(ev, now){
  const dt = eventDateTime(ev);
  if (isSameDay(dt, now)) return "today";
  return dt.getTime() < now.getTime() ? "completed" : "upcoming";
}

function formatDayLabel(dateStr){
  const d = new Date(`${dateStr}T00:00:00`);
  return {
    dayNum: d.getDate(),
    monShort: d.toLocaleDateString("en-US", { month: "short" }).toUpperCase(),
    weekday: d.toLocaleDateString("en-US", { weekday: "long" })
  };
}

function formatTime12(timeStr){
  if (!timeStr) return "";
  const [h, m] = timeStr.split(":").map(Number);
  const period = h >= 12 ? "PM" : "AM";
  const h12 = ((h + 11) % 12) + 1;
  return `${h12}:${pad2(m)} ${period}`;
}

/* ============================================================
   8a. SEO META (uses SITE_CONFIG so title/description stay in sync)
   ============================================================ */
function applySeo(){
  document.title = `${SITE_CONFIG.mandalName} | Ganesh Utsav ${SITE_CONFIG.year}`;
}

/* ============================================================
   8b. NAVBAR
   ============================================================ */
function initNavbar(){
  const navbar = qs("#navbar");
  const toggle = qs("#navToggle");
  const mobileMenu = qs("#mobileMenu");

  window.addEventListener("scroll", () => {
    navbar.classList.toggle("is-scrolled", window.scrollY > 12);
  }, { passive: true });

  function closeMenu(){
    mobileMenu.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open menu");
  }
  function openMenu(){
    mobileMenu.hidden = false;
    toggle.setAttribute("aria-expanded", "true");
    toggle.setAttribute("aria-label", "Close menu");
  }

  toggle.addEventListener("click", () => {
    if (mobileMenu.hidden) openMenu(); else closeMenu();
  });

  qsa("a", mobileMenu).forEach(a => a.addEventListener("click", closeMenu));

  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && !mobileMenu.hidden) closeMenu();
  });

  // Hide the Auction nav item entirely when the auction is disabled.
  if (!AUCTION_CONFIG.enabled) {
    const link = qs("#navAuctionLink");
    const linkMobile = qs("#navAuctionLinkMobile");
    if (link) link.remove();
    if (linkMobile) linkMobile.remove();
  }
}

/* ============================================================
   8c. HERO
   ============================================================ */
function renderHero(){
  qs("#heroPhoto").innerHTML = mediaOrPlaceholder(SITE_CONFIG.heroImage, SITE_CONFIG.heroImageAlt, "Add Bappa's Photo");
}

/* ============================================================
   8d. STATUS / COUNTDOWN
   ============================================================ */
function initCountdown(){
  const { date, time, label, note } = SITE_CONFIG.agaman;
  const target = new Date(`${date}T${time || "00:00"}:00`);
  const { weekday } = formatDayLabel(date);
  const { dayNum, monShort } = formatDayLabel(date);

  qs("#statusLabel").textContent = label || "Bappa Aagman";
  qs("#statusDate").textContent = `${weekday} \u00b7 ${dayNum} ${monShort.charAt(0)}${monShort.slice(1).toLowerCase()}`;
  qs("#statusNote").textContent = note || "";

  function tick(){
    const now = new Date();
    const diff = target.getTime() - now.getTime();
    const countdownEl = qs("#countdown");
    const passedEl = qs("#statusPassed");

    if (diff <= 0) {
      countdownEl.hidden = true;
      passedEl.hidden = false;
      return;
    }
    countdownEl.hidden = false;
    passedEl.hidden = true;

    const totalSecs = Math.floor(diff / 1000);
    const days = Math.floor(totalSecs / 86400);
    const hours = Math.floor((totalSecs % 86400) / 3600);
    const mins = Math.floor((totalSecs % 3600) / 60);
    const secs = totalSecs % 60;

    qs("#cdDays").textContent = pad2(days);
    qs("#cdHours").textContent = pad2(hours);
    qs("#cdMins").textContent = pad2(mins);
    qs("#cdSecs").textContent = pad2(secs);
  }

  tick();
  setInterval(tick, 1000);
}

/* ============================================================
   8e. UTSAV JOURNEY — TIMELINE + UP NEXT
   ============================================================ */
function renderUpNext(){
  const now = new Date();
  const visible = DAILY_SCHEDULE.filter(ev => ev.visible);
  const upcoming = visible
    .filter(ev => eventDateTime(ev).getTime() >= now.getTime())
    .sort((a, b) => eventDateTime(a) - eventDateTime(b));

  const container = qs("#upNext");

  if (upcoming.length === 0) {
    if (visible.length === 0) { container.innerHTML = ""; return; }
    container.innerHTML = `
      <div class="up-next__card">
        <div>
          <div class="up-next__eyebrow">Utsav</div>
          <div class="up-next__title">Yeh saal ki yaadein ab sambhal kar rakhi hain</div>
        </div>
      </div>`;
    return;
  }

  const ev = upcoming[0];
  const { weekday, dayNum, monShort } = formatDayLabel(ev.date);
  container.innerHTML = `
    <div class="up-next__card">
      <div>
        <div class="up-next__eyebrow">Up Next</div>
        <div class="up-next__title">${escapeHtml(ev.title)}</div>
      </div>
      <div class="up-next__when">${weekday} &middot; ${dayNum} ${monShort}<br />${formatTime12(ev.time)}</div>
    </div>`;
}

function renderTimeline(){
  const now = new Date();
  const visible = DAILY_SCHEDULE.filter(ev => ev.visible).sort((a, b) => eventDateTime(a) - eventDateTime(b));
  const list = qs("#timeline");

  if (visible.length === 0) {
    list.innerHTML = `<p class="memories__empty">Utsav ki tafseel jald hi yahan aayegi.</p>`;
    return;
  }

  list.innerHTML = visible.map(ev => {
    const { dayNum, monShort } = formatDayLabel(ev.date);
    const status = getEventStatus(ev, now);
    const statusLabel = status === "today" ? "Today" : status === "completed" ? "Completed" : "Upcoming";
    return `
      <li class="timeline__item">
        <div class="timeline__stamp">
          <span class="day-num">${dayNum}</span>
          <span class="day-mon">${monShort}</span>
        </div>
        <div class="timeline__body">
          <div class="timeline__top">
            <span class="timeline__title">${escapeHtml(ev.title)}</span>
            <span class="timeline__time">${formatTime12(ev.time)}</span>
          </div>
          <p class="timeline__desc">${escapeHtml(ev.description || "")}</p>
          <div class="timeline__media">${mediaOrPlaceholder(ev.image, ev.title, "Add Photo")}</div>
          <span class="status-badge status-badge--${status}">${statusLabel}</span>
        </div>
      </li>`;
  }).join("");
}

/* ============================================================
   8f. MEMORIES GALLERY + LIGHTBOX
   ============================================================ */
let activeMemoryFilter = "all";

function renderMemories(){
  const grid = qs("#memoriesGrid");
  const visible = MEMORIES.filter(m => m.visible);
  const filtered = activeMemoryFilter === "all"
    ? visible
    : visible.filter(m => (m.displayCategory || m.category) === activeMemoryFilter);

  if (filtered.length === 0) {
    grid.innerHTML = `<p class="memories__empty">Yaadein jald hi yahan aayengi — utsav abhi shuru hua hai.</p>`;
    return;
  }

  grid.innerHTML = filtered.map((m, i) => `
    <button class="memory-card" type="button" data-memory-index="${MEMORIES.indexOf(m)}" aria-label="Open ${escapeHtml(m.title || 'memory')}">
      <span class="memory-card__media">
        ${m.type === "video" && m.media
          ? `<video src="${escapeHtml(m.media)}" muted playsinline></video>`
          : mediaOrPlaceholder(m.media, m.title, "Add Photo")}
      </span>
      ${m.type === "video" ? `<span class="memory-card__reel-icon" aria-hidden="true">&#9654;</span>` : ""}
      <span class="memory-card__info">
        <span class="memory-card__caption">${escapeHtml(m.caption || "")}</span>
        <span class="memory-card__meta">${escapeHtml(m.title || "")} &middot; ${escapeHtml(m.date || "")}</span>
      </span>
    </button>
  `).join("");
}

function initMemoryFilters(){
  const filterBar = qs("#memoryFilters");
  filterBar.addEventListener("click", e => {
    const btn = e.target.closest(".filter-btn");
    if (!btn) return;
    qsa(".filter-btn", filterBar).forEach(b => b.classList.remove("is-active"));
    btn.classList.add("is-active");
    activeMemoryFilter = btn.dataset.filter;
    renderMemories();
  });
}

function initLightbox(){
  const lightbox = qs("#lightbox");
  const content = qs("#lightboxContent");
  const caption = qs("#lightboxCaption");
  const closeBtn = qs("#lightboxClose");

  qs("#memoriesGrid").addEventListener("click", e => {
    const card = e.target.closest(".memory-card");
    if (!card) return;
    const m = MEMORIES[Number(card.dataset.memoryIndex)];
    if (!m) return;

    if (m.type === "video" && m.media) {
      content.innerHTML = `<video src="${escapeHtml(m.media)}" controls muted playsinline autoplay></video>`;
    } else {
      content.innerHTML = mediaOrPlaceholder(m.media, m.title, "Add Photo");
    }
    caption.textContent = [m.title, m.caption].filter(Boolean).join(" — ");
    lightbox.hidden = false;
    closeBtn.focus();
  });

  function close(){
    lightbox.hidden = true;
    content.innerHTML = "";
  }
  closeBtn.addEventListener("click", close);
  lightbox.addEventListener("click", e => { if (e.target === lightbox) close(); });
  document.addEventListener("keydown", e => { if (e.key === "Escape" && !lightbox.hidden) close(); });
}

/* ============================================================
   8g. THIS YEAR
   ============================================================ */
function renderFirstYear(){
  qs("#groupPhoto").innerHTML = mediaOrPlaceholder(SITE_CONFIG.groupPhoto, SITE_CONFIG.groupPhotoAlt, "Add Group Photo");
}

/* ============================================================
   8h. OUR PEOPLE
   ============================================================ */
function renderPeople(){
  const container = qs("#peopleGroups");
  container.innerHTML = PEOPLE.map(group => {
    const visibleMembers = group.members.filter(p => p.visible);
    if (visibleMembers.length === 0) return "";
    return `
      <div class="people__group">
        <h3 class="people__group-title">${escapeHtml(group.group)}</h3>
        <div class="people__grid">
          ${visibleMembers.map(p => `
            <div class="person-card">
              <div class="person-card__photo">${mediaOrPlaceholder(p.image, p.name, "Add Photo")}</div>
              <div class="person-card__name">${escapeHtml(p.name)}</div>
              <div class="person-card__role">${escapeHtml(p.role)}</div>
            </div>`).join("")}
        </div>
      </div>`;
  }).join("");
}

/* ============================================================
   8i. EVENTS (reuses DAILY_SCHEDULE — single source of truth)
   ============================================================ */
function renderEvents(){
  const visible = DAILY_SCHEDULE.filter(ev => ev.visible).sort((a, b) => eventDateTime(a) - eventDateTime(b));
  const list = qs("#eventsList");

  if (visible.length === 0) {
    list.innerHTML = `<p class="memories__empty">Events jald hi confirm honge.</p>`;
    return;
  }

  list.innerHTML = visible.map(ev => {
    const { dayNum, monShort } = formatDayLabel(ev.date);
    return `
      <div class="event-card">
        <div class="event-card__date">
          <span class="num">${dayNum}</span>
          <span class="mon">${monShort}</span>
        </div>
        <div class="event-card__divider" aria-hidden="true"></div>
        <div class="event-card__body">
          <div class="event-card__title">${escapeHtml(ev.title)}</div>
          <div class="event-card__meta">${formatTime12(ev.time)} &middot; ${escapeHtml(SITE_CONFIG.location.name)}</div>
          ${ev.description ? `<div class="event-card__desc">${escapeHtml(ev.description)}</div>` : ""}
        </div>
      </div>`;
  }).join("");
}

/* ============================================================
   8j. LOCATION
   ============================================================ */
function renderLocation(){
  qs("#locationName").textContent = SITE_CONFIG.location.name;
  qs("#locationAddress").textContent = SITE_CONFIG.location.address || "Address coming soon.";

  const directionsBtn = qs("#locationDirections");
  if (SITE_CONFIG.location.mapsUrl) {
    directionsBtn.href = SITE_CONFIG.location.mapsUrl;
  } else {
    directionsBtn.href = "#location";
    directionsBtn.setAttribute("aria-disabled", "true");
  }

  qs("#locationMap").innerHTML = mediaOrPlaceholder("", "Map", "Add Maps Link");
}

/* ============================================================
   8k. SOCIAL
   ============================================================ */
function renderSocial(){
  const url = SITE_CONFIG.social.instagram;
  const link = qs("#instagramLink");
  const footerLink = qs("#footerInstagram");

  if (url) {
    link.href = url;
    footerLink.href = url;
  } else {
    link.setAttribute("aria-disabled", "true");
    link.href = "#social";
    footerLink.hidden = true;
  }

  const reels = SITE_CONFIG.social.reels || [];
  const grid = qs("#socialGrid");
  grid.innerHTML = reels.map(r => `
    <a class="social__tile" href="${escapeHtml(r.url || url || "#")}" target="_blank" rel="noopener">
      ${mediaOrPlaceholder(r.media, "Instagram reel", "Add Reel")}
    </a>`).join("");
}

/* ============================================================
   8l. LADDU AUCTION — only mounted when enabled
   ============================================================ */
function renderAuction(){
  if (!AUCTION_CONFIG.enabled) return;

  const mount = qs("#auctionMount");
  const bid = AUCTION_CONFIG.currentBid > 0 ? AUCTION_CONFIG.currentBid : AUCTION_CONFIG.startingBid;

  mount.innerHTML = `
    <section id="auction" class="auction">
      <div class="section-head" data-reveal>
        <h2>Bappa Ka Prasad, Yaadon Ka Hissa.</h2>
        <p>${escapeHtml(AUCTION_CONFIG.title || "Laddu Auction")}</p>
      </div>
      <div class="auction__card" data-reveal>
        <div class="auction__eyebrow">Laddu Auction</div>
        <div class="auction__title">${escapeHtml(AUCTION_CONFIG.title || "Laddu Auction")}</div>
        ${AUCTION_CONFIG.description ? `<p class="auction__desc">${escapeHtml(AUCTION_CONFIG.description)}</p>` : ""}
        <div class="auction__bids">
          <div>
            <div class="auction__bid-label">Starting Bid</div>
            <div class="auction__bid-value">&#8377;${AUCTION_CONFIG.startingBid}</div>
          </div>
          <div>
            <div class="auction__bid-label">Current Bid</div>
            <div class="auction__bid-value">&#8377;${bid}</div>
          </div>
        </div>
        ${AUCTION_CONFIG.endDate ? `<div class="auction__end">Ends ${escapeHtml(AUCTION_CONFIG.endDate)}</div>` : ""}
      </div>
    </section>`;

  initScrollRevealFor(mount);
}

/* ============================================================
   8m. DONATION — only mounted when enabled
   ============================================================ */
function generateDonationNote(){
  const now = new Date();
  const hhmm = `${pad2(now.getHours())}${pad2(now.getMinutes())}`;
  const phone = (DONATION_CONFIG.phoneNumber || "").replace(/\D/g, "");
  return `${phone}${DONATION_CONFIG.notePrefix || "DN"}${hhmm}`;
}

function generateUpiUrl(amount){
  const note = generateDonationNote();
  const params = new URLSearchParams({
    pa: DONATION_CONFIG.upiId,
    pn: DONATION_CONFIG.merchantName || SITE_CONFIG.mandalName,
    am: String(amount),
    cu: "INR",
    tn: note
  });
  return { url: `upi://pay?${params.toString()}`, note };
}

function renderDonation(){
  if (!DONATION_CONFIG.enabled || !DONATION_CONFIG.upiId) return;

  const mount = qs("#donationMount");
  mount.innerHTML = `
    <section id="donation" class="donation">
      <div class="section-head" data-reveal>
        <h2>Donate To Bappa</h2>
        <p>Scan &amp; donate — every contribution becomes part of this year's utsav.</p>
      </div>
      <div class="donation__card" data-reveal>
        <div class="donation__qr" id="donationQr"></div>
        <div class="donation__upi">UPI ID: ${escapeHtml(DONATION_CONFIG.upiId)}</div>
        <div class="donation__amounts" id="donationAmounts">
          <button class="amount-btn" data-amount="100">&#8377;100</button>
          <button class="amount-btn" data-amount="500">&#8377;500</button>
          <button class="amount-btn" data-amount="1000">&#8377;1000</button>
          <button class="amount-btn" data-amount="custom">Custom</button>
        </div>
        <div class="donation__custom" id="donationCustomWrap" hidden>
          <input type="number" min="1" id="donationCustomInput" placeholder="Enter amount" inputmode="numeric" />
        </div>
        <div class="donation__ref">
          <span>Reference: <code id="donationRef"></code></span>
          <button class="donation__copy" id="donationCopy" type="button">Copy</button>
        </div>
        <div class="donation__actions">
          <a href="#" id="donationOpenApp" class="btn btn--primary">Open UPI App</a>
        </div>
        <p class="donation__disclaimer">Please complete the payment in your UPI app. This page does not process or verify payments.</p>
      </div>
    </section>`;

  initScrollRevealFor(mount);
  initDonationInteractions();
}

function initDonationInteractions(){
  let amount = 100;
  let qrInstance = null;

  function refresh(){
    const { url, note } = generateUpiUrl(amount);
    qs("#donationRef").textContent = note;
    qs("#donationOpenApp").href = url;

    const qrHolder = qs("#donationQr");
    qrHolder.innerHTML = "";
    if (window.QRCode) {
      qrInstance = new QRCode(qrHolder, {
        text: url,
        width: 180,
        height: 180,
        colorDark: "#26201B",
        colorLight: "#FFFFFF"
      });
    } else {
      qrHolder.innerHTML = `<div class="media-placeholder">QR loading&hellip;</div>`;
    }
  }

  qs("#donationAmounts").addEventListener("click", e => {
    const btn = e.target.closest(".amount-btn");
    if (!btn) return;
    qsa(".amount-btn", qs("#donationAmounts")).forEach(b => b.classList.remove("is-active"));
    btn.classList.add("is-active");

    const customWrap = qs("#donationCustomWrap");
    if (btn.dataset.amount === "custom") {
      customWrap.hidden = false;
      qs("#donationCustomInput").focus();
      return;
    }
    customWrap.hidden = true;
    amount = Number(btn.dataset.amount);
    refresh();
  });

  qs("#donationCustomInput").addEventListener("input", e => {
    const val = Number(e.target.value);
    if (val > 0) { amount = val; refresh(); }
  });

  qs("#donationCopy").addEventListener("click", () => {
    const ref = qs("#donationRef").textContent;
    navigator.clipboard?.writeText(ref).then(() => {
      const btn = qs("#donationCopy");
      const original = btn.textContent;
      btn.textContent = "Copied";
      setTimeout(() => { btn.textContent = original; }, 1500);
    });
  });

  qs('.amount-btn[data-amount="100"]').classList.add("is-active");
  refresh();
}

/* ============================================================
   8n. FOOTER
   ============================================================ */
function renderFooter(){
  qs("#footerYear").textContent = SITE_CONFIG.year;
}

/* ============================================================
   8o. SCROLL REVEAL
   ============================================================ */
function initScrollRevealFor(root){
  const targets = qsa("[data-reveal]", root);
  if (!targets.length) return;

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReduced) {
    targets.forEach(el => el.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  targets.forEach(el => observer.observe(el));
}

/* ============================================================
   9. INIT
   ============================================================ */
function init(){
  applySeo();
  initNavbar();
  renderHero();
  initCountdown();
  renderUpNext();
  renderTimeline();
  renderMemories();
  initMemoryFilters();
  initLightbox();
  renderFirstYear();
  renderPeople();
  renderEvents();
  renderLocation();
  renderSocial();
  renderAuction();
  renderDonation();
  renderFooter();
  initScrollRevealFor(document);
}

document.addEventListener("DOMContentLoaded", init);
