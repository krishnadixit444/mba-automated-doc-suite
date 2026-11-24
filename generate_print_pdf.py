import os
import sys
import json
import time
import base64
import subprocess
import urllib.request
import websocket

BASE_DIR = '/Users/krishna/.gemini/antigravity/scratch/MBA_Computer_Applications_Assignment'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
HTML_OUT = os.path.join(BASE_DIR, 'assignment_print_ready.html')
DESKTOP_PDF = '/Users/krishna/Desktop/A_IM-2K26-58_krishna_dixit.pdf'
DESKTOP_PDF_GENERIC = '/Users/krishna/Desktop/MBA_MS_IM104C_Practical_Assignment.pdf'
LOCAL_PDF = os.path.join(BASE_DIR, 'A_IM-2K26-58_krishna_dixit.pdf')

def get_b64_img(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: Image not found: {path}")
        return ""
    ext = os.path.splitext(filename)[1].lower().replace('.', '')
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime};base64,{data}"

def build_html():
    # Load all 17 assets
    img_io = get_b64_img('io_architecture.png')
    img_kb = get_b64_img('keyboard.png')
    img_mouse = get_b64_img('mouse.png')
    img_scanner = get_b64_img('scanner.png')
    img_mon = get_b64_img('monitor.png')
    img_prt = get_b64_img('printer.png')
    img_spk = get_b64_img('speaker.png')
    img_word = get_b64_img('ms_word_interface.png')
    img_mm = get_b64_img('mail_merge_workflow.png')
    img_excel = get_b64_img('ms_excel_interface.png')
    img_chart = get_b64_img('excel_chart_example.png')
    img_ppt = get_b64_img('powerpoint_interface.png')
    img_access = get_b64_img('access_rdbms_architecture.png')
    img_search = get_b64_img('search_engine_architecture.png')
    img_email = get_b64_img('email_protocols_architecture.png')
    img_form_student = get_b64_img('student_entry_form_preview.png')
    img_form_po = get_b64_img('product_purchase_order_preview.png')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MBA(MS) Practical Assignment - Computer Application & Web Technology (IM-104C)</title>
    <style>
        @page {{
            size: A4 portrait;
            margin: 16mm 14mm 16mm 14mm;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, 'Helvetica Neue', Arial, sans-serif;
            color: #1e293b;
            line-height: 1.45;
            font-size: 10pt;
            background: #ffffff;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        .page-break {{
            page-break-before: always;
            break-before: page;
        }}

        .no-break {{
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        h1, h2, h3, h4 {{
            page-break-after: avoid;
            break-after: avoid;
            color: #1b365d;
        }}

        h1 {{
            font-size: 16pt;
            font-weight: 700;
            margin-bottom: 8px;
            padding-bottom: 4px;
            border-bottom: 2px solid #1b365d;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        h2 {{
            font-size: 12.5pt;
            font-weight: 700;
            margin-top: 14px;
            margin-bottom: 6px;
            color: #1b365d;
            border-left: 4px solid #0284c7;
            padding-left: 8px;
        }}

        h3 {{
            font-size: 11pt;
            font-weight: 700;
            margin-top: 10px;
            margin-bottom: 4px;
            color: #0284c7;
        }}

        p {{
            margin-bottom: 6px;
            text-align: justify;
        }}

        ul, ol {{
            margin-left: 20px;
            margin-bottom: 8px;
        }}

        li {{
            margin-bottom: 3px;
        }}

        /* Table Styling */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
            font-size: 9pt;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        th, td {{
            border: 1px solid #cbd5e1;
            padding: 6px 8px;
            text-align: left;
            vertical-align: middle;
        }}

        th {{
            background-color: #1b365d;
            color: #ffffff;
            font-weight: 700;
            text-align: center;
        }}

        tr:nth-child(even) td {{
            background-color: #f8fafc;
        }}

        /* Figure and Image Containers */
        .figure-box {{
            text-align: center;
            margin: 10px 0;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .figure-box img {{
            max-width: 92%;
            max-height: 280px;
            height: auto;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        }}

        .figure-box.compact img {{
            max-height: 180px;
        }}

        .caption {{
            font-size: 8pt;
            font-style: italic;
            font-weight: 700;
            color: #64748b;
            margin-top: 4px;
        }}

        /* Callout Box */
        .callout {{
            background-color: #f1f5f9;
            border-left: 4px solid #1b365d;
            padding: 8px 12px;
            margin: 10px 0;
            font-size: 9pt;
            border-radius: 0 6px 6px 0;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .callout-title {{
            font-weight: 700;
            color: #1b365d;
            margin-bottom: 2px;
            font-size: 9.5pt;
        }}

        .alert-box {{
            background-color: #fef3c7;
            border: 1px solid #f59e0b;
            border-radius: 6px;
            padding: 10px 14px;
            margin: 12px 0;
            font-size: 9pt;
            color: #78350f;
            page-break-inside: avoid;
        }}

        /* Code Blocks */
        pre {{
            background-color: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 8px 12px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 8pt;
            line-height: 1.35;
            color: #0f172a;
            white-space: pre-wrap;
            word-break: break-all;
            margin: 8px 0;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        /* Cover Page Styling */
        .cover-page {{
            height: 98vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 3px double #1b365d;
            padding: 30px 24px;
            border-radius: 4px;
            text-align: center;
        }}

        .cover-inst-header {{
            background: #1b365d;
            color: #ffffff;
            padding: 16px 12px;
            border-radius: 6px;
            margin-bottom: 16px;
        }}

        .cover-inst-header h2 {{
            color: #ffffff;
            border-left: none;
            padding: 0;
            font-size: 15pt;
            margin: 0 0 4px 0;
        }}

        .cover-inst-header p {{
            color: #bfdbfe;
            font-size: 9pt;
            margin: 0;
            text-align: center;
        }}

        .cover-title-block h1 {{
            font-size: 18pt;
            color: #1b365d;
            border-bottom: none;
            margin-bottom: 4px;
        }}

        .cover-title-block h3 {{
            color: #0284c7;
            font-size: 13pt;
            margin-bottom: 4px;
        }}

        .cover-title-block p {{
            text-align: center;
            color: #475569;
            font-weight: 700;
            font-size: 10pt;
        }}

        .cover-table {{
            margin: 16px auto;
            width: 95%;
            font-size: 10pt;
        }}

        .cover-table td {{
            padding: 8px 12px;
        }}

        .cover-table td:first-child {{
            font-weight: 700;
            color: #1b365d;
            width: 35%;
            background-color: #f8fafc;
        }}

        .eval-table {{
            margin: 16px auto 0 auto;
            width: 95%;
        }}

        .eval-table th {{
            background-color: #e2e8f0;
            color: #1b365d;
            font-size: 9.5pt;
        }}

        .eval-table td {{
            text-align: center;
            font-weight: 700;
            padding: 10px;
            font-size: 10pt;
        }}
    </style>
</head>
<body>

    <!-- ==================== COVER PAGE ==================== -->
    <div class="cover-page">
        <div>
            <div class="cover-inst-header">
                <h2>International Institute of Professional Studies</h2>
                <p>Devi Ahilya Vishwavidyalaya, Indore (M.P.) — NAAC Accredited 'A+' Grade University</p>
                <p style="font-size: 8pt; margin-top: 2px; color: #93c5fd;">Pioneer Institute of Management & Technical Education Since 1992</p>
            </div>

            <div class="cover-title-block">
                <h1>Practical Laboratory Assignment</h1>
                <h3>Computer Application and Web Technology (IM-104C)</h3>
                <p>CLASS: MBA (MS) 5 Yrs – I SEMESTER (SECTION A & B)</p>
                <p style="color: #64748b; font-size: 9pt; margin-top: 2px;">MAXIMUM MARKS: 20 | PRACTICAL SUBMISSION FILE</p>
            </div>

            <table class="cover-table">
                <tr>
                    <td>Student Name:</td>
                    <td><strong>Krishna Dixit</strong></td>
                </tr>
                <tr>
                    <td>Roll Number:</td>
                    <td><strong>IM-2K26-58</strong></td>
                </tr>
                <tr>
                    <td>Class & Program:</td>
                    <td>MBA (Management Science) 5 Years Integrated – I Semester</td>
                </tr>
                <tr>
                    <td>Section:</td>
                    <td>Section A</td>
                </tr>
                <tr>
                    <td>Course Title & Code:</td>
                    <td>Computer Application and Web Technology (IM-104C)</td>
                </tr>
                <tr>
                    <td>Submission Deadline:</td>
                    <td>13th November, 2026</td>
                </tr>
                <tr>
                    <td>Submission Format:</td>
                    <td>Hard Copy Printout in File & Softcopy Upload (Google Link)</td>
                </tr>
                <tr>
                    <td>Student Signature:</td>
                    <td style="color: #166534; font-weight: 700;">_______________________ &nbsp;&nbsp;&nbsp; Date: 13/11/2026</td>
                </tr>
            </table>
        </div>

        <div>
            <table class="eval-table">
                <tr>
                    <th>Maximum Marks</th>
                    <th>Marks Awarded</th>
                    <th>Examiner / Faculty Signature & Remarks</th>
                </tr>
                <tr>
                    <td>20 Marks</td>
                    <td>_______ / 20</td>
                    <td>______________________________________</td>
                </tr>
            </table>
            <p style="font-size: 8pt; color: #94a3b8; margin-top: 8px;">Strict compliance with original work guidelines. Hard copy submission verified for semester grading.</p>
        </div>
    </div>

    <!-- ==================== TABLE OF CONTENTS & SYLLABUS MAPPING ==================== -->
    <div class="page-break"></div>

    <h1>Practical Assignment Contents & Topic Index</h1>

    <table>
        <tr>
            <th style="width: 12%;">Topic No.</th>
            <th style="width: 63%;">Prescribed Syllabus Topic Coverage</th>
            <th style="width: 25%;">Lab Category</th>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 1</td>
            <td><strong>Input Devices</strong> (Keyboard, Mouse, Scanner) and <strong>Output Devices</strong> (Monitor, Printer, Speaker)</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Computer Hardware</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 2</td>
            <td><strong>MS-Word:</strong> Basic Components, Text Handling, Table Creation & Handling, and Mail Merge Process</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Word Processing Lab</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 3</td>
            <td><strong>MS-Excel:</strong> Components, Formatting, Conditional Formatting, Charts, Sorting, Formulas & 7 Standard Functions</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Spreadsheet Lab</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 4</td>
            <td><strong>MS-PowerPoint:</strong> Basic Components, Text Handling, SmartArt, Slide Master, Transitions & Animations</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Presentation Lab</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 5</td>
            <td><strong>MS-Access:</strong> RDBMS Features, Relational Schema, Advantages, and Commercial Applications</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Database Lab</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 6</td>
            <td><strong>Search Engine & Email:</strong> 4-Stage Search Engine Pipeline, Operators, Email Protocols (SMTP, POP3, IMAP)</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Web & Communication</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: 700; color: #1b365d;">Topic 7</td>
            <td><strong>Web Page Designing:</strong> Student Entry Form and Commercial Product Purchase Order (HTML5/CSS3/JS)</td>
            <td style="text-align: center; color: #0284c7; font-weight: 700;">Web Technology Lab</td>
        </tr>
    </table>

    <div class="alert-box">
        <strong>Mandatory Submission Guidelines:</strong><br>
        1. <strong>Softcopy File Naming:</strong> Save file as <code>Section_Roll_No_Name.docx</code> (e.g. <code>A_IM-2K26-58_krishna_dixit.docx</code>) and upload via official Google Classroom link.<br>
        2. <strong>Hardcopy Submission:</strong> Submit high-resolution printout inside a practical binder file with duly signed cover page.<br>
        3. <strong>Evaluation Weighting:</strong> Marks awarded on the basis of practical formatting features applied across Word, Excel, PowerPoint, Access, and Web forms.
    </div>

    <!-- ==================== TOPIC 1 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 1: Input Devices & Output Devices</h1>
    <p>A modern computer system operates on the fundamental <strong>Input-Process-Output-Storage (IPOS)</strong> architecture. Input devices serve as transducers converting physical human input, text, or analog signals into quantized binary code (0s and 1s) for the Central Processing Unit (CPU). Output devices perform the inverse transformation, translating processed binary data into readable visual, acoustic, or physical forms.</p>

    <div class="figure-box">
        <img src="{img_io}" alt="Computer Hardware Architecture">
        <div class="caption">Figure 1.1: Complete Computer System Architecture — Input, Processing (ALU/CU), Storage, and Output</div>
    </div>

    <h2>1.1 In-Depth Analysis of Input Devices</h2>

    <h3>1.1.1 Keyboard (Primary Alphanumeric Input Device)</h3>
    <p>The keyboard is the primary electro-mechanical alphanumeric text entry and command device. A standard full-sized desktop keyboard features 101 to 104 keys arranged in the standard QWERTY layout.</p>
    <ul>
        <li><strong>Alphanumeric Keys:</strong> Standard letters (A–Z), numbers (0–9), punctuation, and spacebar.</li>
        <li><strong>Function Keys (F1–F12):</strong> Dedicated system shortcuts (e.g., F1 for Help, F5 for Refresh/Slide Show, F7 for Spelling, F12 for Save As).</li>
        <li><strong>Modifier Keys:</strong> Ctrl, Alt, Shift, and Windows/Command key used in key combinations (e.g., Ctrl+S, Alt+Tab).</li>
        <li><strong>Numeric Keypad:</strong> A compact 17-key calculator grid for rapid numeric accounting entry.</li>
        <li><strong>Working Mechanism:</strong> Depressing a key completes an electrical circuit on a matrix grid beneath keycaps. An internal keyboard controller microprocessor scans the grid at high polling rates (125 Hz to 1000 Hz) and transmits an interrupt scan code via USB/Bluetooth to the OS, which maps it via ASCII/Unicode standards.</li>
        <li><strong>Variants:</strong> Mechanical keyboards (individual spring switches offering high durability and tactile feedback), Membrane keyboards (flexible circuit layers with silicone rubber domes), and Ergonomic split keyboards.</li>
    </ul>

    <div class="figure-box compact">
        <img src="{img_kb}" alt="Keyboard">
        <div class="caption">Figure 1.2: Standard Alphanumeric Desktop Keyboard with Functional Key Groups</div>
    </div>

    <h3>1.1.2 Mouse (Graphical Pointing Device)</h3>
    <p>The mouse enables direct graphical manipulation on a Graphical User Interface (GUI), providing spatial positioning, selecting, and navigation controls.</p>
    <ul>
        <li><strong>Working Mechanism:</strong> Modern optical mice incorporate a tiny CMOS sensor and an infrared LED or laser diode. The LED illuminates micro-textures of the surface, and the sensor captures thousands of frames per second. An integrated Digital Signal Processor (DSP) calculates relative movement coordinates (&Delta;X, &Delta;Y) via optical flow algorithms.</li>
        <li><strong>Primary Operations:</strong> Single-click (selection), Double-click (launching applications), Right-click (contextual menu), Click-and-drag (moving objects), and Scroll Wheel (vertical navigation and zoom).</li>
        <li><strong>Sensitivity:</strong> Calibrated in DPI (Dots Per Inch). High DPI settings (1200–3200 DPI) allow swift cursor travel across multi-monitor 4K financial setups.</li>
    </ul>

    <div class="figure-box compact">
        <img src="{img_mouse}" alt="Mouse">
        <div class="caption">Figure 1.3: Optical Desktop Mouse with Scroll Wheel and Precision Optical Sensor</div>
    </div>

    <h3>1.1.3 Scanner (Document Digitization Device)</h3>
    <p>A scanner digitizes physical documents, photographic prints, and printed vouchers into digital raster images (PDF, JPEG, TIFF) or machine-readable text.</p>
    <ul>
        <li><strong>Working Principle:</strong> The physical sheet is illuminated by bright LEDs on a glass platen. A moving carriage containing mirrors and lenses focuses reflected light onto a Charge-Coupled Device (CCD) or Contact Image Sensor (CIS). Light intensity is quantized by an Analog-to-Digital Converter (ADC) into 24-bit or 48-bit RGB color pixels.</li>
        <li><strong>Hardware Types:</strong> Flatbed Scanners (delicate books and certificates), Sheet-fed ADF Scanners (high-volume duplex business scanning), and Handheld/2D Barcode Scanners.</li>
        <li><strong>OCR Integration:</strong> Optical Character Recognition software parses scanned pixel patterns into editable Microsoft Word documents or searchable PDFs.</li>
    </ul>

    <div class="figure-box compact">
        <img src="{img_scanner}" alt="Scanner">
        <div class="caption">Figure 1.4: High-Resolution Optical Flatbed Document Scanner</div>
    </div>

    <h2>1.2 In-Depth Analysis of Output Devices</h2>

    <h3>1.2.1 Monitor (Visual Display Unit)</h3>
    <p>The computer monitor provides real-time visual output for software applications, operating system GUIs, and multimedia streams.</p>
    <ul>
        <li><strong>Display Technologies:</strong> LED-backlit LCDs utilize liquid crystal molecules sandwiched between polarizers that twist under electrical voltage to modulate backlight passage through sub-pixel color filters. In-Plane Switching (IPS) panels provide 178&deg; viewing angles and high color accuracy. OLED displays feature organic self-emitting pixels that achieve true black and infinite contrast ratios.</li>
        <li><strong>Technical Parameters:</strong> Resolution (Full HD 1920&times;1080, 2K QHD 2560&times;1440, 4K UHD 3840&times;2160), Refresh Rate (60 Hz to 144 Hz), Aspect Ratio (16:9 widescreen or 21:9 ultrawide for multi-window financial modeling), and Connectors (HDMI, DisplayPort, USB-C/Thunderbolt).</li>
    </ul>

    <div class="figure-box compact">
        <img src="{img_mon}" alt="Monitor">
        <div class="caption">Figure 1.5: High-Definition IPS LED-Backlit Display Monitor</div>
    </div>

    <h3>1.2.2 Printer (Hard-Copy Output Device)</h3>
    <p>Printers produce permanent physical copies on paper. In business management, printers are categorized into Impact and Non-Impact devices:</p>

    <table>
        <tr>
            <th>Printer Type</th>
            <th>Mechanism</th>
            <th>Speed Range</th>
            <th>Resolution</th>
            <th>Cost / Page</th>
            <th>Commercial Use Case</th>
        </tr>
        <tr>
            <td><strong>Dot Matrix (Impact)</strong></td>
            <td>Pins strike ink ribbon physically</td>
            <td>100–600 CPS</td>
            <td>72–360 DPI</td>
            <td>Very Low (~₹0.15)</td>
            <td>Multi-part carbon receipts, railway tickets</td>
        </tr>
        <tr>
            <td><strong>Inkjet (Non-Impact)</strong></td>
            <td>Sprays liquid ink droplets via piezoelectric nozzles</td>
            <td>10–25 PPM</td>
            <td>1200–4800 DPI</td>
            <td>Moderate (~₹2.50)</td>
            <td>Color presentations, photo proofs</td>
        </tr>
        <tr>
            <td><strong>Laser (Non-Impact)</strong></td>
            <td>Electrostatic drum attracts toner; heat fuser bonds to paper</td>
            <td>25–70+ PPM</td>
            <td>600–2400 DPI</td>
            <td>Low (~₹0.60)</td>
            <td>High-volume contracts, administrative reports</td>
        </tr>
        <tr>
            <td><strong>Thermal (Non-Impact)</strong></td>
            <td>Heated pins chemically activate heat-sensitive paper</td>
            <td>150–300 mm/s</td>
            <td>203–300 DPI</td>
            <td>Very Low (~₹0.10)</td>
            <td>POS cash counters, ATM receipts, courier labels</td>
        </tr>
    </table>

    <div class="figure-box compact">
        <img src="{img_prt}" alt="Laser Printer">
        <div class="caption">Figure 1.6: Enterprise High-Speed Duplex Laser Printer</div>
    </div>

    <h3>1.2.3 Speaker (Acoustic Output Device)</h3>
    <p>Speakers convert stored digital audio data into audible acoustic sound waves. In corporate boardrooms and hybrid workstations, audio output is essential for video conferencing (Zoom, Teams), webinars, corporate training videos, and interactive client demonstrations.</p>
    <ul>
        <li><strong>Sound Generation Principle:</strong> Digital audio streams (MP3, WAV) are decoded by a Digital-to-Analog Converter (DAC) in the sound card into continuous analog electrical signals. An integrated amplifier drives an electromagnetic voice coil suspended near a permanent magnet, vibrating a flexible diaphragm cone to produce sound waves.</li>
        <li><strong>Corporate Features:</strong> Modern corporate setups integrate USB speakerphones with beamforming multi-microphone arrays, acoustic echo cancellation (AEC), and low-latency Bluetooth codecs.</li>
    </ul>

    <div class="figure-box compact">
        <img src="{img_spk}" alt="Desktop Speakers">
        <div class="caption">Figure 1.7: Stereo Multimedia Desktop Speakers with Integrated DAC Amplification</div>
    </div>

    <!-- ==================== TOPIC 2 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 2: Microsoft Word – Core Components, Formatting, Tables & Mail Merge</h1>
    <p>Microsoft Word is the benchmark word processing software used globally for corporate contracts, academic dissertations, executive memos, and mass correspondence.</p>

    <div class="figure-box">
        <img src="{img_word}" alt="MS Word Interface">
        <div class="caption">Figure 2.1: Microsoft Word GUI Workspace Architecture with Ribbon System</div>
    </div>

    <h2>2.1 Basic Components of Microsoft Word</h2>
    <ul>
        <li><strong>Title Bar:</strong> Displays the active file name (e.g. <code>Document1 - Word</code>), AutoSave cloud toggle, search bar (Alt+Q), and window management icons.</li>
        <li><strong>Quick Access Toolbar (QAT):</strong> Customizable toolbar pinned to top-left containing Save (Ctrl+S), Undo (Ctrl+Z), and Redo (Ctrl+Y).</li>
        <li><strong>The Ribbon:</strong> Tabbed control center (File, Home, Insert, Draw, Design, Layout, References, Mailings, Review, View, Help). Each tab contains organized command groups.</li>
        <li><strong>Dialog Box Launchers:</strong> Small diagonal arrows in group corners that open advanced modal settings dialogs (Font dialog: Ctrl+D, Paragraph dialog).</li>
        <li><strong>Document Workspace:</strong> Central WYSIWYG canvas representing physical paper pages (A4, Letter).</li>
        <li><strong>Rulers:</strong> Horizontal and vertical measurement guides used to adjust margins, indents, and tab stops.</li>
        <li><strong>Status Bar:</strong> Bottom bar displaying page count, word count, proofing language, view modes, and zoom slider (10% to 500%).</li>
    </ul>

    <h2>2.2 Text Handling Features in Word Documents</h2>
    <ul>
        <li><strong>Character Formatting:</strong> Typeface selection (Calibri, Aptos, Times New Roman, Arial), point sizing (Title: 16–18pt, Headings: 12–14pt, Body: 10.5–11.5pt), emphasis (Bold Ctrl+B, Italic Ctrl+I, Underline Ctrl+U, Strikethrough), scientific notation (Subscript Ctrl+=, Superscript Ctrl+Shift++), and Change Case (Sentence case, UPPERCASE, Title Case, Shift+F3).</li>
        <li><strong>Paragraph Formatting:</strong> Alignment modes (Left Ctrl+L, Center Ctrl+E, Right Ctrl+R, Justified Ctrl+J), Line Spacing (1.0 to 2.0) with Before/After paragraph padding (e.g. 6pt after), First-Line and Hanging Indents, and Multilevel Lists linked to Heading styles.</li>
        <li><strong>Styles & Themes:</strong> Built-in styles (Normal, Heading 1, Heading 2) guarantee consistent typography and automate one-click Table of Contents generation.</li>
        <li><strong>Page Setup & Layout:</strong> Orientation (Portrait vs Landscape), Margins (Normal 1-inch, Narrow 0.5-inch), Paper Size (A4), and Section Breaks (enabling independent page numbering and mixed orientations).</li>
    </ul>

    <h2>2.3 Step-by-Step Table Creation and Table Handling in MS-Word</h2>

    <h3>2.3.1 Five Methods of Table Creation</h3>
    <ol>
        <li><strong>Grid Selection:</strong> <code>Insert</code> &gt; <code>Table</code> &gt; drag across grid (up to 10&times;8).</li>
        <li><strong>Insert Table Dialog:</strong> <code>Insert</code> &gt; <code>Table</code> &gt; <code>Insert Table...</code> &gt; enter exact columns/rows and choose AutoFit.</li>
        <li><strong>Draw Table Tool:</strong> <code>Insert</code> &gt; <code>Table</code> &gt; <code>Draw Table</code> &gt; manually sketch irregular borders with pencil cursor.</li>
        <li><strong>Convert Text to Table:</strong> Highlight delimited text &gt; <code>Insert</code> &gt; <code>Table</code> &gt; <code>Convert Text to Table</code>.</li>
        <li><strong>Excel Spreadsheet Embedding:</strong> <code>Insert</code> &gt; <code>Table</code> &gt; <code>Excel Spreadsheet</code> &gt; embeds a live calculation sheet.</li>
    </ol>

    <h3>2.3.2 Table Handling Features & Demonstrative Example</h3>
    <p>Accessible via the contextual <code>Table Design</code> and <code>Layout</code> tabs: inserting/deleting rows &amp; columns, merging header cells, splitting cells, AutoFit (to contents / to window), 9-way cell text alignment, rotating text direction, repeating header rows across multi-page tables, and executing in-table formulas like <code>=SUM(ABOVE)</code>.</p>

    <table>
        <tr>
            <th>Roll Number</th>
            <th>Student Name</th>
            <th>Internal (40)</th>
            <th>End-Term (60)</th>
            <th>Total (100)</th>
            <th>Grade</th>
        </tr>
        <tr>
            <td style="text-align: center;"><strong>IM-2K26-58</strong></td>
            <td>Krishna Dixit</td>
            <td style="text-align: center;">36</td>
            <td style="text-align: center;">54</td>
            <td style="text-align: center; font-weight: 700;">90</td>
            <td style="text-align: center; color: #166534; font-weight: 700;">A+ (Outstanding)</td>
        </tr>
        <tr>
            <td style="text-align: center;"><strong>IM-2K26-02</strong></td>
            <td>Ananya Sharma</td>
            <td style="text-align: center;">38</td>
            <td style="text-align: center;">56</td>
            <td style="text-align: center; font-weight: 700;">94</td>
            <td style="text-align: center; color: #166534; font-weight: 700;">A+ (Outstanding)</td>
        </tr>
        <tr>
            <td style="text-align: center;"><strong>IM-2K26-03</strong></td>
            <td>Rohit Verma</td>
            <td style="text-align: center;">31</td>
            <td style="text-align: center;">45</td>
            <td style="text-align: center; font-weight: 700;">76</td>
            <td style="text-align: center; color: #1e40af; font-weight: 700;">B+ (Very Good)</td>
        </tr>
        <tr>
            <td style="text-align: center;"><strong>IM-2K26-04</strong></td>
            <td>Sneha Joshi</td>
            <td style="text-align: center;">34</td>
            <td style="text-align: center;">50</td>
            <td style="text-align: center; font-weight: 700;">84</td>
            <td style="text-align: center; color: #15803d; font-weight: 700;">A (Excellent)</td>
        </tr>
        <tr style="background-color: #e2e8f0; font-weight: 700;">
            <td style="text-align: center;">BENCHMARK</td>
            <td>Class Average Formula</td>
            <td style="text-align: center;">=AVERAGE()</td>
            <td style="text-align: center;">=AVERAGE()</td>
            <td style="text-align: center;">86.00</td>
            <td style="text-align: center;">Class Benchmark</td>
        </tr>
    </table>

    <h2>2.4 The Mail Merge Process with Step-by-Step Practical Implementation</h2>
    <p>Mail Merge is an automated workflow that generates mass personalized communications (e.g. admission offer letters, fee slips, certificates) by linking a static master template with dynamic recipient records.</p>

    <div class="figure-box">
        <img src="{img_mm}" alt="Mail Merge Workflow">
        <div class="caption">Figure 2.2: Microsoft Word Mail Merge Architecture & 6-Step Workflow</div>
    </div>

    <h3>2.4.1 Three Essential Components</h3>
    <ul>
        <li><strong>Main Document:</strong> Master template containing fixed text, logos, and merge field tags (e.g. <code>&lt;&lt;Candidate_Name&gt;&gt;</code>).</li>
        <li><strong>Data Source:</strong> Tabular database (Excel <code>.xlsx</code> or Access <code>.accdb</code>) containing recipient records.</li>
        <li><strong>Merged Document:</strong> Resulting multi-page file with unique, personalized pages for each record.</li>
    </ul>

    <h3>2.4.2 Comprehensive 6-Step Mail Merge Workflow</h3>
    <ol>
        <li><strong>Step 1 (Select Document Type):</strong> <code>Mailings</code> tab &gt; <code>Start Mail Merge</code> &gt; choose <code>Letters</code>.</li>
        <li><strong>Step 2 (Select Starting Document):</strong> Choose <code>Use the current document</code>.</li>
        <li><strong>Step 3 (Connect Data Source):</strong> Click <code>Select Recipients</code> &gt; <code>Use an Existing List...</code> &gt; browse and link <code>MBA_Students_2026.xlsx</code>.</li>
        <li><strong>Step 4 (Insert Merge Fields):</strong> Position cursor &gt; click <code>Insert Merge Field</code> &gt; insert fields: <code>&lt;&lt;Candidate_Name&gt;&gt;</code>, <code>&lt;&lt;Roll_No&gt;&gt;</code>, <code>&lt;&lt;Merit_Rank&gt;&gt;</code>, <code>&lt;&lt;Orientation_Date&gt;&gt;</code>, <code>&lt;&lt;Venue&gt;&gt;</code>.</li>
        <li><strong>Step 5 (Preview Results):</strong> Click <code>Preview Results</code> (ABC icon) to verify dynamic data population across records.</li>
        <li><strong>Step 6 (Complete Merge):</strong> Click <code>Finish &amp; Merge</code> &gt; select <code>Edit Individual Documents</code> to create the final merged document or <code>Print Documents</code> to print directly.</li>
    </ol>

    <div class="callout">
        <div class="callout-title">Master Template Sample Letter (With Merge Fields):</div>
        <p style="font-family: monospace; font-size: 8.5pt; white-space: pre-wrap;">To,\n&lt;&lt;Candidate_Name&gt;&gt;\nRoll Number: &lt;&lt;Roll_No&gt;&gt; | Merit Rank: &lt;&lt;Merit_Rank&gt;&gt;\n\nSubject: Invitation to MBA(MS) Academic Orientation Program 2026\n\nDear &lt;&lt;Candidate_Name&gt;&gt;,\nCongratulations on your admission to the MBA (Management Science) 5 Yrs Integrated Program at IIPS, DAVV, Indore! You are cordially invited to the Academic Orientation Ceremony on &lt;&lt;Orientation_Date&gt;&gt; at &lt;&lt;Venue&gt;&gt;. Please bring this letter and your original verification documents.\n\nWarm regards,\nProgram Coordinator, MBA(MS) 5 Yrs, IIPS DAVV</p>
    </div>

    <!-- ==================== TOPIC 3 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 3: Microsoft Excel – Components, Formatting, Charts, Sorting & 7 Standard Functions</h1>
    <p>Microsoft Excel is a spreadsheet modeling software application engineered for financial calculation, budgeting, quantitative data analysis, and visual dashboard generation.</p>

    <div class="figure-box">
        <img src="{img_excel}" alt="MS Excel Interface">
        <div class="caption">Figure 3.1: Microsoft Excel Application Workspace, Formula Bar, and Data Grid</div>
    </div>

    <h2>3.1 Basic Components of Microsoft Excel</h2>
    <ul>
        <li><strong>Workbook vs Worksheet:</strong> A workbook (<code>.xlsx</code>) contains multiple worksheets. Each sheet comprises <strong>1,048,576 Rows</strong> and <strong>16,384 Columns</strong> (A to XFD).</li>
        <li><strong>Cell &amp; Address:</strong> The intersection of a column and row (e.g. <code>C7</code> denotes Column C, Row 7).</li>
        <li><strong>Name Box:</strong> Displays the coordinate address of the currently active cell or defined named range.</li>
        <li><strong>Formula Bar:</strong> Primary authoring bar for entering values, text, and mathematical formulas preceded by <code>fx</code>.</li>
        <li><strong>Active Cell Pointer:</strong> Highlighted cell framed with a dark border containing the AutoFill handle at the bottom-right.</li>
        <li><strong>Sheet Tabs &amp; Status Bar:</strong> Sheet management tabs at the bottom-left; status bar displays real-time auto-calculations (Average, Count, Sum).</li>
    </ul>

    <h2>3.2 Text and Number Handling Features in Workbook</h2>
    <ul>
        <li><strong>Alignment &amp; Wrap Text:</strong> Horizontal/vertical alignment, text angle orientation, and Wrap Text to expand row height for long text.</li>
        <li><strong>Merge &amp; Center:</strong> Consolidates adjacent cells into a single unified cell with centered text for titles.</li>
        <li><strong>Number Formats:</strong> General, Currency (₹, $), Accounting, Short/Long Date, Percentage (%), and Text format (preserves leading zeros in roll numbers).</li>
        <li><strong>AutoFill &amp; Flash Fill (Ctrl+E):</strong> AutoFill generates logical sequences (months, dates, numbers); Flash Fill applies AI pattern extraction.</li>
        <li><strong>Text to Columns:</strong> Parses single-column delimited text (e.g. "Dixit, Krishna") into separate columns using commas or spaces.</li>
    </ul>

    <h2>3.3 Conditional Formatting</h2>
    <p>Conditional Formatting applies automated styling based on user-defined rules to highlight trends and anomalies for management review:</p>
    <ul>
        <li><strong>Highlight Rules:</strong> Greater Than, Less Than, Between, Equal To, Text that Contains, Duplicate Values.</li>
        <li><strong>Top/Bottom Rules:</strong> Top 10 Items, Top 10%, Bottom 10%, Above Average, Below Average.</li>
        <li><strong>Data Bars &amp; Color Scales:</strong> In-cell gradient bars and 3-color heatmaps (Green-Yellow-Red).</li>
        <li><strong>Icon Sets:</strong> Traffic lights, directional arrows, and flags categorizing KPIs into performance tiers.</li>
    </ul>

    <h2>3.4 Step-by-Step Chart Creation Process in MS-Excel</h2>
    <ol>
        <li><strong>Step 1 (Organize Data):</strong> Structure tabular data with distinct headers and select the range (e.g. A1:D5).</li>
        <li><strong>Step 2 (Insert Chart):</strong> <code>Insert</code> tab &gt; <code>Charts</code> group &gt; click <code>Insert Column or Bar Chart</code> &gt; select <code>2-D Clustered Column</code>.</li>
        <li><strong>Step 3 (Chart Elements):</strong> Click the green <code>+</code> icon on chart border to toggle Chart Title, Axis Titles, Data Labels, Gridlines, and Legend.</li>
        <li><strong>Step 4 (Format &amp; Style):</strong> Use the <code>Chart Design</code> tab to apply professional color schemes and styles.</li>
        <li><strong>Step 5 (Placement):</strong> Embed chart within sheet or relocate to a dedicated Chart Sheet via <code>Move Chart</code>.</li>
    </ol>

    <div class="figure-box">
        <img src="{img_chart}" alt="Excel Chart Example">
        <div class="caption">Figure 3.2: Clustered Column Chart Created in MS-Excel: FY 2026 Quarterly Performance Comparison</div>
    </div>

    <h2>3.5 Step-by-Step Sorting in MS-Excel with Multi-Level Example</h2>
    <p>Procedure for multi-level sorting: Select table data &gt; <code>Data</code> tab &gt; click <code>Sort</code> &gt; check "My data has headers" &gt; configure Primary Level (Department A to Z) &gt; click "Add Level" &gt; configure Secondary Level (Performance Rating High to Low) &gt; click "Add Level" &gt; configure Tertiary Level (Monthly Salary Descending) &gt; Click OK.</p>

    <table>
        <tr>
            <th>Employee ID</th>
            <th>Employee Name</th>
            <th>Department (Sort 1: A-Z)</th>
            <th>Rating (Sort 2: High-to-Low)</th>
            <th>Monthly Salary (Sort 3: Descending)</th>
        </tr>
        <tr>
            <td style="text-align: center;">EMP-104</td>
            <td>Vikram Rathore</td>
            <td>Finance</td>
            <td style="text-align: center; font-weight: 700;">4.8</td>
            <td style="text-align: right;">₹95,000</td>
        </tr>
        <tr>
            <td style="text-align: center;">EMP-101</td>
            <td>Krishna Dixit</td>
            <td>Finance</td>
            <td style="text-align: center; font-weight: 700;">4.2</td>
            <td style="text-align: right;">₹82,000</td>
        </tr>
        <tr>
            <td style="text-align: center;">EMP-105</td>
            <td>Megha Kapoor</td>
            <td>Human Resources</td>
            <td style="text-align: center; font-weight: 700;">4.9</td>
            <td style="text-align: right;">₹88,000</td>
        </tr>
        <tr>
            <td style="text-align: center;">EMP-102</td>
            <td>Ananya Sharma</td>
            <td>Marketing</td>
            <td style="text-align: center; font-weight: 700;">4.7</td>
            <td style="text-align: right;">₹90,000</td>
        </tr>
        <tr>
            <td style="text-align: center;">EMP-103</td>
            <td>Rohit Verma</td>
            <td>Marketing</td>
            <td style="text-align: center; font-weight: 700;">4.1</td>
            <td style="text-align: right;">₹75,000</td>
        </tr>
    </table>

    <h2>3.6 Formulas and Seven Standard Functions with Syntax, Examples & Outputs</h2>
    
    <div class="callout">
        <div class="callout-title">1. SUM Function</div>
        <p><strong>Syntax:</strong> <code>=SUM(number1, [number2], ...)</code><br>
        <strong>Purpose:</strong> Computes the mathematical sum of all numeric values across a range.<br>
        <strong>Dataset:</strong> Monthly product sales in cells C2:C6 = [850000, 1200000, 450000, 320000, 210000].<br>
        <strong>Formula:</strong> <code>=SUM(C2:C6)</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>₹3,030,000.00</code></p>
    </div>

    <div class="callout">
        <div class="callout-title">2. AVERAGE Function</div>
        <p><strong>Syntax:</strong> <code>=AVERAGE(number1, [number2], ...)</code><br>
        <strong>Purpose:</strong> Calculates the arithmetic mean of all numeric arguments in the range.<br>
        <strong>Dataset:</strong> Semester exam marks in cells D2:D6 = [90, 94, 76, 84, 86].<br>
        <strong>Formula:</strong> <code>=AVERAGE(D2:D6)</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>86.00</code></p>
    </div>

    <div class="callout">
        <div class="callout-title">3. COUNT & COUNTA Functions</div>
        <p><strong>Syntax:</strong> <code>=COUNT(value1, ...)</code> and <code>=COUNTA(value1, ...)</code><br>
        <strong>Purpose:</strong> COUNT returns the count of cells with numeric data; COUNTA counts all non-empty cells.<br>
        <strong>Dataset:</strong> Cells B2:B10 contain 7 student names and 2 blank empty rows.<br>
        <strong>Formula:</strong> <code>=COUNTA(B2:B10)</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>7 (Active Registered Students)</code></p>
    </div>

    <div class="callout">
        <div class="callout-title">4. MAX and MIN Functions</div>
        <p><strong>Syntax:</strong> <code>=MAX(number1, ...)</code> and <code>=MIN(number1, ...)</code><br>
        <strong>Purpose:</strong> Evaluates and returns the highest (MAX) and lowest (MIN) numeric values in the range.<br>
        <strong>Dataset:</strong> Quarterly Net Profits in cells E2:E5 = [2000000, 2600000, 3000000, 3600000].<br>
        <strong>Formula:</strong> <code>=MAX(E2:E5)</code> and <code>=MIN(E2:E5)</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>Max = ₹3,600,000 | Min = ₹2,000,000</code></p>
    </div>

    <div class="callout">
        <div class="callout-title">5. IF Function (Logical Decision Modeling)</div>
        <p><strong>Syntax:</strong> <code>=IF(logical_test, [value_if_true], [value_if_false])</code><br>
        <strong>Purpose:</strong> Evaluates a logical condition and returns one value if TRUE and an alternate value if FALSE.<br>
        <strong>Dataset:</strong> Sales target achievement in cell F2 = 108%.<br>
        <strong>Formula:</strong> <code>=IF(F2>=100%, "Bonus Eligible", "Standard Pay")</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>"Bonus Eligible"</code></p>
    </div>

    <div class="callout">
        <div class="callout-title">6. VLOOKUP Function (Vertical Database Lookup)</div>
        <p><strong>Syntax:</strong> <code>=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])</code><br>
        <strong>Purpose:</strong> Searches down the leftmost column of a table for a lookup key and returns data from the specified column in the same row.<br>
        <strong>Dataset:</strong> Student database table A2:D50 has Roll Number in Col 1, Name in Col 2, Grade in Col 4.<br>
        <strong>Formula:</strong> <code>=VLOOKUP("IM-2K26-58", A2:D50, 2, FALSE)</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>"Krishna Dixit" (Exact Match)</code></p>
    </div>

    <div class="callout">
        <div class="callout-title">7. CONCATENATE / CONCAT Function</div>
        <p><strong>Syntax:</strong> <code>=CONCAT(text1, [text2], ...)</code> or <code>=CONCATENATE(text1, text2, ...)</code><br>
        <strong>Purpose:</strong> Combines text strings from multiple individual cells into a single continuous formatted string.<br>
        <strong>Dataset:</strong> First Name in A2 = "Krishna", Last Name in B2 = "Dixit", Roll in C2 = "IM-58".<br>
        <strong>Formula:</strong> <code>=CONCAT(A2, " ", B2, " (", C2, ")")</code> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Required Output:</strong> <code>"Krishna Dixit (IM-58)"</code></p>
    </div>

    <!-- ==================== TOPIC 4 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 4: Microsoft PowerPoint – Components, Slide Master, Transitions & Animations</h1>
    <p>Microsoft PowerPoint is an executive presentation platform used to synthesize complex business models, market research, and strategic plans into visual decks.</p>

    <div class="figure-box">
        <img src="{img_ppt}" alt="MS PowerPoint Interface">
        <div class="caption">Figure 4.1: Microsoft PowerPoint Workspace, Transitions Ribbon, and Slide Canvas</div>
    </div>

    <h2>4.1 Basic Components of Microsoft PowerPoint</h2>
    <ul>
        <li><strong>Slide Thumbnail Pane:</strong> Left navigation bar displaying slide thumbnails for reordering, duplicating (Ctrl+D), or deleting slides.</li>
        <li><strong>Slide Canvas:</strong> The primary central authoring workspace where text boxes, graphics, charts, and multimedia are arranged.</li>
        <li><strong>Notes Pane:</strong> Bottom drawer where private presenter talking points and references are recorded. Visible exclusively to the speaker in Presenter View.</li>
        <li><strong>Ribbon System:</strong> Presentation-specific tabs including Transitions (slide-level movement), Animations (object-level effects), and Slide Show (projection settings).</li>
        <li><strong>View Modes:</strong> Normal View (authoring), Slide Sorter (matrix light-table view for restructuring), Reading View, and Slide Show (F5 for fullscreen).</li>
    </ul>

    <h2>4.2 Text Handling Features on Slides</h2>
    <ul>
        <li><strong>Slide Layouts:</strong> Title Slide, Title and Content, Section Header, Two Content, Comparison, Title Only, Blank.</li>
        <li><strong>Character Spacing:</strong> Tracking presets (Very Tight, Tight, Normal, Loose, Very Loose) to optimize legibility on auditorium projection screens.</li>
        <li><strong>WordArt &amp; Visual Styling:</strong> 3D bevels, subtle drop shadows, glow outlines, and gradient fills.</li>
        <li><strong>Text Alignment &amp; Direction:</strong> Horizontal (Left, Center, Right, Justified), vertical alignment (Top, Middle, Bottom inside shape), and text rotation (Horizontal, 90&deg;, 270&deg;, Stacked).</li>
        <li><strong>SmartArt Conversion:</strong> Selecting bullet points and clicking "Convert to SmartArt" instantly converts text into diagrams: Hierarchies (Org Charts), Processes (Linear Chevrons), Cycles (Feedback loops), and Pyramids (Strategy tiers).</li>
    </ul>

    <h2>4.3 Advanced Presentation Features</h2>

    <h3>4.3.1 Slide Master (Corporate Brand Governance)</h3>
    <p>The Slide Master (<code>View</code> &gt; <code>Slide Master</code>) is the underlying blueprint controlling global formatting across all slides. Any change made to the master slide cascades automatically to all slides: universal company logo placement, corporate typography enforcement (e.g. Arial Bold headers), background styling, and automated footer metadata (slide number, date, confidentiality notices).</p>

    <h3>4.3.2 Slide Transitions vs Custom Animations</h3>

    <table>
        <tr>
            <th>Comparative Parameter</th>
            <th>Slide Transitions</th>
            <th>Custom Animations</th>
        </tr>
        <tr>
            <td><strong>Scope of Action</strong></td>
            <td>Applies to the entire slide as it appears on screen</td>
            <td>Applies to individual text boxes, images, or chart bars within a slide</td>
        </tr>
        <tr>
            <td><strong>Category Types</strong></td>
            <td>Subtle (Fade, Push, Wipe), Exciting (Curtains), Dynamic (Morph)</td>
            <td>Entrance (Green), Emphasis (Yellow), Exit (Red), Motion Paths</td>
        </tr>
        <tr>
            <td><strong>Trigger Mechanism</strong></td>
            <td>On Mouse Click OR Automatically after N seconds</td>
            <td>Start On Click, With Previous (simultaneous), After Previous (sequential)</td>
        </tr>
        <tr>
            <td><strong>Executive Best Practice</strong></td>
            <td>Use subtle Morph or Fade (0.75s to 1.2s duration) for corporate dignity</td>
            <td>Animate bullet points "By Paragraph" to direct audience focus during discussion</td>
        </tr>
    </table>

    <h3>4.3.3 Presenter View and Professional Delivery Tools</h3>
    <p><strong>Presenter View:</strong> When connected to a second display or projector, Presenter View displays the live slide to the audience while showing the speaker the current slide, upcoming slide preview, live elapsed timer, speaker notes, digital laser pointer, and annotation pen.<br>
    <strong>Rehearse Timings:</strong> Records the precise duration spent per slide, assisting speakers in keeping presentations within strict executive time limits.</p>

    <!-- ==================== TOPIC 5 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 5: Microsoft Access – RDBMS Architecture, Features, Advantages & Applications</h1>
    <p>Microsoft Access is a desktop <strong>Relational Database Management System (RDBMS)</strong> that couples the relational Microsoft Jet/ACE database engine with a graphical user interface and rapid application development tools.</p>

    <div class="figure-box">
        <img src="{img_access}" alt="MS Access RDBMS Architecture">
        <div class="caption">Figure 5.1: MS-Access Relational Schema Architecture, Foreign Keys, and Core Objects</div>
    </div>

    <h2>5.1 In-Depth Features of Microsoft Access</h2>

    <h3>5.1.1 Six Core Database Objects</h3>
    <ul>
        <li><strong>1. Tables:</strong> The foundational data repositories structured into Rows (Records) and Columns (Fields/Attributes). Every field has a strict data type (Short Text, Number, Date/Time, Currency, AutoNumber, Yes/No).</li>
        <li><strong>2. Queries:</strong> SQL-driven query tools that filter, calculate, sort, and join multi-table records. Types include Select Queries, Parameter Queries, and Action Queries (Append, Update, Delete, Make-Table).</li>
        <li><strong>3. Forms:</strong> Customized graphical user interfaces for safe data entry, record searching, and navigation. Forms protect underlying tables from accidental structure changes.</li>
        <li><strong>4. Reports:</strong> Formatted, printable layouts designed for executive presentation, aggregation, export to PDF, and automated mailing labels.</li>
        <li><strong>5. Macros:</strong> Automated sequences of pre-built actions executed on user events (e.g. clicking a button to open a form or validate data).</li>
        <li><strong>6. Modules:</strong> Blocks of Visual Basic for Applications (VBA) code enabling complex business logic and external system integration.</li>
    </ul>

    <h3>5.1.2 Relational Integrity & Data Modeling</h3>
    <ul>
        <li><strong>Primary Key (PK):</strong> A field that uniquely identifies each record in a table (e.g. <code>StudentID</code> or <code>ProductCode</code>). Guarantees entity integrity and cannot contain null values.</li>
        <li><strong>Foreign Key (FK):</strong> A field in a child table that references the Primary Key of a parent table, establishing relational linkage.</li>
        <li><strong>Relationship Cardinality:</strong> One-to-One (1:1), One-to-Many (1:N e.g. One Customer to Multiple Orders), and Many-to-Many (M:N, resolved via junction table).</li>
        <li><strong>Referential Integrity:</strong> Engine-level constraint preventing orphan records: an order cannot be created for a non-existent CustomerID, with cascading updates/deletes options.</li>
    </ul>

    <h2>5.2 Advantages of Microsoft Access for Business Organizations</h2>
    <ul>
        <li><strong>Cost-Effective:</strong> Included within standard Microsoft 365 and Office Professional bundles, avoiding enterprise licensing fees of Oracle or SAP.</li>
        <li><strong>Rapid Application Development (RAD):</strong> Built-in wizards allow managers to create working multi-table applications (forms, queries, reports) in hours without coding.</li>
        <li><strong>Data Integrity:</strong> Enforces strict data types, input masks, and validation rules that prevent dirty data entry inherent in flat spreadsheets.</li>
        <li><strong>Multi-User Workgroup Support:</strong> Supports simultaneous access for up to 255 concurrent users via split database architecture (Frontend GUI linked to Backend data file).</li>
        <li><strong>Office Integration:</strong> Seamlessly exchanges data with Excel, drives Mail Merge in Word, and can upsize to Microsoft SQL Server / Azure Cloud as organizational data grows.</li>
    </ul>

    <h2>5.3 Concrete Business Applications of MS-Access</h2>
    <ul>
        <li><strong>Small Business CRM &amp; Sales Tracking:</strong> Customer demographics, interaction histories, lead stages, quotation statuses, and follow-up schedules.</li>
        <li><strong>Inventory &amp; Warehouse Tracking:</strong> Stock keeping units (SKUs), reorder thresholds, supplier contact directories, and purchase order receipts.</li>
        <li><strong>Academic Student Information Systems:</strong> Student bio-data, course registrations, semester exam grades, fee payments, and automated report card generation.</li>
        <li><strong>HR &amp; Payroll Administration:</strong> Employee profiles, leave balances, performance appraisal records, and departmental allocations.</li>
    </ul>

    <!-- ==================== TOPIC 6 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 6: Internet Technologies – Search Engine Architecture & Email Protocols</h1>

    <h2>6.1 In-Depth Analysis of Search Engines</h2>
    <p>A search engine is an automated software system designed to discover, index, and retrieve hyperlinked information across the World Wide Web based on user-submitted keywords.</p>

    <div class="figure-box">
        <img src="{img_search}" alt="Search Engine Architecture">
        <div class="caption">Figure 6.1: Search Engine Operation — Web Crawling, Inverted Indexing, Query Processing & SERP Ranking</div>
    </div>

    <h3>6.1.1 The Four-Stage Architecture of Modern Search Engines</h3>
    <ul>
        <li><strong>1. Web Crawling:</strong> Automated bots (e.g. Googlebot, Bingbot) scan the web by discovering new and updated pages through hyperlinks, XML sitemaps, and robots.txt directives.</li>
        <li><strong>2. Indexing &amp; Tokenization:</strong> Harvested web pages are parsed, cleaned of HTML tags, tokenized into keywords, and cataloged into an <strong>Inverted Index</strong> database. An inverted index maps each distinct word to a list of URLs where it occurs, along with positional weights and metadata.</li>
        <li><strong>3. Query Processing:</strong> When a search is entered, natural language processing models (e.g. RankBrain, BERT) analyze the query to correct spelling, identify synonyms, understand search intent, and incorporate geographical context.</li>
        <li><strong>4. Ranking &amp; SERP Rendering:</strong> The ranking algorithm evaluates over 200 ranking signals (including PageRank backlink authority, content relevance, mobile usability, page speed, and SSL security) to sort candidate pages and deliver the Search Engine Results Page (SERP) in fractions of a second.</li>
    </ul>

    <h3>6.1.2 Advanced Search Operators for Executive Information Retrieval</h3>
    <ul>
        <li><strong>Exact Match (<code>"..."</code>):</strong> <code>"MBA Management Science syllabus"</code> (returns pages containing the exact phrase).</li>
        <li><strong>Domain Filter (<code>site:</code>):</strong> <code>site:dauniv.ac.in exam schedule</code> (restricts search results strictly to DAVV official servers).</li>
        <li><strong>Filetype Filter (<code>filetype:</code>):</strong> <code>financial statement analysis filetype:pdf</code> (retrieves downloadable PDF files).</li>
        <li><strong>Negative Keyword (<code>-</code>):</strong> <code>cloud storage providers -amazon</code> (excludes AWS from comparative search).</li>
    </ul>

    <h2>6.2 Electronic Mail (Email) Systems and Protocol Architecture</h2>
    <p>Email is the primary formal communication protocol across global business and governance, relying on a store-and-forward client-server architecture.</p>

    <div class="figure-box">
        <img src="{img_email}" alt="Email Protocols Architecture">
        <div class="caption">Figure 6.2: End-to-End Email Protocol Architecture — MUA, SMTP Transmission & IMAP/POP3 Delivery</div>
    </div>

    <h3>6.2.1 Core Email Communication Protocols</h3>

    <table>
        <tr>
            <th>Protocol Name</th>
            <th>Full Expansion &amp; Ports</th>
            <th>Operational Mechanism</th>
            <th>Primary Business Use Case</th>
        </tr>
        <tr>
            <td><strong>SMTP</strong></td>
            <td>Simple Mail Transfer Protocol<br>Port 25 (relay), Port 587 (STARTTLS)</td>
            <td><strong>Push Protocol:</strong> Transmits outgoing email from client to server and handles server-to-server relay</td>
            <td>Sending outbound corporate emails across internet MTAs</td>
        </tr>
        <tr>
            <td><strong>POP3</strong></td>
            <td>Post Office Protocol Version 3<br>Port 110 (plain), Port 995 (SSL/TLS)</td>
            <td><strong>Pull Protocol:</strong> Downloads messages to local client storage and deletes them from the server by default</td>
            <td>Single-device access with constrained server storage capacity</td>
        </tr>
        <tr>
            <td><strong>IMAP</strong></td>
            <td>Internet Message Access Protocol<br>Port 143 (plain), Port 993 (SSL/TLS)</td>
            <td><strong>Two-Way Synchronization:</strong> Messages remain stored on the server; read states and folders sync across devices</td>
            <td>Modern multi-device access (Smartphones, Laptops, Webmail)</td>
        </tr>
    </table>

    <h3>6.2.2 Anatomy of an Email Message & Security</h3>
    <ul>
        <li><strong>Header Fields:</strong> <code>From</code> (originating address), <code>To</code> (primary recipients), <code>Cc</code> (Carbon Copy for informed parties), <code>Bcc</code> (Blind Carbon Copy for confidential distribution), <code>Subject</code> (concise summary), <code>Date</code>, and <code>Message-ID</code>.</li>
        <li><strong>Attachments &amp; MIME:</strong> Multipurpose Internet Mail Extensions (MIME) encodes binary files (PDF contracts, Excel sheets, JPEG images) into base64 text blocks transmitted alongside message text.</li>
        <li><strong>Security Governance:</strong> <strong>SPF</strong> (validates authorized sending IP addresses in DNS), <strong>DKIM</strong> (cryptographic signature verifying message integrity in transit), and <strong>DMARC</strong> (enforces domain handling policies: monitor, quarantine, or reject).</li>
    </ul>

    <!-- ==================== TOPIC 7 ==================== -->
    <div class="page-break"></div>

    <h1>Topic 7: Web Page Designing – Student Entry Form & Commercial Purchase Order</h1>
    <p>Web forms serve as the primary interactive mechanism for capturing structured data in browser-based applications using HTML5, CSS3, and JavaScript.</p>

    <h2>7.1 Web Form 1: Student Admission & Entry Form</h2>
    <p><strong>Required Form Fields:</strong> Student Roll No., Name of Student, Program Name, Class, and Section.</p>

    <div class="figure-box">
        <img src="{img_form_student}" alt="Student Entry Form Preview">
        <div class="caption">Figure 7.1: Rendered Browser Interface of Student Admission & Entry Form (IIPS DAVV)</div>
    </div>

    <h3>7.1.1 Full Semantic HTML5 and CSS3 Source Code (student_entry_form.html)</h3>
    <pre>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Student Admission Entry Form | IIPS DAVV&lt;/title&gt;
    &lt;style&gt;
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f1f5f9; padding: 24px; display: flex; justify-content: center; }}
        .card {{ background: #fff; width: 100%; max-width: 600px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); overflow: hidden; }}
        .header {{ background: #1e3a8a; color: #fff; padding: 20px; text-align: center; }}
        form {{ padding: 24px; }}
        .form-group {{ margin-bottom: 16px; }}
        label {{ display: block; font-weight: 600; font-size: 13px; margin-bottom: 6px; color: #1e293b; }}
        input[type="text"], select {{ width: 100%; padding: 10px; border: 1.5px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; }}
        .radio-group {{ display: flex; gap: 20px; padding: 6px 0; }}
        .btn-submit {{ background: #1e3a8a; color: #fff; padding: 12px; border: none; border-radius: 6px; font-weight: 600; width: 100%; cursor: pointer; }}
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="card"&gt;
        &lt;div class="header"&gt;
            &lt;h2&gt;International Institute of Professional Studies, DAVV&lt;/h2&gt;
            &lt;p&gt;Student Admission &amp; Academic Registration Form&lt;/p&gt;
        &lt;/div&gt;
        &lt;form action="#" method="POST"&gt;
            &lt;div class="form-group"&gt;
                &lt;label for="rollNo"&gt;Roll Number *&lt;/label&gt;
                &lt;input type="text" id="rollNo" name="rollNo" value="IM-2K26-58" placeholder="e.g. IM-2K26-58" required pattern="^[A-Za-z0-9\-]+$"&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
                &lt;label for="name"&gt;Name of Student *&lt;/label&gt;
                &lt;input type="text" id="name" name="name" value="Krishna Dixit" placeholder="Enter Full Name" required&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
                &lt;label for="program"&gt;Program Name *&lt;/label&gt;
                &lt;select id="program" name="program" required&gt;
                    &lt;option value="MBA(MS) 5 Yrs" selected&gt;MBA (Management Science) 5 Yrs Integrated&lt;/option&gt;
                    &lt;option value="MBA(Tourism) 5 Yrs"&gt;MBA (Tourism) 5 Yrs Integrated&lt;/option&gt;
                    &lt;option value="MCA 6 Yrs"&gt;MCA 6 Yrs Integrated&lt;/option&gt;
                &lt;/select&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
                &lt;label for="class"&gt;Class &amp; Semester *&lt;/label&gt;
                &lt;select id="class" name="class" required&gt;
                    &lt;option value="MBA(MS) - 1st Year (Semester I)" selected&gt;1st Year (Semester I)&lt;/option&gt;
                    &lt;option value="MBA(MS) - 1st Year (Semester II)"&gt;1st Year (Semester II)&lt;/option&gt;
                &lt;/select&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
                &lt;label&gt;Section *&lt;/label&gt;
                &lt;div class="radio-group"&gt;
                    &lt;label&gt;&lt;input type="radio" name="section" value="Section A" checked required&gt; Section A&lt;/label&gt;
                    &lt;label&gt;&lt;input type="radio" name="section" value="Section B" required&gt; Section B&lt;/label&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;button type="submit" class="btn-submit"&gt;Register Student Record&lt;/button&gt;
        &lt;/form&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

    <h2>7.2 Web Form 2: Commercial Product Purchase Order Form</h2>
    <p><strong>Required Form Fields:</strong> Product Name, Product Code, Price, Quantity, and Date. (Includes dynamic JavaScript calculation for Total Order Value).</p>

    <div class="figure-box">
        <img src="{img_form_po}" alt="Purchase Order Form Preview">
        <div class="caption">Figure 7.2: Rendered Browser Interface of Enterprise Product Purchase Order Form</div>
    </div>

    <h3>7.2.1 Full Semantic HTML5, CSS3 and JavaScript Source Code (product_purchase_order.html)</h3>
    <pre>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Commercial Product Purchase Order&lt;/title&gt;
    &lt;style&gt;
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; padding: 24px; display: flex; justify-content: center; }}
        .po-box {{ background: #fff; width: 100%; max-width: 620px; border-radius: 10px; border: 1px solid #cbd5e1; box-shadow: 0 4px 15px rgba(0,0,0,0.06); padding: 28px; }}
        .po-header {{ background: #059669; color: #fff; margin: -28px -28px 24px -28px; padding: 20px; text-align: center; border-radius: 9px 9px 0 0; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
        .full {{ grid-column: span 2; }}
        label {{ display: block; font-weight: 600; font-size: 13px; margin-bottom: 6px; color: #334155; }}
        input {{ width: 100%; padding: 10px; border: 1.5px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-size: 14px; }}
        .calc-box {{ background: #ecfdf5; border: 1.5px dashed #34d399; padding: 14px; border-radius: 6px; margin: 18px 0; text-align: center; font-weight: 700; color: #065f46; }}
        .btn-order {{ background: #059669; color: #fff; padding: 12px; border: none; border-radius: 6px; font-weight: 600; width: 100%; cursor: pointer; }}
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="po-box"&gt;
        &lt;div class="po-header"&gt;
            &lt;h2&gt;Commercial Purchase Order Form&lt;/h2&gt;
            &lt;p&gt;Enterprise Procurement Management System&lt;/p&gt;
        &lt;/div&gt;
        &lt;form oninput="calcTotal()"&gt;
            &lt;div class="grid"&gt;
                &lt;div class="full"&gt;
                    &lt;label&gt;Product Name *&lt;/label&gt;
                    &lt;input type="text" id="pname" placeholder="e.g. Dell Latitude 5430 Business Laptop" required&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;label&gt;Product Code *&lt;/label&gt;
                    &lt;input type="text" id="pcode" placeholder="e.g. PRD-DELL-5430" required&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;label&gt;Order Date *&lt;/label&gt;
                    &lt;input type="date" id="pdate" value="2026-11-14" required&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;label&gt;Unit Price (₹) *&lt;/label&gt;
                    &lt;input type="number" id="price" placeholder="0.00" min="0.01" step="0.01" required&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;label&gt;Quantity *&lt;/label&gt;
                    &lt;input type="number" id="qty" placeholder="1" min="1" step="1" required&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="calc-box" id="totalDisplay"&gt;Total Order Value: ₹0.00&lt;/div&gt;
            &lt;button type="submit" class="btn-order"&gt;Generate Official Purchase Order&lt;/button&gt;
        &lt;/form&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function calcTotal() {{
            const p = parseFloat(document.getElementById('price').value) || 0;
            const q = parseInt(document.getElementById('qty').value, 10) || 0;
            document.getElementById('totalDisplay').innerText = 'Total Order Value: ₹' + (p * q).toLocaleString('en-IN', {{minimumFractionDigits: 2}});
        }}
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>

</body>
</html>"""

    with open(HTML_OUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated print-ready HTML: {HTML_OUT}")
    return HTML_OUT

def convert_html_to_pdf(html_path):
    print("Launching Chrome in headless mode for print-to-PDF conversion...")
    port = 9444
    proc = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless',
        f'--remote-debugging-port={port}',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-dev-shm-usage'
    ], stderr=subprocess.PIPE)

    time.sleep(1.5)
    try:
        # Get target tab
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/json/list') as res:
            tabs = json.loads(res.read())
            ws_url = tabs[0]['webSocketDebuggerUrl']

        ws = websocket.create_connection(ws_url)
        ws.send(json.dumps({'id': 1, 'method': 'Page.enable'}))
        ws.recv()

        # Navigate to local file URL
        file_url = f"file://{os.path.abspath(html_path)}"
        ws.send(json.dumps({'id': 2, 'method': 'Page.navigate', 'params': {'url': file_url}}))

        # Wait for Page.loadEventFired
        while True:
            m = json.loads(ws.recv())
            if m.get('method') == 'Page.loadEventFired':
                break

        time.sleep(0.5)

        # Print to PDF params
        header_html = (
            '<div style="font-size: 7.5pt; width: 100%; text-align: right; color: #64748b; '
            'font-family: Arial, sans-serif; padding-right: 28px; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px;">'
            'IIPS, DAVV | MBA(MS) 5 Yrs - I SEMESTER | Computer Application and Web Technology (IM-104C)'
            '</div>'
        )
        footer_html = (
            '<div style="font-size: 7.5pt; width: 100%; display: flex; justify-content: space-between; '
            'color: #64748b; font-family: Arial, sans-serif; padding: 2px 28px 0 28px; border-top: 1px solid #e2e8f0;">'
            '<span>Practical Assignment Record</span>'
            '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>'
            '</div>'
        )

        print_params = {
            'landscape': False,
            'displayHeaderFooter': True,
            'printBackground': True,
            'paperWidth': 8.27,      # A4 Width in inches
            'paperHeight': 11.69,    # A4 Height in inches
            'marginTop': 0.65,       # Margins in inches
            'marginBottom': 0.65,
            'marginLeft': 0.6,
            'marginRight': 0.6,
            'headerTemplate': header_html,
            'footerTemplate': footer_html,
            'preferCSSPageSize': True
        }

        ws.send(json.dumps({'id': 3, 'method': 'Page.printToPDF', 'params': print_params}))

        while True:
            m = json.loads(ws.recv())
            if m.get('id') == 3:
                pdf_data = base64.b64decode(m['result']['data'])
                break

        # Save to Desktop and Local
        with open(DESKTOP_PDF, 'wb') as f:
            f.write(pdf_data)
        with open(DESKTOP_PDF_GENERIC, 'wb') as f:
            f.write(pdf_data)
        with open(LOCAL_PDF, 'wb') as f:
            f.write(pdf_data)

        print(f"PDF Successfully Generated!\nSaved to:")
        print(f"1. Desktop: {DESKTOP_PDF}")
        print(f"2. Desktop: {DESKTOP_PDF_GENERIC}")
        print(f"3. Workspace: {LOCAL_PDF}")

    finally:
        proc.terminate()

if __name__ == '__main__':
    html_file = build_html()
    convert_html_to_pdf(html_file)
