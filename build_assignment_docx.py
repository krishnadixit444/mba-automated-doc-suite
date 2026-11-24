import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

BASE_DIR = '/Users/krishna/.gemini/antigravity/scratch/MBA_Computer_Applications_Assignment'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUTPUT_DOCX = os.path.join(BASE_DIR, 'A_IM-2K26-58_krishna_dixit.docx')
GENERIC_DOCX = os.path.join(BASE_DIR, 'MBA_MS_IM104C_Practical_Assignment.docx')

# Color Palette Constants
COLOR_PRIMARY_HEX = "1B365D"      # Deep Navy
COLOR_SECONDARY_HEX = "0284C7"    # Ocean Blue / Cyan
COLOR_ACCENT_HEX = "0D9488"       # Teal
COLOR_TEXT_HEX = "1E293B"         # Slate Charcoal
COLOR_MUTED_HEX = "64748B"        # Gray Muted
COLOR_LIGHT_BG_HEX = "F1F5F9"     # Very Light Slate
COLOR_BORDER_HEX = "CBD5E1"       # Light Slate Border

COLOR_PRIMARY = RGBColor(27, 54, 93)
COLOR_SECONDARY = RGBColor(2, 132, 199)
COLOR_TEXT = RGBColor(30, 41, 59)
COLOR_MUTED = RGBColor(100, 116, 139)

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    cell._tc.get_or_add_tcPr().append(tcMar)

