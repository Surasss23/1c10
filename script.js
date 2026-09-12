/* =========================================================
   BAL GANESH MITRA MANDAL — CONFIG + DATA
   =========================================================
   IMPORTANT:
   Normally, you only need to edit the sections marked
   "EDIT HERE". Everything below that is website logic.
   ========================================================= */


// =========================================================
// SITE CONFIGURATION
// EDIT HERE
// =========================================================

const SITE_CONFIG = {

  // Mandal name
  mandalName: "Bal Ganesh Mitra Mandal",

  // Current year
  year: 2026,

  // Main Bappa image
  // Example: "assets/hero.jpg"
  heroImage: "",

  // Group photo
  // Example: "assets/group.jpg"
  groupPhoto: "",

  // Location
  location: {
    name: "Bal Ganesh Mitra Mandal",

    // Add your complete address here
    address: "Address will be added here.",

    // Add your Google Maps URL here
    mapsUrl: ""
  },

  // Social links
  social: {
    // Add your Instagram profile URL here
    instagram: ""
  },

  // Bappa Aagman
  agaman: {

    // Date: YYYY-MM-DD
    date: "2026-09-13",

    // Time: HH:MM
    // Leave empty if exact time is not confirmed.
    time: "18:00"
  }
};


// =========================================================
// DAILY SCHEDULE
// EDIT HERE
// =========================================================
//
// You can add, remove or edit any day.
//
// Fields:
//
// date        = YYYY-MM-DD
// day         = day name
// title       = event title
// time        = event time
// description = short description
// image       = image path
// status      = planned / live / done
// visible     = true / false
//
// Example image:
// "assets/events/aagman.jpg"
// =========================================================

const DAILY_SCHEDULE = [

  {
    date: "2026-09-13",
    day: "SUNDAY",
    title: "BAPPA AAGMAN",
    time: "SHAM KO",
    description: "Pehli dastak, pehli khushi.",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-14",
    day: "MONDAY",
    title: "DAY 2",
    time: "",
    description: "Har subah Bappa ke naam.",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-15",
    day: "TUESDAY",
    title: "DAY 3",
    time: "",
    description: "",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-16",
    day: "WEDNESDAY",
    title: "DAY 4",
    time: "",
    description: "",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-17",
    day: "THURSDAY",
    title: "ANNAM PRASADAM",
    time: "",
    description: "Prasad ka swaad, Bappa ka aashirwad.",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-18",
    day: "FRIDAY",
    title: "DAY 6",
    time: "",
    description: "",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-19",
    day: "SATURDAY",
    title: "DAY 7",
    time: "",
    description: "",
    image: "",
    status: "planned",
    visible: true
  },

  {
    date: "2026-09-20",
    day: "SUNDAY",
    title: "VISARJAN",
    time: "",
    description: "",
    image: "",
    status: "planned",
    visible: true
  }

];


// =========================================================
// MEMORIES
// EDIT HERE
// =========================================================
//
// type:
// "photo" = image
// "video" = reel/video
//
// category:
// "photos"
// "reels"
// "aarti"
// "events"
// "behind"
//
// Example:
//
// {
//   type: "photo",
//   category: "events",
//   date: "13 Sep 2026",
//   title: "Bappa Aagman",
//   caption: "Bappa aaye, khushiyan laaye.",
//   media: "assets/memories/aagman-01.jpg"
// }
//
// =========================================================

const MEMORIES = [

  {
    type: "photo",
    category: "photos",
    date: "13 Sep 2026",
    title: "Bappa Aagman",
    caption: "Shuruaat chhoti ho sakti hai, yaadein nahi.",
    media: ""
  },

  {
    type: "photo",
    category: "aarti",
    date: "2026",
    title: "Aarti Moments",
    caption: "Har aarti mein ek saath.",
    media: ""
  },

  {
    type: "photo",
    category: "events",
    date: "2026",
    title: "Utsav Moments",
    caption: "Bappa aaye, khushiyan laaye.",
    media: ""
  },

  {
    type: "video",
    category: "reels",
    date: "2026",
    title: "Festival Reel",
    caption: "Ek pal, ek kahaani.",
    media: ""
  },

  {
    type: "photo",
    category: "behind",
    date: "2026",
    title: "Behind The Scenes",
    caption: "Bappa ke peeche, hum sab.",
    media: ""
  }

];


