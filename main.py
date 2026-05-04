from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, 
                                 Table, TableStyle, HRFlowable, PageBreak,
                                 KeepTogether)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

doc = SimpleDocTemplate(
    "/home/claude/TG_ICET_2025_Complete_Mentor_Guide.pdf",
    pagesize=A4,
    rightMargin=18*mm, leftMargin=18*mm,
    topMargin=20*mm, bottomMargin=20*mm,
    title="TG ICET 2025 Complete Mentor Guide",
    author="ICET Expert Mentor"
)

W, H = A4
styles = getSampleStyleSheet()

# Color palette
DARK_BLUE  = colors.HexColor("#1A237E")
MED_BLUE   = colors.HexColor("#1565C0")
LIGHT_BLUE = colors.HexColor("#E3F2FD")
ORANGE     = colors.HexColor("#E65100")
ORANGE_LT  = colors.HexColor("#FFF3E0")
GREEN      = colors.HexColor("#1B5E20")
GREEN_LT   = colors.HexColor("#E8F5E9")
RED        = colors.HexColor("#B71C1C")
RED_LT     = colors.HexColor("#FFEBEE")
YELLOW_LT  = colors.HexColor("#FFFDE7")
PURPLE     = colors.HexColor("#4A148C")
PURPLE_LT  = colors.HexColor("#F3E5F5")
TEAL       = colors.HexColor("#004D40")
GREY_LIGHT = colors.HexColor("#F5F5F5")
GOLD       = colors.HexColor("#F57F17")

def S(name, **kw):
    base = styles[name]
    return ParagraphStyle(name+"_custom_"+str(id(kw)), parent=base, **kw)

# Custom styles
TITLE_S = S("Title", fontSize=26, textColor=DARK_BLUE, spaceAfter=4, 
            leading=32, alignment=TA_CENTER, fontName="Helvetica-Bold")
SUBTITLE_S = S("Normal", fontSize=13, textColor=MED_BLUE, spaceAfter=2,
               alignment=TA_CENTER, fontName="Helvetica")
H1 = S("Heading1", fontSize=17, textColor=colors.white, spaceAfter=6,
        spaceBefore=14, fontName="Helvetica-Bold", leading=22)
H2 = S("Heading2", fontSize=13, textColor=DARK_BLUE, spaceAfter=4,
        spaceBefore=10, fontName="Helvetica-Bold")
H3 = S("Heading3", fontSize=11, textColor=ORANGE, spaceAfter=3,
        spaceBefore=7, fontName="Helvetica-Bold")
BODY = S("Normal", fontSize=9.5, leading=14, spaceAfter=3, textColor=colors.black)
BODY_B = S("Normal", fontSize=9.5, leading=14, spaceAfter=3, 
           textColor=colors.black, fontName="Helvetica-Bold")
SMALL = S("Normal", fontSize=8.5, leading=12, spaceAfter=2, textColor=colors.HexColor("#333333"))
TRICK = S("Normal", fontSize=9, leading=13, textColor=TEAL, fontName="Helvetica-Bold", spaceAfter=2)
HINGLISH = S("Normal", fontSize=9, leading=13, textColor=PURPLE, 
             fontName="Helvetica-Oblique", spaceAfter=2)
ANSWER = S("Normal", fontSize=9.5, leading=13, textColor=GREEN, 
           fontName="Helvetica-Bold", spaceAfter=2)
BULLET = S("Normal", fontSize=9.5, leading=14, leftIndent=12, spaceAfter=2,
           firstLineIndent=-12)
WARNING = S("Normal", fontSize=9, leading=13, textColor=RED, fontName="Helvetica-Bold")
CENTER_B = S("Normal", fontSize=10, alignment=TA_CENTER, fontName="Helvetica-Bold")

def banner(text, bg=DARK_BLUE, fg=colors.white, size=16):
    """Return a coloured header table row."""
    ts = TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TEXTCOLOR",  (0,0), (-1,-1), fg),
        ("ALIGN",      (0,0), (-1,-1), "CENTER"),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("FONTNAME",   (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), size),
    ])
    return Table([[text]], colWidths=[W - 36*mm], style=ts)

def info_box(text, bg=LIGHT_BLUE, border=MED_BLUE):
    ts = TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX",        (0,0), (-1,-1), 1.2, border),
        ("LEFTPADDING",(0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0),(-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ])
    return Table([[Paragraph(text, BODY)]], colWidths=[W - 36*mm], style=ts)

def trick_box(text):
    ts = TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), GREEN_LT),
        ("BOX",        (0,0), (-1,-1), 1.2, GREEN),
        ("LEFTPADDING",(0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0),(-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ])
    return Table([[Paragraph("⚡ QUICK TRICK: " + text, TRICK)]], 
                 colWidths=[W - 36*mm], style=ts)

def hinglish_box(text):
    ts = TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), PURPLE_LT),
        ("BOX",        (0,0), (-1,-1), 1.2, PURPLE),
        ("LEFTPADDING",(0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0),(-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ])
    return Table([[Paragraph("🌟 YAAD RAKHO (Hinglish): " + text, HINGLISH)]],
                 colWidths=[W - 36*mm], style=ts)

def warning_box(text):
    ts = TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), RED_LT),
        ("BOX",        (0,0), (-1,-1), 1.2, RED),
        ("LEFTPADDING",(0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0),(-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ])
    return Table([[Paragraph("⚠ " + text, WARNING)]], colWidths=[W - 36*mm], style=ts)

def q_table(q_num, topic, question, answer, explanation, trick, hinglish_ex):
    """Build a styled question block."""
    ts = TableStyle([
        ("BOX",        (0,0), (-1,-1), 1, MED_BLUE),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[GREY_LIGHT, colors.white]),
        ("LEFTPADDING",(0,0), (-1,-1), 7),
        ("RIGHTPADDING",(0,0),(-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ])
    hdr = Paragraph(f"<b>Q{q_num} | {topic}</b>", 
                    S("Normal", textColor=colors.white, fontName="Helvetica-Bold", fontSize=9.5))
    hdr_ts = TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), MED_BLUE),
        ("LEFTPADDING",(0,0),(-1,-1),7),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ])
    rows = [
        [Paragraph(f"<b>Question:</b> {question}", BODY)],
        [Paragraph(f"<b>Answer:</b> {answer}", ANSWER)],
        [Paragraph(f"<b>Solution:</b> {explanation}", BODY)],
    ]
    t = Table(rows, colWidths=[W - 36*mm], style=ts)
    return KeepTogether([
        Table([[hdr]], colWidths=[W - 36*mm], style=hdr_ts),
        t,
        trick_box(trick),
        hinglish_box(hinglish_ex),
        Spacer(1, 4),
    ])

story = []

# ═══════════════════════════════════════════════════════════
# COVER PAGE
# ═══════════════════════════════════════════════════════════
story.append(Spacer(1, 30*mm))

cover_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), DARK_BLUE),
    ("ALIGN",      (0,0), (-1,-1), "CENTER"),
    ("TOPPADDING", (0,0), (-1,-1), 20),
    ("BOTTOMPADDING",(0,0),(-1,-1),20),
    ("BOX",        (0,0), (-1,-1), 3, GOLD),
])
story.append(Table([
    [Paragraph("TG ICET 2025", S("Title", fontSize=32, textColor=GOLD, fontName="Helvetica-Bold", alignment=TA_CENTER))],
    [Paragraph("COMPLETE EXPERT MENTOR GUIDE", S("Normal", fontSize=16, textColor=colors.white, fontName="Helvetica-Bold", alignment=TA_CENTER))],
    [Paragraph("Based on 2025 Actual Papers (3 Shifts)", S("Normal", fontSize=11, textColor=colors.lightblue, alignment=TA_CENTER))],
], colWidths=[W - 36*mm], style=cover_ts))

story.append(Spacer(1, 8*mm))

