import os
from PIL import Image, ImageDraw, ImageFont

ASSETS = '/Users/krishna/.gemini/antigravity/scratch/MBA_Computer_Applications_Assignment/assets'
os.makedirs(ASSETS, exist_ok=True)

def get_font(size, bold=False):
    try:
        path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf'
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, coords, radius=10, fill=None, outline=None, width=1):
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=width)

def draw_arrow(draw, start, end, color=(70, 80, 95), width=2, arrow_size=8):
    x1, y1 = start
    x2, y2 = end
    draw.line([start, end], fill=color, width=width)
    import math
    angle = math.atan2(y2 - y1, x2 - x1)
    # arrow head
    xa = x2 - arrow_size * math.cos(angle - math.pi / 6)
    ya = y2 - arrow_size * math.sin(angle - math.pi / 6)
    xb = x2 - arrow_size * math.cos(angle + math.pi / 6)
    yb = y2 - arrow_size * math.sin(angle + math.pi / 6)
    draw.polygon([(x2, y2), (xa, ya), (xb, yb)], fill=color)

# 1. IO Architecture Diagram
def create_io_arch():
    w, h = 900, 480
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Title Banner
    draw_rounded_rect(draw, (20, 15, w-20, 65), radius=8, fill=(30, 58, 138))
    f_title = get_font(22, bold=True)
    draw.text((w/2, 40), "Computer System Hardware Architecture: Input - Process - Output - Storage", fill=(255, 255, 255), anchor="mm", font=f_title)
    
    # 4 Main Blocks
    # Input Devices Block
    draw_rounded_rect(draw, (30, 90, 220, 390), radius=10, fill=(239, 246, 255), outline=(59, 130, 246), width=2)
    draw_rounded_rect(draw, (30, 90, 220, 130), radius=10, fill=(59, 130, 246))
    draw.text((125, 110), "INPUT DEVICES", fill=(255, 255, 255), anchor="mm", font=get_font(15, bold=True))
    inputs = ["• Keyboard (Text / Commands)", "• Mouse (Pointing / GUI)", "• Scanner (Image / OCR)", "• Microphone (Audio)", "• Web Camera (Video)", "• Barcode / QR Reader"]
    y = 155
    for item in inputs:
        draw.text((45, y), item, fill=(30, 41, 59), font=get_font(13))
        y += 35
        
    # Central Processing Unit (CPU)
    draw_rounded_rect(draw, (290, 90, 610, 310), radius=10, fill=(240, 253, 244), outline=(34, 197, 94), width=2)
    draw_rounded_rect(draw, (290, 90, 610, 130), radius=10, fill=(34, 197, 94))
    draw.text((450, 110), "CENTRAL PROCESSING UNIT (CPU)", fill=(255, 255, 255), anchor="mm", font=get_font(15, bold=True))
    
    # ALU Box
    draw_rounded_rect(draw, (310, 150, 590, 210), radius=6, fill=(255, 255, 255), outline=(22, 163, 74), width=1)
    draw.text((450, 170), "Arithmetic Logic Unit (ALU)", fill=(21, 128, 61), anchor="mm", font=get_font(14, bold=True))
    draw.text((450, 192), "Performs Mathematical (+,-,*,/) & Logical Ops", fill=(71, 85, 105), anchor="mm", font=get_font(11))
    
    # Control Unit Box
    draw_rounded_rect(draw, (310, 225, 590, 285), radius=6, fill=(255, 255, 255), outline=(22, 163, 74), width=1)
    draw.text((450, 245), "Control Unit (CU) & Registers", fill=(21, 128, 61), anchor="mm", font=get_font(14, bold=True))
    draw.text((450, 267), "Directs Data Flow, Fetches & Decodes Instructions", fill=(71, 85, 105), anchor="mm", font=get_font(11))
    
    # Storage Block (Bottom)
    draw_rounded_rect(draw, (290, 340, 610, 450), radius=10, fill=(254, 243, 199), outline=(245, 158, 11), width=2)
    draw_rounded_rect(draw, (290, 340, 610, 375), radius=10, fill=(245, 158, 11))
    draw.text((450, 357), "MEMORY & STORAGE UNIT", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    draw.text((450, 395), "• Primary Memory: RAM (Volatile) & ROM (BIOS)", fill=(120, 53, 15), anchor="mm", font=get_font(12, bold=True))
    draw.text((450, 420), "• Secondary Storage: SSD, HDD, Flash Drives, Cloud Storage", fill=(146, 64, 14), anchor="mm", font=get_font(12))

    # Output Devices Block
    draw_rounded_rect(draw, (680, 90, 870, 390), radius=10, fill=(254, 242, 242), outline=(239, 68, 68), width=2)
    draw_rounded_rect(draw, (680, 90, 870, 130), radius=10, fill=(239, 68, 68))
    draw.text((775, 110), "OUTPUT DEVICES", fill=(255, 255, 255), anchor="mm", font=get_font(15, bold=True))
    outputs = ["• Monitor (Visual Display)", "• Printer (Hard Copy)", "• Speaker (Audio Output)", "• Projector (Display)", "• Headphones (Personal)", "• Plotter (Vector Graphics)"]
    y = 155
    for item in outputs:
        draw.text((695, y), item, fill=(30, 41, 59), font=get_font(13))
        y += 35
        
    # Arrows
    draw_arrow(draw, (220, 200), (285, 200), color=(37, 99, 235), width=3, arrow_size=10)
    draw_arrow(draw, (615, 200), (675, 200), color=(220, 38, 38), width=3, arrow_size=10)
    # Bidirectional arrows CPU <-> Memory
    draw_arrow(draw, (420, 312), (420, 338), color=(217, 119, 6), width=3, arrow_size=8)
    draw_arrow(draw, (480, 338), (480, 312), color=(217, 119, 6), width=3, arrow_size=8)
    
    im.save(os.path.join(ASSETS, 'io_architecture.png'), quality=95)
    print("Created io_architecture.png")

# 2. MS Word Interface Schematic
def create_word_interface():
    w, h = 900, 520
    im = Image.new('RGB', (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    # Title Bar
    draw.rectangle([0, 0, w, 36], fill=(43, 87, 154))
    draw.text((20, 18), "AutoSave  OFF   |   Document1 - Microsoft Word", fill=(255, 255, 255), anchor="lm", font=get_font(13, bold=True))
    draw.text((w - 70, 18), "—   □   ✕", fill=(255, 255, 255), anchor="lm", font=get_font(14, bold=True))
    
    # Ribbon Tabs
    draw.rectangle([0, 36, w, 68], fill=(241, 245, 249))
    tabs = ["File", "Home", "Insert", "Draw", "Design", "Layout", "References", "Mailings", "Review", "View", "Help"]
    tx = 20
    for i, t in enumerate(tabs):
        is_active = (t == "Home")
        if is_active:
            draw.rectangle([tx-6, 38, tx+48, 68], fill=(255, 255, 255), outline=(203, 213, 225), width=1)
            draw.line([tx-6, 68, tx+48, 68], fill=(43, 87, 154), width=3)
            draw.text((tx+21, 52), t, fill=(43, 87, 154), anchor="mm", font=get_font(13, bold=True))
            tx += 58
        else:
            draw.text((tx+15, 52), t, fill=(51, 65, 85), anchor="mm", font=get_font(12))
            tx += 62
            
    # Ribbon Toolbar Area
    draw.rectangle([0, 68, w, 155], fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    
    # Ribbon Groups (Clipboard, Font, Paragraph, Styles, Editing)
    groups = [
        ("Clipboard", 10, 140, ["Paste", "Cut", "Copy", "Painter"]),
        ("Font", 150, 360, ["Calibri (Body)  ▼   12  ▼", "B   I   U   ab   x₂  x²   A▼  🖍▼"]),
        ("Paragraph", 370, 590, ["•▼  123▼  ≡▼   ≣   ⇥  ⇤", "Left | Center | Right | Justify"]),
        ("Styles", 600, 770, ["Normal   No Spacing   Heading 1", "Heading 2   Title   Subtitle"]),
        ("Editing", 780, 890, ["Find 🔍", "Replace 🔄", "Select ▼"])
    ]
    for name, gx1, gx2, lines in groups:
        draw_rounded_rect(draw, (gx1, 74, gx2, 148), radius=4, fill=(250, 250, 252), outline=(226, 232, 240))
        draw.line([gx2, 74, gx2, 148], fill=(226, 232, 240), width=1)
        draw.text(((gx1+gx2)/2, 140), name, fill=(100, 116, 139), anchor="mm", font=get_font(10, bold=True))
        y_text = 90
        for l in lines:
            draw.text(((gx1+gx2)/2, y_text), l, fill=(30, 41, 59), anchor="mm", font=get_font(11))
            y_text += 24
            
    # Horizontal Ruler
    draw.rectangle([0, 155, w, 175], fill=(241, 245, 249), outline=(226, 232, 240))
    for rx in range(120, 780, 20):
        draw.line([rx, 168, rx, 174], fill=(148, 163, 184), width=1)
    for inch in range(1, 7):
        rx = 120 + inch * 90
        draw.text((rx, 162), str(inch), fill=(71, 85, 105), anchor="mm", font=get_font(9))

    # Canvas (Document Paper)
    draw.rectangle([130, 185, 770, 485], fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    # Text lines on document
    draw.text((160, 205), "BUSINESS REPORT & PRACTICAL DOCUMENTATION", fill=(43, 87, 154), font=get_font(14, bold=True))
    draw.text((160, 230), "MBA (Management Science) - Integrated 5 Years Program", fill=(100, 116, 139), font=get_font(11, bold=True))
    draw.line([160, 248, 740, 248], fill=(203, 213, 225), width=1)
    
    sample_text = [
        "Microsoft Word is a graphical word processing program that users can type with.",
        "Its purpose is to allow users to type and save documents. Similar to other word processors,",
        "it has helpful tools to make documents. Text handling features include fonts, paragraphs,",
        "styles, tables, mail merge, page setup, header/footer, and spell check automation."
    ]
    sy = 265
    for st in sample_text:
        draw.text((160, sy), st, fill=(51, 65, 85), font=get_font(12))
        sy += 24

    # Sample Table on canvas
    draw_rounded_rect(draw, (160, 375, 740, 460), radius=4, outline=(71, 85, 105), width=1)
    draw.rectangle([160, 375, 740, 400], fill=(43, 87, 154))
    draw.text((210, 388), "Student Name", fill=(255, 255, 255), anchor="mm", font=get_font(11, bold=True))
    draw.text((360, 388), "Roll Number", fill=(255, 255, 255), anchor="mm", font=get_font(11, bold=True))
    draw.text((500, 388), "Subject Code", fill=(255, 255, 255), anchor="mm", font=get_font(11, bold=True))
    draw.text((650, 388), "Marks Obtained", fill=(255, 255, 255), anchor="mm", font=get_font(11, bold=True))
    # Row 1
    draw.line([160, 400, 740, 400], fill=(203, 213, 225))
    draw.text((210, 415), "Krishna Dixit", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((360, 415), "IM-2K26-58", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((500, 415), "IM-104C", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((650, 415), "19 / 20", fill=(22, 163, 74), anchor="mm", font=get_font(11, bold=True))
    # Row 2
    draw.line([160, 430, 740, 430], fill=(203, 213, 225))
    draw.text((210, 445), "Ananya Sharma", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((360, 445), "IM-2K26-02", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((500, 445), "IM-104C", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((650, 445), "20 / 20", fill=(22, 163, 74), anchor="mm", font=get_font(11, bold=True))
    
    # Status Bar
    draw.rectangle([0, 490, w, 520], fill=(43, 87, 154))
    draw.text((20, 505), "Page 1 of 1    |    184 Words    |    English (United States)    |    Accessibility: Good to go", fill=(255, 255, 255), anchor="lm", font=get_font(11))
    draw.text((w - 180, 505), "Focus   ⊞  🗎  ▤   —  ●  + 100%", fill=(255, 255, 255), anchor="lm", font=get_font(11))
    
    # Callout overlays for annotation
    # Callout 1: Quick Access & Title Bar
    draw.line([250, 18, 320, 18], fill=(239, 68, 68), width=2)
    # Callout 2: Ribbon
    draw_rounded_rect(draw, (790, 80, 885, 105), radius=4, fill=(239, 68, 68))
    draw.text((837, 92), "Ribbon Tabs", fill=(255, 255, 255), anchor="mm", font=get_font(10, bold=True))

    im.save(os.path.join(ASSETS, 'ms_word_interface.png'), quality=95)
    print("Created ms_word_interface.png")

# 3. Mail Merge Workflow Diagram
def create_mail_merge_flow():
    w, h = 900, 420
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Title Banner
    draw_rounded_rect(draw, (20, 15, w-20, 65), radius=8, fill=(15, 76, 129))
    draw.text((w/2, 40), "MS-Word Mail Merge Architecture & 6-Step Workflow", fill=(255, 255, 255), anchor="mm", font=get_font(20, bold=True))
    
    # Block 1: Main Document
    draw_rounded_rect(draw, (30, 95, 250, 240), radius=8, fill=(240, 249, 255), outline=(2, 132, 199), width=2)
    draw_rounded_rect(draw, (30, 95, 250, 130), radius=8, fill=(2, 132, 199))
    draw.text((140, 112), "1. MAIN DOCUMENT", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    draw.text((140, 150), "Contains fixed standard text\nand dynamic merge fields:", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((140, 195), "Dear <<Candidate_Name>>,\nYour Roll: <<Roll_No>>\nRank: <<Rank>>", fill=(3, 105, 161), anchor="mm", font=get_font(12, bold=True))

    # Block 2: Data Source
    draw_rounded_rect(draw, (30, 260, 250, 400), radius=8, fill=(240, 253, 244), outline=(22, 163, 74), width=2)
    draw_rounded_rect(draw, (30, 260, 250, 295), radius=8, fill=(22, 163, 74))
    draw.text((140, 277), "2. DATA SOURCE", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    draw.text((140, 315), "Structured recipient records\n(Excel Sheet, Access DB, Outlook):", fill=(30, 41, 59), anchor="mm", font=get_font(11))
    draw.text((140, 360), "[Name, RollNo, Email, Address]\nRecord 1: Krishna Dixit\nRecord 2: Ananya Sharma", fill=(21, 128, 61), anchor="mm", font=get_font(11, bold=True))

    # Block 3: Mail Merge Engine (Middle)
    draw_rounded_rect(draw, (330, 110, 570, 385), radius=10, fill=(254, 243, 199), outline=(217, 119, 6), width=2)
    draw_rounded_rect(draw, (330, 110, 570, 150), radius=10, fill=(217, 119, 6))
    draw.text((450, 130), "3. MAIL MERGE WIZARD", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    
    steps = [
        "Step 1: Select Document Type (Letters)",
        "Step 2: Select Starting Document",
        "Step 3: Connect & Filter Recipients",
        "Step 4: Insert Merge Fields (<< >>)",
        "Step 5: Preview Dynamic Records",
        "Step 6: Complete Merge (Print/Email)"
    ]
    y_step = 175
    for s in steps:
        draw_rounded_rect(draw, (345, y_step-12, 555, y_step+16), radius=4, fill=(255, 255, 255), outline=(245, 158, 11), width=1)
        draw.text((450, y_step+2), s, fill=(120, 53, 15), anchor="mm", font=get_font(11, bold=True))
        y_step += 35

    # Block 4: Merged Output (Right)
    draw_rounded_rect(draw, (650, 110, 870, 385), radius=8, fill=(250, 245, 255), outline=(147, 51, 234), width=2)
    draw_rounded_rect(draw, (650, 110, 870, 150), radius=8, fill=(147, 51, 234))
    draw.text((760, 130), "4. MERGED OUTPUT", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    
    # Letters generated
    draw_rounded_rect(draw, (670, 170, 850, 225), radius=6, fill=(255, 255, 255), outline=(168, 85, 247), width=1)
    draw.text((760, 188), "Personalized Letter 1", fill=(107, 33, 168), anchor="mm", font=get_font(11, bold=True))
    draw.text((760, 208), "Dear Krishna Dixit (IM-2K26-58)", fill=(71, 85, 105), anchor="mm", font=get_font(10))

    draw_rounded_rect(draw, (670, 240, 850, 295), radius=6, fill=(255, 255, 255), outline=(168, 85, 247), width=1)
    draw.text((760, 258), "Personalized Letter 2", fill=(107, 33, 168), anchor="mm", font=get_font(11, bold=True))
    draw.text((760, 278), "Dear Ananya Sharma (IM-2K26-02)", fill=(71, 85, 105), anchor="mm", font=get_font(10))

    draw_rounded_rect(draw, (670, 310, 850, 365), radius=6, fill=(255, 255, 255), outline=(168, 85, 247), width=1)
    draw.text((760, 328), "Personalized Letter N...", fill=(107, 33, 168), anchor="mm", font=get_font(11, bold=True))
    draw.text((760, 348), "Sent to Printer / Email Inbox", fill=(71, 85, 105), anchor="mm", font=get_font(10))

    # Connecting Arrows
    draw_arrow(draw, (250, 170), (325, 210), color=(2, 132, 199), width=3, arrow_size=10)
    draw_arrow(draw, (250, 330), (325, 280), color=(22, 163, 74), width=3, arrow_size=10)
    draw_arrow(draw, (575, 247), (645, 247), color=(147, 51, 234), width=3, arrow_size=10)

    im.save(os.path.join(ASSETS, 'mail_merge_workflow.png'), quality=95)
    print("Created mail_merge_workflow.png")

# 4. MS Excel Interface Schematic
def create_excel_interface():
    w, h = 900, 520
    im = Image.new('RGB', (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    # Title Bar
    draw.rectangle([0, 0, w, 36], fill=(16, 124, 65))
    draw.text((20, 18), "AutoSave  ON   |   Financial_Model_2026.xlsx - Excel", fill=(255, 255, 255), anchor="lm", font=get_font(13, bold=True))
    draw.text((w - 70, 18), "—   □   ✕", fill=(255, 255, 255), anchor="lm", font=get_font(14, bold=True))
    
    # Ribbon Tabs
    draw.rectangle([0, 36, w, 68], fill=(241, 245, 249))
    tabs = ["File", "Home", "Insert", "Page Layout", "Formulas", "Data", "Review", "View", "Automate", "Help"]
    tx = 20
    for t in tabs:
        is_active = (t == "Home")
        if is_active:
            draw.rectangle([tx-6, 38, tx+48, 68], fill=(255, 255, 255), outline=(203, 213, 225), width=1)
            draw.line([tx-6, 68, tx+48, 68], fill=(16, 124, 65), width=3)
            draw.text((tx+21, 52), t, fill=(16, 124, 65), anchor="mm", font=get_font(13, bold=True))
            tx += 58
        else:
            draw.text((tx+20, 52), t, fill=(51, 65, 85), anchor="mm", font=get_font(12))
            tx += 72
            
    # Formula Bar & Name Box Area
    draw.rectangle([0, 68, w, 105], fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    # Name Box
    draw_rounded_rect(draw, (10, 74, 90, 98), radius=3, fill=(248, 250, 252), outline=(203, 213, 225))
    draw.text((50, 86), "C7", fill=(16, 124, 65), anchor="mm", font=get_font(13, bold=True))
    # fx symbol
    draw.text((110, 86), "fx", fill=(100, 116, 139), anchor="mm", font=get_font(14, bold=True))
    # Formula Input box
    draw_rounded_rect(draw, (130, 74, w-15, 98), radius=3, fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((145, 86), "=SUM(C2:C6)", fill=(30, 41, 59), anchor="lm", font=get_font(13, bold=True))

    # Grid Area
    # Headers
    col_w = 120
    cols = ["", "A", "B", "C", "D", "E", "F", "G"]
    col_x = [0, 45, 180, 310, 440, 570, 700, 830, w]
    
    draw.rectangle([0, 106, w, 132], fill=(226, 232, 240))
    for i in range(1, len(cols)):
        draw.line([col_x[i], 106, col_x[i], 480], fill=(226, 232, 240), width=1)
        draw.text(((col_x[i]+col_x[i+1])/2, 119), cols[i], fill=(71, 85, 105), anchor="mm", font=get_font(12, bold=True))
        
    # Rows
    rows_data = [
        ("1", ["Product Line", "Region", "Q1 Sales (₹)", "Q2 Sales (₹)", "Growth %", "Status"]),
        ("2", ["Smartphones", "North", "850,000", "920,000", "+8.2%", "Target Achieved"]),
        ("3", ["Laptops", "West", "1,200,000", "1,450,000", "+20.8%", "Target Achieved"]),
        ("4", ["Tablets", "South", "450,000", "410,000", "-8.9%", "Under Target"]),
        ("5", ["Wearables", "East", "320,000", "380,000", "+18.8%", "Target Achieved"]),
        ("6", ["Accessories", "Central", "210,000", "260,000", "+23.8%", "Target Achieved"]),
        ("7", ["TOTAL / FORMULA", "All", "3,030,000", "3,420,000", "+12.9%", "OVERALL PASS"])
    ]
    
    ry = 132
    for r_idx, (r_num, r_vals) in enumerate(rows_data):
        # Row header
        draw.rectangle([0, ry, 45, ry+35], fill=(241, 245, 249), outline=(226, 232, 240))
        draw.text((22, ry+17), r_num, fill=(71, 85, 105), anchor="mm", font=get_font(12, bold=True))
        
        # Row content
        for c_idx, val in enumerate(r_vals):
            x1 = col_x[c_idx+1]
            x2 = col_x[c_idx+2]
            
            # Row 1 is header
            if r_idx == 0:
                draw.rectangle([x1, ry, x2, ry+35], fill=(248, 250, 252))
                draw.text(((x1+x2)/2, ry+17), val, fill=(15, 23, 42), anchor="mm", font=get_font(11, bold=True))
            elif r_idx == 6: # Total row
                draw.rectangle([x1, ry, x2, ry+35], fill=(240, 253, 244))
                color = (16, 124, 65) if c_idx in [2, 3, 5] else (30, 41, 59)
                draw.text(((x1+x2)/2, ry+17), val, fill=color, anchor="mm", font=get_font(11, bold=True))
            else:
                # Active cell C7 highlight or cell styling
                bg = (255, 255, 255)
                # Conditional formatting simulation for Status
                if c_idx == 5:
                    bg = (220, 252, 231) if "Achieved" in val else (254, 226, 226)
                draw.rectangle([x1, ry, x2, ry+35], fill=bg)
                draw.text(((x1+x2)/2, ry+17), val, fill=(30, 41, 59), anchor="mm", font=get_font(11))
                
        draw.line([0, ry+35, w, ry+35], fill=(226, 232, 240), width=1)
        ry += 35
        
    # Active Cell border on C7
    # C is col_x[3] to col_x[4], row 7 is ry-35
    draw.rectangle([col_x[3]-1, ry-36, col_x[4]+1, ry], fill=None, outline=(16, 124, 65), width=3)
    
    # Sheet Tabs at bottom
    draw.rectangle([0, 460, w, 490], fill=(241, 245, 249), outline=(203, 213, 225))
    draw_rounded_rect(draw, (20, 463, 120, 490), radius=3, fill=(255, 255, 255))
    draw.line([20, 488, 120, 488], fill=(16, 124, 65), width=3)
    draw.text((70, 475), "Sales_Summary", fill=(16, 124, 65), anchor="mm", font=get_font(11, bold=True))
    draw.text((150, 475), "Quarterly_P&L", fill=(100, 116, 139), anchor="mm", font=get_font(11))
    draw.text((230, 475), "Charts", fill=(100, 116, 139), anchor="mm", font=get_font(11))
    draw.text((280, 475), "➕", fill=(16, 124, 65), anchor="mm", font=get_font(12))

    # Status Bar
    draw.rectangle([0, 490, w, 520], fill=(16, 124, 65))
    draw.text((20, 505), "Ready    |    Average: 606,000    |    Count: 5    |    Sum: 3,030,000", fill=(255, 255, 255), anchor="lm", font=get_font(11, bold=True))
    draw.text((w - 180, 505), "Normal   PageLayout   —  ●  + 100%", fill=(255, 255, 255), anchor="lm", font=get_font(11))

    im.save(os.path.join(ASSETS, 'ms_excel_interface.png'), quality=95)
    print("Created ms_excel_interface.png")

# 5. MS PowerPoint Interface Schematic
def create_ppt_interface():
    w, h = 900, 520
    im = Image.new('RGB', (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    # Title Bar
    draw.rectangle([0, 0, w, 36], fill=(196, 62, 28))
    draw.text((20, 18), "AutoSave  ON   |   MBA_Marketing_Presentation.pptx - PowerPoint", fill=(255, 255, 255), anchor="lm", font=get_font(13, bold=True))
    draw.text((w - 70, 18), "—   □   ✕", fill=(255, 255, 255), anchor="lm", font=get_font(14, bold=True))
    
    # Ribbon Tabs
    draw.rectangle([0, 36, w, 68], fill=(241, 245, 249))
    tabs = ["File", "Home", "Insert", "Draw", "Design", "Transitions", "Animations", "Slide Show", "Record", "Review", "View"]
    tx = 15
    for t in tabs:
        is_active = (t == "Transitions")
        if is_active:
            draw.rectangle([tx-4, 38, tx+68, 68], fill=(255, 255, 255), outline=(203, 213, 225), width=1)
            draw.line([tx-4, 68, tx+68, 68], fill=(196, 62, 28), width=3)
            draw.text((tx+32, 52), t, fill=(196, 62, 28), anchor="mm", font=get_font(12, bold=True))
            tx += 74
        else:
            draw.text((tx+26, 52), t, fill=(51, 65, 85), anchor="mm", font=get_font(11))
            tx += 66
            
    # Transitions Toolbar
    draw.rectangle([0, 68, w, 140], fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    trans = ["None", "Morph", "Fade", "Push", "Wipe", "Split", "Reveal", "Cut", "Random Bars"]
    bx = 30
    for tr in trans:
        draw_rounded_rect(draw, (bx, 76, bx+75, 128), radius=4, fill=(248, 250, 252), outline=(203, 213, 225))
        draw.rectangle([bx+15, 82, bx+60, 108], fill=(226, 232, 240))
        draw.text((bx+37, 120), tr, fill=(71, 85, 105), anchor="mm", font=get_font(9, bold=True))
        bx += 88
    # Timing & Sound Box
    draw_rounded_rect(draw, (750, 74, 885, 134), radius=4, fill=(254, 242, 242), outline=(252, 165, 165))
    draw.text((817, 90), "Timing & Effect", fill=(185, 28, 28), anchor="mm", font=get_font(10, bold=True))
    draw.text((817, 108), "Duration: 01.50 s", fill=(71, 85, 105), anchor="mm", font=get_font(9))
    draw.text((817, 122), "Apply To All ⏩", fill=(30, 41, 59), anchor="mm", font=get_font(9, bold=True))

    # Left Slide Thumbnail Pane
    draw.rectangle([0, 140, 170, 490], fill=(241, 245, 249), outline=(203, 213, 225))
    draw.text((85, 155), "SLIDES (3)", fill=(100, 116, 139), anchor="mm", font=get_font(11, bold=True))
    # Thumbnail 1 (Active)
    draw_rounded_rect(draw, (15, 175, 155, 260), radius=4, fill=(255, 255, 255), outline=(196, 62, 28), width=2)
    draw.text((25, 185), "1", fill=(196, 62, 28), font=get_font(10, bold=True))
    draw.rectangle([40, 195, 140, 215], fill=(254, 226, 226))
    draw.text((90, 205), "Title Slide", fill=(153, 27, 27), anchor="mm", font=get_font(9, bold=True))
    draw.line([45, 230, 135, 230], fill=(203, 213, 225), width=2)
    draw.line([55, 242, 125, 242], fill=(203, 213, 225), width=2)
    
    # Thumbnail 2
    draw_rounded_rect(draw, (15, 275, 155, 360), radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    draw.text((25, 285), "2", fill=(100, 116, 139), font=get_font(10, bold=True))
    draw.text((90, 310), "Market Analysis", fill=(71, 85, 105), anchor="mm", font=get_font(9, bold=True))
    draw.rectangle([35, 325, 85, 350], fill=(226, 232, 240))
    draw.rectangle([95, 325, 145, 350], fill=(226, 232, 240))

    # Thumbnail 3
    draw_rounded_rect(draw, (15, 375, 155, 460), radius=4, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    draw.text((25, 385), "3", fill=(100, 116, 139), font=get_font(10, bold=True))
    draw.text((90, 410), "Financial Projections", fill=(71, 85, 105), anchor="mm", font=get_font(9, bold=True))

    # Center Workspace / Slide Canvas
    draw.rectangle([170, 140, w, 490], fill=(226, 232, 240))
    # The Slide (16:9 widescreen ratio)
    draw_rounded_rect(draw, (230, 160, 840, 470), radius=6, fill=(255, 255, 255), outline=(148, 163, 184), width=1)
    # Slide Decorative Header
    draw_rounded_rect(draw, (230, 160, 840, 190), radius=6, fill=(196, 62, 28))
    draw.rectangle([230, 180, 840, 190], fill=(196, 62, 28))
    # Slide Title Box
    draw_rounded_rect(draw, (270, 210, 800, 280), radius=6, fill=(254, 242, 242), outline=(252, 165, 165))
    draw.text((535, 235), "EXECUTIVE BUSINESS STRATEGY 2026-2030", fill=(153, 27, 27), anchor="mm", font=get_font(16, bold=True))
    draw.text((535, 260), "MBA(MS) 5 Yrs - International Institute of Professional Studies, DAVV", fill=(100, 116, 139), anchor="mm", font=get_font(11))
    
    # Slide Content Grid
    col_w = 160
    cards = [
        ("1. Market Research", "Identify target consumer\nsegments and unmet needs."),
        ("2. Product Strategy", "Develop AI-powered scalable\ncloud productivity tools."),
        ("3. Go-To-Market", "Omnichannel distribution\nand targeted digital marketing.")
    ]
    cx = 270
    for c_title, c_desc in cards:
        draw_rounded_rect(draw, (cx, 305, cx+165, 415), radius=6, fill=(248, 250, 252), outline=(203, 213, 225), width=1)
        draw.text((cx+82, 325), c_title, fill=(196, 62, 28), anchor="mm", font=get_font(11, bold=True))
        draw.text((cx+82, 365), c_desc, fill=(51, 65, 85), anchor="mm", font=get_font(10))
        cx += 185
        
    draw.text((535, 445), "Speaker Notes: Introduce the team, high-level mission statement, and strategic milestones.", fill=(100, 116, 139), anchor="mm", font=get_font(10, bold=False))

    # Status Bar
    draw.rectangle([0, 490, w, 520], fill=(196, 62, 28))
    draw.text((20, 505), "Slide 1 of 3    |    English (US)    |    Notes    |    Comments", fill=(255, 255, 255), anchor="lm", font=get_font(11, bold=True))
    draw.text((w - 180, 505), "Normal  Slide Sorter  Reading  🖥️  —  ●  + 68%", fill=(255, 255, 255), anchor="lm", font=get_font(11))

    im.save(os.path.join(ASSETS, 'powerpoint_interface.png'), quality=95)
    print("Created powerpoint_interface.png")

# 6. MS Access RDBMS Architecture
def create_access_architecture():
    w, h = 900, 480
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Title Banner
    draw_rounded_rect(draw, (20, 15, w-20, 65), radius=8, fill=(164, 55, 0))
    draw.text((w/2, 40), "MS-Access Relational Database (RDBMS) Schema & Object Architecture", fill=(255, 255, 255), anchor="mm", font=get_font(19, bold=True))

    # Table 1: tbl_Customers
    draw_rounded_rect(draw, (40, 95, 280, 285), radius=8, fill=(255, 255, 255), outline=(164, 55, 0), width=2)
    draw_rounded_rect(draw, (40, 95, 280, 130), radius=8, fill=(164, 55, 0))
    draw.text((160, 112), "tbl_Customers (Table)", fill=(255, 255, 255), anchor="mm", font=get_font(13, bold=True))
    cust_fields = [
        ("🔑 CustomerID", "AutoNumber (PK)"),
        ("  CustomerName", "Short Text"),
        ("  EmailAddress", "Short Text"),
        ("  PhoneNumber", "Short Text"),
        ("  City", "Short Text")
    ]
    fy = 145
    for fn, ft in cust_fields:
        draw.text((55, fy), fn, fill=(30, 41, 59), font=get_font(11, bold=('PK' in ft)))
        draw.text((200, fy), ft, fill=(100, 116, 139), font=get_font(10))
        fy += 26

    # Table 2: tbl_Orders
    draw_rounded_rect(draw, (340, 95, 580, 285), radius=8, fill=(255, 255, 255), outline=(164, 55, 0), width=2)
    draw_rounded_rect(draw, (340, 95, 580, 130), radius=8, fill=(164, 55, 0))
    draw.text((460, 112), "tbl_Orders (Table)", fill=(255, 255, 255), anchor="mm", font=get_font(13, bold=True))
    order_fields = [
        ("🔑 OrderID", "AutoNumber (PK)"),
        ("🔗 CustomerID", "Number (FK)"),
        ("  OrderDate", "Date/Time"),
        ("  TotalAmount", "Currency"),
        ("  OrderStatus", "Short Text")
    ]
    fy = 145
    for fn, ft in order_fields:
        draw.text((355, fy), fn, fill=(30, 41, 59), font=get_font(11, bold=('PK' in ft or 'FK' in ft)))
        draw.text((500, fy), ft, fill=(100, 116, 139), font=get_font(10))
        fy += 26

    # Table 3: tbl_OrderDetails & Products
    draw_rounded_rect(draw, (640, 95, 870, 285), radius=8, fill=(255, 255, 255), outline=(164, 55, 0), width=2)
    draw_rounded_rect(draw, (640, 95, 870, 130), radius=8, fill=(164, 55, 0))
    draw.text((755, 112), "tbl_Products (Table)", fill=(255, 255, 255), anchor="mm", font=get_font(13, bold=True))
    prod_fields = [
        ("🔑 ProductCode", "Short Text (PK)"),
        ("  ProductName", "Short Text"),
        ("  UnitPrice", "Currency"),
        ("  UnitsInStock", "Number"),
        ("  Category", "Short Text")
    ]
    fy = 145
    for fn, ft in prod_fields:
        draw.text((655, fy), fn, fill=(30, 41, 59), font=get_font(11, bold=('PK' in ft)))
        draw.text((790, fy), ft, fill=(100, 116, 139), font=get_font(10))
        fy += 26

    # Relational link line
    draw.line([280, 145, 340, 171], fill=(220, 38, 38), width=3)
    draw.text((305, 140), "1", fill=(220, 38, 38), font=get_font(12, bold=True))
    draw.text((320, 175), "∞", fill=(220, 38, 38), font=get_font(14, bold=True))

    draw.line([580, 171, 640, 145], fill=(37, 99, 235), width=3)
    draw.text((600, 175), "∞", fill=(37, 99, 235), font=get_font(14, bold=True))
    draw.text((625, 140), "1", fill=(37, 99, 235), font=get_font(12, bold=True))

    # Access Core Objects Summary (Bottom)
    objs = [
        ("QUERIES", "SQL Filters, Calculated Fields,\nJoin Multi-table datasets"),
        ("FORMS", "User-friendly GUI screens for\nsafe data entry & navigation"),
        ("REPORTS", "Formatted printable summaries,\nPDF export, mailing labels"),
        ("MACROS & VBA", "Automate workflows, validation\nand custom business logic")
    ]
    ox = 40
    for oname, odesc in objs:
        draw_rounded_rect(draw, (ox, 320, ox+195, 440), radius=6, fill=(255, 247, 237), outline=(251, 146, 60), width=1)
        draw.rectangle([ox, 320, ox+195, 350], fill=(234, 88, 12))
        draw.text((ox+97, 335), oname, fill=(255, 255, 255), anchor="mm", font=get_font(12, bold=True))
        draw.text((ox+97, 395), odesc, fill=(67, 20, 7), anchor="mm", font=get_font(10))
        ox += 220

    im.save(os.path.join(ASSETS, 'access_rdbms_architecture.png'), quality=95)
    print("Created access_rdbms_architecture.png")

# 7. Search Engine Architecture
def create_search_engine_arch():
    w, h = 900, 440
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Title Banner
    draw_rounded_rect(draw, (20, 15, w-20, 65), radius=8, fill=(66, 133, 244))
    draw.text((w/2, 40), "How Search Engines Work: Crawling, Indexing, Ranking & Serving", fill=(255, 255, 255), anchor="mm", font=get_font(19, bold=True))

    stages = [
        ("1. WEB CRAWLING", "Bots / Spiders (Googlebot, Bingbot)\ntraverse billions of web pages\nfollowing links (URLs & Sitemaps).", (239, 246, 255), (59, 130, 246), 40),
        ("2. INDEXING & PARSING", "Extracts keywords, headings, metadata.\nBuilds massive Inverted Index database\nmapping terms to web documents.", (240, 253, 244), (34, 197, 94), 255),
        ("3. QUERY PROCESSING", "Understands user intent, synonyms,\nspelling corrections, and semantic\ncontext (RankBrain, MUM, BERT).", (254, 243, 199), (245, 158, 11), 470),
        ("4. RANKING & SERP", "Scores 200+ signals (PageRank,\nrelevance, speed, mobile usability).\nRenders ranked results on SERP.", (254, 242, 242), (239, 68, 68), 685)
    ]
    for s_title, s_desc, bg, border, sx in stages:
        draw_rounded_rect(draw, (sx, 110, sx+175, 330), radius=8, fill=bg, outline=border, width=2)
        draw_rounded_rect(draw, (sx, 110, sx+175, 155), radius=8, fill=border)
        draw.text((sx+87, 132), s_title, fill=(255, 255, 255), anchor="mm", font=get_font(11, bold=True))
        draw.text((sx+87, 235), s_desc, fill=(30, 41, 59), anchor="mm", font=get_font(10))
        
        # Connectors
        if sx < 685:
            draw_arrow(draw, (sx+178, 220), (sx+212, 220), color=(100, 116, 139), width=3, arrow_size=8)

    # Search Operators Callout Box at bottom
    draw_rounded_rect(draw, (40, 360, 860, 415), radius=6, fill=(248, 250, 252), outline=(203, 213, 225))
    draw.text((450, 375), "Advanced Search Operators: \"exact phrase\"  |  site:edu.in  |  filetype:pdf  |  intitle:syllabus  |  -keyword (exclude)", fill=(30, 41, 59), anchor="mm", font=get_font(12, bold=True))
    draw.text((450, 398), "Example Query: site:dauniv.ac.in filetype:pdf \"MBA MS syllabus\" (Locates authentic university curriculum document)", fill=(71, 85, 105), anchor="mm", font=get_font(11))

    im.save(os.path.join(ASSETS, 'search_engine_architecture.png'), quality=95)
    print("Created search_engine_architecture.png")

# 8. Email Protocols Architecture
def create_email_protocols_arch():
    w, h = 900, 440
    im = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    
    # Title Banner
    draw_rounded_rect(draw, (20, 15, w-20, 65), radius=8, fill=(217, 48, 37))
    draw.text((w/2, 40), "Email Protocol Architecture: End-to-End Message Delivery (SMTP, POP3, IMAP)", fill=(255, 255, 255), anchor="mm", font=get_font(18, bold=True))

    # Sender Node
    draw_rounded_rect(draw, (30, 140, 180, 280), radius=8, fill=(239, 246, 255), outline=(59, 130, 246), width=2)
    draw.text((105, 175), "SENDER CLIENT", fill=(30, 58, 138), anchor="mm", font=get_font(12, bold=True))
    draw.text((105, 205), "(MUA - Outlook /", fill=(71, 85, 105), anchor="mm", font=get_font(11))
    draw.text((105, 225), "Gmail Web App)", fill=(71, 85, 105), anchor="mm", font=get_font(11))
    draw.text((105, 255), "sender@iips.edu", fill=(37, 99, 235), anchor="mm", font=get_font(10, bold=True))

    # Sender SMTP Server
    draw_rounded_rect(draw, (250, 120, 410, 300), radius=8, fill=(254, 243, 199), outline=(217, 119, 6), width=2)
    draw.text((330, 150), "SENDER MAIL SERVER", fill=(146, 64, 14), anchor="mm", font=get_font(11, bold=True))
    draw.text((330, 175), "(MTA - SMTP Server)", fill=(71, 85, 105), anchor="mm", font=get_font(10))
    draw.text((330, 210), "Checks SPF / DKIM", fill=(180, 83, 9), anchor="mm", font=get_font(10))
    draw.text((330, 235), "Performs DNS MX Lookup", fill=(180, 83, 9), anchor="mm", font=get_font(10))
    draw.text((330, 265), "Port 587 (STARTTLS)", fill=(22, 101, 52), anchor="mm", font=get_font(10, bold=True))

    # Recipient SMTP Server
    draw_rounded_rect(draw, (490, 120, 650, 300), radius=8, fill=(254, 243, 199), outline=(217, 119, 6), width=2)
    draw.text((570, 150), "RECEIVING SERVER", fill=(146, 64, 14), anchor="mm", font=get_font(11, bold=True))
    draw.text((570, 175), "(MTA / MDA Mailbox)", fill=(71, 85, 105), anchor="mm", font=get_font(10))
    draw.text((570, 210), "Spam & Antivirus Filter", fill=(180, 83, 9), anchor="mm", font=get_font(10))
    draw.text((570, 235), "Stores in User Mailbox", fill=(180, 83, 9), anchor="mm", font=get_font(10))
    draw.text((570, 265), "Port 25 (Server-to-Server)", fill=(22, 101, 52), anchor="mm", font=get_font(10, bold=True))

    # Recipient Node
    draw_rounded_rect(draw, (720, 140, 870, 280), radius=8, fill=(240, 253, 244), outline=(34, 197, 94), width=2)
    draw.text((795, 175), "RECIPIENT CLIENT", fill=(21, 128, 61), anchor="mm", font=get_font(12, bold=True))
    draw.text((795, 205), "(MUA - Mobile App /", fill=(71, 85, 105), anchor="mm", font=get_font(11))
    draw.text((795, 225), "Desktop Client)", fill=(71, 85, 105), anchor="mm", font=get_font(11))
    draw.text((795, 255), "student@gmail.com", fill=(22, 163, 74), anchor="mm", font=get_font(10, bold=True))

    # Flow Arrows & Labels
    # Sender -> Sender SMTP
    draw_arrow(draw, (180, 200), (245, 200), color=(217, 119, 6), width=3, arrow_size=8)
    draw.text((212, 185), "SMTP", fill=(217, 119, 6), anchor="mm", font=get_font(10, bold=True))

    # Sender SMTP -> Receiver SMTP
    draw_arrow(draw, (410, 200), (485, 200), color=(217, 48, 37), width=3, arrow_size=8)
    draw.text((450, 185), "INTERNET (SMTP)", fill=(217, 48, 37), anchor="mm", font=get_font(10, bold=True))

    # Receiver SMTP -> Recipient Client
    draw_arrow(draw, (650, 200), (715, 200), color=(34, 197, 94), width=3, arrow_size=8)
    draw.text((682, 185), "IMAP / POP3", fill=(34, 197, 94), anchor="mm", font=get_font(10, bold=True))

    # Protocol Comparison Cards at bottom
    draw_rounded_rect(draw, (40, 335, 430, 415), radius=6, fill=(240, 249, 255), outline=(186, 230, 253))
    draw.text((235, 355), "IMAP (Internet Message Access Protocol - Port 993 SSL)", fill=(2, 132, 199), anchor="mm", font=get_font(11, bold=True))
    draw.text((235, 385), "Two-way live synchronization. Emails remain stored on server;\nchanges reflect instantly on Phone, Laptop, and Webmail.", fill=(51, 65, 85), anchor="mm", font=get_font(10))

    draw_rounded_rect(draw, (470, 335, 860, 415), radius=6, fill=(254, 242, 242), outline=(254, 202, 202))
    draw.text((665, 355), "POP3 (Post Office Protocol 3 - Port 995 SSL)", fill=(220, 38, 38), anchor="mm", font=get_font(11, bold=True))
    draw.text((665, 385), "One-way download. Messages are downloaded to a single device\nand deleted from server. Lacks multi-device sync capability.", fill=(51, 65, 85), anchor="mm", font=get_font(10))

    im.save(os.path.join(ASSETS, 'email_protocols_architecture.png'), quality=95)
    print("Created email_protocols_architecture.png")

# 9. Student Entry Form UI Preview
def create_student_form_preview():
    w, h = 800, 600
    im = Image.new('RGB', (w, h), (241, 245, 249))
    draw = ImageDraw.Draw(im)
    
    # Browser Window Chrome
    draw_rounded_rect(draw, (20, 15, w-20, h-15), radius=10, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    # Browser title bar
    draw_rounded_rect(draw, (20, 15, w-20, 55), radius=10, fill=(241, 245, 249))
    draw.rectangle([20, 45, w-20, 55], fill=(241, 245, 249))
    draw.ellipse([35, 28, 47, 40], fill=(239, 68, 68))
    draw.ellipse([55, 28, 67, 40], fill=(245, 158, 11))
    draw.ellipse([75, 28, 87, 40], fill=(34, 197, 94))
    # URL bar
    draw_rounded_rect(draw, (120, 24, w-50, 46), radius=6, fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((140, 35), "🔒 https://iips.davv.ac.in/admissions/student_entry_form.html", fill=(71, 85, 105), anchor="lm", font=get_font(11))

    # Form Container Card
    draw_rounded_rect(draw, (60, 75, w-60, h-35), radius=8, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    
    # Header Banner
    draw_rounded_rect(draw, (60, 75, w-60, 135), radius=8, fill=(30, 58, 138))
    draw.rectangle([60, 125, w-60, 135], fill=(30, 58, 138))
    draw.text((w/2, 95), "IIPS - DAVV, INDORE", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    draw.text((w/2, 118), "STUDENT ADMISSION & REGISTRATION ENTRY FORM", fill=(191, 219, 254), anchor="mm", font=get_font(12))

    fields = [
        ("Roll Number *", "IM-2K26-58", "text"),
        ("Student Full Name *", "Krishna Dixit", "text"),
        ("Program Name *", "MBA (Management Science) 5 Yrs Integrated", "select"),
        ("Class *", "MBA(MS) - 1st Year (Semester I)", "select"),
        ("Section *", "Section A", "radio")
    ]
    
    fy = 160
    for label, val, ftype in fields:
        draw.text((100, fy), label, fill=(15, 23, 42), font=get_font(12, bold=True))
        
        if ftype == "radio":
            # Radio options
            draw.ellipse([100, fy+22, 116, 38+fy], fill=(255, 255, 255), outline=(37, 99, 235), width=2)
            draw.ellipse([104, fy+26, 112, 34+fy], fill=(37, 99, 235))
            draw.text((125, fy+29), "Section A", fill=(30, 41, 59), anchor="lm", font=get_font(12))
            
            draw.ellipse([240, fy+22, 256, 38+fy], fill=(255, 255, 255), outline=(148, 163, 184), width=2)
            draw.text((265, fy+29), "Section B", fill=(30, 41, 59), anchor="lm", font=get_font(12))
        else:
            # Input Box
            draw_rounded_rect(draw, (100, fy+20, w-100, fy+54), radius=5, fill=(248, 250, 252), outline=(203, 213, 225))
            draw.text((115, fy+37), val, fill=(30, 41, 59), anchor="lm", font=get_font(12))
            if ftype == "select":
                draw.text((w-130, fy+37), "▼", fill=(100, 116, 139), anchor="lm", font=get_font(11))
                
        fy += 68
        
    # Buttons
    draw_rounded_rect(draw, (100, fy+15, 250, fy+55), radius=5, fill=(30, 58, 138))
    draw.text((175, fy+35), "Submit Entry", fill=(255, 255, 255), anchor="mm", font=get_font(13, bold=True))

    draw_rounded_rect(draw, (270, fy+15, 390, fy+55), radius=5, fill=(241, 245, 249), outline=(203, 213, 225))
    draw.text((330, fy+35), "Reset Form", fill=(71, 85, 105), anchor="mm", font=get_font(13, bold=True))

    im.save(os.path.join(ASSETS, 'student_entry_form_preview.png'), quality=95)
    print("Created student_entry_form_preview.png")

# 10. Product Purchase Order UI Preview
def create_purchase_order_preview():
    w, h = 800, 600
    im = Image.new('RGB', (w, h), (241, 245, 249))
    draw = ImageDraw.Draw(im)
    
    # Browser Window Chrome
    draw_rounded_rect(draw, (20, 15, w-20, h-15), radius=10, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    # Browser title bar
    draw_rounded_rect(draw, (20, 15, w-20, 55), radius=10, fill=(241, 245, 249))
    draw.rectangle([20, 45, w-20, 55], fill=(241, 245, 249))
    draw.ellipse([35, 28, 47, 40], fill=(239, 68, 68))
    draw.ellipse([55, 28, 67, 40], fill=(245, 158, 11))
    draw.ellipse([75, 28, 87, 40], fill=(34, 197, 94))
    # URL bar
    draw_rounded_rect(draw, (120, 24, w-50, 46), radius=6, fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((140, 35), "🔒 https://enterprise-procure.com/orders/purchase_order.html", fill=(71, 85, 105), anchor="lm", font=get_font(11))

    # Form Container Card
    draw_rounded_rect(draw, (60, 75, w-60, h-35), radius=8, fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    
    # Header Banner
    draw_rounded_rect(draw, (60, 75, w-60, 135), radius=8, fill=(5, 150, 105))
    draw.rectangle([60, 125, w-60, 135], fill=(5, 150, 105))
    draw.text((w/2, 95), "ENTERPRISE PROCUREMENT PORTAL", fill=(255, 255, 255), anchor="mm", font=get_font(14, bold=True))
    draw.text((w/2, 118), "COMMERCIAL PRODUCT PURCHASE ORDER", fill=(209, 250, 229), anchor="mm", font=get_font(12))

    fields = [
        ("Product Name *", "Dell Latitude 5430 Business Laptop 16GB / 512GB SSD"),
        ("Product Code *", "PRD-DELL-5430-IN"),
        ("Unit Price (₹) *", "68,500.00"),
        ("Quantity (Units) *", "15"),
        ("Order Date *", "2026-11-14")
    ]
    
    fy = 160
    for label, val in fields:
        draw.text((100, fy), label, fill=(15, 23, 42), font=get_font(12, bold=True))
        draw_rounded_rect(draw, (100, fy+20, w-100, fy+54), radius=5, fill=(248, 250, 252), outline=(203, 213, 225))
        draw.text((115, fy+37), val, fill=(30, 41, 59), anchor="lm", font=get_font(12))
        fy += 68

    # Dynamic calculation summary box
    draw_rounded_rect(draw, (100, fy+10, w-100, fy+45), radius=5, fill=(236, 253, 245), outline=(52, 211, 153))
    draw.text((115, fy+27), "Calculated Total Order Value: 15 × ₹68,500 = ₹1,027,500.00 (Excl. Taxes)", fill=(6, 95, 70), anchor="lm", font=get_font(12, bold=True))

    # Buttons
    fy += 55
    draw_rounded_rect(draw, (100, fy, 260, fy+40), radius=5, fill=(5, 150, 105))
    draw.text((180, fy+20), "Generate Order", fill=(255, 255, 255), anchor="mm", font=get_font(13, bold=True))

    draw_rounded_rect(draw, (280, fy, 400, fy+40), radius=5, fill=(241, 245, 249), outline=(203, 213, 225))
    draw.text((340, fy+20), "Clear Values", fill=(71, 85, 105), anchor="mm", font=get_font(13, bold=True))

    im.save(os.path.join(ASSETS, 'product_purchase_order_preview.png'), quality=95)
    print("Created product_purchase_order_preview.png")

if __name__ == "__main__":
    create_io_arch()
    create_word_interface()
    create_mail_merge_flow()
    create_excel_interface()
    create_ppt_interface()
    create_access_architecture()
    create_search_engine_arch()
    create_email_protocols_arch()
    create_student_form_preview()
    create_purchase_order_preview()
    print("All diagrams generated successfully!")