// =========================================================
// PEOPLE
// EDIT HERE
// =========================================================
//
// Set visible:false to hide a member.
//
// =========================================================

const PEOPLE = [

  {
    name: "Member Name",
    role: "Volunteer",
    image: "",
    visible: true
  },

  {
    name: "Member Name",
    role: "Decoration Team",
    image: "",
    visible: true
  },

  {
    name: "Member Name",
    role: "Aarti Team",
    image: "",
    visible: true
  },

  {
    name: "Member Name",
    role: "Prasadam Team",
    image: "",
    visible: true
  },

  {
    name: "Member Name",
    role: "Event Team",
    image: "",
    visible: true
  },

  {
    name: "Member Name",
    role: "Mandal Member",
    image: "",
    visible: true
  }

];


// =========================================================
// LADDU AUCTION
// EDIT HERE
// =========================================================
//
// enabled:false
// = auction completely hidden
//
// enabled:true
// = auction automatically appears
//
// NOTE:
// This is frontend-only.
// Real bidding requires a backend.
// =========================================================

const AUCTION_CONFIG = {

  enabled: false,

  title: "Laddu Auction",

  startingBid: 100,

  currentBid: 0,

  endDate: "",

  description: "Bappa ka prasad, yaadon ka hissa."

};


// =========================================================
// DONATION
// EDIT HERE ONLY WHEN YOU ARE READY
// =========================================================
//
// enabled:false
// = entire donation section hidden
//
// enabled:true
// = donation section appears
//
// IMPORTANT:
// Do not put someone else's UPI ID or phone number here.
// =========================================================

const DONATION_CONFIG = {

  enabled: false,

  // Example:
  // "example@upi"
  upiId: "",

  merchantName: "Bal Ganesh Mitra Mandal",

  // Example:
  // "9876543210"
  phoneNumber: "",

  // Donation reference prefix
  notePrefix: "DN"

};


// =========================================================
// WEBSITE LOGIC
// DO NOT NORMALLY EDIT BELOW THIS LINE
// =========================================================


// ---------------------------------------------------------
// BASIC HELPERS
// ---------------------------------------------------------

const $ = (selector, root = document) =>
  root.querySelector(selector);

const $$ = (selector, root = document) =>
  [...root.querySelectorAll(selector)];


// Prevent HTML injection when displaying config/data
function esc(value) {

  return String(value ?? "").replace(
    /[&<>"']/g,

    character => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#039;"
    }[character])
  );
}


// Placeholder
function placeholderHTML(label = "ADD PHOTO") {

  return `<span>${esc(label)}</span>`;
}


// Background image helper
function mediaStyle(path) {

  if (!path) return "";

  return `style="background-image:url('${String(path)
    .replace(/'/g, "%27")}')"`;
}


// Format date
function formatDate(dateString) {

  const date = new Date(`${dateString}T00:00:00`);

  if (Number.isNaN(date.getTime())) {
    return dateString;
  }

  return date
    .toLocaleDateString("en-IN", {
      day: "2-digit",
      month: "short"
    })
    .toUpperCase();
}


// Full date
function formatFullDate(dateString) {

  const date = new Date(`${dateString}T00:00:00`);

  if (Number.isNaN(date.getTime())) {
    return dateString;
  }

  return date.toLocaleDateString("en-IN", {
    weekday: "long",
    day: "numeric",
    month: "long"
  });
}


// Convert event to Date
function parseEventDate(event) {

  const time =
    /^\d{2}:\d{2}$/.test(event.time || "")
      ? event.time
      : "23:59";

  return new Date(`${event.date}T${time}:00`);
}


// Determine event status
function getStatus(event) {

  const eventTime = parseEventDate(event).getTime();

  const now = Date.now();

  if (eventTime < now) {
    return "done";
  }

  if (event.status === "live") {
    return "live";
  }

  return "planned";
}


// Only allow normal external URLs
function safeExternal(url) {

  return /^https?:\/\//i.test(url || "")
    ? url
    : "#";
}


// =========================================================
// SITE CONFIGURATION SETUP
// =========================================================