info_rows = [
    ["📅 Exam Date", "14th May 2026 (Morning)"],
    ["⏱ Duration", "150 Minutes | 200 Questions | 200 Marks"],
    ["📚 Sections", "Analytical Ability (75M) + Mathematical Ability (75M) + Communication (50M)"],
    ["🎯 Target", "Score 140+ with Smart Strategy"],
    ["📄 Based On", "TG ICET 2025: June 8 Shift 1, June 8 Shift 2, June 9 Shift 1"],
]
info_ts = TableStyle([
    ("BACKGROUND", (0,0), (0,-1), MED_BLUE),
    ("TEXTCOLOR",  (0,0), (0,-1), colors.white),
    ("FONTNAME",   (0,0), (0,-1), "Helvetica-Bold"),
    ("BACKGROUND", (1,0), (1,-1), LIGHT_BLUE),
    ("BOX",        (0,0), (-1,-1), 1, MED_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.white),
    ("LEFTPADDING",(0,0),(-1,-1), 8),
    ("RIGHTPADDING",(0,0),(-1,-1),8),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("FONTSIZE",   (0,0), (-1,-1), 9.5),
])
story.append(Table(info_rows, colWidths=[55*mm, W-36*mm-55*mm], style=info_ts))

story.append(Spacer(1, 10*mm))
story.append(Paragraph("✅ Smart Strategies  ✅ Section-Wise Analysis  ✅ Solved Questions with Tricks",
                        S("Normal", fontSize=10, alignment=TA_CENTER, textColor=DARK_BLUE, fontName="Helvetica-Bold")))
story.append(Paragraph("✅ Day-wise Study Plan  ✅ Hinglish Examples  ✅ Last-Minute Revision Sheet",
                        S("Normal", fontSize=10, alignment=TA_CENTER, textColor=DARK_BLUE, fontName="Helvetica-Bold")))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 0: EXAM OVERVIEW
# ═══════════════════════════════════════════════════════════
story.append(banner("📋 EXAM STRUCTURE & PAPER ANALYSIS", DARK_BLUE))
story.append(Spacer(1, 4))

struct_data = [
    ["Section", "Sub-topics", "Questions", "Marks", "Time Target"],
    ["SECTION A\nAnalytical Ability", 
     "Data Sufficiency (20Q)\nProblem Solving - Series (20Q)\nProblem Solving - Coding (5Q)\nDate/Time/Arrangement (0-5Q)", 
     "45", "75", "45 min"],
    ["SECTION B\nMathematical Ability", 
     "Arithmetic (Numbers, %, SI/CI, Ratios) ~20Q\nAlgebraic Ability (Eqns, Matrices) ~10Q\nGeometrical Ability (Areas, Mensuration) ~10Q\nStatistics (Mean, Mode, Median) ~5Q\nSet Theory / Venn ~5Q", 
     "75", "75", "65 min"],
    ["SECTION C\nCommunication Ability", 
     "Business & Computer Vocabulary ~10Q\nFunctional Grammar ~15Q\nReading Comprehension ~15Q\nBusiness Correspondence ~10Q",
     "50", "50", "40 min"],
    ["TOTAL", "", "200 (Attempt ALL)", "200", "150 min"],
]
struct_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (-1,1), LIGHT_BLUE),
    ("BACKGROUND", (0,2), (-1,2), GREEN_LT),
    ("BACKGROUND", (0,3), (-1,3), YELLOW_LT),
    ("BACKGROUND", (0,4), (-1,4), ORANGE_LT),
    ("BOX",        (0,0), (-1,-1), 1.5, DARK_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN",      (2,0), (-1,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("FONTNAME",   (0,4), (-1,4), "Helvetica-Bold"),
    ("BACKGROUND", (0,4), (-1,4), MED_BLUE),
    ("TEXTCOLOR",  (0,4), (-1,4), colors.white),
])
story.append(Table(struct_data, colWidths=[35*mm, 85*mm, 18*mm, 15*mm, 18*mm], style=struct_ts))
story.append(Spacer(1, 6))

story.append(Paragraph("KEY PATTERN FINDINGS from 3 Papers (2025 Actual Exams)", H2))
patterns = [
    ["🔑 Finding", "📊 Details", "⭐ Priority"],
    ["Data Sufficiency = ALWAYS 20Q", "All 3 papers had exactly 20 DS questions. Answers are always: 1=Only I, 2=Only II, 3=Both needed, 4=Neither sufficient", "★★★★★"],
    ["Series/Analogies = 10-12Q each paper", "Both number series AND letter/word analogies appear. Odd-one-out is most frequent sub-type", "★★★★★"],
    ["Arithmetic dominates Math section", "Number system, percentages, SI/CI, ratios appear in 25-30 out of 75 questions", "★★★★★"],
    ["Coding-Decoding = 5Q consistently", "Letter shifting pattern (LAMP→LWDC type) very common", "★★★★☆"],
    ["Date-Time-Arrangement = 5-8Q", "Bus/train timing problems and seating arrangement types appear", "★★★★☆"],
    ["Communication = Easy 35+/50", "Grammar and vocabulary are predictable, comprehension is manageable", "★★★★☆"],
    ["No Negative Marking!", "Attempt ALL 200 questions - never leave blank", "★★★★★"],
]
pat_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ORANGE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, ORANGE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, GREY_LIGHT]),
    ("TEXTCOLOR",  (2,1), (2,-1), GREEN),
    ("FONTNAME",   (2,1), (2,-1), "Helvetica-Bold"),
    ("ALIGN",      (2,0), (2,-1), "CENTER"),
])
story.append(Table(patterns, colWidths=[45*mm, 100*mm, 25*mm], style=pat_ts))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 1: TOPIC PRIORITY RANKING
# ═══════════════════════════════════════════════════════════
story.append(banner("🏆 TOPIC PRIORITY: MOST TO LEAST IMPORTANT", ORANGE))
story.append(Spacer(1, 4))

priority_data = [
    ["Rank", "Topic", "Avg Q/Paper", "Difficulty", "Study Time"],
    ["#1", "Data Sufficiency (DS)", "20", "Medium", "1.5 hrs"],
    ["#2", "Number Series & Odd-One-Out", "10", "Easy-Med", "1 hr"],
    ["#3", "Arithmetic (%, Ratio, SI/CI, Profit-Loss)", "20-25", "Medium", "2 hrs"],
    ["#4", "Letter Analogy & Coding-Decoding", "10-12", "Easy", "45 min"],
    ["#5", "Functional Grammar (Tense, Articles, Prepositions)", "10-12", "Easy", "1 hr"],
    ["#6", "Reading Comprehension", "10-15", "Medium", "45 min"],
    ["#7", "Algebraic Equations & Matrices", "8-10", "Med-Hard", "1 hr"],
    ["#8", "Mensuration & Geometry (Areas, Volumes)", "8-10", "Medium", "45 min"],
    ["#9", "Statistics (Mean/Mode/Median)", "5", "Easy", "30 min"],
    ["#10", "Vocabulary & Business Terms", "8-10", "Easy", "30 min"],
    ["#11", "Date, Time & Arrangement Problems", "5-8", "Medium", "30 min"],
    ["#12", "Venn Diagrams & Sets", "4-5", "Easy", "20 min"],
]
pri_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (-1,4), colors.HexColor("#FFD54F")),
    ("BACKGROUND", (0,5), (-1,8), LIGHT_BLUE),
    ("BACKGROUND", (0,9), (-1,-1), GREEN_LT),
    ("BOX",        (0,0), (-1,-1), 1.5, DARK_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.grey),
    ("FONTSIZE",   (0,0), (-1,-1), 9),
    ("ALIGN",      (0,0), (0,-1), "CENTER"),
    ("ALIGN",      (2,0), (4,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("FONTNAME",   (0,1), (0,4), "Helvetica-Bold"),
    ("TEXTCOLOR",  (0,1), (0,4), RED),
])
story.append(Table(priority_data, colWidths=[12*mm, 70*mm, 22*mm, 22*mm, 22*mm], style=pri_ts))
story.append(Spacer(1,4))
story.append(info_box("🟡 Top 4 topics = 55-60 marks. Master them FIRST. 🟢 Topics 5-8 = 35-40 more marks. Focus next. 🔵 Topics 9-12 = Easy 15-20 marks. Quick wins!", YELLOW_LT, GOLD))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 2: SOLVED QUESTIONS WITH TRICKS
# ═══════════════════════════════════════════════════════════
story.append(banner("📝 SECTION A: ANALYTICAL ABILITY — SOLVED QUESTIONS", DARK_BLUE))
story.append(Spacer(1, 4))

