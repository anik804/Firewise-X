# -*- coding: utf-8 -*-
"""
Generator script for two comprehensive Bengali DOCX documents:
1. FIREWISE-X_Research_Analysis_Report_BN.docx
2. FIREWISE-X_Website_User_Guide_BN.docx
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets cell padding."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_header(doc, title_text, subtitle_text):
    """Adds a stylish header section."""
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run(title_text)
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(24)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(11, 44, 91) # Deep Navy

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run(subtitle_text)
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(13)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(79, 110, 138) # Steel Blue

    doc.add_paragraph() # Spacer

def add_heading_1(doc, text):
    h = doc.add_heading(level=1)
    run = h.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(16, 52, 96)
    return h

def add_heading_2(doc, text):
    h = doc.add_heading(level=2)
    run = h.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 86, 160)
    return h

def add_callout(doc, text, title="নোট / মূল বার্তা:"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    p = cell.paragraphs[0]
    r_title = p.add_run(f"📌 {title} ")
    r_title.bold = True
    r_title.font.size = Pt(10.5)
    r_title.font.color.rgb = RGBColor(16, 52, 96)
    
    r_text = p.add_run(text)
    r_text.font.size = Pt(10)
    r_text.font.color.rgb = RGBColor(33, 37, 41)
    doc.add_paragraph() # Spacer

# ==============================================================================
# DOCUMENT 1: RESEARCH & ANALYSIS REPORT
# ==============================================================================
def generate_research_doc():
    doc = docx.Document()
    
    # Page Setup
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    add_header(
        doc,
        "FIREWISE-X: নাসা মাইক্রোগ্র্যাভিটি দহন বিজ্ঞান ও গবেষণা বিশ্লেষণ রিপোর্ট",
        "NASA International Space Apps Challenge 2026 | Challenge: Flame in Freefall\nইনভেস্টিগেশন: NASA BASS-II (PSI-25) | DOI: 10.60555/4qc4-de67"
    )

    add_callout(
        doc,
        "এই গবেষণা রিপোর্টে নাসা স্পেস অ্যাপস চ্যালেঞ্জের জন্য প্রস্তুতকৃত FIREWISE-X প্রজেক্টের যাবতীয় বৈজ্ঞানিক ভিত্তি, আইএসএস-এর BASS-II এক্সপেরিমেন্টের ডেটাসেট বিশ্লেষণ, রাসায়নিক পরিমাপ, ক্লাসিক্যাল কম্পিউটার ভিশন ব্যবহারের যৌক্তিকতা এবং অফিসিয়াল টেকনিক্যাল পেপারের উদ্ধৃতি সম্পূর্ণ বাংলায় লিপিবদ্ধ করা হয়েছে।",
        "নির্বাহী সারসংক্ষেপ (Executive Summary)"
    )

    # Section 1
    add_heading_1(doc, "১. গবেষণার পটভূমি ও মূল সমস্যা (The Microgravity Flame Paradox)")
    p = doc.add_paragraph()
    p.add_run(
        "পৃথিবীতে আগুন লাগলে বায়ুমণ্ডলের স্বাভাবিক পরিচলন প্রক্রিয়ায় (Natural Buoyancy / Thermal Convection) "
        "গরম ধোঁয়া ও গ্যাস হালকা হয়ে উপরের দিকে উঠে যায় এবং নিচের দিক থেকে তাজা অক্সিজেনযুক্ত বাতাস শিখায় প্রবেশ করে। "
        "এর ফলে পৃথিবীতে আগুন সাধারণত শঙ্কু আকৃতির (🔺 Cone shape) হয়ে উপরের দিকে দ্রুত ছড়ায়। নাসার ঐতিহ্যবাহী গ্রাউন্ড স্ট্যান্ডার্ড "
        "(NASA-STD-6001 Test #1) এই ওপরের দিকে পোড়ার প্রক্রিয়াকে 'Worst Case' বা সবচেয়ে ঝুঁকিপূর্ণ ধরে ম্যাটেরিয়ালের অগ্নি-নিরাপত্তা পরীক্ষা করে।\n\n"
        "কিন্তু মহাশূন্যে বা আন্তর্জাতিক মহাকাশ স্টেশনে (ISS) কোনো কার্যকর মাধ্যাকর্ষণ নেই (Microgravity)। ফলে:\n"
        "১. কোনো প্রাকৃতিক পরিচলন বা প্লবতা থাকে না (No buoyancy-driven flow)।\n"
        "২. গরম গ্যাস উপরে উঠতে পারে না; শিখা চারদিকে সমানভাবে ছড়িয়ে গোলাকার (🔵 Spherical / Hemispherical) রূপ নেয়।\n"
        "৩. আগুন খুব ধীরগতিতে জ্বলে, কিন্তু এটি অত্যন্ত মারাত্মক অসম্পূর্ণ দহন (Incomplete Pyrolysis/Combustion) তৈরি করে।\n"
        "৪. সীমিত বায়ুচলাচলে (Forced Ventilation) প্লাস্টিক ও ইনসুলেশন ম্যাটেরিয়াল ধিকিধিকি পুড়ে প্রচুর পরিমাণে বিষাক্ত কার্বন মনোক্সাইড (CO) নির্গত করে, যা মহাকাশচারীদের জীবনকে সরাসরি বিপদে ফেলে।"
    )

    # Section 2
    add_heading_1(doc, "২. নাসা BASS-II (PSI-25) ডেটাসেটের বিশদ বিশ্লেষণ")
    p = doc.add_paragraph()
    p.add_run(
        "BASS-II (Burning and Suppression of Solids - II) হলো নাসার ফিজিক্যাল সায়েন্সেস ইনফরমেটিক্স (PSI) রিপোজিটরির অধীনে পরিচালিত "
        "একটি অত্যন্ত গুরুত্বপূর্ণ মহাকাশ ফ্লাইট এক্সপেরিমেন্ট (DOI: 10.60555/4qc4-de67)। এটি আন্তর্জাতিক মহাকাশ স্টেশনের "
        "মাইক্রোগ্র্যাভিটি সায়েন্স গ্লোভসবক্স (MSG)-এ একটি ছোট উইন্ড টানেলে সফলভাবে সম্পন্ন হয়েছিল।"
    )

    # Table of Dataset Stats
    table = doc.add_table(rows=7, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    stats = [
        ("তদন্তের নাম (Investigation)", "Burning and Suppression of Solids - II (BASS-II / PSI-25)"),
        ("ফ্লাইট প্ল্যাটফর্ম (Flight Facility)", "International Space Station (ISS), Microgravity Science Glovebox (MSG)"),
        ("মোট টেস্টের সংখ্যা (Total Flight Tests)", "১২৯টি সম্পন্ন পরীক্ষা (CSV ফাইলে নথিবদ্ধ)"),
        ("প্রধান গবেষকবৃন্দ (Principal Investigators)", "৬ জন শীর্ষ বিজ্ঞানী (Bhattacharjee, Miller, Olson, T'ien, Fernandez-Pello, Ferkul)"),
        ("অক্সিজেন পরিসর (Oxygen Concentration)", "১৩.৫% থেকে ২২.২% (নাইট্রোজেন মিশিয়ে ক্যাবিনের অক্সিজেন কমিয়ে পরীক্ষা)"),
        ("বিষাক্ত CO গ্যাস নির্গমন (Peak Carbon Monoxide)", "৯৫০ ppm পর্যন্ত রেকর্ড করা হয়েছে (টেস্ট O13a)"),
        ("ফ্লাইট ভিডিও রেকর্ড (Raw Video Footage)", "টেস্ট B1, T22 সহ ডজনখানেক আসল মহাকাশ ক্যামেরা ফুটেজ ও স্টিল সিকোয়েন্স")
    ]
    for row_idx, (k, v) in enumerate(stats):
        cell_k, cell_v = table.cell(row_idx, 0), table.cell(row_idx, 1)
        cell_k.width = Inches(2.5)
        cell_v.width = Inches(4.5)
        cell_k.text = k
        cell_v.text = v
        cell_k.paragraphs[0].runs[0].font.bold = True
        set_cell_background(cell_k, "F7F9FB")
        set_cell_margins(cell_k)
        set_cell_margins(cell_v)
    doc.add_paragraph()

    # Section 3
    add_heading_1(doc, "৩. ৬ জন প্রধান বিজ্ঞানী (PIs) ও তাদের গবেষণার ক্ষেত্র")
    p = doc.add_paragraph()
    p.add_run(
        "BASS-II এক্সপেরিমেন্টে ৬ জন শীর্ষ আমেরিকান গবেষক আলাদা আলাদা বৈজ্ঞানিক প্রশ্ন নিয়ে কাজ করেছেন:\n\n"
        "১. ড. সুব্রত ভট্টাচার্য (Bhattacharjee - SDSU): ২২টি টেস্ট (B1-B22)। তিনি ১০০ থেকে ৪০০ মাইক্রোমিটার পুরু পাতলা PMMA ফিল্ম "
        "বাতাসের বিপরীত দিকে (Opposed Flow) কীভাবে পোড়ে এবং ফ্যান বন্ধ করলে রেডিয়েটিভ এক্সটিংকশনে কীভাবে নিভে যায় তা প্রমাণ করেছেন।\n\n"
        "২. ড. ফ্লেচার জে. মিলার (Miller - SDSU): ২০টি টেস্ট (M1-M20)। তিনি ১ থেকে ৫ মিলিমিটার পুরু PMMA স্ল্যাব নিয়ে কাজ করেছেন। "
        "তার পরীক্ষায় দেখা গেছে পুরু স্ল্যাব দুই দিক থেকে জ্বলে (Two-sided burn) ক্যাবিনের অক্সিজেন ৩.২% কমিয়ে ফেলে এবং ৫০০+ ppm CO তৈরি করে।\n\n"
        "৩. ড. স্যান্ড্রা এল. ওলসন (Olson - NASA GRC): ২২টি টেস্ট (O1-O22)। তিনি ১/৪\", ৩/৮\" এবং ১/২\" ব্যাসের PMMA রড নিয়ে ফ্ল্যামেবিলিটি বাউন্ডারি "
        "নির্ধারণ করেছেন। তার পরিচালিত O13a টেস্টে পুরো ডেটাসেটের সর্বোচ্চ ৯৫০ ppm বিষাক্ত CO নির্গত হয়েছিল।\n\n"
        "৪. ড. কার্লোস ফার্নান্দেজ-পেলো (Fernandez-Pello - UC Berkeley): ২৫টি টেস্ট (P1-P25)। তিনি PMMA সিলিন্ডারে এক্সটিংকশন বা নিভে যাওয়ার সীমা "
        "এবং ফ্যানের স্পিড বারবার পরিবর্তনের (Oscillating flow) প্রভাব গবেষণা করেছেন।\n\n"
        "৫. ড. জেমস এস. তিয়েন (T'ien - CWRU): ২৯টি টেস্ট (T1-T29)। তিনি স্পেসক্রাফটের ইনসুলেশন উপাদান SIBAL এবং গোলাকার জ্বালানিতে "
        "বাতাসের অনুকূলে (Concurrent flow) শিখার বৃদ্ধি ও নিভে যাওয়া পরীক্ষা করেছেন।\n\n"
        "৬. ড. পল ভি. ফারকুল (Ferkul - NASA GRC): ৪টি টেস্ট (F1-F4)। তিনি মহাকাশচারীদের পোশাকের উপাদান Nomex III অ্যারামিড ফ্যাব্রিক "
        "এবং মোমবাতির শিখা পরীক্ষা করে মহাকাশ পোশাকের উচ্চ অগ্নি-প্রতিরোধ ক্ষমতা নিশ্চিত করেছেন।"
    )

    # Section 4
    add_heading_1(doc, "৪. বৈজ্ঞানিক পরিমাপ ও রাসায়নিক সম্পর্কের পর্যবেক্ষণ")
    p = doc.add_paragraph()
    p.add_run(
        "১২৯টি টেস্টের ডেটা অ্যানালাইসিস করে আমরা তিনটি মূল রাসায়নিক সম্পর্ক দেখতে পাই:\n\n"
        "ক. অক্সিজেন হ্রাস বনাম CO₂ বৃদ্ধি: দহনের মূল সমীকরণ হলো Fuel + O₂ → CO₂ + H₂O + Heat। যেসব টেস্টে বেশি অক্সিজেন খরচ হয়েছে "
        "(যেমন Miller-এর M5 টেস্টে ৩.২% O₂ হ্রাস), সেখানে CO₂ উৎপাদন সর্বোচ্চ ৩.২২%-এ পৌঁছেছে।\n\n"
        "খ. অসম্পূর্ণ দহন ও কার্বন মনোক্সাইড (CO) সংকট: মহাকাশে বাতাস ধীরে চললে আগুনের ভেতরের অংশে পর্যাপ্ত অক্সিজেন পৌঁছাতে পারে না। "
        "ফলে সম্পূর্ণ দহনের বদলে অসম্পূর্ণ দহন ঘটে প্রচুর CO গ্যাস নির্গত হয়। টেস্ট O13a-তে সেন্সরের রিডিং ৯৫০ ppm ছাড়িয়ে গিয়েছিল, "
        "যা পৃথিবীর যেকোনো আবাসিক সুরক্ষা সীমার (৫০ ppm) চেয়ে ১৯ গুণ বেশি বিপজ্জনক!\n\n"
        "গ. ফ্লো রেস্ট্রিক্টর ও এক্সটিংকশন বনাম ব্লোঅফ: ফ্লো রেস্ট্রিক্টর ০ (সর্বোচ্চ বাতাস) দিলে আগুন তীব্রভাবে জ্বলে, কিন্তু অতিরিক্ত বাতাসে "
        "শিখা উবে যাওয়ার (Blow-off) ঘটনা ঘটে। অন্যদিকে ফ্লো রেস্ট্রিক্টর ২ (কম বাতাস) দিলে বাতাস কমে গিয়ে আগুন নিজে নিজেই নিভে যায় (Radiative Extinction)।"
    )

    # Section 5
    add_heading_1(doc, "৫. কেন ডিপ লার্নিং নয়? ক্লাসিক্যাল সিভি ও এক্সপ্লেনেবল এআই-এর যৌক্তিকতা")
    p = doc.add_paragraph()
    p.add_run(
        "নাসা স্পেস অ্যাপস প্রতিযোগিতায় অনেক দল ভুল করে বিশাল আকারের নিউরাল নেটওয়ার্ক (YOLO, ResNet ইত্যাদি) ট্রেইন করার দাবি করে। "
        "আমাদের গবেষণায় এবং নাসার অফিসিয়াল রিভিউয়ারদের মূল্যায়নে পরিষ্কারভাবে উল্লেখ করা হয়েছে কেন এটি বৈজ্ঞানিকভাবে ভুল:\n\n"
        "১. স্মল-স্যাম্পল ওভারফিটিং (Small-Sample Overfitting): পুরো এক্সপেরিমেন্টে মাত্র ১২৯টি টেস্টের রেকর্ড রয়েছে। এতো ছোট ডেটাসেটে "
        "ডিপ লার্নিং চালালে তা মারাত্মক ওভারফিট করে এবং জাজরা এর কোনো গ্রহণযোগ্যতা দেন না।\n\n"
        "২. ব্ল্যাক-বক্স বনাম ব্যাখ্যামূলক বিজ্ঞান (Explainable Science): নাসা কোনো 'ব্ল্যাক-বক্স প্রেডিকশন' চায় না যেখানে এআই আন্দাজে কোনো ঝুঁকি শতাংশ বলে। "
        "নাসা চায় স্বচ্ছ পদার্থবিজ্ঞান ও প্রমাণভিত্তিক বিশ্লেষণ।\n\n"
        "৩. ক্লাসিক্যাল কম্পিউটার ভিশন (Classical CV): ফ্রেম-বাই-ফ্রেম আগুনের প্রজেক্টেড এরিয়া মাপার জন্য আমরা Rec.709 Luma থ্রেশহোল্ডিং "
        "(L = 0.2126R + 0.7152G + 0.0722B) ব্যবহার করেছি। এটি শতভাগ স্বচ্ছ, কোনো কাল্পনিক পিক্সেল তৈরি করে না এবং রিয়েল-টাইমে ব্রাউজারে চলে।\n\n"
        "৪. রোবাস্ট স্ট্যাটিস্টিক্যাল ডিটেকশন (Robust Z-Score): সেন্সর নয়েজ ও চরম স্পাইক (৯৫০ ppm) চিহ্নিত করতে আমরা সাধারণ স্ট্যান্ডার্ড ডেভিয়েশনের বদলে "
        "মিডিয়ান ও ম্যাড (Median Absolute Deviation) ভিত্তিক মডিফাইড Z-স্কোর ব্যবহার করেছি:\n"
    )
    
    # Formula callout
    add_callout(
        doc,
        "Z = 0.6745 × (x - median) / MAD\n"
        "এখানে MAD = median(|x - median|)। এই অ্যালগরিদমটি চরম আউটলায়ার থাকার পরেও স্থির বেসলাইন ধরে রাখতে পারে, যা সাধারণ গড়ের ক্ষেত্রে সম্ভব নয়।",
        "গাণিতিক সূত্র (Robust Modified Z-Score Formula)"
    )

    # Section 6
    add_heading_1(doc, "৬. পিয়ার-রিভিউড নাসার টেকনিক্যাল পেপার ও এভিডেন্স সংযোগ")
    p = doc.add_paragraph()
    p.add_run(
        "FIREWISE-X সিস্টেমের প্রতিটি অ্যানোমালি সরাসরি পিয়ার-রিভিউড জার্নাল পেপারের সাথে সংযুক্ত:\n\n"
        "১. Bhattacharjee et al. (2015) — Combustion and Flame (DOI: 10.1016/j.combustflame.2015.10.023): "
        "পাতলা ফিল্মে বাতাস বন্ধ করলে কেন আগুন নিভে যায় তার রেডিয়েটিভ এক্সটিংকশন সীমা প্রমাণ করে (টেস্ট B1-এর ভিত্তি)।\n\n"
        "২. Olson & Ferkul (2017) — Combustion and Flame (DOI: 10.1016/j.combustflame.2017.03.001): "
        "PMMA রডের অসম্পূর্ণ দহন এবং কম অক্সিজেনে ৯৫০ ppm পর্যন্ত বিষাক্ত CO নির্গমনের তাত্ত্বিক প্রমাণ দেয় (টেস্ট O13a-এর ভিত্তি)।\n\n"
        "৩. NASA/TM-20210011385 (2021) — BASS-II Summary Report (NTRS ID: 20210011385): "
        "আইএসএস-এর সম্পূর্ণ ১২৯টি টেস্টের অফিসিয়াল গ্রাউন্ড ট্রুথ ও ক্রু অবজারভেশন রেকর্ড।\n\n"
        "৪. Zhao, T'ien et al. (2016) — Proc. Combust. Inst. (DOI: 10.1016/j.proci.2016.06.028): "
        "SIBAL ফ্যাব্রিক ইনসুলেশন উপাদানের কনকারেন্ট ফ্লো ফ্লেম স্প্রেড ও কুয়েনচিং মডেল।\n\n"
        "৫. Shah, Miller et al. (2015) — ResearchGate 281871773: "
        "মাঝারি পুরুত্বের স্ল্যাবে গভীর পাইরোলাইসিস এবং চরম তাপ ও গ্যাস উৎপাদনের থার্মাল মডেল (টেস্ট M5-এর ভিত্তি)।"
    )

    # Section 7
    add_heading_1(doc, "৭. বৈজ্ঞানিক সততা ও অনেস্ট অ্যাবস্টেনশন (Honest Abstention)")
    p = doc.add_paragraph()
    p.add_run(
        "FIREWISE-X-এর সবচেয়ে বড় শক্তি হলো এর বৈজ্ঞানিক সততা। আমাদের সিস্টেম:\n"
        "• ভিডিও ক্যামেরায় স্কেল রুলার না থাকায় ক্ষেত্রফলকে বর্গ সেন্টিমিটার দাবি না করে পিক্সেল স্কয়ার (px²) হিসেবে প্রকাশ করে।\n"
        "• ২ডি প্রজেক্টেড এরিয়া থেকে আন্দাজে কোনো ৩ডি ভলিউম্যাট্রিক হিট রিলিজ রেট দাবি করে না।\n"
        "• কোনো ডেটা অনুপস্থিত থাকলে শূন্য (0) না বসিয়ে স্পষ্টভাবে 'Not Recorded' বলে অ্যাবস্টেইন (Abstain) করে।"
    )

    file_path = os.path.join(r"D:\Nasa FINAL", "FIREWISE-X_Research_Analysis_Report_BN.docx")
    doc.save(file_path)
    print(f"Successfully generated: {file_path}")

# ==============================================================================
# DOCUMENT 2: WEBSITE USER GUIDE & FEATURE WALKTHROUGH
# ==============================================================================
def generate_user_guide_doc():
    doc = docx.Document()
    
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    add_header(
        doc,
        "FIREWISE-X: ওয়েবসাইট ব্যবহার নির্দেশিকা ও সম্পূর্ণ ফিচার ওয়াকথ্রু",
        "Next.js ও ক্লায়েন্ট-সাইড ক্যানভাস চালিত মহাকাশ অগ্নি-নিরাপত্তা রিসার্চ ড্যাশবোর্ড\nলোকাল ইউআরএল: http://localhost:3000"
    )

    add_callout(
        doc,
        "এই নির্দেশিকায় FIREWISE-X ওয়েবসাইটের প্রতিটি মেনু, বোতাম, চার্ট, কম্পিউটার ভিশন টুল এবং ফিল্টারের কার্যপ্রণালী সহজ বাংলায় বিস্তারিত ব্যাখ্যা করা হয়েছে। প্রেজেন্টেশন বা মূল্যায়নের সময় কীভাবে ওয়েবসাইটটি প্রদর্শন করতে হবে, তা এই গাইডে বর্ণিত হয়েছে।",
        "ইউজার গাইড সারসংক্ষেপ"
    )

    # Tab 1: Navigation & Architecture
    add_heading_1(doc, "১. প্রযুক্তিগত আর্কিটেকচার ও নেভিগেশন বার")
    p = doc.add_paragraph()
    p.add_run(
        "FIREWISE-X একটি আধুনিক Next.js সিঙ্গেল-পেজ অ্যাপ্লিকেশন (SPA)। এটি সম্পূর্ণ অফলাইন-সেফ এবং ব্রাউজারেই আসল নাসার ডেটা প্রসেস করে।\n\n"
        "স্ক্রিনের শীর্ষে স্টিকি ন্যাভিগেশন বার রয়েছে, যার মধ্যে ৭টি প্রধান সেকশনের বোতাম রয়েছে:\n"
        "• 🔥 FIREWISE-X লোগো ও অফিসিয়াল নাসা ডেটাসেট ট্যাগ (NASA PSI-25 · BASS-II)\n"
        "• Home (হোম পেজ - `#/`)\n"
        "• Mission Control (মিশন কন্ট্রোল - `#/mc`)\n"
        "• 129 Tests Explorer (১২৯টি টেস্টের এক্সপ্লোরার - `#/exp`)\n"
        "• Flame Studio (CV) (কম্পিউটার ভিশন স্টুডিও - `#/flame`)\n"
        "• Sensors & Anomaly (সেন্সর ও অ্যানোমালি অ্যানালাইসিস - `#/sensor`)\n"
        "• Evidence Engine (এভিডেন্স ও রিসার্চ পেপার লাইব্রেরি - `#/evid`)\n"
        "• Compare Runs (পাশাপাশি দুটি টেস্ট তুলনা - `#/cmp`)"
    )

    # Tab 2: Home Page
    add_heading_1(doc, "২. হোম পেজ (Home — `#/`)")
    p = doc.add_paragraph()
    p.add_run(
        "হোম পেজটি পুরো প্রজেক্টের কেন্দ্রীয় পরিচিতি তুলে ধরে:\n\n"
        "১. হিরো ব্যানার (Hero Section): মহাকাশের দহন প্যারাডক্স (Understand the Flame. Follow the Evidence) সংক্ষেপে তুলে ধরে। "
        "এখানে তিনটি কুইক লঞ্চ বোতাম রয়েছে: Launch Mission Control, Explore 129 Flight Tests, এবং Analyze ISS Video।\n\n"
        "২. কুইক স্ট্যাটস গ্রিড (Quick Stats): নাসার ডেটার পরিধি এক পলকে দেখায়:\n"
        "   - ১২৯টি ফ্লাইট টেস্ট\n"
        "   - ৬ জন প্রিন্সিপাল ইনভেস্টিগেটর\n"
        "   - ৯৫০ ppm পিক টক্সিক CO গ্যাস স্পাইক\n"
        "   - ২টি সরাসরি আইএসএস ফ্লাইট ভিডিও ক্লিপ\n"
        "   - ৬টি অফিসিয়াল নাসা টেকনিক্যাল পেপার লিংকড\n\n"
        "৩. আর্কিটেকচার হাইলাইটস: ডেটা প্রোভেন্যান্স, ক্লাসিক্যাল সিভি এবং এভিডেন্স-গ্রাউন্ডেড ইনসাইটের তিনটি ফিচার কার্ড।"
    )

    # Tab 3: Mission Control
    add_heading_1(doc, "৩. মিশন কন্ট্রোল (Mission Control — `#/mc`)")
    p = doc.add_paragraph()
    p.add_run(
        "এটি ওয়েবসাইটের সবচেয়ে গুরুত্বপূর্ণ অ্যানালিটিক্যাল ড্যাশবোর্ড:\n\n"
        "১. হিরো রান সিলেক্টর (Hero Run Dropdown): ওপরের ড্রপডাউন থেকে ৫টি নির্বাচিত বাস্তব নাসার টেস্ট বেছে নেওয়া যায়:\n"
        "   • B1: পাতলা PMMA ফিল্ম — ফ্যান বন্ধ হতেই দ্রুত নিভে যাওয়া।\n"
        "   • M5: ৩ মিমি পুরু PMMA স্ল্যাব — বিশাল অগ্নিকাণ্ড, ৩.২% অক্সিজেন হ্রাস ও ৫০০+ ppm CO।\n"
        "   • O13a: ১/২ ইঞ্চি PMMA রড — ৯৫০ ppm বিষাক্ত কার্বন মনোক্সাইড নির্গমন।\n"
        "   • T22: ১ সেমি SIBAL স্পেসক্রাফট ইনসুলেশন ফ্যাব্রিক ফ্লেম স্প্রেড।\n"
        "   • F1: Nomex III স্পেসস্যুট ফ্যাব্রিক ফায়ার সাপ্রেশন ও চার্ড হওয়া।\n\n"
        "২. বাম কলাম (Test Metadata Card): নির্বাচিত টেস্টের আইডি, গবেষকের নাম, উপাদানের ধরন ও পুরুত্ব, বাতাসের গতি, "
        "প্রারম্ভিক ও চূড়ান্ত অক্সিজেন লেভেল এবং পিক CO পিপিএম তালিকাভুক্ত দেখায়।\n\n"
        "৩. ডান কলাম (Live Telemetry Canvas Chart): ব্রাউজারের ক্যানভাসে রিয়েল-টাইমে দুটি রেখা প্লট হয়:\n"
        "   • কমলা রেখা (Orange Curve): কার্বন মনোক্সাইডের (CO ppm) বৃদ্ধি।\n"
        "   • সায়ান রেখা (Cyan Curve): ক্যাবিনের অক্সিজেনের (O₂ %) হ্রাস।\n"
        "   • লাল ড্যাশ লাইন (Red Dashed Anomaly Markers): ইগনিশন পয়েন্ট, ফ্যান কমানো বা এক্সটিংকশনের মুহূর্তগুলো স্বয়ংক্রিয়ভাবে ফ্ল্যাগ করে।\n\n"
        "৪. গ্রাউন্ড ট্রুথ কার্ড (NASA Ground Truth Card): NASA/TM-20210011385 অফিসিয়াল রিপোর্ট থেকে সরাসরি আসল টেস্টে কী ঘটেছিল তা প্রদর্শন করে।\n\n"
        "৫. অ্যাকশন বোতামসমূহ:\n"
        "   • 📥 Export Run CSV: ক্লিক করলেই ওই টেস্টের প্রতি সেকেন্ডের টাইম-সিরিজ ডেটা সিএসভি ফাইলে ডাউনলোড হয়ে যায়।\n"
        "   • 🖨️ Print Report: এক ক্লিকে সম্পূর্ণ স্ক্রিনকে প্রিন্ট-ফ্রেন্ডলি ক্লিন ডকুমেন্টে পরিণত করে পিডিএফ সেভ করা যায়।\n"
        "   • 🎥 Open ISS Video in Flame Studio: সরাসরি ওই টেস্টের ভিডিও প্লেয়ারে নিয়ে যায়।"
    )

    # Tab 4: 129 Tests Explorer
    add_heading_1(doc, "৪. ১২৯ টেস্ট এক্সপ্লোরার (129 Tests Explorer — `#/exp`)")
    p = doc.add_paragraph()
    p.add_run(
        "নাসার BASS-II এক্সপেরিমেন্টের সম্পূর্ণ ১২৯টি টেস্ট ব্রাউজ ও ফিল্টার করার শক্তিশালী সার্চ ইঞ্জিন:\n\n"
        "১. লাইভ সার্চ বার (Live Search Bar): টেস্ট আইডি (যেমন B1, M5), গবেষকের নাম (Bhattacharjee, Miller), বা ম্যাটেরিয়াল দিয়ে লিখলেই সাথে সাথে ফিল্টার হয়।\n\n"
        "২. ড্রপডাউন ফিল্টারসমূহ:\n"
        "   • Investigator Filter: ৬ জন পিআই-এর যেকোনো একজনকে সিলেক্ট করে তার সব টেস্ট দেখা যায়।\n"
        "   • Material Filter: PMMA Film, Slab, Rod, SIBAL, Nomex Fabric ইত্যাদি অনুযায়ী ফিল্টার।\n"
        "   • Toxicity Level Filter: Low (<50 ppm), Moderate (50-200), High (200-500), Critical (500+ ppm CO)।\n"
        "   • Flow Restrictor Filter: 0 (Unrestricted), 1 (Medium), 2 (Max Restriction)।\n\n"
        "৩. ইন্টারেক্টিভ টেবিল (Interactive Table): প্রতিটি টেস্টের প্রারম্ভিক ও চূড়ান্ত অক্সিজেন, CO₂ বৃদ্ধি এবং CO পিপিএম পরিষ্কার কালার-কোডেড ব্যাজে দেখায়।\n\n"
        "৪. 'Inspect' বোতাম ও পপ-আপ মডাল: টেবিলে যেকোনো টেস্টের ডানপাশের 'Inspect' বোতামে চাপ দিলে একটি পরিচ্ছন্ন মডাল উইন্ডো ভেসে ওঠে, "
        "যেখানে ওই টেস্টের ফ্রেম সংখ্যা, ফ্যান ডিসপ্লে রিডিং এবং জিএমটি ডে সহ সম্পূর্ণ রেকর্ড দেখা যায়।"
    )

    # Tab 5: Flame Analysis Studio
    add_heading_1(doc, "৫. ফ্লেম অ্যানালাইসিস স্টুডিও (Flame Studio CV — `#/flame`)")
    p = doc.add_paragraph()
    p.add_run(
        "ভিডিওর প্রতিটি ফ্রেমে কম্পিউটার ভিশন চালিয়ে আগুনের আচরণ মাপার ল্যাবরেটরি:\n\n"
        "১. ভিডিও সিলেক্টর: টেস্ট B1 (পাতলা ফিল্ম) এবং টেস্ট T22 (সিবাল ইনসুলেশন)-এর আসল আইএসএস ফ্লাইট ভিডিও নির্বাচন করা যায়।\n\n"
        "২. অরিজিনাল ভিডিও প্লেয়ার (বাম পাশে): আসল MP4 ভিডিও চলে। ইউজার যেকোনো মুহূর্তে ভিডিও পজ (Pause) করতে পারেন বা টাইমলাইনে স্ক্রাব (Scrub) করতে পারেন।\n\n"
        "৩. ক্লাসিক্যাল সিভি ক্যানভাস (ডান পাশে): ভিডিওর বর্তমান ফ্রেমটি ক্যানভাসে ড্র হয়। লুমিন্যান্স থ্রেশহোল্ডিংয়ের মাধ্যমে আগুনের উজ্জ্বল পিক্সেলগুলো সোনালী রঙে সেগমেন্ট হয়। "
        "একই সাথে আগুনের চারদিকে সায়ান রঙের বাউন্ডিং বক্স এবং কেন্দ্রে লাল রঙের সেন্ট্রয়েড (●) রিয়েল-টাইমে আঁকা হয়।\n\n"
        "৪. লাইভ ৪টি মেট্রিক্স ডিসপ্লে:\n"
        "   • Luminous Area: উজ্জ্বল শিখার ক্ষেত্রফল (px²)\n"
        "   • Length × Width: আগুনের দৈর্ঘ্য ও প্রস্থের বাউন্ডিং মাপ\n"
        "   • Perimeter: প্রান্তীয় পিক্সেল সংখ্যা বা পরিধি\n"
        "   • Centroid (X, Y): ফ্রেমের ভেতর আগুনের গতিশীল কেন্দ্রবিন্দুর স্থানাঙ্ক\n\n"
        "৫. থ্রেশহোল্ড স্লাইডার (Luminance Slider): ৪০ থেকে ২২০ পর্যন্ত উজ্জ্বলতার মাত্রা পরিবর্তন করে ব্যাকগ্রাউন্ড গ্লো থেকে মূল শিখাকে আলাদা করা যায়।\n\n"
        "৬. 'Sample 20 Frames' বোতাম: এটি চাপলে সিস্টেম পুরো ভিডিও জুড়ে স্বয়ংক্রিয়ভাবে ২০টি ফ্রেম স্ক্যান করে নিচে **Flame Area History Curve** প্লট করে দেয়, "
        "যা থেকে দেখা যায় কীভাবে বাতাস কমার সাথে সাথে শিখা প্রথমে বড় হয়ে পরবর্তীতে হঠাৎ সম্পূর্ণ নিভে যায়।"
    )

    # Tab 6: Sensors & Anomaly
    add_heading_1(doc, "৬. সেন্সর ও অ্যানোমালি অ্যানালাইসিস (Sensors & Anomaly — `#/sensor`)")
    p = doc.add_paragraph()
    p.add_run(
        "সেন্সর ডেটায় আকস্মিক বিপদ চিহ্নিত করার টুল:\n\n"
        "১. চ্যানেল সিলেক্টর: Carbon Monoxide (ppm), Oxygen (% vol), Carbon Dioxide (% vol), বা Airflow Speed (cm/s) নির্বাচন করা যায়।\n\n"
        "২. দুটি অ্যালগরিদমের তুলনা:\n"
        "   • বাটন ১ (Proposed Robust Rolling Z-score): মিডিয়ান ও ম্যাড ভিত্তিক অ্যালগরিদম। এটি ৯৫০ ppm-এর মতো এক্সট্রিম স্পাইক থাকলেও স্বাভাবিক বেসলাইন নষ্ট করে না।\n"
        "   • বাটন ২ (Baseline Standard Deviation): গড় ও স্ট্যান্ডার্ড ডেভিয়েশন ভিত্তিক ট্র্যাডিশনাল পদ্ধতি। এটি বড় স্পাইকে পুরো বেসলাইনকে বিকৃত করে ফেলে।\n\n"
        "৩. থ্রেশহোল্ড স্লাইডার (|Z| > threshold): সংবেদনশীলতা ১.৫ থেকে ৬.০ পর্যন্ত অ্যাডজাস্ট করা যায়।\n\n"
        "৪. অ্যানোমালি চার্ট: ক্যানভাসে নির্বাচিত সিগন্যালের কার্ভ আঁকা হয় এবং যেখানেই অ্যানোমালি ধরা পড়ে, সেখানে উজ্জ্বল লাল বৃত্ত (<span style='color:red'>●</span>) ফুটে ওঠে।"
    )

    # Tab 7: Evidence Engine
    add_heading_1(doc, "৭. এভিডেন্স ইঞ্জিন (Evidence Engine — `#/evid`)")
    p = doc.add_paragraph()
    p.add_run(
        "নাসার অফিসিয়াল গবেষণাপত্রের লাইব্রেরি:\n\n"
        "১. সার্চ ও ক্যাটাগরি ফিল্টার: এক্সটিংকশন বাউন্ডারি, রড টক্সিসিটি, ফ্যাব্রিক সেফটি ইত্যাদি ক্যাটাগরিতে পেপার ফিল্টার করা যায়।\n\n"
        "২. এভিডেন্স কার্ডের ভেতরের তথ্য:\n"
        "   • গবেষণাপত্রের শিরোনাম, লেখক ও জার্নালের বিবরণ।\n"
        "   • Key Finding: পেপারের মূল আবিষ্কার।\n"
        "   • Supports (সবুজ লেখা): এই পেপার নাসার কোন ফ্লাইট টেস্ট বা ফলাফলকে সমর্থন করে।\n"
        "   • Honest Limitations (হলুদ লেখা): পেপারের সীমাবদ্ধতা কী এবং কোন দাবিটি করা যাবে না (যেমন: পাতলা ফিল্মের ফলাফল পুরু স্ল্যাবে প্রযোজ্য নয়)।\n\n"
        "৩. 'Open Publication ↗' বোতাম: ক্লিক করলেই সরাসরি অফিসিয়াল DOI পেজ বা NASA NTRS পোর্টালে নিয়ে যায়।"
    )

    # Tab 8: Compare Runs
    add_heading_1(doc, "৮. কম্পেয়ার রানস (Compare Runs — `#/cmp`)")
    p = doc.add_paragraph()
    p.add_run(
        "পাশাপাশি দুটি মহাকাশ পরীক্ষার তুলনা করার ম্যাট্রিক্স:\n\n"
        "১. ড্রপডাউন থেকে Run A (যেমন পাতলা ফিল্ম B1) এবং Run B (যেমন পুরু স্ল্যাব M5) সিলেক্ট করা যায়।\n\n"
        "২. তুলনা টেবিল: পাশাপাশি রেখে তুলনা করে দেখায়:\n"
        "   • জ্বালানির পুরুত্ব (Thickness: ০.১ মিমি বনাম ৩.০ মিমি)\n"
        "   • অক্সিজেন ড্রপ (০% বনাম -৩.২%)\n"
        "   • বিষাক্ত CO নির্গমন (৬ ppm বনাম ৫৫০ ppm)\n"
        "   • বিপদ স্তর (Low বনাম Critical Danger)\n"
        "   • চূড়ান্ত ফলাফল (দ্রুত নিভে যাওয়া বনাম মারাত্মক অগ্নিকাণ্ড)"
    )

    # Tab 9: Presentation Walkthrough
    add_heading_1(doc, "৯. জাজদের সামনে প্রেজেন্টেশনের ৩-মিনিটের আদর্শ ক্রম")
    p = doc.add_paragraph()
    p.add_run(
        "ভিডিও রেকর্ডিং বা লাইভ ডেমোর সময় নিচের ধারাবাহিকতায় ট্যাবগুলোতে ক্লিক করতে হবে:\n\n"
        "১. Home (০:০০-০:২০): সমস্যার কথা বলবে (মহাকাশে আগুন উপরের দিকে যায় না, ধিকিধিকি জ্বলে প্রচুর CO তৈরি করে)।\n"
        "২. Mission Control (০:২০-০:৫০): টেস্ট O13a সিলেক্ট করে দেখাবে—কীভাবে সেন্সরে ৯৫০ ppm বিষাক্ত CO স্পাইক উঠেছিল এবং নিচে নাসার রিপোর্ট লিংকড।\n"
        "৩. Flame Studio (০:৫০-১:৩৫): ভিডিও প্লে করবে, স্লাইডার নাড়িয়ে দেখাবে ফ্রেম-বাই-ফ্রেম পিক্সেল এরিয়া মাপা হচ্ছে এবং 'Sample 20 Frames' চেপে গ্রাফ দেখাবে।\n"
        "৪. Sensors & Anomaly (১:৩৫-২:১০): Robust Z-score চেপে দেখাবে কীভাবে অ্যালগরিদমটি লাল ডট দিয়ে অস্বাভাবিক ঘটনা ফ্ল্যাগ করে।\n"
        "৫. 129 Tests Explorer (২:১০-২:৪০): ফিল্টারে চাপ দিয়ে দেখাবে পুরো ১২৯টি রিয়েল টেস্ট এক পলকে ফিল্টার হয়ে যাচ্ছে।\n"
        "৬. Evidence Engine (২:৪০-৩:০০): আসল পেপারের ডিওআই এবং অনেস্ট অ্যাবস্টেনশন দেখিয়ে শেষ করবে।"
    )

    file_path = os.path.join(r"D:\Nasa FINAL", "FIREWISE-X_Website_User_Guide_BN.docx")
    doc.save(file_path)
    print(f"Successfully generated: {file_path}")

if __name__ == "__main__":
    generate_research_doc()
    generate_user_guide_doc()
    print("ALL WORD DOCUMENTS GENERATED SUCCESSFULLY!")