function setupConfig() {

  document.title =
    `${SITE_CONFIG.mandalName} | Ganesh Utsav ${SITE_CONFIG.year}`;


  // Year
  $("#heroYear").textContent =
    SITE_CONFIG.year;

  $("#footerYear").textContent =
    SITE_CONFIG.year;


  // Location
  $("#locationName").textContent =
    SITE_CONFIG.location.name ||
    SITE_CONFIG.mandalName;

  $("#locationAddress").textContent =
    SITE_CONFIG.location.address ||
    "Address will be added here.";

  $("#directionsLink").href =
    safeExternal(SITE_CONFIG.location.mapsUrl);


  // Instagram
  $("#instagramLink").href =
    safeExternal(SITE_CONFIG.social.instagram);

  $("#footerInstagram").href =
    safeExternal(SITE_CONFIG.social.instagram);


  $("#footerLocation").textContent =
    SITE_CONFIG.location.name ||
    "Location";


  // Hero image
  const hero =
    $("#heroMedia");

  if (SITE_CONFIG.heroImage) {

    hero.classList.add("has-media");

    hero.style.backgroundImage =
      `url("${SITE_CONFIG.heroImage}")`;
  }


  // Group photo
  const group =
    $(".group-media");

  if (SITE_CONFIG.groupPhoto) {

    group.classList.add("has-media");

    group.style.backgroundImage =
      `url("${SITE_CONFIG.groupPhoto}")`;
  }


  // SEO
  const ogTitle =
    document.querySelector(
      'meta[property="og:title"]'
    );

  if (ogTitle) {
    ogTitle.content = document.title;
  }


  const ogImage =
    document.querySelector(
      'meta[property="og:image"]'
    );

  if (ogImage) {
    ogImage.content =
      SITE_CONFIG.heroImage || "";
  }

}


// =========================================================
// DAILY SCHEDULE
// =========================================================

function renderDaily() {

  const root =
    $("#dailySchedule");

  const events =
    DAILY_SCHEDULE.filter(
      event => event.visible !== false
    );


  if (!events.length) {

    root.innerHTML = `
      <p class="body-copy">
        Utsav schedule will be added soon.
      </p>
    `;

    return;
  }


  root.innerHTML =
    events.map(event => {

      const status =
        getStatus(event);

      const statusLabel =
        status === "done"
          ? "COMPLETED"
          : status === "live"
            ? "HAPPENING NOW"
            : "UPCOMING";


      return `

        <article class="timeline-item reveal">

          <span
            class="timeline-dot"
            aria-hidden="true">
          </span>


          <div class="timeline-date">

            <strong>
              ${esc(formatDate(event.date))}
            </strong>

            <span>
              ${esc(event.day)}
            </span>

          </div>


          <div class="timeline-main">

            <div>

              <h3>
                ${esc(event.title)}
              </h3>


              ${
                event.time
                  ? `
                    <span class="event-time">
                      ${esc(event.time)}
                    </span>
                  `
                  : ""
              }


              <p>
                ${esc(event.description || "")}
              </p>


              <span class="event-status ${status}">
                ${statusLabel}
              </span>

            </div>


            <div
              class="media-placeholder timeline-media ${
                event.image
                  ? "has-media"
                  : ""
              }"
              ${mediaStyle(event.image)}
            >

              ${placeholderHTML("ADD PHOTO")}

            </div>

          </div>

        </article>

      `;

    }).join("");


  observeReveals();

  renderUpNext(events);
}


// =========================================================
// UP NEXT
// =========================================================

function renderUpNext(
  events =
    DAILY_SCHEDULE.filter(
      event => event.visible !== false
    )
) {

  const next =
    events

      .map(event => ({
        event,
        date: parseEventDate(event)
      }))

      .filter(item =>
        item.date.getTime() > Date.now()
      )

      .sort(
        (a, b) =>
          a.date - b.date
      )[0];


  const root =
    $("#upNext");


  if (!next) {

    root.innerHTML = `
      <span class="eyebrow">
        UP NEXT
      </span>

      <strong>
        Utsav memories in the making
      </strong>

      <span>
        Stay with Bappa
      </span>
    `;

    return;
  }


  const event =
    next.event;


  root.innerHTML = `

    <span class="eyebrow">
      UP NEXT
    </span>

    <strong>
      ${esc(event.title)}
    </strong>

    <span>
      ${esc(formatFullDate(event.date))}

      ${
        event.time
          ? ` • ${esc(event.time)}`
          : ""
      }

    </span>

  `;
}


// =========================================================
// MEMORY GALLERY
// =========================================================