story.append(Paragraph("PART 1: DATA SUFFICIENCY (20 Questions — 20 Marks)", H2))
story.append(Spacer(1, 3))

# DS Options Explanation
ds_options = [
    ["Option", "Meaning — MEMORIZE THIS!"],
    ["Option 1", "Statement I ALONE is sufficient; Statement II is NOT needed"],
    ["Option 2", "Statement II ALONE is sufficient; Statement I is NOT needed"],
    ["Option 3", "BOTH Statements I and II together are needed (neither alone works)"],
    ["Option 4", "NEITHER statement alone nor together is sufficient (cannot be determined)"],
]
ds_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (0,-1), LIGHT_BLUE),
    ("FONTNAME",   (0,1), (0,-1), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, TEAL),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 9.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),7),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
])
story.append(Table(ds_options, colWidths=[20*mm, 151*mm], style=ds_ts))
story.append(Spacer(1, 4))

story.append(q_table(
    "DS-1", "Data Sufficiency — Geometry",
    "What is the area of the circle? (I) Perimeter is 54π cm. (II) Area of inscribed triangle is 365 sq.cm.",
    "Option 1 — Statement I alone is sufficient",
    "From (I): Circumference = 2πr = 54π → r = 27. Area = πr² = 729π. This gives a unique answer. "
    "From (II): Triangle area doesn't uniquely determine circle radius. So only (I) is needed.",
    "Perimeter alone → find radius → find area. Statement I always wins for circle problems if circumference is given.",
    "Jaise ek rasgulla ki gol goli ka gher pata hai, toh uska area nikal sakte ho. But andar ki mithai ki size se gher nahi pata."
))

story.append(q_table(
    "DS-2", "Data Sufficiency — Cost of Fencing",
    "What is the cost of erecting a fence around a rectangular field? (I) Cost of fencing is Rs.150/m. (II) Area = 20000 sq.m.",
    "Option 4 — Neither statement alone nor together is sufficient",
    "To find fencing cost, you need: Perimeter × Rate. Rate (I) = Rs.150/m. Area (II) = 20000 sq.m. "
    "But area alone doesn't give perimeter! (Many rectangles have same area but different perimeters.) "
    "E.g. 100×200 and 50×400 both = 20000 area but different perimeters. So NEITHER is sufficient!",
    "Key formula: Cost of fencing = PERIMETER × Rate. Area doesn't give perimeter unless dimensions are given. "
    "If neither statement gives perimeter or both dimensions → Answer is Option 4.",
    "Ghar ke aas-paas fence lagana hai. Rate pata hai (Rs.150/m) aur area pata hai (20000). "
    "But area se fence ka length nahi pata kyunki shape change ho sakti hai!"
))

story.append(q_table(
    "DS-3", "Data Sufficiency — Algebra (Quadratic)",
    "Are the roots of 4ax² + 5bx + 6c = 0 real? (I) a:b:c = 2:3:4. (II) a+b+c = 27.",
    "Option 1 — Statement I alone is sufficient",
    "Roots are real if Discriminant (D) = (5b)² - 4(4a)(6c) ≥ 0 → 25b² - 96ac ≥ 0. "
    "From (I): a=2k, b=3k, c=4k → 25(9k²) - 96(2k)(4k) = 225k² - 768k² = -543k² < 0. NOT real! "
    "Statement I gives a definite answer (No, not real). Statement II gives actual values but needs both. So (I) alone works!",
    "Discriminant test: b²-4ac ≥ 0 means real roots. If ratio is given, substitute and check sign.",
    "Jaise cricket mein target pata hai aur run rate ratio pata hai, toh match possible hai ya nahi check kar sakte ho — "
    "actual score jaane bina!"
))

story.append(q_table(
    "DS-4", "Data Sufficiency — Simple Interest",
    "What is the simple interest earned on a fixed deposit? (I) Deposit kept for 1 year. (II) Amount deposited = Rs.10,000.",
    "Option 4 — Neither sufficient",
    "SI Formula: SI = (P × R × T)/100. We need P, R, and T. "
    "Statement I gives T=1 year. Statement II gives P=10,000. But Rate R is MISSING from both! "
    "Without R, we cannot calculate SI. So NEITHER is sufficient.",
    "SI needs 3 things: Principal (P), Rate (R), Time (T). If any ONE is missing → Answer is Option 4 (Neither).",
    "Jaise bank mein paisa rakha, 1 saal ke liye, 10,000 ka. But interest rate (rate of return) pata nahi. "
    "Toh interest nahi nikaal sakte! Bank wale bhi nahi batayenge bina rate ke!"
))

story.append(q_table(
    "DS-5", "Data Sufficiency — Statistics",
    "Find average of 10 numbers in ascending order. (I) Average of first 4 and last 4 = 20. (II) Sum of middle 2 = 15.",
    "Option 3 — Both needed",
    "We need sum of all 10 numbers. "
    "From (I): (Sum of first 4) + (Sum of last 4) = 8×20 = 160. "
    "From (II): Sum of middle 2 = 15. "
    "Total = 160 + 15 = 175. Average = 175/10 = 17.5. BOTH are needed!",
    "Total sum = Group sums. When numbers are split into sub-groups, you need ALL sub-group sums for the total.",
    "10 students ka average nikalna hai. 4+4 ka average pata hai, beech ke 2 ka sum pata hai. "
    "Dono milao tab total nikalta hai — akele nahi chalta!"
))

story.append(q_table(
    "DS-6", "Data Sufficiency — Arrangement",
    "29 persons in a row. How many persons between A and B? (I) A is 24th from beginning. (II) B is 19th from end.",
    "Option 3 — Both needed",
    "From (I): A is at position 24. From (II): B is at position (29-19+1) = 11. "
    "Both together: Positions of A=24 and B=11. Persons between = 24-11-1 = 12. "
    "You need BOTH positions to find the gap!",
    "Position from end → Position from start = (Total - position from end + 1). "
    "Persons BETWEEN = |Pos A - Pos B| - 1. Always subtract 1 for 'between'.",
    "Class mein 29 bacche line mein khade hain. A 24th hai front se, B 19th hai back se. "
    "Dono positions pata hain tab beech mein kitne hain pata chalega!"
))

story.append(q_table(
    "DS-7", "Data Sufficiency — Volume of Cone",
    "Volume of right circular cone? (I) Semi-vertical angle = 30°. (II) Slant height = 17cm.",
    "Option 3 — Both needed",
    "Volume = (1/3)πr²h. From (I): tan(30°) = r/h → r = h/√3. Still 2 unknowns. "
    "From (II): l = 17cm, and l² = r² + h². Using (I) ratio: r = h/√3, so h² + h²/3 = 289 → h can be found. "
    "Then r and finally Volume. BOTH needed!",
    "Cone: r² + h² = l² (slant height formula). Semi-vertical angle gives r/h ratio. Combine both to get exact r and h.",
    "Ice cream cone — angle jaante ho (kitna mota hai top pe), aur side ki length jaante ho. "
    "Dono milao tab volume nikalega. Akele nahi!"
))

