import json

data = json.load(open("data/data.json"))
p = data["person"]
skills = data["skills"]
certs = data["certifications"]
exp = data["experience"]
projects = data["projects"]
edu = data["education"]
hobbies = data["hobbies"]

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About Me"),
    ("education.html", "Education"),
    ("skills.html", "Skills"),
    ("projects.html", "Projects"),
    ("hobbies.html", "Hobbies"),
    ("cv.html", "CV"),
    ("contact.html", "Contact"),
]

def nav_html(active):
    items = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ''
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "\n        ".join(items)

INITIALS = "".join([w[0] for w in p["name"].split()]).upper()

def header(active):
    return f"""  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="index.html"><strong>{p['name'].upper()}</strong><span class="brand-id">// CpE.2026</span></a>
      <input type="checkbox" id="nav-toggle">
      <label class="nav-toggle-label" for="nav-toggle">MENU</label>
      <nav class="pinstrip" aria-label="Primary">
        <ul>
        {nav_html(active)}
        </ul>
      </nav>
    </div>
  </header>"""

FOOTER = f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <h4>{p['name']}</h4>
          <p style="max-width:32ch;color:var(--text-muted-light);font-size:.88rem;">Final year Computer Engineering student, Ahmadu Bello University, Zaria &mdash; focused on AI/ML, computer vision, and systems.</p>
        </div>
        <div>
          <h4>Sitemap</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Me</a></li>
            <li><a href="education.html">Education</a></li>
            <li><a href="skills.html">Skills</a></li>
          </ul>
        </div>
        <div>
          <h4>More</h4>
          <ul>
            <li><a href="projects.html">Projects</a></li>
            <li><a href="hobbies.html">Hobbies</a></li>
            <li><a href="cv.html">CV</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:{p['email']}">{p['email']}</a></li>
            <li>{p['phone']}</li>
            <li>{p['location']}</li>
            <li><a href="{p['linkedin']}">LinkedIn</a> &middot; <a href="{p['github']}">GitHub</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 {p['name']}. All rights reserved.</span>
        <span>Department of Computer Engineering &mdash; Ahmadu Bello University, Zaria</span>
      </div>
    </div>
  </footer>"""

def head(title, desc, jsonld="", extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} &middot; {p['name']}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
{extra}{jsonld}</head>"""

print("helpers ready")

# ---------------- index.html ----------------
jsonld_home = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "{p['name']}",
    "jobTitle": "{p['title']}",
    "affiliation": {{
      "@type": "CollegeOrUniversity",
      "name": "{p['institution']}"
    }},
    "email": "mailto:{p['email']}",
    "telephone": "{p['phone']}",
    "url": "index.html",
    "sameAs": ["{p['linkedin']}", "{p['github']}"],
    "knowsAbout": ["Computer Engineering", "Artificial Intelligence", "Machine Learning", "Computer Vision", "Python", "PyTorch"]
  }}
  </script>