function renderMemories(filter = "all") {

  const root =
    $("#memoryGrid");


  const items =
    MEMORIES.filter(
      memory =>
        filter === "all" ||
        memory.category === filter
    );


  if (!items.length) {

    root.innerHTML = `
      <p class="body-copy">
        Memories will appear here as the
        festival unfolds.
      </p>
    `;

    return;
  }


  root.innerHTML =

    items.map(memory => {

      const index =
        MEMORIES.indexOf(memory);


      return `

        <article
          class="memory-card reveal"
          data-memory-index="${index}"
          tabindex="0"
          role="button"
          aria-label="Open ${esc(memory.title)}"
        >

          <div
            class="
              memory-card-media
              ${memory.media ? "has-media" : ""}
            "
            ${mediaStyle(memory.media)}
          >

            ${placeholderHTML(
              memory.type === "video"
                ? "ADD REEL / VIDEO"
                : "ADD PHOTO"
            )}

          </div>


          <div class="memory-card-info">

            <strong>
              ${esc(memory.title)}
            </strong>

            <small>
              ${esc(memory.date)}

              ${
                memory.type === "video"
                  ? " • REEL"
                  : ""
              }

            </small>


            <p>
              ${esc(memory.caption)}
            </p>

          </div>

        </article>

      `;

    }).join("");


  observeReveals();
}


// =========================================================
// MEMORY FILTERS
// =========================================================

function setupMemoryFilters() {

  const labels = {

    all: "ALL",

    photos: "PHOTOS",

    reels: "REELS",

    aarti: "AARTI",

    events: "EVENTS",

    behind: "BEHIND THE SCENES"

  };


  const root =
    $("#memoryFilters");


  root.innerHTML =

    Object.entries(labels)

      .map(
        ([key, label]) => `

          <button
            type="button"
            data-filter="${key}"
            class="${key === "all" ? "active" : ""}"
          >
            ${label}
          </button>

        `
      )

      .join("");


  root.addEventListener(
    "click",
    event => {

      const button =
        event.target.closest("button");


      if (!button) return;


      $$(".filter-row button")
        .forEach(
          btn =>
            btn.classList.remove("active")
        );


      button.classList.add("active");


      renderMemories(
        button.dataset.filter
      );

    }
  );

}


// =========================================================
// PEOPLE
// =========================================================

function renderPeople() {

  const root =
    $("#peopleGrid");


  const people =
    PEOPLE.filter(
      person =>
        person.visible !== false
    );


  if (!people.length) {

    root.innerHTML = `
      <p class="body-copy">
        The people behind the festival
        will be added here.
      </p>
    `;

    return;
  }


  root.innerHTML =

    people.map(person => `

      <article class="person-card reveal">

        <div
          class="
            media-placeholder
            person-media
            ${person.image ? "has-media" : ""}
          "
          ${mediaStyle(person.image)}
        >

          ${placeholderHTML("ADD PORTRAIT")}

        </div>


        <div class="person-info">

          <strong>
            ${esc(person.name)}
          </strong>

          <span>
            ${esc(person.role)}
          </span>

        </div>

      </article>

    `).join("");


  observeReveals();
}


// =========================================================
// EVENTS
// =========================================================

function renderEvents() {

  const root =
    $("#eventList");


  const events =
    DAILY_SCHEDULE.filter(
      event =>
        event.visible !== false
    );


  if (!events.length) {

    root.innerHTML = `
      <p class="body-copy">
        Events will be announced soon.
      </p>
    `;

    return;
  }


  root.innerHTML =

    events.map(event => `

      <article class="event-row reveal">

        <div class="event-row-date">

          ${esc(formatDate(event.date))}

          <br>

          <span>
            ${esc(event.day)}
          </span>

        </div>


        <div>

          <h3>
            ${esc(event.title)}
          </h3>

          <p>
            ${
              esc(
                event.description ||
                "Details will be updated."
              )
            }
          </p>

        </div>


        <div class="event-row-time">

          ${esc(
            event.time ||
            "TIME TBA"
          )}

        </div>

      </article>

    `).join("");


  observeReveals();
}


// =========================================================
// COUNTDOWN
// =========================================================