story.append(Spacer(1, 6))
story.append(Paragraph("DS MASTER STRATEGY — Read This Before Attempting!", H3))
ds_strategy = [
    ["DS Answer Decision Tree", ""],
    ["Step 1", "Read the QUESTION carefully. Identify WHAT is needed (one value? formula?)."],
    ["Step 2", "Check Statement I ALONE. Can it give a unique answer? If YES → Option 1."],
    ["Step 3", "If No, check Statement II ALONE. If YES → Option 2."],
    ["Step 4", "If neither alone, try BOTH together. If YES → Option 3."],
    ["Step 5", "If still can't solve → Option 4 (Neither sufficient)."],
    ["TIME TRICK", "Spend max 45 sec per DS question. If confused between 3 and 4, go with 3."],
    ["COMMON PATTERN", "If question needs 2+ variables (like P, R, T or L, B for rectangle), "
     "usually need both statements → Option 3."],
]
ds_strat_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,-1), "Helvetica-Bold"),
    ("SPAN",       (0,0), (-1,0)),
    ("ALIGN",      (0,0), (-1,0), "CENTER"),
    ("BOX",        (0,0), (-1,-1), 1, TEAL),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 9),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),7),
    ("BACKGROUND", (0,1), (0,-1), LIGHT_BLUE),
    ("BACKGROUND", (0,6), (-1,7), YELLOW_LT),
    ("FONTNAME",   (0,6), (0,-1), "Helvetica-Bold"),
    ("TEXTCOLOR",  (0,6), (0,7), RED),
    ("ROWBACKGROUNDS",(0,1),(-1,5),[colors.white, GREY_LIGHT]),
])
story.append(Table(ds_strategy, colWidths=[30*mm, 141*mm], style=ds_strat_ts))
story.append(PageBreak())

# ─── PROBLEM SOLVING ─────────────────────────────────────────────────────────
story.append(Paragraph("PART 2: PROBLEM SOLVING — SERIES & ANALOGIES (20 Questions — 20 Marks)", H2))
story.append(Spacer(1, 3))
story.append(info_box("5 sub-sections: A) Series (Odd-one-out + Analogies) | B) Data Analysis "
                       "| C) Coding-Decoding | D) Date/Time | E) Relations. "
                       "Series and Coding are the highest-frequency!"))
story.append(Spacer(1, 4))

story.append(q_table(
    "PS-1", "Number Series — Odd One Out",
    "75, 57, 54, 64, 36, 87, 69, 93 — Find the odd one out.",
    "Answer: 64",
    "All other numbers: 75, 57, 36, 87, 69, 93 are either multiples of 3 or have digits summing to a multiple of 3. "
    "75: 7+5=12 ✓ | 57: 5+7=12 ✓ | 54: 5+4=9 ✓ | 36: 3+6=9 ✓ | 87: 8+7=15 ✓ | 69: 6+9=15 ✓ | 93: 9+3=12 ✓. "
    "But 64: 6+4=10 ✗ — NOT a multiple of 3. ODD ONE OUT = 64.",
    "Digit Sum Rule: Add all digits. If divisible by 3 → multiple of 3. Quick shortcut for odd-one-out!",
    "Jaise 6 doston ki group mein sab Hyderabadi hain but ek Chennai ka hai — woh 'odd one out' hai! "
    "Yahan 64 woh Chennai wala hai!"
))

story.append(q_table(
    "PS-2", "Fraction Series — Odd One Out",
    "21/11, 31/19, 43/29, 57/41, 73/55, 91/70 — Find the odd one out.",
    "Answer: 91/70",
    "Pattern: Look at numerators: 21, 31, 43, 57, 73, 91 — differences are 10, 12, 14, 16, 18 ✓. "
    "Denominators: 11, 19, 29, 41, 55, 70 — differences: 8, 10, 12, 14, 16... "
    "Expected: 55+16=71, but given 70. So 91/70 is wrong — should be 91/71.",
    "In fraction series, check numerator AND denominator patterns SEPARATELY. Differences increase by 2 often.",
    "School register mein saare roll numbers ek pattern mein hain — 1 number galat lag raha hai? "
    "Alag se check karo differences. Wahi odd one out hai!"
))

story.append(q_table(
    "PS-3", "Number Series — Odd One Out",
    "45, 75, 175, 245, 315, 605, 845 — Find the odd one out.",
    "Answer: 315",
    "All numbers divisible by 5: ✓. Check divisibility by 35: "
    "45÷35=1.28 ✗... Try another pattern. "
    "45=5×9, 75=5×15, 175=5×35, 245=5×49, 315=5×63, 605=5×121, 845=5×169. "
    "Multipliers: 9, 15, 35, 49, 121, 169. Are these perfect squares? 9=3², 25=5²(missing!), 49=7², 121=11², 169=13². "
    "75 should be 5×25=125. Actually: 75 is odd... 315: 5×63, 63 is not a perfect square factor. Ans=315.",
    "For 'all divisible by X' series: factor out X and check if the quotients follow a pattern (squares, primes, etc.).",
    "Jaise market mein sab items ek category ke hain — electronics, electronics — aur ek item groceries. "
    "Category pattern dekho, odd one pakad lo!"
))

story.append(q_table(
    "PS-4", "Number Series — Mixed",
    "83, 31, 29, 23, 17, 19, 39, 53 — Find the odd one out.",
    "Answer: 39",
    "83: composite. 31: prime. 29: prime. 23: prime. 17: prime. 19: prime. 53: prime. "
    "But 39 = 3×13 — NOT a prime number! Also 83 is composite... "
    "Pattern check by differences: 83,31(-52), 29(-2), 23(-6), 17(-6), 19(+2), 39(+20), 53(+14) — irregular. "
    "Most numbers are prime except 39 and 83. Since 83 is at start, 39 is the clear odd one out.",
    "Prime check quick: Not divisible by 2, 3, 5, 7 → prime. For 39: 39÷3=13. So 39 is composite → ODD ONE OUT.",
    "Jaise sab students first division mein hain aur ek second division. Divisibility se quickly identify karo "
    "kaun composite hai!"
))

story.append(q_table(
    "PS-5", "Letter Analogy — Coding",
    "(8)Z : (27)Y :: (64)B : ____",
    "Answer: 125A",
    "Pattern: 8=2³, Z=26th letter (26-2=24, no...). Try: 8=2³, and Z=position counted from end (Z=1st from end). "
    "27=3³, Y=2nd from end. 64=4³, B=2nd from start... Hmm. "
    "Revised: 8=2³, Z is 26th letter (26). 27=3³, Y is 25th. 64=4³, B is 2nd. "
    "Pattern: cube number pairs with a letter such that cube-root + letter-position = 28. "
    "2+26=28✓, 3+25=28✓, 4+2=6✗. Try: Cube root corresponds to reverse alphabet: 2→Z(-1), 3→Y(-1)... "
    "4→X would be next. But B is 2nd letter. 64B → next should be 5³=125, letter A (1st). Answer: 125A.",
    "In letter analogies: always check BOTH the number pattern (squares/cubes) AND the letter position pattern simultaneously.",
    "Jaise password mein number aur letter dono ka pattern hai — ek badal raha hai dusra bhi badlega "
    "ek rule ke hisaab se!"
))

story.append(q_table(
    "PS-6", "Letter Series — Coding/Decoding",
    "___: JUBA :: CRSY : APQW",
    "Answer: LWDC",
    "Pattern: C→A (−2), R→P (−2), S→Q (−2), Y→W (−2). Every letter shifted back by 2. "
    "So for JUBA→reverse logic: J+2=L, U+2=W, B+2=D, A+2=C → LWDC. Answer = LWDC.",
    "Coding rule check: Find difference between corresponding letters in given pair. Apply SAME shift to unknown.",
    "Jaise ATM ka PIN shift hoga: agar 1234 → 3456 (har digit +2), toh 5678 → 7890. Same rule apply karo!"
))

story.append(q_table(
    "PS-7", "Date & Time Problems",
    "Bus to Hyderabad runs every 45 min. Board says last bus left 13 min ago, next bus at 5:18 pm. What time is announcement?",
    "Answer: 4:46 pm (Option 3)",
    "Next bus is at 5:18 pm. Time interval = 45 minutes. "
    "Previous bus left 13 min ago. So previous bus left at (current time - 13 min). "
    "Next bus = previous bus time + 45 min. "
    "Let current time = T. Previous bus at T-13. Next bus at T-13+45 = T+32 = 5:18 pm. "
    "So T = 5:18 - 32 min = 4:46 pm.",
    "Timeline method: Draw a timeline. Mark previous bus, current time, next bus. "
    "Interval = 45 min. Previous + 45 = Next. Current = Previous + 13.",
    "Jaise Hyderabad se ek bus station pe: pata hai pichhli bus 13 min pehle gayi, agli bus 5:18 pe aayegi, "
    "interval 45 min hai. Backward calculate karo!"
))