def set_table_borders(table, color="D3D3D3", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_field(p, field_name):
    fldSimple = OxmlElement('w:fldSimple')
    fldSimple.set(qn('w:instr'), field_name)
    p._p.append(fldSimple)

def build_document():
    doc = Document()

    # Page Margins: 1 inch all around
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        s.different_first_page_header_footer = True

    # Setup Running Header & Footer for Subsequent Pages
    section = sections[0]
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("IIPS, DAVV | MBA(MS) 5 Yrs - I SEMESTER | Computer Application and Web Technology (IM-104C)")
    hrun.font.name = "Arial"
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = COLOR_MUTED

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun1 = fp.add_run("Practical Assignment Record  |  ")
    frun1.font.name = "Arial"
    frun1.font.size = Pt(9)
    frun1.font.color.rgb = COLOR_MUTED
    frun2 = fp.add_run("Page ")
    frun2.font.name = "Arial"
    frun2.font.size = Pt(9)
    frun2.font.color.rgb = COLOR_MUTED
    add_field(fp, 'PAGE')
    frun3 = fp.add_run(" of ")
    frun3.font.name = "Arial"
    frun3.font.size = Pt(9)
    frun3.font.color.rgb = COLOR_MUTED
    add_field(fp, 'NUMPAGES')

    # ==================== COVER PAGE ====================
    # Institution Header Banner Box
    cp_tbl = doc.add_table(rows=1, cols=1)
    cp_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_cell = cp_tbl.cell(0, 0)
    set_cell_background(c_cell, "1B365D")
    set_cell_margins(c_cell, top=280, bottom=280, left=240, right=240)
    
    cp_p = c_cell.paragraphs[0]
    cp_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = cp_p.add_run("International Institute of Professional Studies\nDevi Ahilya Vishwavidyalaya, Indore (M.P.)\n")
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(15)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(255, 255, 255)
    
    r_subinst = cp_p.add_run("Accredited 'A+' Grade by NAAC | Pioneer Institute of Management & Technology")
    r_subinst.font.name = "Arial"
    r_subinst.font.size = Pt(9.5)
    r_subinst.font.color.rgb = RGBColor(191, 219, 254)

    # Spacing
    p_sp1 = doc.add_paragraph()
    p_sp1.paragraph_format.space_before = Pt(20)
    p_sp1.paragraph_format.space_after = Pt(4)

    # Document Title Block
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ass = p_title.add_run("PRACTICAL LABORATORY ASSIGNMENT\n")
    r_ass.font.name = "Arial"
    r_ass.font.size = Pt(18)
    r_ass.font.bold = True
    r_ass.font.color.rgb = COLOR_PRIMARY

    r_course = p_title.add_run("COURSE: COMPUTER APPLICATION AND WEB TECHNOLOGY\nCOURSE CODE: IM-104C\n")
    r_course.font.name = "Arial"
    r_course.font.size = Pt(13)
    r_course.font.bold = True
    r_course.font.color.rgb = COLOR_SECONDARY

    r_class = p_title.add_run("PROGRAM: CLASS - MBA (MS) 5 Yrs - I SEMESTER (SECTION-A AND B)\nMAXIMUM MARKS: 20")
    r_class.font.name = "Arial"
    r_class.font.size = Pt(11)
    r_class.font.bold = True
    r_class.font.color.rgb = RGBColor(71, 85, 105)

    # Decorative Line
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(18)
    r_div = p_line.add_run("―" * 48)
    r_div.font.color.rgb = RGBColor(203, 213, 225)

    # Student Identification Details Table (Mandatory Cover Page Details)
    details_tbl = doc.add_table(rows=8, cols=2)
    details_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(details_tbl, color="CBD5E1", sz="6")
    
    meta_rows = [
        ("Student Name:", "Krishna Dixit"),
        ("Roll Number:", "IM-2K26-58"),
        ("Class & Semester:", "MBA (Management Science) 5 Years - Semester I"),
        ("Section:", "Section A"),
        ("Subject Name & Code:", "Computer Application and Web Technology (IM-104C)"),
        ("Submission Due Date:", "13th November, 2026"),
        ("Total Number of Pages:", "Complete Assignment Record (Pages 1 to End)"),
        ("Student Signature & Date:", "___________________________   Date: 13/11/2026")
    ]
    
    col_w_0 = Inches(2.2)
    col_w_1 = Inches(4.3)
    
    for idx, (label, val) in enumerate(meta_rows):
        row = details_tbl.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = col_w_0
        c1.width = col_w_1
        
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF" if idx < 7 else "F0FDF4")
        set_cell_margins(c0, top=100, bottom=100, left=140, right=140)
        set_cell_margins(c1, top=100, bottom=100, left=140, right=140)
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r0 = p0.add_run(label)
        r0.font.name = "Arial"
        r0.font.size = Pt(10.5)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_PRIMARY
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1 = p1.add_run(val)
        r1.font.name = "Arial"
        r1.font.size = Pt(10.5)
        if idx == 7:
            r1.font.bold = True
            r1.font.color.rgb = RGBColor(22, 101, 52)
        else:
            r1.font.color.rgb = COLOR_TEXT

    # Faculty & Evaluation Box
    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_before = Pt(14)
    p_sp2.paragraph_format.space_after = Pt(4)

    eval_tbl = doc.add_table(rows=2, cols=3)
    eval_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(eval_tbl, color="CBD5E1", sz="6")
    for r_i, r in enumerate(eval_tbl.rows):
        for c_i, c in enumerate(r.cells):
            set_cell_margins(c, top=100, bottom=100, left=100, right=100)
            if r_i == 0:
                set_cell_background(c, "E2E8F0")
            else:
                set_cell_background(c, "FFFFFF")
                
    headers_eval = ["Maximum Marks", "Marks Awarded", "Faculty Signature & Remarks"]
    for c_i, h in enumerate(headers_eval):
        p = eval_tbl.rows[0].cells[c_i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = COLOR_PRIMARY

    vals_eval = ["20 Marks", "_____ / 20", "_________________________"]
    for c_i, v in enumerate(vals_eval):
        p = eval_tbl.rows[1].cells[c_i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(v)
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = COLOR_TEXT

    doc.add_page_break()

    # ==================== TABLE OF CONTENTS & SYLLABUS MAPPING ====================
    p_toc_head = doc.add_paragraph()
    r_th = p_toc_head.add_run("ASSIGNMENT CONTENTS & TOPIC OUTLINE")
    r_th.font.name = "Arial"
    r_th.font.size = Pt(16)
    r_th.font.bold = True
    r_th.font.color.rgb = COLOR_PRIMARY
    p_toc_head.paragraph_format.space_after = Pt(12)

    toc_tbl = doc.add_table(rows=8, cols=3)
    toc_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(toc_tbl, color="CBD5E1", sz="6")
    
    toc_items = [
        ("Topic 1", "Input Devices (Keyboard, Mouse, Scanner) & Output Devices (Monitor, Printer, Speaker)", "Hardware & Peripherals"),
        ("Topic 2", "MS-Word: Basic Components, Text Handling, Table Creation & Handling, Mail Merge", "Word Processing Lab"),
        ("Topic 3", "MS-Excel: Components, Formatting, Conditional Formatting, Charts, Sorting, Formulas & 7 Standard Functions", "Spreadsheet Modelling Lab"),
        ("Topic 4", "MS-PowerPoint: Basic Components, Text Handling, SmartArt, Slide Master, Transitions & Animations", "Executive Presentations"),
        ("Topic 5", "MS-Access: RDBMS Features, Relational Schema, Advantages & Business Applications", "Database Management Lab"),
        ("Topic 6", "Internet Technologies: Search Engine Architecture & Operators, Email Protocols (SMTP, POP3, IMAP)", "Web & Communications"),
        ("Topic 7", "Web Page Designing: Student Entry Form & Commercial Product Purchase Order (HTML5/CSS3/JS)", "Web Technology Lab")
    ]
    
    # Header row
    th_cells = toc_tbl.rows[0].cells
    th_cells[0].width = Inches(1.0)
    th_cells[1].width = Inches(4.2)
    th_cells[2].width = Inches(1.3)
    for i, t in enumerate(["Unit", "Detailed Practical Syllabus Coverage", "Lab Category"]):
        set_cell_background(th_cells[i], "1B365D")
        set_cell_margins(th_cells[i], top=120, bottom=120, left=140, right=140)
        p = th_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if i > 0 else WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(t)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (t_no, t_title, t_cat) in enumerate(toc_items):
        row = toc_tbl.rows[idx+1]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width = Inches(1.0)
        c1.width = Inches(4.2)
        c2.width = Inches(1.3)
        
        bg = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, top=90, bottom=90, left=120, right=120)
            
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(t_no)
        r0.font.name = "Arial"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_PRIMARY
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(t_title)
        r1.font.name = "Arial"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = COLOR_TEXT
        
        p2 = c2.paragraphs[0]
        r2 = p2.add_run(t_cat)
        r2.font.name = "Arial"
        r2.font.size = Pt(9)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_SECONDARY

    # Instructions Callout Box
    p_sp3 = doc.add_paragraph()
    p_sp3.paragraph_format.space_before = Pt(16)
    
    inst_tbl = doc.add_table(rows=1, cols=1)
    inst_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    icell = inst_tbl.cell(0, 0)
    set_cell_background(icell, "FEF3C7")
    set_cell_margins(icell, top=140, bottom=140, left=180, right=180)
    
    ip = icell.paragraphs[0]
    ir_title = ip.add_run("IMPORTANT PRACTICAL & SUBMISSION GUIDELINES\n")
    ir_title.font.name = "Arial"
    ir_title.font.size = Pt(11)
    ir_title.font.bold = True
    ir_title.font.color.rgb = RGBColor(146, 64, 14)
    
    guidelines_text = (
        "• Softcopy Filename Convention: Section_Roll_No_Name (e.g. A_IM-2K26-58_krishna_dixit.docx).\n"
        "• Hardcopy File Submission: Submit complete printout in practical folder with signed cover page.\n"
        "• Marking Scheme: High weighting on practical formatting, step-by-step illustrations, realistic business examples, and clean output presentations across MS-Office tools.\n"
        "• Academic Honesty: Original practical implementation; zero marks awarded for unverified copied work."
    )
    ir_body = ip.add_run(guidelines_text)
    ir_body.font.name = "Arial"
    ir_body.font.size = Pt(9.5)
    ir_body.font.color.rgb = RGBColor(120, 53, 15)

    doc.add_page_break()

    # Helper function for adding headings and callouts
    def add_section_header(num, title):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(20)
        h.paragraph_format.space_after = Pt(8)
        h.paragraph_format.keep_with_next = True
        
        r_num = h.add_run(f"TOPIC {num}: ")
        r_num.font.name = "Arial"
        r_num.font.size = Pt(14)
        r_num.font.bold = True
        r_num.font.color.rgb = COLOR_SECONDARY
        
        r_t = h.add_run(title)
        r_t.font.name = "Arial"
        r_t.font.size = Pt(14)
        r_t.font.bold = True
        r_t.font.color.rgb = COLOR_PRIMARY
        
        # Bottom divider
        p_div = doc.add_paragraph()
        p_div.paragraph_format.space_after = Pt(10)
        r_d = p_div.add_run("―" * 55)
        r_d.font.color.rgb = RGBColor(203, 213, 225)

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = COLOR_PRIMARY

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = COLOR_SECONDARY

    def add_p(text, bold_prefix=None, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Arial"
            rb.font.size = Pt(10)
            rb.font.bold = True
            rb.font.color.rgb = COLOR_PRIMARY
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = COLOR_TEXT
        return p

    def add_bullet(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Arial"
            rb.font.size = Pt(10)
            rb.font.bold = True
            rb.font.color.rgb = COLOR_PRIMARY
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = COLOR_TEXT

    def add_image_box(img_name, caption, width=Inches(5.5)):
        img_path = os.path.join(ASSETS_DIR, img_name)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            run = p_img.add_run()
            run.add_picture(img_path, width=width)
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(10)
            rc = p_cap.add_run(f"Figure: {caption}")
            rc.font.name = "Arial"
            rc.font.size = Pt(8.5)
            rc.font.italic = True
            rc.font.bold = True
            rc.font.color.rgb = COLOR_MUTED

    def add_callout(title, text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = tbl.cell(0, 0)
        set_cell_background(c, "F1F5F9")
        set_cell_margins(c, top=100, bottom=100, left=140, right=140)
        
        # Add thick primary border on left
        tcPr = c._tc.get_or_add_tcPr()
        borders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="none"/>
                <w:left w:val="single" w:sz="24" w:space="0" w:color="1B365D"/>
                <w:bottom w:val="none"/>
                <w:right w:val="none"/>
            </w:tcBorders>
        ''')
        tcPr.append(borders)
        
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        rt = p.add_run(f"Practical Tip / Business Insight: {title}\n")
        rt.font.name = "Arial"
        rt.font.size = Pt(9.5)
        rt.font.bold = True
        rt.font.color.rgb = COLOR_PRIMARY
        
        rb = p.add_run(text)
        rb.font.name = "Arial"
        rb.font.size = Pt(9)
        rb.font.color.rgb = COLOR_TEXT
        
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(4)
        p_sp.paragraph_format.space_after = Pt(4)

    def add_code_box(code_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = tbl.cell(0, 0)
        set_cell_background(c, "F8FAFC")
        set_cell_margins(c, top=80, bottom=80, left=120, right=120)
        set_table_borders(tbl, color="CBD5E1", sz="4")
        
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(code_text)
        r.font.name = "Consolas"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(15, 23, 42)
        
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(4)
        p_sp.paragraph_format.space_after = Pt(4)

    # ==================== TOPIC 1 ====================
    add_section_header("1", "Input Devices & Output Devices")
    
    add_p("A modern computer system operates on the fundamental IPO (Input-Process-Output-Storage) architecture. Input devices act as transducers that convert human-understandable physical actions, text, or analog signals into binary machine code (0s and 1s) for the Central Processing Unit (CPU). Output devices perform the inverse operation, decoding processed binary information into visual, auditory, or tangible forms suitable for human comprehension and business analysis.")
    
    add_image_box("io_architecture.png", "Complete Computer System Architecture: Input, Processing, Storage, and Output", width=Inches(5.8))
    
    add_h2("1.1 In-Depth Analysis of Input Devices")
    
    add_h3("1.1.1 Keyboard (Primary Alphanumeric Input Device)")
    add_p("The keyboard is the standard electro-mechanical text entry and command device. A modern standard full-sized keyboard incorporates 101 to 104 keys arranged in the QWERTY layout (named after the first six letters of the top alphabetic row).")
    add_bullet(" Alphanumeric keys (A-Z, 0-9), punctuation marks, spacebar.", "• Key Sections:")
    add_bullet(" Dedicated F1 (Help) through F12 (Save As / developer tools) executing predefined system shortcuts.", "• Function Keys:")
    add_bullet(" Ctrl, Alt, Shift, and Windows/Command key used in combination with other keys to trigger OS actions.", "• Modifier Keys:")
    add_bullet(" Compact 17-key grid on the right designed for rapid accounting and data entry.", "• Numeric Keypad:")
    add_bullet(" Arrow keys, Home, End, Page Up, Page Down, Insert, and Delete.", "• Cursor & Navigation Keys:")
    add_bullet("Under each keycap lies a key switch. When depressed, it completes an electrical circuit on a matrix grid. A dedicated keyboard controller microprocessor scans the matrix (at up to 1000 Hz polling rate), identifies the row-column intersection, and transmits an interrupt scan code via USB/Bluetooth to the OS, which maps it via ASCII/Unicode character sets.", "• Working Principle:")
    add_bullet("Mechanical switches (Cherry MX, Gateron with distinct tactile feedback and high durability), Membrane switches (inexpensive silicone domes found in office keyboards), and Ergonomic split keyboards (contoured to mitigate repetitive strain injuries such as Carpal Tunnel Syndrome).", "• Commercial Variants:")

    add_image_box("keyboard.png", "Ergonomic QWERTY Keyboard with Function Keys and Alphanumeric Layout", width=Inches(4.2))

    add_h3("1.1.2 Mouse (Primary Graphical Pointing Device)")
    add_p("Invented by Douglas Engelbart in 1964 and revolutionized by modern graphical user interfaces (GUI), the mouse enables direct manipulation of on-screen interface elements.")
    add_bullet("Modern optical mice house a tiny low-resolution CMOS camera and an LED/Laser diode. As the mouse slides over a surface, the LED illuminates the micro-textures, and the sensor captures thousands of microscopic frames per second. An internal Digital Signal Processor (DSP) calculates optical flow vectors (ΔX, ΔY) and transmits coordinate packets to the computer cursor.", "• Working Mechanism:")
    add_bullet("Single-click (selection), Double-click (opening files/programs), Right-click (contextual menu), Click-and-Drag (moving objects, selecting text blocks), and Scroll Wheel (vertical navigation and middle-click auto-scroll).", "• Functional Operations:")
    add_bullet("Sensitivity is calibrated in DPI (Dots Per Inch) or CPI (Counts Per Inch). Higher DPI allows swift cursor navigation across multi-monitor 4K financial setups with minimal wrist exertion.", "• Resolution & Metrics:")

    add_image_box("mouse.png", "Modern Optical Mouse with High-Precision Sensor and Scroll Wheel", width=Inches(3.2))

    add_h3("1.1.3 Scanner (Document Digitization Device)")
    add_p("A scanner captures physical documents, photographs, barcodes, and business vouchers, converting optical reflections into raster digital image files (JPEG, PNG, PDF) or editable text.")
    add_bullet("The document is placed face-down on a glass platen. An array of bright LEDs illuminates the sheet as a motorized scan head moves beneath. Mirrors and lenses focus the reflected light onto a Charge-Coupled Device (CCD) or Contact Image Sensor (CIS). The photosensors convert light intensities into analog voltages, which an Analog-to-Digital Converter (ADC) quantizes into 24-bit or 48-bit RGB color values.", "• Working Principle:")
    add_bullet("Flatbed Scanners (ideal for bound books and certificates), Sheet-fed Scanners (high-volume double-sided batch feeders for accounting invoices), Handheld Scanners, and 2D Barcode/QR Scanners.", "• Hardware Types:")
    add_bullet("When coupled with Optical Character Recognition (OCR) software, scanned document images are automatically converted into editable Word or searchable PDF documents, drastically streamlining Enterprise Content Management (ECM).", "• OCR Integration:")

    add_image_box("scanner.png", "High-Resolution Optical Flatbed Scanner for Business Document Archiving", width=Inches(3.4))

    add_h2("1.2 In-Depth Analysis of Output Devices")
    
    add_h3("1.2.1 Monitor (Primary Visual Display Device)")
    add_p("The computer monitor is the primary visual display unit (VDU) responsible for rendering graphical user interfaces, data tables, video feeds, and software workspaces in real-time.")
    add_bullet("Liquid Crystal Displays with LED backlighting utilize liquid crystal molecules sandwiched between polarizing filters. When electrical voltage is applied, the crystals twist, modulating the passage of LED backlight through sub-pixels (Red, Green, Blue). IPS (In-Plane Switching) panels provide superior color accuracy and 178° wide viewing angles, essential for design and executive data analysis.", "• LCD / LED Technology:")
    add_bullet("Organic Light Emitting Diode displays employ organic carbon-based compounds that emit their own light when energized, enabling true blacks (infinite contrast ratio) and ultra-thin form factors.", "• OLED Technology:")
    add_bullet("Resolution (Full HD 1920x1080, 2K QHD 2560x1440, 4K UHD 3840x2160), Refresh Rate (60Hz to 144Hz for fluid scrolling), Aspect Ratio (16:9 widescreen, 21:9 ultra-wide for multi-window financial modeling), and Connectors (HDMI, DisplayPort, USB-C / Thunderbolt).", "• Key Performance Metrics:")

    add_image_box("monitor.png", "High-Definition LED Backlit IPS Display Monitor", width=Inches(3.4))

    add_h3("1.2.2 Printer (Hard Copy Output Device)")
    add_p("Printers transform electronic documents into tangible hard-copy physical records on paper or specialized media. In enterprise management, printers are categorized into Impact and Non-Impact devices.")
    
    # Printer Comparison Table
    prt_tbl = doc.add_table(rows=5, cols=6)
    prt_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(prt_tbl, color="CBD5E1", sz="6")
    
    prt_headers = ["Printer Category", "Technology Mechanism", "Speed Range", "Resolution", "Cost / Page", "Typical Business Application"]
    for c_i, h in enumerate(prt_headers):
        c = prt_tbl.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    prt_data = [
        ("Dot Matrix (Impact)", "Pins strike ink ribbon against paper physically", "100 - 600 CPS", "72 - 360 DPI", "Extremely Low (~₹0.15)", "Multi-part carbon copy receipts, railway tickets"),
        ("Inkjet (Non-Impact)", "Microscopic liquid ink droplets sprayed via piezoelectric nozzles", "10 - 25 PPM", "1200 - 4800 DPI", "Moderate to High (~₹2.50)", "High-quality color photo printing, small office desks"),
        ("Laser (Non-Impact)", "Laser beam charges drum, attracts toner powder, heated by fuser", "25 - 70+ PPM", "600 - 2400 DPI", "Low (~₹0.60)", "High-volume corporate contracts, reports, legal filings"),
        ("Thermal (Non-Impact)", "Heated pins react with heat-sensitive chemical paper", "150 - 300 mm/s", "203 - 300 DPI", "Very Low (~₹0.10)", "POS billing machines, ATM receipts, shipping barcodes")
    ]
    
    for r_i, row_vals in enumerate(prt_data):
        row = prt_tbl.rows[r_i+1]
        bg = "F8FAFC" if r_i % 2 == 1 else "FFFFFF"
        for c_i, val in enumerate(row_vals):
            c = row.cells[c_i]
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=70, right=70)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_TEXT

    add_image_box("printer.png", "Enterprise High-Speed Laser Printer with Automatic Duplexing", width=Inches(3.2))

    add_h3("1.2.3 Speaker (Audio / Acoustic Output Device)")
    add_p("Computer speakers convert stored digital audio data into audible acoustic sound waves. In corporate boardrooms and remote enterprise operations, audio clarity is indispensable for video conferencing, webinars, multimedia corporate training, and interactive client demonstrations.")
    add_bullet("Digital audio streams (MP3, WAV, AAC) stored as binary samples are decoded by a Digital-to-Analog Converter (DAC) inside the computer sound card into continuous analog electrical audio signals. An amplifier amplifies the signal to drive an electromagnetic voice coil suspended near a permanent magnet. The coil vibrates a cone-shaped diaphragm, producing pressure waves in the air perceived as sound.", "• Sound Generation Principle:")
    add_bullet("Frequency response (20 Hz - 20,000 Hz spanning bass, midrange, and treble), Total Harmonic Distortion (THD < 1%), Signal-to-Noise Ratio (SNR > 85 dB), and RMS Power (Wattage).", "• Performance Specifications:")
    add_bullet("Modern enterprise workstations leverage USB speakerphones with beamforming multi-microphone arrays, acoustic echo cancellation (AEC), and Bluetooth low-latency codecs for hybrid executive team meetings.", "• Business Utility:")

    add_image_box("speaker.png", "Stereo Multimedia Desktop Speakers with Integrated DAC Amplification", width=Inches(3.2))

    add_callout("Hardware Lifecycle Strategy", "For enterprise MBA managers, selecting input/output hardware requires total cost of ownership (TCO) evaluation: accounting for laser toner yields, ergonomics to minimize workplace injuries, and high-resolution monitors to increase financial analyst productivity.")

    doc.add_page_break()

    # ==================== TOPIC 2 ====================
    add_section_header("2", "Microsoft Word: Core Components, Text Handling, Tables & Mail Merge")
    
    add_p("Microsoft Word is the global benchmark word processing application. Part of the Microsoft 365 productivity suite, it enables executives, researchers, and administrators to produce professional documents, academic theses, corporate contracts, and personalized mass correspondence with rigorous typographic control.")
    
    add_image_box("ms_word_interface.png", "Microsoft Word Graphic User Interface Architecture with Ribbon System", width=Inches(5.8))
    
    add_h2("2.1 Basic Interface Components of Microsoft Word")
    add_bullet("Located at the very top of the window, displaying the current document name (e.g. Document1 - Word), cloud synchronization status (AutoSave toggle), search box (Alt+Q), and window management icons (Minimize, Maximize/Restore, Close).", "1. Title Bar:")
    add_bullet("Customizable toolbar pinned to the top-left containing frequently accessed commands such as Save (Ctrl+S), Undo (Ctrl+Z), and Redo (Ctrl+Y).", "2. Quick Access Toolbar (QAT):")
    add_bullet("The command center introduced in Office 2007, organized into logical contextual Tabs (File, Home, Insert, Draw, Design, Layout, References, Mailings, Review, View, Help). Each tab contains organized Groups (e.g., Clipboard, Font, Paragraph, Styles).", "3. The Ribbon:")
    add_bullet("Small diagonal arrows at the bottom-right corner of ribbon groups that open advanced modal settings dialogs (e.g., Font dialog with Ctrl+D, Paragraph formatting dialog).", "4. Dialog Box Launchers:")
    add_bullet("The central white canvas representing the physical page (A4, Letter) where text, shapes, and tables are authored and visually rendered via WYSIWYG (What You See Is What You Get).", "5. Document Workspace / Canvas:")
    add_bullet("Horizontal and vertical measurement bars used for setting margins, first-line indents, hanging indents, and tab stops (Left, Center, Right, Decimal).", "6. Rulers:")
    add_bullet("Bottom strip providing real-time metadata including current page number, total word count, language proofing dictionary, macro recorder, view mode shortcuts (Read Mode, Print Layout, Web Layout), and the interactive Zoom Slider (10% to 500%).", "7. Status Bar:")

    add_h2("2.2 Comprehensive Text Handling Features in Word Documents")
    add_p("Effective typography enhances legibility and communicates executive authority. Microsoft Word provides granular control over character, paragraph, and global document formatting:")
    
    add_h3("2.2.1 Character & Font Formatting")
    add_bullet("Standard executive typography employs clean serif (Times New Roman, Georgia) or sans-serif (Calibri, Aptos, Arial) typefaces sized appropriately (Title: 16-18pt, Headings: 12-14pt, Body: 10.5-11.5pt).", "• Font Family & Size:")
    add_bullet("Bold (Ctrl+B), Italic (Ctrl+I), Underline (Ctrl+U, with double/dotted underline options), and Strikethrough for revisions.", "• Font Styles:")
    add_bullet("Subscript (Ctrl+= e.g., H₂O) and Superscript (Ctrl+Shift++ e.g., X² + Y² = Z²), essential for chemical and mathematical documentation.", "• Scientific Notations:")
    add_bullet("Sentence case, lowercase, UPPERCASE, Capitalize Each Word (Title Case), and tOGGLE cASE (Shift+F3 shortcut).", "• Change Case:")
    add_bullet("Character spacing (Expanded / Condensed by point fractions), Kerning for fonts above specified point sizes, and Ligatures.", "• Advanced Typography:")

    add_h3("2.2.2 Paragraph Formatting & Alignment")
    add_bullet("Left Align (Ctrl+L, standard business correspondence), Center (Ctrl+E, titles/certificates), Right Align (Ctrl+R, dates/signatures), and Justify (Ctrl+J, aligns both left and right margins evenly for formal publications).", "• Alignment Modes:")
    add_bullet("Configurable from Single (1.0), 1.15, 1.5, to Double (2.0) spacing, alongside Before and After paragraph spacing (e.g., 6pt after) to eliminate manual empty enter presses.", "• Line & Paragraph Spacing:")
    add_bullet("First-Line Indent (indents the opening sentence of each paragraph) and Hanging Indent (indents all subsequent lines after the first, standard for APA/Harvard academic bibliographies).", "• Indentation Controls:")
    add_bullet("Bulleted lists with custom glyphs, Numbered hierarchical sequences (1, a, i), and Multilevel Lists linked to Heading styles for structured corporate governance manuals.", "• Bulleted & Numbered Lists:")

    add_h3("2.2.3 Styles, Themes, and Structural Tools")
    add_bullet("Applying pre-configured styles (Normal, Heading 1, Heading 2, Subtitle) ensures typographic consistency across 100+ page documents and automates one-click Table of Contents generation.", "• Built-In Styles:")
    add_bullet("Supports wildcard search (`*`, `?`), regex-style patterns, and formatting search (e.g., replacing all bold italic text with corporate branding blue).", "• Find & Replace (Ctrl+H):")
    add_bullet("Page breaks (Ctrl+Enter) versus Section breaks (Next Page, Continuous, Even/Odd Page). Section breaks allow independent page orientations (Portrait for text, Landscape for wide financial tables) and unique headers/footers within the same document.", "• Page & Section Breaks:")

    add_h2("2.3 Step-by-Step Table Creation and Table Handling in MS-Word")
    add_p("Tables present structured quantitative data, schedules, and comparative matrices cleanly.")
    
    add_h3("2.3.1 Five Methods of Table Creation in Word")
    add_bullet("Navigate to Insert Tab > Table > drag mouse across the visual grid (up to 10 columns by 8 rows).", "Method 1 (Grid Selection):")
    add_bullet("Insert Tab > Table > Click 'Insert Table...' > specify exact Number of Columns (e.g. 5) and Number of Rows (e.g. 10), and select AutoFit behavior.", "Method 2 (Insert Table Dialog):")
    add_bullet("Insert Tab > Table > Click 'Draw Table'. Use the pencil cursor to draw outer boundaries and interior cell lines for complex irregular forms.", "Method 3 (Draw Table Tool):")
    add_bullet("Highlight raw text separated by commas, tabs, or semicolons > Insert Tab > Table > Click 'Convert Text to Table'.", "Method 4 (Convert Text to Table):")
    add_bullet("Insert Tab > Table > Excel Spreadsheet. Embeds a live Excel worksheet with full formula calculation capability directly inside Word.", "Method 5 (Excel Spreadsheet Embedding):")

    add_h3("2.3.2 Advanced Table Handling Features with Practical Demonstration")
    add_bullet("Adding/Deleting rows & columns via contextual Table Tools Layout tab or the mini toolbar.", "• Structural Manipulation:")
    add_bullet("Merging multiple header cells into one consolidated title cell, and splitting a single cell into multiple sub-columns.", "• Merge & Split Cells:")
    add_bullet("AutoFit to Contents (snugs borders to cell text), AutoFit to Window (expands table to margins), and Fixed Column Width.", "• AutoFit Intelligence:")
    add_bullet("Top Left, Top Center, Top Right, Center Left, Center Middle, Center Right, Bottom Left, Bottom Center, Bottom Right, alongside Text Direction (horizontal / vertical 90° / 270°).", "• 9-Way Cell Alignment:")
    add_bullet("Under Layout tab, enabling 'Repeat Header Rows' ensures that when a table spans 10 pages, the column headers automatically print at the top of every page.", "• Repeating Header Rows:")
    add_bullet("Click Layout > Formula to execute mathematical functions like `=SUM(ABOVE)`, `=AVERAGE(LEFT)`, or `=PRODUCT(ABOVE)` without launching Excel.", "• In-Table Mathematical Formulas:")

    # Table Practical Demonstration Example
    add_h3("Practical Business Example: MBA(MS) Student Semester Grade Sheet Table")
    
    tbl_demo = doc.add_table(rows=6, cols=6)
    tbl_demo.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_demo, color="CBD5E1", sz="6")
    
    headers_demo = ["Roll Number", "Student Name", "Internal Marks (40)", "End-Term Marks (60)", "Total Score (100)", "Performance Grade"]
    for c_i, h in enumerate(headers_demo):
        c = tbl_demo.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    demo_data = [
        ("IM-2K26-58", "Krishna Dixit", "36", "54", "90", "A+ (Outstanding)"),
        ("IM-2K26-02", "Ananya Sharma", "38", "56", "94", "A+ (Outstanding)"),
        ("IM-2K26-03", "Rohit Verma", "31", "45", "76", "B+ (Very Good)"),
        ("IM-2K26-04", "Sneha Joshi", "34", "50", "84", "A (Excellent)"),
        ("AVERAGE", "Class Batch Benchmark", "=AVERAGE(C2:C5)", "=AVERAGE(D2:D5)", "86.0", "Class Average")
    ]
    
    for r_i, rvals in enumerate(demo_data):
        row = tbl_demo.rows[r_i+1]
        is_avg = (r_i == 4)
        bg = "E2E8F0" if is_avg else ("F8FAFC" if r_i % 2 == 1 else "FFFFFF")
        for c_i, val in enumerate(rvals):
            c = row.cells[c_i]
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_i != 1 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.bold = is_avg
            r.font.color.rgb = COLOR_PRIMARY if is_avg else COLOR_TEXT

    add_h2("2.4 The Mail Merge Process with Step-by-Step Practical Implementation")
    add_p("Mail Merge is one of the most powerful corporate productivity automation features in MS-Word. It allows an organization to generate hundreds or thousands of personalized letters, fee receipts, internship offer letters, admission cards, envelopes, or personalized emails by merging a static Main Document template with a structured Data Source.")

    add_image_box("mail_merge_workflow.png", "Microsoft Word Mail Merge Architecture & 6-Step Automated Workflow", width=Inches(5.8))

    add_h3("2.4.1 Three Essential Architectural Components of Mail Merge")
    add_bullet("The master template containing the standard corporate boilerplate text, headers, university logos, and dynamic placeholders known as Merge Fields (e.g., `<<Student_Name>>`).", "1. Main Document:")
    add_bullet("The structured database containing variable recipient records. Typically an Excel spreadsheet (.xlsx), Access database (.accdb), or Outlook Contacts folder.", "2. Data Source:")
    add_bullet("The resulting multi-page output containing a unique, fully populated personalized letter or document for every single row in the data source.", "3. Merged Document:")

    add_h3("2.4.2 Comprehensive 6-Step Mail Merge Procedure")
    add_bullet("Open Word > Mailings Tab > Start Mail Merge > Choose document format: Letters, E-mail Messages, Envelopes, Labels, or Directory.", "Step 1 (Select Document Type):")
    add_bullet("Select 'Use the current document', 'Start from a template', or 'Start from existing document'.", "Step 2 (Select Starting Document):")
    add_bullet("Click 'Select Recipients' > 'Use an Existing List...' > Browse and connect to the recipient Excel workbook (`MBA_Students_2026.xlsx`) and choose the active worksheet.", "Step 3 (Connect Data Source):")
    add_bullet("Position insertion point in the letter > Click 'Insert Merge Field' on Mailings tab > select fields: `<<Candidate_Name>>`, `<<Roll_No>>`, `<<Program>>`, `<<Scholarship_Amount>>`, `<<Orientation_Date>>`.", "Step 4 (Insert Merge Fields):")
    add_bullet("Click 'Preview Results' (ABC icon). Use the record navigation buttons (◀, ▶) to verify how individual student records populate into the placeholders.", "Step 5 (Preview Records):")
    add_bullet("Click 'Finish & Merge' > select 'Print Documents' (direct hardcopy print) or 'Edit Individual Documents' (creates a single master .docx containing all letters for final inspection).", "Step 6 (Complete the Merge):")

    add_callout("Mail Merge Business Example", "Below is the real-world MBA Orientation Invitation Letter template and its corresponding data source table, illustrating how placeholder fields dynamically transform into personalized letters.")

    # Data Source Sample Table
    add_p("Sample Recipient Data Source (Excel Table: tbl_MBA_Admissions):", bold_prefix="Data Source Schema: ")
    
    mm_tbl = doc.add_table(rows=4, cols=5)
    mm_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(mm_tbl, color="CBD5E1", sz="6")
    mm_headers = ["Candidate_Name", "Roll_No", "Merit_Rank", "Orientation_Date", "Venue"]
    for c_i, h in enumerate(mm_headers):
        c = mm_tbl.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=70, right=70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    mm_records = [
        ("Krishna Dixit", "IM-2K26-58", "Rank 04", "18th Nov 2026", "Auditorium Hall A, IIPS DAVV"),
        ("Ananya Sharma", "IM-2K26-02", "Rank 01", "18th Nov 2026", "Auditorium Hall A, IIPS DAVV"),
        ("Rohit Verma", "IM-2K26-03", "Rank 12", "18th Nov 2026", "Auditorium Hall A, IIPS DAVV")
    ]
    for r_i, rvals in enumerate(mm_records):
        row = mm_tbl.rows[r_i+1]
        for c_i, val in enumerate(rvals):
            c = row.cells[c_i]
            set_cell_background(c, "F8FAFC" if r_i % 2 == 1 else "FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_TEXT

    # Main Document Template Sample
    add_h3("Master Letter Template with Merge Fields Inserted:")
    template_text = (
        "To,\n"
        "<<Candidate_Name>>\n"
        "Roll Number: <<Roll_No>>\n"
        "Merit Admission Rank: <<Merit_Rank>>\n\n"
        "Subject: Invitation to MBA (Management Science) Academic Orientation Program 2026\n\n"
        "Dear <<Candidate_Name>>,\n\n"
        "Congratulations on your admission to the prestigious MBA(MS) 5 Yrs Integrated Program at IIPS, DAVV, Indore! We are pleased to formally invite you to the Inaugural Academic Orientation Ceremony scheduled on <<Orientation_Date>> at <<Venue>>.\n\n"
        "Please carry this letter and your original verification documents. We look forward to welcoming you to the IIPS family.\n\n"
        "Warm regards,\n"
        "Program Coordinator, MBA(MS) 5 Yrs\n"
        "International Institute of Professional Studies, DAVV, Indore"
    )
    add_p(template_text)

    doc.add_page_break()

    # ==================== TOPIC 3 ====================
    add_section_header("3", "Microsoft Excel: Components, Formatting, Charts, Sorting & 7 Standard Functions")
    
    add_p("Microsoft Excel is the world's most ubiquitous spreadsheet application, serving as the foundational tool for corporate financial modeling, statistical analysis, budgeting, and business intelligence across global enterprises.")
    
    add_image_box("ms_excel_interface.png", "Microsoft Excel Application Workspace, Formula Bar, and Data Grid", width=Inches(5.8))
    
    add_h2("3.1 Basic Components of Microsoft Excel")
    add_bullet("An Excel document (.xlsx) is a Workbook that contains one or more Worksheets (spreadsheets). Each worksheet consists of a massive grid comprising 1,048,576 Rows (numbered 1, 2, 3...) and 16,384 Columns (lettered A through XFD).", "• Workbook vs Worksheet Architecture:")
    add_bullet("The fundamental unit of data storage created by the intersection of a column and a row. It is uniquely referenced by its alphanumeric coordinate (e.g. C7 denotes Column C, Row 7).", "• Cell & Cell Address:")
    add_bullet("Located on the left side of the formula bar, it displays the address of the currently selected cell or named data range.", "• Name Box:")
    add_bullet("The primary execution input bar located above the column headers. It displays the raw formula or constant value stored in the active cell, preceded by the function wizard icon (`fx`).", "• Formula Bar:")
    add_bullet("The highlighted cell bounded by a bold colored border with a tiny fill handle square at its bottom-right corner.", "• Active Cell Pointer:")
    add_bullet("Located at the bottom left, allowing users to switch between worksheets, rename sheets, apply tab colors, and insert new sheets with the '+' button.", "• Sheet Tabs:")
    add_bullet("Bottom bar displaying operational state ('Ready', 'Edit') and dynamic auto-calculations (Average, Count, Sum) for any currently highlighted cell range without requiring explicit formulas.", "• Status Bar Quick Metrics:")

    add_h2("3.2 Text and Number Handling Features in Workbook")
    add_bullet("Left alignment for text labels, Right alignment for numeric data, Center alignment for codes/dates. Vertical alignment (Top, Middle, Bottom) and Orientation (angling text diagonally or vertically 90° for narrow columnar headers).", "• Alignment & Orientation:")
    add_bullet("Automatically increases cell row height to wrap lengthy textual entries onto multiple lines within a single column width.", "• Wrap Text:")
    add_bullet("Combines multiple adjacent cells into a single unified cell and centers the contents horizontally, standard for top-level report titles.", "• Merge & Center:")
    add_bullet("General, Number (with decimal place controls), Currency (₹, $, €), Accounting (aligns currency symbols and decimal points vertically), Short Date (DD/MM/YYYY), Long Date, Percentage (multiplies by 100 and displays %), and Text format (preserves leading zeros in employee IDs and phone numbers).", "• Data & Number Formatting:")
    add_bullet("Dragging the bottom-right fill handle automatically generates logical sequences (Jan, Feb, Mar; Monday, Tuesday; 1, 2, 3; custom departmental lists).", "• AutoFill Series:")
    add_bullet("Pressing Ctrl+E executes Flash Fill, an AI pattern-matching engine that automatically extracts or combines text (e.g. extracting first names from email addresses).", "• Flash Fill (Ctrl+E):")
    add_bullet("Data Tab > Text to Columns divides single-cell delimited data (e.g., 'Patel, Kamal') into separate columnar cells based on commas, spaces, or custom separators.", "• Text to Columns Wizard:")

    add_h2("3.3 Conditional Formatting with Practical Business Scenario")
    add_p("Conditional Formatting dynamically applies cell formatting (fill colors, borders, font styles, data bars, and icon indicators) based on user-defined criteria or formulas, instantly highlighting business anomalies, risks, and achievements.")
    
    add_bullet("Greater Than, Less Than, Between, Equal To, Text that Contains, Duplicate Values.", "• Highlight Cells Rules:")
    add_bullet("Top 10 Items, Top 10%, Bottom 10%, Above Average, Below Average.", "• Top/Bottom Rules:")
    add_bullet("Horizontal colored gradient/solid bars whose lengths correspond to cell values, providing an in-cell mini bar chart.", "• Data Bars:")
    add_bullet("Bi-color and tri-color heatmaps (e.g., Green-Yellow-Red) visualizing relative intensity and distribution across financial statements.", "• Color Scales:")
    add_bullet("Traffic lights (Red, Yellow, Green circles), directional arrows (▲, ▶, ▼), flags, and stars visualizing KPI performance tiers.", "• Icon Sets:")
    add_bullet("Custom formulas such as `=AND($D2>100000, $E2=\"Pending\")` highlight high-value delayed invoices automatically.", "• Formula-Driven Rules:")

    add_h2("3.4 Step-by-Step Chart Creation Process in MS-Excel")
    add_p("Data visualization transforms raw numerical tables into intuitive graphical narratives that empower management executives to discern trends and make data-driven decisions.")
    
    add_bullet("Clustered Column / Bar (comparing categories), Line Chart (tracking trends over time/quarters), Pie / Doughnut (composition of a whole, 100% total), Scatter (XY) (correlation analysis), and Combo Charts (combining Column + Line with secondary Y-axis).", "• Core Chart Types:")

    add_h3("3.4.1 Step-by-Step Chart Creation Workflow")
    add_bullet("Arrange data in a clean contiguous tabular structure with distinct row and column headers. Highlight the target range (e.g. A1:D5).", "Step 1 (Organize & Select Data):")
    add_bullet("Navigate to Insert Tab > Charts Group > click 'Insert Column or Bar Chart' > select '2-D Clustered Column'.", "Step 2 (Insert Chart):")
    add_bullet("Click the green '+' icon on the chart border to toggle Chart Title, Axis Titles (Horizontal & Vertical), Data Labels (showing exact values atop bars), Data Table, Gridlines, and Legend.", "Step 3 (Add & Format Chart Elements):")
    add_bullet("Use the Chart Design tab to apply modern color palettes, switch rows/columns, or change chart style to dark executive theme.", "Step 4 (Style & Color Customization):")
    add_bullet("Click 'Move Chart' to keep it as an embedded object within the worksheet or relocate it to a dedicated standalone Chart Sheet.", "Step 5 (Chart Placement):")

    add_image_box("excel_chart_example.png", "MS-Excel Clustered Column Chart: FY 2026 Quarterly Performance Comparison", width=Inches(5.6))

    add_h2("3.5 Step-by-Step Sorting in MS-Excel with Multi-Level Example")
    add_p("Sorting arranges tabular data rows alphabetically, numerically, or chronologically, facilitating rapid data analysis.")
    
    add_h3("3.5.1 Single-Level vs Multi-Level Custom Sorting Procedure")
    add_bullet("Click any cell within the target column > Data Tab > click 'Sort A to Z' (ascending) or 'Sort Z to A' (descending).", "• Single-Level Sort:")
    add_bullet("Select entire data range (including headers) > Data Tab > Sort (opens Sort Dialog Box).", "• Multi-Level Sort (Step-by-Step):")
    add_bullet("Ensure 'My data has headers' checkbox is ticked.", "  - Step A:")
    add_bullet("Under 'Sort by', choose Primary Column (e.g., 'Department'), Sort On ('Cell Values'), Order ('A to Z').", "  - Step B:")
    add_bullet("Click 'Add Level' button. Under 'Then by', select Secondary Column (e.g., 'Performance Rating'), Order ('Largest to Smallest').", "  - Step C:")
    add_bullet("Click 'Add Level' again. Select 'Salary (₹)', Order ('Largest to Smallest'). Click OK.", "  - Step D:")

    # Before and After Sorting Table
    add_h3("Demonstration Dataset: Multi-Level Sorting (Department A-Z, then Performance Rating High-to-Low)")
    
    sort_tbl = doc.add_table(rows=6, cols=5)
    sort_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(sort_tbl, color="CBD5E1", sz="6")
    
    s_headers = ["Employee ID", "Employee Name", "Department", "Rating (1-5)", "Monthly Salary (₹)"]
    for c_i, h in enumerate(s_headers):
        c = sort_tbl.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=70, right=70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    s_data = [
        ("EMP-104", "Vikram Rathore", "Finance", "4.8", "₹95,000"),
        ("EMP-101", "Krishna Dixit", "Finance", "4.2", "₹82,000"),
        ("EMP-105", "Megha Kapoor", "Human Resources", "4.9", "₹88,000"),
        ("EMP-102", "Ananya Sharma", "Marketing", "4.7", "₹90,000"),
        ("EMP-103", "Rohit Verma", "Marketing", "4.1", "₹75,000")
    ]
    for r_i, rvals in enumerate(s_data):
        row = sort_tbl.rows[r_i+1]
        for c_i, val in enumerate(rvals):
            c = row.cells[c_i]
            set_cell_background(c, "F8FAFC" if r_i % 2 == 1 else "FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_TEXT

    add_h2("3.6 Formulas and Seven Standard Functions with Syntax, Examples & Required Outputs")
    add_p("An Excel formula is an expression that calculates values, always commencing with an equals sign (`=`). A function is a pre-built mathematical, statistical, or logical algorithm built directly into the Excel calculation engine. Formulas utilize relative references (`A1`, which adjust when copied) or absolute references (`$A$1`, which remain locked to a specific coordinate).")
    
    # 7 Standard Functions Detail
    func_specs = [
        ("1. SUM Function",
         "Syntax: =SUM(number1, [number2], ...)",
         "Calculates the total mathematical sum of all numeric values across a designated cell range.",
         "Dataset: Monthly Sales in cells C2:C6 = [850000, 1200000, 450000, 320000, 210000]",
         "Exact Formula: =SUM(C2:C6)",
         "Required Output: ₹3,030,000.00"),
        
        ("2. AVERAGE Function",
         "Syntax: =AVERAGE(number1, [number2], ...)",
         "Calculates the statistical arithmetic mean of all numeric arguments in the range.",
         "Dataset: Semester Marks in cells D2:D6 = [90, 94, 76, 84, 86]",
         "Exact Formula: =AVERAGE(D2:D6)",
         "Required Output: 86.00"),
        
        ("3. COUNT & COUNTA Functions",
         "Syntax: =COUNT(value1, ...) and =COUNTA(value1, ...)",
         "COUNT returns the number of cells containing purely numeric data. COUNTA returns the number of non-empty cells (both text and numbers).",
         "Dataset: Cells B2:B10 contain 7 student names and 2 blank empty rows.",
         "Exact Formula: =COUNTA(B2:B10)",
         "Required Output: 7 (Active Registered Candidates)"),
        
        ("4. MAX and MIN Functions",
         "Syntax: =MAX(number1, ...) and =MIN(number1, ...)",
         "Returns the highest (MAX) and lowest (MIN) numeric values within the evaluated range.",
         "Dataset: Quarterly Net Profits in cells E2:E5 = [2000000, 2600000, 3000000, 3600000]",
         "Exact Formula: =MAX(E2:E5) & =MIN(E2:E5)",
         "Required Output: Maximum = ₹3,600,000.00 | Minimum = ₹2,000,000.00"),
        
        ("5. IF Function (Logical Decision Modeling)",
         "Syntax: =IF(logical_test, [value_if_true], [value_if_false])",
         "Evaluates a conditional expression; returns one value if TRUE and an alternate value if FALSE. Can be nested for multi-tier evaluation.",
         "Dataset: Employee Target Achievement % in cell F2 = 108%",
         "Exact Formula: =IF(F2>=100%, \"Bonus Eligible\", \"Standard Pay\")",
         "Required Output: \"Bonus Eligible\""),
        
        ("6. VLOOKUP Function (Vertical Database Search)",
         "Syntax: =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])",
         "Searches vertically down the leftmost column of a table for a lookup value and returns the corresponding value from a specified column in the same row.",
         "Dataset: Table A2:D50 has Roll Number in Col 1, Student Name in Col 2, Grade in Col 4.",
         "Exact Formula: =VLOOKUP(\"IM-2K26-58\", A2:D50, 2, FALSE)",
         "Required Output: \"Krishna Dixit\" (Exact Match Search)"),
        
        ("7. CONCATENATE / CONCAT Function",
         "Syntax: =CONCAT(text1, [text2], ...) or =CONCATENATE(text1, text2, ...)",
         "Merges text strings from two or more cells into a single continuous formatted string.",
         "Dataset: First Name in A2 = \"Krishna\", Last Name in B2 = \"Dixit\", Roll in C2 = \"IM-58\"",
         "Exact Formula: =CONCAT(A2, \" \", B2, \" (\", C2, \")\")",
         "Required Output: \"Krishna Dixit (IM-58)\"")
    ]
    
    for f_title, f_syn, f_desc, f_data, f_form, f_out in func_specs:
        add_h3(f_title)
        add_bullet(f_syn, "• ")
        add_bullet(f_desc, "• Functional Purpose: ")
        add_bullet(f_data, "• Practical Scenario: ")
        add_bullet(f_form, "• Formula Implemented: ")
        add_bullet(f_out, "• Calculated Output Result: ")

    doc.add_page_break()

    # ==================== TOPIC 4 ====================
    add_section_header("4", "Microsoft PowerPoint: Components, Text Handling, Transitions & Animations")
    
    add_p("Microsoft PowerPoint is the industry-standard executive presentation software. It allows business strategists, entrepreneurs, and managers to synthesize complex corporate narratives, financial models, and strategic visions into compelling visual slide decks.")
    
    add_image_box("powerpoint_interface.png", "Microsoft PowerPoint Workspace, Transitions Ribbon, and Slide Canvas", width=Inches(5.8))
    
    add_h2("4.1 Basic Components of Microsoft PowerPoint")
    add_bullet("Located on the left side, displaying miniature thumbnail previews of all presentation slides in sequential order. Slides can be dragged to reorder, duplicated (Ctrl+D), hidden, or deleted.", "• Slide Navigation / Thumbnail Pane:")
    add_bullet("The primary central workspace where slide layout elements, text boxes, images, diagrams, charts, and video embeds are positioned and authored.", "• Slide Workspace / Canvas:")
    add_bullet("Bottom expandable drawer beneath the slide canvas where presenter scripts, talking points, and statistical citations are entered. These notes appear exclusively to the speaker during Presenter View and are hidden from the audience.", "• Notes Pane (Speaker Notes):")
    add_bullet("Contains presentation-specific tabs including Transitions (slide-level movement), Animations (object-level entrance/exit effects), and Slide Show (delivery settings).", "• PowerPoint Ribbon System:")
    add_bullet("Located on the bottom right: Normal View (authoring), Slide Sorter View (light-table matrix grid for bulk reorganization), Reading View (borderless window preview), and Slide Show (F5 for fullscreen projection).", "• Presentation View Modes:")

    add_h2("4.2 Text Handling Features on Slides")
    add_p("Unlike MS-Word where text flows continuously down pages, PowerPoint text is contained inside discrete, modular Text Placeholders or Text Boxes:")
    
    add_bullet("Pre-configured slide structures including Title Slide, Title and Content, Section Header, Two Content, Comparison, Title Only, and Blank.", "• Standard Slide Layouts:")
    add_bullet("PowerPoint offers Character Spacing presets (Very Tight, Tight, Normal, Loose, Very Loose) to optimize legibility on auditorium projection screens.", "• Character Spacing & Kerning:")
    add_bullet("Stylized typographical effects incorporating 3D bevels, drop shadows, glow effects, and gradient stroke outlines.", "• WordArt & Text Effects:")
    add_bullet("Horizontal (Left, Center, Right, Justified), Vertical Alignment (Top, Middle, Bottom inside shape), and Multi-Column Text inside a single text box.", "• Multi-Directional Text Alignment:")
    add_bullet("Transforms horizontal text into Vertical (Stacked) or Rotated 90° / 270°, essential for side banners and timeline labels.", "• Text Direction:")
    add_bullet("Selecting any bulleted list and clicking 'Convert to SmartArt' instantly transforms raw bullet text into sophisticated diagrams: Hierarchies (Org Charts), Processes (Linear Chevrons), Cycles (Feedback loops), and Pyramids (Maslow's hierarchy / strategy tiers).", "• SmartArt Conversion:")

    add_h2("4.3 Comprehensive Additional Features with Practical Implementation")
    
    add_h3("4.3.1 Slide Master (Corporate Brand Governance)")
    add_p("The Slide Master is the underlying template blueprint that controls global formatting across every slide in the deck. By editing the Slide Master (View Tab > Slide Master), a company can enforce unified brand guidelines: placing the corporate logo at the top right, locking header fonts (e.g. Arial Bold), setting background colors, and formatting footer placeholders (automatic slide number, date, confidentiality notices). Any change made to the master slide cascades instantaneously across all 50+ slides.")

    add_h3("4.3.2 Slide Transitions vs Custom Animations")
    add_p("It is vital to distinguish between Slide Transitions (which occur between slides) and Custom Animations (which apply to individual objects on a single slide):")
    
    # Transitions vs Animations Table
    trans_tbl = doc.add_table(rows=5, cols=3)
    trans_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(trans_tbl, color="CBD5E1", sz="6")
    
    t_headers = ["Parameter", "Slide Transitions", "Custom Animations"]
    for c_i, h in enumerate(t_headers):
        c = trans_tbl.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    t_data = [
        ("Scope of Action", "Applies to the entire slide as it appears on screen", "Applies to individual text boxes, images, or chart bars within a slide"),
        ("Category Types", "Subtle (Fade, Push, Wipe), Exciting (Curtains, Ripple), Dynamic (Morph)", "Entrance (Green), Emphasis (Yellow), Exit (Red), Motion Paths"),
        ("Trigger Event", "Advance on Mouse Click OR Automatically after N seconds", "Start On Click, Start With Previous, or Start After Previous"),
        ("Executive Best Practice", "Use subtle Morph or Fade (0.75s to 1.2s duration) for corporate dignity", "Animate bullet points 'By Paragraph' so discussion focuses on one point at a time")
    ]
    for r_i, rvals in enumerate(t_data):
        row = trans_tbl.rows[r_i+1]
        for c_i, val in enumerate(rvals):
            c = row.cells[c_i]
            set_cell_background(c, "F8FAFC" if r_i % 2 == 1 else "FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i > 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.bold = (c_i == 0)
            r.font.color.rgb = COLOR_PRIMARY if c_i == 0 else COLOR_TEXT

    add_h3("4.3.3 Presenter View and Professional Delivery Features")
    add_bullet("When connected to a dual-monitor or projector setup, Presenter View displays the live slide to the audience while showing the speaker the current slide, upcoming slide preview, live elapsed timer, speaker notes, digital laser pointer, and pen annotation tools.", "• Presenter View:")
    add_bullet("Slide Show Tab > Rehearse Timings records the exact time spent per slide, assisting speakers in pacing their presentations to conform to strict corporate board limits.", "• Rehearse Timings:")

    doc.add_page_break()

    # ==================== TOPIC 5 ====================
    add_section_header("5", "Microsoft Access: Features, Advantages & Business Applications")
    
    add_p("Microsoft Access is a desktop Relational Database Management System (RDBMS) that combines the relational Microsoft Jet Database Engine with a graphical user interface and rapid application development software tools. While spreadsheets like Excel store flat two-dimensional data grids, Access manages interconnected multi-table relational databases governed by strict data integrity rules.")
    
    add_image_box("access_rdbms_architecture.png", "MS-Access Relational Schema Architecture, Foreign Keys, and Core Objects", width=Inches(5.8))
    
    add_h2("5.1 In-Depth Features of Microsoft Access")
    
    add_h3("5.1.1 Six Core Database Objects")
    add_bullet("The foundational data repositories structured into Rows (Records) and Columns (Fields/Attributes). Each field has a defined data type and validation rule.", "1. Tables:")
    add_bullet("SQL-powered search and calculation mechanisms used to retrieve, filter, sort, combine, and summarize data across multiple related tables. Types include Select Queries, Parameter Queries, and Action Queries (Append, Update, Delete, Make-Table).", "2. Queries:")
    add_bullet("Custom graphical user interfaces (GUI) designed for data entry, editing, and navigation. Forms prevent accidental modification of underlying table structures and can embed subforms.", "3. Forms:")
    add_bullet("Formatted, printable documents that summarize, aggregate, and present database records for executive decision-making. Reports support multi-level grouping and automated mailing label generation.", "4. Reports:")
    add_bullet("Automated sequences of pre-built actions executed without requiring programming, such as opening forms, validating records, or printing reports upon button clicks.", "5. Macros:")
    add_bullet("VBA (Visual Basic for Applications) code blocks enabling sophisticated business logic, API integrations, and custom database routines.", "6. Modules:")

    add_h3("5.1.2 Relational Integrity & Data Modeling")
    add_bullet("A field (or combination of fields) that uniquely identifies every record in a table (e.g., `StudentID` or `ProductCode`). It guarantees entity integrity and cannot contain null values.", "• Primary Key (PK):")
    add_bullet("A field in a child table that refers directly to the Primary Key of a parent table, establishing a formal relationship.", "• Foreign Key (FK):")
    add_bullet("One-to-One (e.g., Employee to Company Car), One-to-Many (e.g., One Customer to Multiple Purchase Orders), and Many-to-Many (e.g., Multiple Students enrolled in Multiple Courses, resolved via a junction table).", "• Relationship Cardinality:")
    add_bullet("Prevents orphan records: ensuring that an order cannot be created for a nonexistent CustomerID, and cascading updates/deletes when parent records are modified.", "• Referential Integrity:")

    add_h2("5.2 Advantages of Microsoft Access for Business Organizations")
    add_bullet("Included in standard Microsoft 365 and Office Professional bundles, avoiding the massive licensing fees of enterprise systems like Oracle or SAP.", "1. Cost-Effective Solution:")
    add_bullet("Business managers can design fully functional relational systems (tables, forms, reports) in hours using built-in wizards without writing complex code.", "2. Rapid Application Development (RAD):")
    add_bullet("Strict field data types (AutoNumber, Currency, Date/Time, Yes/No), input masks (e.g. phone number formats), and validation rules eliminate dirty data and duplication inherent in flat spreadsheets.", "3. Data Integrity & Redundancy Reduction:")
    add_bullet("Supports simultaneous access for up to 255 concurrent users (ideal for small to mid-sized departmental teams) via split database architecture (Frontend GUI linked to Backend data tables).", "4. Multi-User Workgroup Support:")
    add_bullet("Seamlessly imports and exports data to Microsoft Excel, creates Mail Merge letters in Word, and can upsize to enterprise Microsoft SQL Server / Azure Cloud as the business expands.", "5. Enterprise Office Integration:")

    add_h2("5.3 Concrete Business Applications of MS-Access")
    add_bullet("Tracking customer demographics, lead stages, interaction history, quotation statuses, and automated follow-up scheduling.", "• Small Business CRM & Sales Tracking:")
    add_bullet("Managing stock keeping units (SKUs), reorder thresholds, supplier directories, warehouse bin locations, and purchase order histories.", "• Inventory & Warehouse Management:")
    add_bullet("Universities utilize Access to maintain student bio-data, course registrations, fee receipts, semester examination marks, and automated grade report generation.", "• Academic Student Information Systems:")
    add_bullet("Tracking employee attendance, leave balances, performance appraisals, departmental allocations, and monthly salary slip compilation.", "• Human Resource & Payroll Databases:")

    doc.add_page_break()

    # ==================== TOPIC 6 ====================
    add_section_header("6", "Internet Technologies: Search Engine Architecture & Email Protocols")
    
    add_p("The modern internet ecosystem is powered by search engines that organize humanity's digital knowledge and electronic mail systems that underpin global corporate communication.")
    
    add_image_box("search_engine_architecture.png", "Search Engine Operation: Crawling, Inverted Indexing, Query Processing & SERP", width=Inches(5.8))
    
    add_h2("6.1 In-Depth Analysis of Search Engines")
    add_p("A search engine is an automated software program designed to discover, index, and retrieve hyperlinked information available on the World Wide Web based on user-submitted keywords.")

    add_h3("6.1.1 The Four-Stage Architecture of Modern Search Engines")
    add_bullet("Automated bots or spiders (such as Googlebot or Bingbot) continuously traverse the web 24/7. Crawlers discover web pages by following hyperlinks from known URLs, reading XML sitemaps, and parsing robots.txt rules.", "1. Web Crawling:")
    add_bullet("The harvested HTML web pages are parsed, stripped of boilerplate markup, tokenized, and cataloged into an enormous Inverted Index database. An inverted index functions like the index at the back of a textbook: mapping distinct keyword terms to the exact list of URLs where they occur, alongside term frequency and positional weights.", "2. Indexing & Tokenization:")
    add_bullet("When a user types a search prompt, natural language processing (NLP) models (e.g., Google RankBrain, BERT, MUM) parse the query, correcting spelling mistakes, discerning search intent, identifying geographical context, and analyzing synonyms.", "3. Query Processing:")
    add_bullet("Proprietary ranking algorithms evaluate over 200 ranking signals (including PageRank backlink authority, content relevance, mobile-friendliness, page load speed, and domain trustworthiness) to score candidates and render the final Search Engine Results Page (SERP) in less than 0.3 seconds.", "4. Ranking & SERP Rendering:")

    add_h3("6.1.2 Advanced Search Operators for Executive Information Retrieval")
    add_bullet("Forces the search engine to return pages containing that exact continuous phrase without word alterations.", '• Exact Match (" "):', space_after=2)
    add_p('Example: "MBA Management Science syllabus" (filters out pages where these words appear scattered).', bold_prefix="  ")
    add_bullet("Restricts search queries strictly to a specific domain name or top-level domain.", "• Domain Filter (site:):", space_after=2)
    add_p("Example: site:dauniv.ac.in exam schedule (retrieves results exclusively from DAVV official servers).", bold_prefix="  ")
    add_bullet("Restricts results to specific file formats such as PDF, PPTX, or XLSX.", "• Filetype Filter (filetype:):", space_after=2)
    add_p("Example: strategic management case study filetype:pdf (retrieves downloadable academic case studies).", bold_prefix="  ")
    add_bullet("Hyphen operator excludes specific unwanted terms from search results.", "• Negative Keyword (-):", space_after=2)
    add_p("Example: cloud storage providers -amazon (excludes AWS from comparative search).", bold_prefix="  ")

    add_h2("6.2 Electronic Mail (Email) Systems and Protocol Architecture")
    add_p("Email is the primary formal communication protocol across global business and governance. Unlike web browsing which utilizes HTTP/HTTPS request-response flows, email employs a store-and-forward client-server architecture utilizing distinct push and pull protocols.")

    add_image_box("email_protocols_architecture.png", "End-to-End Email Architecture: Client MUA, SMTP Transmission & IMAP/POP3 Delivery", width=Inches(5.8))

    add_h3("6.2.1 Core Email Communication Protocols")
    
    # Protocols Comparison Table
    proto_tbl = doc.add_table(rows=4, cols=4)
    proto_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(proto_tbl, color="CBD5E1", sz="6")
    
    p_headers = ["Protocol Name", "Full Expansion & Default Ports", "Operational Mechanism", "Primary Business Use Case"]
    for c_i, h in enumerate(p_headers):
        c = proto_tbl.rows[0].cells[c_i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=70, right=70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    p_data = [
        ("SMTP", "Simple Mail Transfer Protocol\nPort 25 (relay), Port 587 (STARTTLS)", "Push Protocol: Transmits outgoing messages from sender MUA to mail server and server-to-server relay", "Sending all outbound corporate emails and relaying across internet MTAs"),
        ("POP3", "Post Office Protocol Version 3\nPort 110 (plain), Port 995 (SSL/TLS)", "Pull Protocol: Downloads messages to local client storage and deletes from server by default", "Single-device legacy access with constrained server storage capacity"),
        ("IMAP", "Internet Message Access Protocol\nPort 143 (plain), Port 993 (SSL/TLS)", "Two-Way Synchronization: Messages remain on server; folders and read states sync across all devices", "Modern multi-device enterprise communication (Smartphone, Laptop, Webmail)")
    ]
    for r_i, rvals in enumerate(p_data):
        row = proto_tbl.rows[r_i+1]
        for c_i, val in enumerate(rvals):
            c = row.cells[c_i]
            set_cell_background(c, "F8FAFC" if r_i % 2 == 1 else "FFFFFF")
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i > 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.bold = (c_i == 0)
            r.font.color.rgb = COLOR_PRIMARY if c_i == 0 else COLOR_TEXT

    add_h3("6.2.2 Anatomy of an Email Message")
    add_bullet("From (Sender address), To (Primary recipients), Cc (Carbon Copy for informed parties), Bcc (Blind Carbon Copy for confidential distribution where addresses remain concealed), Subject (concise executive summary), Date, and Message-ID.", "• Envelope & Headers:")
    add_bullet("The message text formatted in plain ASCII or structured HTML styling.", "• Message Body:")
    add_bullet("MIME (Multipurpose Internet Mail Extensions) encodes binary files (PDF contracts, Excel spreadsheets, JPEG images) into base64 text blocks transmitted alongside the email.", "• Attachments & MIME:")

    add_h3("6.2.3 Enterprise Email Security & Cyber Governance")
    add_bullet("Validates that outgoing mail originates from authorized IP addresses listed in the domain's DNS TXT record.", "• SPF (Sender Policy Framework):")
    add_bullet("Attaches a cryptographic digital signature to email headers, allowing receiving servers to verify that the message was not tampered with in transit.", "• DKIM (DomainKeys Identified Mail):")
    add_bullet("Enforces domain governance policies instructing receiving servers whether to accept, quarantine, or reject spoofed emails.", "• DMARC:")

    doc.add_page_break()

    # ==================== TOPIC 7 ====================
    add_section_header("7", "Web Page Designing: Student Entry Form & Commercial Purchase Order")
    
    add_p("Web forms represent the primary interactive bridge for electronic data capture across web browsers. Built on HTML5, CSS3, and JavaScript, forms allow users to submit structured records directly to backend application servers.")

    add_h2("7.1 Design and Implementation of Student Entry Form")
    add_p("Required Form Fields: Student Roll No., Name of Student, Program Name, Class, and Section.")

    add_image_box("student_entry_form_preview.png", "Rendered Browser Interface of Student Admission & Entry Form (IIPS DAVV)", width=Inches(5.6))

    add_h3("7.1.1 Full Semantic HTML5 and CSS3 Source Code (student_entry_form.html)")
    
    code_student = (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "    <meta charset=\"UTF-8\">\n"
        "    <title>Student Admission Entry Form | IIPS DAVV</title>\n"
        "    <style>\n"
        "        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f1f5f9; padding: 24px; display: flex; justify-content: center; }\n"
        "        .card { background: #fff; width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); overflow: hidden; }\n"
        "        .header { background: #1e3a8a; color: #fff; padding: 20px; text-align: center; }\n"
        "        form { padding: 24px; }\n"
        "        .form-group { margin-bottom: 16px; }\n"
        "        label { display: block; font-weight: 600; font-size: 13px; margin-bottom: 6px; color: #1e293b; }\n"
        "        input[type=\"text\"], select { width: 100%; padding: 10px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px; box-sizing: border-box; }\n"
        "        .radio-group { display: flex; gap: 20px; padding: 6px 0; }\n"
        "        .btn-submit { background: #1e3a8a; color: #fff; padding: 12px 24px; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; width: 100%; }\n"
        "    </style>\n"
        "</head>\n"
        "<body>\n"
        "    <div class=\"card\">\n"
        "        <div class=\"header\">\n"
        "            <h2>International Institute of Professional Studies, DAVV</h2>\n"
        "            <p>Student Admission & Academic Registration Form</p>\n"
        "        </div>\n"
        "        <form action=\"#\" method=\"POST\">\n"
        "            <div class=\"form-group\">\n"
        "                <label for=\"rollNo\">Roll Number *</label>\n"
        "                <input type=\"text\" id=\"rollNo\" name=\"rollNo\" value=\"IM-2K26-58\" placeholder=\"e.g. IM-2K26-58\" required pattern=\"^[A-Za-z0-9\\-]+$\">\n"
        "            </div>\n"
        "            <div class=\"form-group\">\n"
        "                <label for=\"name\">Name of Student *</label>\n"
        "                <input type=\"text\" id=\"name\" name=\"name\" value=\"Krishna Dixit\" placeholder=\"Enter Full Name\" required>\n"
        "            </div>\n"
        "            <div class=\"form-group\">\n"
        "                <label for=\"program\">Program Name *</label>\n"
        "                <select id=\"program\" name=\"program\" required>\n"
        "                    <option value=\"MBA(MS) 5 Yrs\" selected>MBA (Management Science) 5 Yrs Integrated</option>\n"
        "                    <option value=\"MBA(Tourism) 5 Yrs\">MBA (Tourism) 5 Yrs Integrated</option>\n"
        "                    <option value=\"MCA 6 Yrs\">MCA 6 Yrs Integrated</option>\n"
        "                </select>\n"
        "            </div>\n"
        "            <div class=\"form-group\">\n"
        "                <label for=\"class\">Class & Semester *</label>\n"
        "                <select id=\"class\" name=\"class\" required>\n"
        "                    <option value=\"MBA(MS) - 1st Year (Semester I)\" selected>1st Year (Semester I)</option>\n"
        "                    <option value=\"MBA(MS) - 1st Year (Semester II)\">1st Year (Semester II)</option>\n"
        "                </select>\n"
        "            </div>\n"
        "            <div class=\"form-group\">\n"
        "                <label>Section *</label>\n"
        "                <div class=\"radio-group\">\n"
        "                    <label><input type=\"radio\" name=\"section\" value=\"Section A\" checked required> Section A</label>\n"
        "                    <label><input type=\"radio\" name=\"section\" value=\"Section B\" required> Section B</label>\n"
        "                </div>\n"
        "            </div>\n"
        "            <button type=\"submit\" class=\"btn-submit\">Register Student Record</button>\n"
        "        </form>\n"
        "    </div>\n"
        "</body>\n"
        "</html>"
    )
    add_code_box(code_student)

    add_h2("7.2 Design and Implementation of Product Purchase Order Form")
    add_p("Required Form Fields: Product Name, Product Code, Price, Quantity, and Date. (Includes dynamic JavaScript calculation for Total Order Value).")

    add_image_box("product_purchase_order_preview.png", "Rendered Browser Interface of Enterprise Product Purchase Order Form", width=Inches(5.6))

    add_h3("7.2.1 Full Semantic HTML5 and JavaScript Source Code (product_purchase_order.html)")
    
    code_po = (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "    <meta charset=\"UTF-8\">\n"
        "    <title>Commercial Product Purchase Order</title>\n"
        "    <style>\n"
        "        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; padding: 24px; display: flex; justify-content: center; }\n"
        "        .po-box { background: #fff; width: 100%; max-width: 620px; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 15px rgba(0,0,0,0.06); padding: 28px; }\n"
        "        .po-header { background: #059669; color: #fff; margin: -28px -28px 24px -28px; padding: 20px; text-align: center; border-radius: 9px 9px 0 0; }\n"
        "        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }\n"
        "        .full { grid-column: span 2; }\n"
        "        label { display: block; font-weight: 600; font-size: 13px; margin-bottom: 6px; color: #334155; }\n"
        "        input { width: 100%; padding: 10px; border: 1.5px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-size: 14px; }\n"
        "        .calc-box { background: #ecfdf5; border: 1.5px dashed #34d399; padding: 14px; border-radius: 6px; margin: 18px 0; text-align: center; font-weight: 700; color: #065f46; }\n"
        "        .btn-order { background: #059669; color: #fff; padding: 12px; border: none; border-radius: 6px; font-weight: 600; width: 100%; cursor: pointer; }\n"
        "    </style>\n"
        "</head>\n"
        "<body>\n"
        "    <div class=\"po-box\">\n"
        "        <div class=\"po-header\">\n"
        "            <h2>Commercial Purchase Order Form</h2>\n"
        "            <p>Enterprise Procurement Management System</p>\n"
        "        </div>\n"
        "        <form oninput=\"calcTotal()\">\n"
        "            <div class=\"grid\">\n"
        "                <div class=\"full\">\n"
        "                    <label>Product Name *</label>\n"
        "                    <input type=\"text\" id=\"pname\" placeholder=\"e.g. Dell Latitude 5430 Business Laptop\" required>\n"
        "                </div>\n"
        "                <div>\n"
        "                    <label>Product Code *</label>\n"
        "                    <input type=\"text\" id=\"pcode\" placeholder=\"e.g. PRD-DELL-5430\" required>\n"
        "                </div>\n"
        "                <div>\n"
        "                    <label>Order Date *</label>\n"
        "                    <input type=\"date\" id=\"pdate\" value=\"2026-11-14\" required>\n"
        "                </div>\n"
        "                <div>\n"
        "                    <label>Unit Price (₹) *</label>\n"
        "                    <input type=\"number\" id=\"price\" placeholder=\"0.00\" min=\"0.01\" step=\"0.01\" required>\n"
        "                </div>\n"
        "                <div>\n"
        "                    <label>Quantity *</label>\n"
        "                    <input type=\"number\" id=\"qty\" placeholder=\"1\" min=\"1\" step=\"1\" required>\n"
        "                </div>\n"
        "            </div>\n"
        "            <div class=\"calc-box\" id=\"totalDisplay\">Total Order Value: ₹0.00</div>\n"
        "            <button type=\"submit\" class=\"btn-order\">Generate Official Purchase Order</button>\n"
        "        </form>\n"
        "    </div>\n"
        "    <script>\n"
        "        function calcTotal() {\n"
        "            const p = parseFloat(document.getElementById('price').value) || 0;\n"
        "            const q = parseInt(document.getElementById('qty').value, 10) || 0;\n"
        "            document.getElementById('totalDisplay').innerText = 'Total Order Value: ₹' + (p * q).toLocaleString('en-IN', {minimumFractionDigits: 2});\n"
        "        }\n"
        "    </script>\n"
        "</body>\n"
        "</html>"
    )
    add_code_box(code_po)

    add_callout("Web Form Technical Architecture", "Both forms utilize semantic HTML5 tags (<form>, <fieldset>, <legend>, <label>, <input>, <select>, <button>) along with strict client-side validation attributes (required, pattern, min, step) to prevent malformed database entries.")

    # Save document
    doc.save(OUTPUT_DOCX)
    doc.save(GENERIC_DOCX)
    print(f"Document successfully created and saved at:\n1. {OUTPUT_DOCX}\n2. {GENERIC_DOCX}")

if __name__ == "__main__":
    build_document()