function setupCountdown() {

  const agamanEvent =
    DAILY_SCHEDULE.find(
      event =>
        event.date ===
        SITE_CONFIG.agaman.date
    );


  const title =
    agamanEvent?.title ||
    "Bappa Aagman";


  $("#momentTitle").textContent =
    title;


  const date =
    new Date(
      `${SITE_CONFIG.agaman.date}T00:00:00`
    );


  $("#momentDate").textContent =

    `${
      date
        .toLocaleDateString(
          "en-IN",
          { weekday: "long" }
        )
        .toUpperCase()
    } • ${
      formatDate(
        SITE_CONFIG.agaman.date
      )
    }`;


  $("#momentTime").textContent =

    SITE_CONFIG.agaman.time

      ? new Date(
          `1970-01-01T${SITE_CONFIG.agaman.time}`
        )
        .toLocaleTimeString(
          "en-IN",
          {
            hour: "numeric",
            minute: "2-digit"
          }
        )
        .toUpperCase()

      : "SHAM KO";


  function tick() {

    const target =
      new Date(
        `${SITE_CONFIG.agaman.date}T${
          SITE_CONFIG.agaman.time ||
          "18:00"
        }:00`
      );


    let difference =
      target.getTime() -
      Date.now();


    if (difference < 0) {
      difference = 0;
    }


    const days =
      Math.floor(
        difference / 86400000
      );


    difference %= 86400000;


    const hours =
      Math.floor(
        difference / 3600000
      );


    difference %= 3600000;


    const minutes =
      Math.floor(
        difference / 60000
      );


    difference %= 60000;


    const seconds =
      Math.floor(
        difference / 1000
      );


    $("#countDays").textContent =
      String(days).padStart(2, "0");


    $("#countHours").textContent =
      String(hours).padStart(2, "0");


    $("#countMinutes").textContent =
      String(minutes).padStart(2, "0");


    $("#countSeconds").textContent =
      String(seconds).padStart(2, "0");

  }


  tick();

  setInterval(
    tick,
    1000
  );

}


// =========================================================
// NAVIGATION
// =========================================================

function setupNav() {

  const header =
    $("#siteHeader");

  const toggle =
    $("#menuToggle");

  const menu =
    $("#siteMenu");


  window.addEventListener(
    "scroll",
    () => {

      header.classList.toggle(
        "scrolled",
        window.scrollY > 20
      );

    },
    { passive: true }
  );


  toggle.addEventListener(
    "click",
    () => {

      const open =
        menu.classList.toggle(
          "open"
        );


      toggle.setAttribute(
        "aria-expanded",
        String(open)
      );


      document.body.classList.toggle(
        "menu-open",
        open
      );

    }
  );


  menu.addEventListener(
    "click",
    event => {

      if (
        event.target.closest("a")
      ) {

        menu.classList.remove(
          "open"
        );


        toggle.setAttribute(
          "aria-expanded",
          "false"
        );


        document.body.classList.remove(
          "menu-open"
        );

      }

    }
  );

}


// =========================================================
// SCROLL REVEAL
// =========================================================

let revealObserver;


function observeReveals() {

  if (
    !("IntersectionObserver" in window)
  ) {

    $$(".reveal")
      .forEach(
        element =>
          element.classList.add(
            "visible"
          )
      );

    return;
  }


  if (!revealObserver) {

    revealObserver =
      new IntersectionObserver(

        entries => {

          entries.forEach(
            entry => {

              if (
                entry.isIntersecting
              ) {

                entry.target.classList.add(
                  "visible"
                );


                revealObserver.unobserve(
                  entry.target
                );

              }

            }
          );

        },

        {
          threshold: 0.08
        }

      );

  }


  $$(".reveal:not(.visible)")
    .forEach(
      element =>
        revealObserver.observe(
          element
        )
    );

}


// =========================================================
// LIGHTBOX
// =========================================================

let currentMemoryIndex = 0;


function openMemory(index) {

  const memory =
    MEMORIES[index];


  if (!memory) return;


  currentMemoryIndex =
    index;


  const root =
    $("#lightboxContent");


  let media;


  if (memory.media) {

    if (memory.type === "video") {

      media = `

        <video
          src="${esc(memory.media)}"
          controls
          playsinline
          preload="metadata"
        ></video>

      `;

    } else {

      media = `

        <img
          src="${esc(memory.media)}"
          alt="${esc(memory.title)}"
        >

      `;

    }

  } else {

    media = `

      <div
        class="media-placeholder"
        style="
          width:min(75vw,700px);
          height:60vh;
        "
      >

        ${placeholderHTML(
          memory.type === "video"
            ? "ADD REEL / VIDEO"
            : "ADD PHOTO"
        )}

      </div>

    `;

  }


  root.innerHTML = `

    ${media}

    <div class="lightbox-caption">

      <strong>
        ${esc(memory.title)}
      </strong>

      ·

      ${esc(memory.date)}

      <br>

      ${esc(memory.caption)}

    </div>

  `;


  $("#lightbox").hidden =
    false;


  document.body.classList.add(
    "menu-open"
  );


  $("#lightboxClose").focus();

}