story.append(PageBreak())

# ─── MATHEMATICAL ABILITY ────────────────────────────────────────────────────
story.append(banner("📐 SECTION B: MATHEMATICAL ABILITY — KEY TOPICS & SOLUTIONS", GREEN))
story.append(Spacer(1, 4))
story.append(info_box("75 Questions | 75 Marks | Target: Attempt all, expect 55+ correct. "
                        "Arithmetic (Numbers, %, SI/CI, Profit-Loss) = MOST MARKS."))
story.append(Spacer(1, 4))

story.append(Paragraph("ARITHMETIC — FORMULAS & TRICKS", H2))

formulas_data = [
    ["Topic", "Key Formula", "Quick Trick"],
    ["Simple Interest", "SI = PRT/100\nAmount = P + SI", "If R missing → can't solve. Check before starting."],
    ["Compound Interest", "A = P(1+R/100)^n\nCI = A - P", "For 2 years: CI = P[(R/100) + (R/100)² + 2R/100] (use approximation)"],
    ["Profit & Loss", "Profit% = (Profit/CP)×100\nSP = CP(1+P%/100)", "If SP>CP → Profit. If SP<CP → Loss. Simple!"],
    ["Percentage", "X% of Y = XY/100\n% increase = (Change/Original)×100", "Common: 1/8=12.5%, 1/6=16.67%, 1/4=25%, 1/3=33.33%"],
    ["Ratio & Proportion", "a:b :: c:d → ad=bc\nMean proportion: b²=ac", "Cross multiply to check ratio problems quickly."],
    ["Time & Work", "If A in x days, B in y days,\nTogether: 1/x + 1/y = 1/T", "LCM method: Assign total work = LCM of days. Easier!"],
    ["Speed-Distance-Time", "D = S×T; S = D/T; T = D/S\nAverage speed = 2S1S2/(S1+S2)", "Unit conversion: km/h to m/s → multiply by 5/18"],
    ["Area Formulas", "Rectangle: L×B\nCircle: πr²\nTriangle: ½bh", "Perimeter ≠ Area! Don't mix them up."],
    ["Sequence: AP", "nth term: a+(n-1)d\nSum: n/2[2a+(n-1)d]", "Common difference = any term - previous term."],
]
form_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GREEN),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, GREEN),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[GREEN_LT, colors.white]),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("BACKGROUND", (2,1), (2,-1), YELLOW_LT),
])
story.append(Table(formulas_data, colWidths=[35*mm, 75*mm, 61*mm], style=form_ts))
story.append(Spacer(1, 6))

story.append(q_table(
    "M-1", "Number System — Divisibility",
    "A number when divided by 6 gives remainder 3. What is the remainder when squared and divided by 6?",
    "Answer: 3",
    "Number = 6k + 3. Square = (6k+3)² = 36k² + 36k + 9 = 6(6k²+6k+1) + 3. "
    "Remainder = 3.",
    "Use algebra: write number as (divisor × quotient + remainder). Square it. Re-extract the remainder.",
    "Jaise ek baccha class mein 3rd seat pe baitha hai (3rd from multiple of 6). "
    "Uska square bhi 3rd seat pe hi baithega!"
))

story.append(q_table(
    "M-2", "Percentages",
    "A's income is 20% more than B's. By what % is B's income less than A's?",
    "Answer: 16.67% (= 100/6 %)",
    "If B = 100, A = 120. B is less than A by (120-100)/120 × 100 = 20/120 × 100 = 16.67%.",
    "Formula: If X is r% MORE than Y, then Y is r/(100+r)×100 LESS than X. "
    "Quick: 20% more → 20/120×100 = 16.67% less.",
    "Salary example: Agar Raju ki salary Sita se 20% zyada hai, "
    "toh Sita ki salary Raju se kitne % kam hai? Answer: 16.67%!"
))

story.append(q_table(
    "M-3", "Algebra — Quadratic Equations",
    "Find nature of roots of 2x² - 5x + 3 = 0",
    "Answer: Real and distinct roots",
    "Discriminant D = b² - 4ac = (-5)² - 4(2)(3) = 25 - 24 = 1. "
    "D > 0 → Real and distinct roots.",
    "D > 0: Real & distinct. D = 0: Real & equal. D < 0: Complex (no real roots). "
    "Just calculate b² - 4ac in 10 seconds!",
    "Cricket analogy: Discriminant batata hai ki match ho sakta hai (real roots) ya nahi. "
    "D>0 matlab match confirm, D=0 tie, D<0 match cancelled!"
))

story.append(q_table(
    "M-4", "Statistics — Mean, Mode, Median",
    "Find the median of: 3, 7, 2, 1, 8, 5, 4, 6, 9, 10",
    "Answer: 5.5",
    "Arrange in order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. "
    "n=10 (even). Median = average of 5th and 6th terms = (5+6)/2 = 5.5.",
    "Even n: Median = (n/2 th + (n/2+1) th)/2. Odd n: Median = ((n+1)/2) th term. ALWAYS arrange first!",
    "10 doston ki height arrange karo. Beech ke do logon ki height ka average lo — wahi median hai!"
))

story.append(q_table(
    "M-5", "Geometry — Areas",
    "What is the area of a triangle with sides 13, 14, 15?",
    "Answer: 84 sq units",
    "Use Heron's formula: s = (13+14+15)/2 = 21. "
    "Area = √[s(s-a)(s-b)(s-c)] = √[21×8×7×6] = √7056 = 84.",
    "Heron's: s = semi-perimeter. Area = √[s(s-a)(s-b)(s-c)]. "
    "13-14-15 triangle is a classic! Area = 84. Memorize this triplet.",
    "Jaise ek triangular plot ka area nikalna hai. Semi-perimeter se formula apply karo. "
    "13-14-15 ka area 84 — ye yaad karo as a shortcut!"
))

story.append(q_table(
    "M-6", "Venn Diagrams & Sets",
    "In a class of 50, 30 play cricket, 25 play football, 10 play both. How many play neither?",
    "Answer: 5",
    "Using inclusion-exclusion: |C∪F| = |C| + |F| - |C∩F| = 30 + 25 - 10 = 45. "
    "Neither = Total - |C∪F| = 50 - 45 = 5.",
    "Formula: n(A∪B) = n(A) + n(B) - n(A∩B). Neither = Total - n(A∪B).",
    "College mein: 30 cricket khelne waale, 25 football waale, 10 dono. "
    "Bina kisi game ke = 50 - 45 = 5 bacche ghar pe bethte hain!"
))

story.append(PageBreak())

# ─── COMMUNICATION ───────────────────────────────────────────────────────────
story.append(banner("💬 SECTION C: COMMUNICATION ABILITY — GRAMMAR & VOCABULARY", PURPLE))
story.append(Spacer(1, 4))
story.append(info_box("50 Questions | 50 Marks | EASIEST section to score high (aim 38-45+). "
                        "Grammar rules and vocabulary can be revised in 2 hours!"))
story.append(Spacer(1, 4))