"""

body_home = f"""<body>
{header("index.html")}
  <main id="main">
    <section class="hero blueprint registration">
      <div class="reg-marks"><span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span></div>
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">Portfolio &middot; Rev. 2026</p>
          <h1>Engineering systems that see, learn, and stay <span class="accent">running.</span></h1>
          <p class="lede">I'm {p['name']}, a final-year Computer Engineering student at Ahmadu Bello University, Zaria, working across AI/ML, computer vision, and hands-on systems support. This site documents what I've built and how I think.</p>
          <ul class="trace-list">
            <li>Python</li><li>PyTorch</li><li>Computer Vision</li><li>Arduino / ESP32-CAM</li><li>Systems &amp; Networking</li>
          </ul>
          <a class="btn solid" href="projects.html">View Projects</a>
          <a class="btn ghost-light" href="cv.html">See CV</a>
        </div>
        <div class="figure-panel">
          <div class="chip" style="overflow:hidden;">
            <img src="assets/images/profile.jpg" alt="Portrait of {p['name']}" style="width:100%;height:100%;object-fit:cover;">
          </div>
          <div class="figure-caption"><span>FIG. 1 &mdash; {p['name'].upper()}</span><span>ZARIA, NG</span></div>
        </div>
      </div>
    </section>

    <section class="block on-paper">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">&sect; 01 Overview</p>
          <h2>A quick map of this site</h2>
          <p>Eight pages, each documenting one part of who I am as an engineer &mdash; from background and coursework to the projects I've actually shipped.</p>
        </div>
        <div class="grid cols-4">
          <div class="card"><span class="tag">01</span><h3>About Me</h3><p>Background, interests, and what drives my engineering choices.</p></div>
          <div class="card"><span class="tag">02</span><h3>Education</h3><p>Academic timeline and coursework highlights.</p></div>
          <div class="card"><span class="tag">03</span><h3>Skills</h3><p>Languages, tools, and platforms I work with.</p></div>
          <div class="card"><span class="tag">04</span><h3>Projects</h3><p>AI/ML, computer vision, and systems builds with full write-ups.</p></div>
        </div>
      </div>
    </section>

    <section class="block on-navy blueprint">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">&sect; 02 Featured Build</p>
          <h2>ESP32-CAM Vision Node</h2>
          <p>A low-cost edge AI capture node built on the ESP32-CAM, feeding frames into a lightweight vision pipeline for basic object detection.</p>
        </div>
        <a class="btn ghost-light" href="projects.html#prj-001">Read the write-up</a>
      </div>
    </section>
  </main>
{FOOTER}
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(head("Home", f"Portfolio of {p['name']}, final year Computer Engineering student at Ahmadu Bello University, Zaria.", jsonld_home) + "\n" + body_home)

print("index.html written")

# ---------------- about.html ----------------
body_about = f"""<body>
{header("about.html")}
  <main id="main">
    <section class="hero blueprint registration" style="padding:3.5rem 0;">
      <div class="reg-marks"><span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span></div>
      <div class="wrap">
        <p class="eyebrow">&sect; 01 About</p>
        <h1 style="max-width:20ch;">About Me</h1>
      </div>
    </section>
    <section class="block on-paper">
      <div class="wrap grid cols-2" style="align-items:start;">
        <div>
          <p>I'm {p['name']}, a final-year Computer Engineering student at Ahmadu Bello University, Zaria. My interest sits at the intersection of systems and intelligence &mdash; I like taking a machine from "it turns on" to "it can see, decide, or adapt."</p>
          <p>My background started in hands-on computer maintenance and troubleshooting, working as an intern at Mahir Computers since 2018, which gave me a solid grounding in how systems actually fail and get fixed. From there I've moved into AI/ML and computer vision, working with Python and PyTorch, and pairing that with embedded platforms like Arduino and the ESP32-CAM to bring models closer to the physical world.</p>
          <p>[Placeholder: add a paragraph here about your personal engineering philosophy, what got you into Computer Engineering, and what kind of problems you want to work on after graduation.]</p>
          <a class="btn" href="cv.html">View full CV</a>
        </div>
        <div class="card">
          <span class="tag">Snapshot</span>
          <table class="datasheet" style="margin-top:1rem;">
            <tr><th>Name</th><td>{p['name']}</td></tr>
            <tr><th>Programme</th><td>B.Eng. Computer Engineering</td></tr>
            <tr><th>Institution</th><td>{p['institution']}</td></tr>
            <tr><th>Focus</th><td>{p['focus_area']}</td></tr>
            <tr><th>Location</th><td>{p['location']}</td></tr>
          </table>
        </div>
      </div>
    </section>
    <section class="block on-paper-2">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">&sect; 02 Values</p>
          <h2>How I approach engineering work</h2>
        </div>
        <div class="grid cols-3">
          <div class="card"><span class="tag">Rigor</span><h3>Measure, don't assume</h3><p>I prototype early and test against real data rather than trusting a design on paper alone.</p></div>
          <div class="card"><span class="tag">Clarity</span><h3>Document as I build</h3><p>Clean write-ups and commit history &mdash; future-me is a stakeholder too.</p></div>
          <div class="card"><span class="tag">Practicality</span><h3>Fix what's in front of me</h3><p>Years of hands-on troubleshooting taught me to solve the real problem, not the theoretical one.</p></div>
        </div>
      </div>
    </section>
  </main>
{FOOTER}
</body>
</html>"""

with open("about.html", "w") as f:
    f.write(head("About Me", f"About {p['name']}, final year Computer Engineering student.") + "\n" + body_about)
print("about.html written")