function closeMemory() {

  $("#lightbox").hidden =
    true;


  document.body.classList.remove(
    "menu-open"
  );


  $("#lightboxContent").innerHTML =
    "";

}


function stepMemory(direction) {

  if (!MEMORIES.length) return;


  let nextIndex =
    currentMemoryIndex +
    direction;


  if (
    nextIndex < 0
  ) {

    nextIndex =
      MEMORIES.length - 1;

  }


  if (
    nextIndex >=
    MEMORIES.length
  ) {

    nextIndex = 0;

  }


  openMemory(
    nextIndex
  );

}


function setupLightbox() {

  const grid =
    $("#memoryGrid");


  grid.addEventListener(
    "click",
    event => {

      const card =
        event.target.closest(
          "[data-memory-index]"
        );


      if (!card) return;


      openMemory(
        Number(
          card.dataset.memoryIndex
        )
      );

    }
  );


  grid.addEventListener(
    "keydown",
    event => {

      const card =
        event.target.closest(
          "[data-memory-index]"
        );


      if (
        !card
      ) return;


      if (
        event.key === "Enter" ||
        event.key === " "
      ) {

        event.preventDefault();


        openMemory(
          Number(
            card.dataset.memoryIndex
          )
        );

      }

    }
  );


  $("#lightboxClose")
    .addEventListener(
      "click",
      closeMemory
    );


  $("#lightboxPrev")
    .addEventListener(
      "click",
      () =>
        stepMemory(-1)
    );


  $("#lightboxNext")
    .addEventListener(
      "click",
      () =>
        stepMemory(1)
    );


  $("#lightbox")
    .addEventListener(
      "click",
      event => {

        if (
          event.target.id ===
          "lightbox"
        ) {

          closeMemory();

        }

      }
    );


  document.addEventListener(
    "keydown",
    event => {

      if (
        $("#lightbox").hidden
      ) return;


      if (
        event.key === "Escape"
      ) {

        closeMemory();

      }


      if (
        event.key === "ArrowLeft"
      ) {

        stepMemory(-1);

      }


      if (
        event.key === "ArrowRight"
      ) {

        stepMemory(1);

      }

    }
  );

}


// =========================================================
// AUCTION
// =========================================================

function setupAuction() {

  const section =
    $("#auction");


  if (
    !AUCTION_CONFIG.enabled
  ) {

    section.hidden =
      true;

    return;
  }


  section.hidden =
    false;


  $("#auctionTitle").textContent =
    AUCTION_CONFIG.title;


  $("#auctionDescription").textContent =
    AUCTION_CONFIG.description;


  $("#startingBid").textContent =
    `₹${
      Number(
        AUCTION_CONFIG.startingBid ||
        0
      ).toLocaleString("en-IN")
    }`;


  $("#currentBid").textContent =
    `₹${
      Number(
        AUCTION_CONFIG.currentBid ||
        0
      ).toLocaleString("en-IN")
    }`;


  $("#auctionEnd").textContent =

    AUCTION_CONFIG.endDate
      ? formatFullDate(
          AUCTION_CONFIG.endDate
        )
      : "—";

}


// =========================================================
// DONATION REFERENCE
// =========================================================
//
// Format:
//
// PHONE + DN + HHMM
//
// Example:
//
// 9876543210DN1256
//
// =========================================================

function generateDonationReference() {

  const phone =
    String(
      DONATION_CONFIG.phoneNumber ||
      ""
    ).replace(
      /\D/g,
      ""
    );


  const now =
    new Date();


  const hours =
    String(
      now.getHours()
    ).padStart(
      2,
      "0"
    );


  const minutes =
    String(
      now.getMinutes()
    ).padStart(
      2,
      "0"
    );


  return (
    phone +
    DONATION_CONFIG.notePrefix +
    hours +
    minutes
  );

}


// =========================================================
// UPI PAYMENT LINK
// =========================================================

function upiIntent(amount) {

  const reference =
    generateDonationReference();


  const params =
    new URLSearchParams({

      pa:
        DONATION_CONFIG.upiId,

      pn:
        DONATION_CONFIG.merchantName,

      am:
        String(amount),

      cu:
        "INR",

      tn:
        reference

    });


  return (
    `upi://pay?${params.toString()}`
  );

}