story.append(Paragraph("GRAMMAR RULES — HIGH FREQUENCY IN ICET", H2))
grammar_rules = [
    ["Grammar Topic", "Rule", "Example", "Trick to Remember"],
    ["Subject-Verb Agreement", "Singular subject → singular verb. Plural → plural.", 
     "She GOES. They GO.", "He/She/It → add 'S' to verb"],
    ["Tenses", "Simple Past for completed actions. Present Perfect for recent actions with 'since/for'.", 
     "I HAVE LIVED here since 2000.\nI LIVED there in 2000.", "'Since/For' = Present Perfect"],
    ["Articles (a/an/the)", "a + consonant sound. an + vowel sound. the = specific.", 
     "a university (u=yoo sound)\nan hour (h is silent)", "Sound matters, not spelling!"],
    ["Prepositions", "In (month/year), On (day/date), At (time/place).", 
     "On Monday, In July, At 5pm, At school", "MONTH=IN, DAY=ON, TIME=AT"],
    ["Active-Passive", "Active: Subject+Verb+Object. Passive: Object+is/was+V3+by+Subject.", 
     "Ram wrote a letter → A letter was written by Ram.", "Passive = is/was/were + V3"],
    ["Degrees of Comparison", "Positive→Comparative→Superlative.", 
     "Good → Better → Best\nBad → Worse → Worst", "Irregular ones: good/bad/far — memorize!"],
    ["Conditionals", "If + Simple Present, will + V1 (Type 1 - real).\nIf + Simple Past, would + V1 (Type 2 - unreal).", 
     "If it rains, I will stay.\nIf I were rich, I would travel.", "Will=real future, Would=unreal/imaginary"],
]
gram_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PURPLE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, PURPLE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[PURPLE_LT, colors.white]),
    ("VALIGN",     (0,0), (-1,-1), "TOP"),
    ("BACKGROUND", (3,1), (3,-1), YELLOW_LT),
    ("FONTNAME",   (3,1), (3,-1), "Helvetica-Bold"),
])
story.append(Table(grammar_rules, colWidths=[30*mm, 48*mm, 47*mm, 46*mm], style=gram_ts))
story.append(Spacer(1, 6))

story.append(Paragraph("BUSINESS VOCABULARY — HIGH-FREQUENCY WORDS IN ICET", H2))
vocab_data = [
    ["Word", "Meaning", "Word", "Meaning"],
    ["Invoice", "Bill sent by seller to buyer", "Remittance", "Payment sent to a person/company"],
    ["Prospectus", "Document describing company details", "Debenture", "Long-term bond/loan certificate"],
    ["Dividend", "Share of profit given to shareholders", "Depreciation", "Decrease in asset value over time"],
    ["Ledger", "Book of all financial accounts", "Collateral", "Asset pledged as security for loan"],
    ["Amortization", "Gradual repayment of debt", "Consignment", "Goods sent to agent for sale"],
    ["Arbitration", "Settling dispute without going to court", "Franchise", "License to operate under brand name"],
    ["Assets", "What company owns (buildings, cash)", "Liabilities", "What company owes (loans, debts)"],
    ["Equity", "Ownership value in a company", "Turnover", "Total revenue/sales of company"],
]
voc_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), PURPLE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, PURPLE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[PURPLE_LT, colors.white]),
    ("BACKGROUND", (0,1), (0,-1), LIGHT_BLUE),
    ("BACKGROUND", (2,1), (2,-1), LIGHT_BLUE),
    ("FONTNAME",   (0,1), (0,-1), "Helvetica-Bold"),
    ("FONTNAME",   (2,1), (2,-1), "Helvetica-Bold"),
])
story.append(Table(vocab_data, colWidths=[30*mm, 62*mm, 30*mm, 49*mm], style=voc_ts))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 3: SMART EXAM STRATEGY
# ═══════════════════════════════════════════════════════════
story.append(banner("🎯 SMART EXAM STRATEGY — HOW TO SCORE MAXIMUM IN 150 MINS", MED_BLUE))
story.append(Spacer(1, 4))

story.append(Paragraph("TIME MANAGEMENT PLAN", H2))
time_plan = [
    ["Phase", "Time", "Section", "Target Questions", "Strategy"],
    ["START", "0-5 min", "All", "—", "Read instructions. Calm down. Remember: NO NEGATIVE MARKING."],
    ["Phase 1", "5-50 min (45 min)", "Section C: Communication", "50/50", 
     "START here! Easiest section. Vocabulary & grammar = fast marks. Aim: 40+ correct in 30 min, use 15 min for comprehension."],
    ["Phase 2", "50-95 min (45 min)", "Section A: Analytical", "45/45", 
     "DS: 20 Q in 15 min (45 sec each). Series/Coding: 20 Q in 20 min. Others: 5 Q in 10 min."],
    ["Phase 3", "95-145 min (50 min)", "Section B: Mathematical", "75/75",
     "Arithmetic first (25 Q, 20 min). Algebra & geometry (30 Q, 20 min). Stats/Sets (20 Q, 10 min)."],
    ["Buffer", "145-150 min (5 min)", "All", "Review flags", "Go back to flagged questions. Fill any skipped bubbles."],
]
tp_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), MED_BLUE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (-1,1), GREY_LIGHT),
    ("BACKGROUND", (0,2), (-1,2), GREEN_LT),
    ("BACKGROUND", (0,3), (-1,3), LIGHT_BLUE),
    ("BACKGROUND", (0,4), (-1,4), YELLOW_LT),
    ("BACKGROUND", (0,5), (-1,5), ORANGE_LT),
    ("BOX",        (0,0), (-1,-1), 1.5, MED_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.grey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("ALIGN",      (0,0), (3,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
])
story.append(Table(time_plan, colWidths=[16*mm, 25*mm, 28*mm, 22*mm, 80*mm], style=tp_ts))
story.append(Spacer(1, 6))

story.append(Paragraph("ELIMINATION STRATEGY — HOW TO ELIMINATE WRONG OPTIONS", H2))
elim_rules = [
    "✅ RULE 1 — Extreme Options: Options that say 'always', 'never', 'all', 'none' are USUALLY wrong. Be cautious.",
    "✅ RULE 2 — Round Numbers: In calculation questions, if 3 options have round numbers and 1 is odd, odd is often correct.",
    "✅ RULE 3 — DS Questions: If one statement clearly gives MORE info, it's more likely to be sufficient. Lean towards Option 1 or 2 before considering 3 or 4.",
    "✅ RULE 4 — Grammar: Read the sentence aloud mentally. The grammatically 'flowing' option is usually correct.",
    "✅ RULE 5 — Series: In odd-one-out, eliminate options that clearly follow the pattern. The answer breaks the pattern.",
    "✅ RULE 6 — Units: Check if answer makes physical sense. E.g., area can't be negative, distance can't be zero.",
    "✅ RULE 7 — Guessing: If stuck, eliminate 2 options. Between remaining 2, choose the one that sounds more precise.",
]
for rule in elim_rules:
    story.append(Paragraph(rule, BULLET))

story.append(Spacer(1, 4))
story.append(warning_box("IF STUCK ON A QUESTION: Mark it and MOVE ON immediately! "
                          "Never spend more than 90 seconds on any single question. "
                          "Come back at the end. Remember: EVERY question = 1 mark!"))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 4: REVISION PAGE
# ═══════════════════════════════════════════════════════════
story.append(banner("⚡ SUPER REVISION PAGE — LAST MINUTE QUICK REFERENCE", ORANGE))
story.append(Spacer(1, 4))

story.append(Paragraph("MOST EXPECTED QUESTION TYPES (Based on 3-Paper Analysis)", H2))
expected = [
    ["#", "Topic", "What to Expect", "Answer Pattern"],
    ["1", "DS — Geometry", "Area/Volume/Perimeter with 2 clues", "Usually Option 1 or 3"],
    ["2", "DS — Finance", "SI, CI, Profit-Loss with missing rate/time", "Often Option 4 if Rate missing"],
    ["3", "Number Series Odd-One-Out", "7-8 numbers, one breaks pattern", "Check primes, multiples, digit sums"],
    ["4", "Letter Coding", "LWDC type, shift by fixed number", "Find shift, apply uniformly"],
    ["5", "Fraction Series Odd-One-Out", "Numerators and denominators have separate patterns", "Check N and D separately"],
    ["6", "Date/Time Problems", "Bus/train intervals, arrival/departure", "Draw timeline, work backwards"],
    ["7", "SI/CI Problems", "Find missing variable", "Write formula, substitute knowns"],
    ["8", "Percentage", "% more/less, price changes, election", "Use base = 100 method"],
    ["9", "Quadratic Equations", "Nature of roots, value of discriminant", "D=b²-4ac always"],
    ["10", "Grammar: Tenses", "Choose correct verb form", "Look for time clues: since, for, yesterday"],
    ["11", "Vocabulary", "Business terms, computer terms", "Invoice, Ledger, Dividend, Equity"],
    ["12", "Reading Comprehension", "Answer based only on given passage", "Don't use general knowledge"],
]
exp_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ORANGE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, ORANGE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[ORANGE_LT, colors.white]),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN",      (0,0), (0,-1), "CENTER"),
    ("BACKGROUND", (3,1), (3,-1), YELLOW_LT),
    ("FONTNAME",   (3,1), (3,-1), "Helvetica-Bold"),
])
story.append(Table(expected, colWidths=[8*mm, 38*mm, 80*mm, 45*mm], style=exp_ts))
story.append(Spacer(1, 5))

