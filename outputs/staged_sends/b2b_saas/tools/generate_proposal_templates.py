from __future__ import annotations

import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "hvac_dispatcher",
    "real_estate_proposal",
    "tattoo_studio_booking",
    "auto_detailer_intake",
    "dog_groomer_booking",
    "dental_appointment_sms",
    "coach_booking",
    "freelance_contract_sender",
)


def build(slug: str) -> Path:
    starter = ROOT / slug / "vertical_starter"
    site = json.loads((ROOT / slug / "landing" / "site.json").read_text(encoding="utf-8"))
    flow = json.loads((starter / "workflow.json").read_text(encoding="utf-8"))
    output = starter / "templates" / "proposal_template.pdf"
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=colors.HexColor(site["accent_dark"]), spaceAfter=8))
    styles.add(ParagraphStyle(name="TitleX", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=24, textColor=colors.HexColor("#14201d"), spaceAfter=6))
    styles.add(ParagraphStyle(name="Subtle", parent=styles["BodyText"], fontSize=9, leading=13, textColor=colors.HexColor("#62706b")))
    styles.add(ParagraphStyle(name="Right", parent=styles["BodyText"], alignment=TA_RIGHT, fontSize=9, leading=13))
    styles.add(ParagraphStyle(name="Step", parent=styles["BodyText"], fontSize=8.2, leading=10, textColor=colors.HexColor("#14201d")))
    doc = SimpleDocTemplate(str(output), pagesize=LETTER, leftMargin=.6 * inch, rightMargin=.6 * inch, topMargin=.45 * inch, bottomMargin=.45 * inch, title=f"{site['vertical']} workflow proposal")
    story = []
    story.append(Table([[Paragraph("HFO VERTICAL OPS", styles["Eyebrow"]), Paragraph("PROPOSAL TEMPLATE<br/>Valid for 14 days", styles["Right"])]], colWidths=[4.2 * inch, 2.5 * inch], style=TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LINEBELOW", (0,0), (-1,-1), .7, colors.HexColor("#c9d0c8")), ("BOTTOMPADDING", (0,0), (-1,-1), 10)])))
    story.append(Spacer(1, 10))
    story.append(Paragraph(site["headline"], styles["TitleX"]))
    story.append(Paragraph("Prepared for: [CLIENT BUSINESS] | Prepared by: [PROVIDER]", styles["Subtle"]))
    story.append(Spacer(1, 9))
    story.append(Paragraph("THE NARROW OUTCOME", styles["Eyebrow"]))
    story.append(Paragraph(site["outcome"], styles["Heading2"]))
    story.append(Paragraph(site["after"], styles["BodyText"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("PROPOSED WORKFLOW", styles["Eyebrow"]))
    rows = []
    for index, step in enumerate(flow["steps"], start=1):
        rows.append([Paragraph(f"{index:02d}", styles["Eyebrow"]), Paragraph(f"<b>{step['name']}</b><br/>{step['output']}", styles["Step"]), Paragraph(step["gate"], styles["Subtle"])])
    table = Table(rows, colWidths=[.42 * inch, 3.8 * inch, 2.5 * inch], repeatRows=0)
    table.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#fffdf7")), ("BOX", (0,0), (-1,-1), .7, colors.HexColor("#c9d0c8")), ("INNERGRID", (0,0), (-1,-1), .35, colors.HexColor("#dfe4dd")), ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5), ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7)]))
    story.append(table)
    story.append(Spacer(1, 8))
    story.append(Paragraph("COMMERCIALS", styles["Eyebrow"]))
    pricing = Table([[Paragraph("IMPLEMENTATION", styles["Eyebrow"]), Paragraph("MANAGED CARE", styles["Eyebrow"])], [Paragraph("<b>$1,500</b> one time", styles["Heading2"]), Paragraph("<b>$249</b> / month", styles["Heading2"])], [Paragraph("Configuration, branded proposal template, test pass, and team handoff.", styles["Subtle"]), Paragraph("Monitoring, small fixes, and one monthly workflow tune-up.", styles["Subtle"])]], colWidths=[3.35 * inch, 3.35 * inch])
    pricing.setStyle(TableStyle([("BOX", (0,0), (-1,-1), 1, colors.HexColor(site["accent"])), ("INNERGRID", (0,0), (-1,-1), .35, colors.HexColor("#dfe4dd")), ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#f5f2e8")), ("VALIGN", (0,0), (-1,-1), "TOP"), ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6), ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8)]))
    story.append(pricing)
    story.append(Spacer(1, 7))
    story.append(Paragraph("BOUNDARIES AND ACCEPTANCE", styles["Eyebrow"]))
    story.append(Paragraph("This starter does not activate live payments, send customer communications, or deploy into a production customer account. Final scope, data handling, integrations, and acceptance tests must be approved in writing before implementation.", styles["Subtle"]))
    story.append(Spacer(1, 7))
    story.append(Table([[Paragraph("Accepted by: __________________________", styles["BodyText"]), Paragraph("Date: __________________", styles["Right"])]], colWidths=[4.6 * inch, 2.1 * inch], style=TableStyle([("LINEABOVE", (0,0), (-1,-1), .7, colors.HexColor("#c9d0c8")), ("TOPPADDING", (0,0), (-1,-1), 12)])))
    doc.build(story)
    return output


if __name__ == "__main__":
    for item in SLUGS:
        print(build(item))