// =========================================================
// QR CODE
// =========================================================

function renderQr(text) {

  const root =
    $("#qrCode");


  root.innerHTML =
    "";


  if (!text) {

    root.innerHTML =
      placeholderHTML(
        "ADD UPI ID"
      );

    return;
  }


  if (window.QRCode) {

    new QRCode(
      root,
      {
        text: text,
        width: 170,
        height: 170,
        correctLevel:
          QRCode.CorrectLevel.M
      }
    );

  } else {

    root.innerHTML = `

      <div
        class="media-placeholder"
        style="
          height:154px;
          border:0;
        "
      >

        ${placeholderHTML(
          "QR LIBRARY NOT LOADED"
        )}

      </div>

    `;

  }

}


// =========================================================
// DONATION SETUP
// =========================================================

function setupDonation() {

  const section =
    $("#donation");


  // Completely hide if disabled
  if (
    !DONATION_CONFIG.enabled
  ) {

    section.hidden =
      true;

    return;
  }


  section.hidden =
    false;


  $("#merchantName").textContent =
    DONATION_CONFIG.merchantName;


  $("#upiDisplay").textContent =

    DONATION_CONFIG.upiId ||

    "Add UPI ID in script.js";


  let amount = 100;


  const customWrap =
    $("#customAmountWrap");


  const customInput =
    $("#customAmount");


  function refreshDonation() {

    const customValue =
      Number(
        customInput.value
      );


    const selectedAmount =

      amount === "custom"

        ? customValue

        : Number(amount);


    const valid =

      Number.isFinite(
        selectedAmount
      ) &&

      selectedAmount > 0 &&

      DONATION_CONFIG.upiId;


    const reference =
      generateDonationReference();


    $("#donationReference")
      .textContent =
      reference;


    if (valid) {

      const link =
        upiIntent(
          selectedAmount
        );


      $("#upiButton")
        .href =
        link;


      renderQr(
        link
      );

    } else {

      $("#upiButton")
        .href =
        "#";


      renderQr(
        ""
      );

    }

  }


  // Amount buttons
  $("#amounts")
    .addEventListener(
      "click",
      event => {

        const button =
          event.target.closest(
            "button"
          );


        if (!button) return;


        $$("#amounts button")
          .forEach(
            btn =>
              btn.classList.remove(
                "active"
              )
          );


        button.classList.add(
          "active"
        );


        amount =
          button.dataset.amount;


        if (
          amount ===
          "custom"
        ) {

          customWrap.hidden =
            false;

        } else {

          customWrap.hidden =
            true;

        }


        refreshDonation();

      }
    );


  customInput
    .addEventListener(
      "input",
      refreshDonation
    );


  $("#copyReference")
    .addEventListener(
      "click",
      async () => {

        try {

          await navigator
            .clipboard
            .writeText(
              $("#donationReference")
                .textContent
            );


          $("#copyReference")
            .textContent =
            "Copied";


          setTimeout(
            () => {

              $("#copyReference")
                .textContent =
                "Copy";

            },
            1200
          );

        } catch {

          // Clipboard may not be available
          // on some browsers.
        }

      }
    );


  refreshDonation();

}


// =========================================================
// LOAD QR LIBRARY
// =========================================================
//
// QR library is loaded ONLY when donation
// is enabled.
//
// =========================================================

function loadQrLibrary() {

  if (
    !DONATION_CONFIG.enabled
  ) return;


  const script =
    document.createElement(
      "script"
    );


  script.src =
    "https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js";


  script.onload =
    () => {

      setupDonation();

    };


  script.onerror =
    () => {

      setupDonation();

    };


  document.head.appendChild(
    script
  );

}


// =========================================================
// INITIALIZE WEBSITE
// =========================================================

document.addEventListener(
  "DOMContentLoaded",
  () => {

    setupConfig();

    setupNav();

    setupCountdown();

    renderDaily();

    setupMemoryFilters();

    renderMemories();

    renderPeople();

    renderEvents();

    setupLightbox();

    setupAuction();


    if (
      DONATION_CONFIG.enabled
    ) {

      loadQrLibrary();

    }


    observeReveals();


    // Refresh UP NEXT every minute
    setInterval(
      () => {
        renderUpNext();
      },
      60000
    );

  }
);