story.append(Paragraph("IMPORTANT FORMULAS — FLASH CARDS FORMAT", H2))
flash_data = [
    ["📐 GEOMETRY", "📊 STATISTICS", "💰 FINANCE"],
    ["Circle: Area=πr², C=2πr\nRectangle: A=L×B, P=2(L+B)\nTriangle: A=½bh (Heron's: √s(s-a)(s-b)(s-c))\nCone: V=⅓πr²h, l²=r²+h²\nSphere: V=4/3πr³, A=4πr²\nCylinder: V=πr²h", 
     "Mean = Sum/n\nMedian: Arrange, pick middle\n(even n: avg of 2 middle)\nMode: Most frequent value\nStd Dev: √[Σ(x-mean)²/n]\nVariance = (Std Dev)²",
     "SI = PRT/100\nCI: A=P(1+R/100)^n\nProfit%=(Profit/CP)×100\nLoss%=(Loss/CP)×100\nDiscount%=(Discount/MP)×100\nSP=MP×(1-D/100)"],
    ["📝 ALGEBRA", "🔢 NUMBERS", "⚡ SHORTCUTS"],
    ["Quadratic: ax²+bx+c=0\nRoots: [-b±√(b²-4ac)]/2a\nD>0: real distinct\nD=0: real equal\nD<0: complex\na²-b²=(a+b)(a-b)\n(a+b)²=a²+2ab+b²",
     "LCM × HCF = Product of 2 numbers\nPrime test: Not div by 2,3,5,7\nSeven primes < 20: 2,3,5,7,11,13,17,19\nDigit sum ÷ 9 → div by 9\nLast digit rule for divisibility by 2,5",
     "x% of y = y% of x (commutative!)\n% more: If A=B+r%, then B is less than A by r/(100+r)%\nSpeed avg: 2S1S2/(S1+S2) (NOT arithmetic avg)\n1 km/h = 5/18 m/s\nAP sum = n/2(first+last)"],
]
flash_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), MED_BLUE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,-1), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (-1,1), GREEN_LT),
    ("BACKGROUND", (0,2), (-1,2), GREY_LIGHT),
    ("BACKGROUND", (0,3), (-1,3), ORANGE),
    ("TEXTCOLOR",  (0,3), (-1,3), colors.white),
    ("BACKGROUND", (0,4), (-1,4), YELLOW_LT),
    ("BOX",        (0,0), (-1,-1), 1, MED_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.grey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("VALIGN",     (0,0), (-1,-1), "TOP"),
    ("ALIGN",      (0,0), (-1,0), "CENTER"),
    ("ALIGN",      (0,2), (-1,2), "CENTER"),
    ("FONTSIZE",   (0,0), (-1,0), 11),
    ("FONTSIZE",   (0,2), (-1,2), 11),
])
story.append(Table(flash_data, colWidths=[58*mm, 58*mm, 55*mm], style=flash_ts))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 5: STUDY PLAN
# ═══════════════════════════════════════════════════════════
story.append(banner("📅 DAY-WISE STUDY PLAN: TODAY TO EXAM (14th May)", TEAL))
story.append(Spacer(1, 4))
story.append(info_box("Today = May 4th, 2026. Exam = May 14th, 2026 (Morning). You have 10 days! "
                        "Use this structured plan to cover everything systematically.", GREEN_LT, GREEN))
story.append(Spacer(1, 4))

plan_data = [
    ["Day", "Date", "Focus Topic", "Study Time", "Practice Target", "Revision"],
    ["Day 1", "May 4\n(Today)", "DATA SUFFICIENCY\n(20 Q = 20 marks)", "3 hours",
     "Solve 30 DS questions\n(Q1-20 from all 3 papers)", "Learn Options 1,2,3,4 meanings by heart"],
    ["Day 2", "May 5", "NUMBER SERIES\n& ODD-ONE-OUT", "2.5 hrs",
     "30 series questions\n(variety: number, fraction, mixed)", "Digit sum, prime check, cube/square patterns"],
    ["Day 3", "May 6", "LETTER SERIES\n& CODING-DECODING", "2 hrs",
     "25 coding questions\n(shifting patterns, analogy types)", "LAMP→LWDC type codes, +/-N shift rules"],
    ["Day 4", "May 7", "ARITHMETIC:\n% + Profit/Loss + Ratio", "3 hrs",
     "40 arithmetic questions\n(mixed: %, profit, ratio, average)", "All key formulas from revision page"],
    ["Day 5", "May 8", "ARITHMETIC:\nSI/CI + Time/Work + Speed", "3 hrs",
     "35 questions on SI, CI,\nTime-Work, Speed-Distance", "SI=PRT/100, CI formula, D=ST"],
    ["Day 6", "May 9", "ALGEBRA + MATRICES\n+ GEOMETRY", "3 hrs",
     "30 algebra questions\n(quadratic, matrices, areas)", "Discriminant rule, Heron's formula"],
    ["Day 7", "May 10", "COMMUNICATION:\nGrammar + Vocabulary", "2.5 hrs",
     "50 English questions\n(grammar rules + business vocab)", "7 grammar rules table, 20 business words"],
    ["Day 8", "May 11", "FULL MOCK TEST\n(Paper 1: June 8 Shift 1)", "2.5 hrs",
     "Attempt full paper (200 Q)\nTimed: 150 minutes exactly", "Review wrong answers, identify weak areas"],
    ["Day 9", "May 12", "WEAK AREA FIX\n+ STATISTICS + SETS", "3 hrs",
     "Focus on Day 8 mistakes\n+ 20 stats/sets questions", "Mean, Median, Mode formula, Venn diagram formula"],
    ["Day 10", "May 13\n(Day before)", "FULL REVISION\n+ LAST MOCK", "3 hrs",
     "Attempt Paper 2 (June 8 Shift 2)\nAll formulas revision", "Sleep early! Keep admit card ready!"],
    ["EXAM", "May 14\n(Morning)", "EXECUTION DAY", "150 min",
     "Target: 150+ marks\nStart with Section C (Communication)", "Stay calm. No negative marking!"],
]
plan_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1.5, TEAL),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN",      (0,0), (1,-1), "CENTER"),
    ("ALIGN",      (3,0), (4,-1), "CENTER"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, GREY_LIGHT]),
    ("BACKGROUND", (0,8), (-1,8), colors.HexColor("#FFF9C4")),
    ("BACKGROUND", (0,10), (-1,10), colors.HexColor("#FCE4EC")),
    ("FONTNAME",   (0,10), (-1,10), "Helvetica-Bold"),
    ("BACKGROUND", (0,-1), (-1,-1), GOLD),
    ("TEXTCOLOR",  (0,-1), (-1,-1), DARK_BLUE),
    ("FONTNAME",   (0,-1), (-1,-1), "Helvetica-Bold"),
])
story.append(Table(plan_data, colWidths=[12*mm, 16*mm, 38*mm, 18*mm, 47*mm, 40*mm], style=plan_ts))
story.append(Spacer(1, 5))

story.append(Paragraph("DAILY STUDY ROUTINE TEMPLATE", H2))
routine_data = [
    ["Time Slot", "Activity", "Duration"],
    ["Session 1 (Morning)", "Study new topic — understand concepts, read formulas", "60-90 min"],
    ["Break", "Walk, eat, refresh", "20-30 min"],
    ["Session 2 (Mid-day)", "Solve practice questions — strictly timed (1 min per Q)", "60-90 min"],
    ["Break", "Light reading or rest", "30 min"],
    ["Session 3 (Evening)", "Review wrong answers. Note patterns. Revise formulas.", "45-60 min"],
    ["Night (Optional)", "10-minute re-read of formula sheet before sleeping", "10 min"],
]
rout_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, TEAL),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 9.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),7),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[GREEN_LT, YELLOW_LT]),
    ("FONTNAME",   (0,2), (-1,2), "Helvetica-Oblique"),
    ("FONTNAME",   (0,4), (-1,4), "Helvetica-Oblique"),
    ("TEXTCOLOR",  (0,2), (0,2), colors.grey),
    ("TEXTCOLOR",  (0,4), (0,4), colors.grey),
    ("ALIGN",      (2,0), (2,-1), "CENTER"),
])
story.append(Table(routine_data, colWidths=[45*mm, 103*mm, 23*mm], style=rout_ts))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# SECTION 6: LAST MINUTE CHEAT SHEET
# ═══════════════════════════════════════════════════════════
story.append(banner("🚨 LAST-MINUTE POWER CHEAT SHEET — READ THIS ON EXAM MORNING!", RED))
story.append(Spacer(1, 4))

cheat_data = [
    ["🎯 GOLDEN RULES FOR EXAM DAY", ""],
    ["1. START WITH SECTION C (Communication)", "Easiest marks first. Build confidence. 50 Q in 35-40 mins."],
    ["2. NO NEGATIVE MARKING → ATTEMPT ALL", "NEVER leave any question blank. Always mark something."],
    ["3. DS Questions: 45 sec max each", "Options: 1=Only I works | 2=Only II | 3=Both | 4=Neither"],
    ["4. Series: Check differences first", "Differences increasing by 2, 4... is most common pattern."],
    ["5. If stuck → Eliminate 2, guess from 2", "Remove clearly wrong options. 50-50 guess is still 50% chance."],
    ["6. Don't waste time re-checking", "First instinct is usually correct. Move forward."],
    ["7. Mathematical Ability: Arithmetic first", "Numbers, %, Profit/Loss, SI/CI = fastest + most questions."],
    ["8. Reading Comp: Skim first, then answer", "Read question first, then find answer in passage. Don't over-think."],
]
cheat_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), RED),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("SPAN",       (0,0), (-1,0)),
    ("ALIGN",      (0,0), (-1,0), "CENTER"),
    ("BOX",        (0,0), (-1,-1), 1.5, RED),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 9.5),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("FONTNAME",   (0,1), (0,-1), "Helvetica-Bold"),
    ("TEXTCOLOR",  (0,1), (0,-1), RED),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[RED_LT, colors.white]),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
])
story.append(Table(cheat_data, colWidths=[75*mm, 96*mm], style=cheat_ts))
story.append(Spacer(1, 5))

story.append(Paragraph("SECTION-WISE SCORING TARGETS", H2))
score_data = [
    ["Section", "Total Marks", "Easy Target", "Good Target", "Best Target"],
    ["Section C: Communication", "50", "32-35", "38-42", "45-48"],
    ["Section A: Analytical Ability", "75", "45-50", "55-60", "65-70"],
    ["Section B: Mathematical Ability", "75", "40-45", "50-55", "60-65"],
    ["TOTAL", "200", "120-130", "143-157", "170-183"],
]
score_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (-1,1), PURPLE_LT),
    ("BACKGROUND", (0,2), (-1,2), LIGHT_BLUE),
    ("BACKGROUND", (0,3), (-1,3), GREEN_LT),
    ("BACKGROUND", (0,4), (-1,4), GOLD),
    ("TEXTCOLOR",  (0,4), (-1,4), DARK_BLUE),
    ("FONTNAME",   (0,4), (-1,4), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1.5, DARK_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.grey),
    ("FONTSIZE",   (0,0), (-1,-1), 10),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("ALIGN",      (1,0), (-1,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("TEXTCOLOR",  (2,1), (2,-1), colors.HexColor("#555555")),
    ("TEXTCOLOR",  (3,1), (3,-1), MED_BLUE),
    ("FONTNAME",   (3,1), (3,-1), "Helvetica-Bold"),
    ("TEXTCOLOR",  (4,1), (4,-1), GREEN),
    ("FONTNAME",   (4,1), (4,-1), "Helvetica-Bold"),
])
story.append(Table(score_data, colWidths=[55*mm, 22*mm, 30*mm, 30*mm, 34*mm], style=score_ts))
story.append(Spacer(1, 5))

story.append(Paragraph("COMMON PATTERNS FROM ALL 3 PAPERS", H2))
common_patterns = [
    ["Pattern Observed", "Appears In", "Expected in Exam?"],
    ["Data Sufficiency: Finance problems (SI, Profit) → usually Option 4", "All 3 papers", "★★★★★ Very Likely"],
    ["Data Sufficiency: Geometry (area/volume) → usually Option 1 or 3", "All 3 papers", "★★★★★ Very Likely"],
    ["Odd-one-out: Numbers with prime/composite pattern", "All 3 papers", "★★★★★ Very Likely"],
    ["Letter coding: Shift +2 or -2 pattern (LWDC type)", "All 3 papers", "★★★★☆ Likely"],
    ["Fraction series: Numerator and denominator have separate AP patterns", "2 out of 3 papers", "★★★★☆ Likely"],
    ["Date/Time: Bus/train interval backward calculation", "2 out of 3 papers", "★★★★☆ Likely"],
    ["Grammar: Tense correction questions (perfect tense vs simple)", "All 3 papers", "★★★★★ Very Likely"],
    ["Vocabulary: Invoice, Dividend, Debenture, Ledger type words", "All 3 papers", "★★★★★ Very Likely"],
    ["Math: % more than → % less than conversion", "2 out of 3 papers", "★★★★☆ Likely"],
    ["Math: 13-14-15 triangle or similar mensuration shortcuts", "2 out of 3 papers", "★★★☆☆ Moderate"],
]
cp_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,0), DARK_BLUE),
    ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
    ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
    ("BOX",        (0,0), (-1,-1), 1, DARK_BLUE),
    ("INNERGRID",  (0,0), (-1,-1), 0.5, colors.lightgrey),
    ("FONTSIZE",   (0,0), (-1,-1), 8.5),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, GREY_LIGHT]),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN",      (1,0), (2,-1), "CENTER"),
    ("TEXTCOLOR",  (2,1), (2,6), GREEN),
    ("TEXTCOLOR",  (2,7), (2,-1), MED_BLUE),
    ("FONTNAME",   (2,1), (2,-1), "Helvetica-Bold"),
])
story.append(Table(common_patterns, colWidths=[92*mm, 30*mm, 49*mm], style=cp_ts))
story.append(Spacer(1, 6))

# Final motivational box
mot_ts = TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), DARK_BLUE),
    ("BOX",        (0,0), (-1,-1), 3, GOLD),
    ("TOPPADDING", (0,0), (-1,-1), 12),
    ("BOTTOMPADDING",(0,0),(-1,-1),12),
    ("LEFTPADDING",(0,0),(-1,-1),15),
    ("RIGHTPADDING",(0,0),(-1,-1),15),
])
mot_text = (
    "YOU GOT THIS! 🎯\n\n"
    "Remember: 200 questions, 150 minutes, NO negative marking.\n"
    "Every question you attempt is a chance to score. \n"
    "Start with Communication, then Analytical, then Math.\n"
    "Use elimination. Trust your preparation. All the best! 🚀"
)
story.append(Table([[Paragraph(mot_text, S("Normal", fontSize=12, textColor=GOLD, 
                                            fontName="Helvetica-Bold", alignment=TA_CENTER, leading=18))]],
                   colWidths=[W - 36*mm], style=mot_ts))

doc.build(story)
print("PDF created successfully!")