# -*- coding: utf-8 -*-
"""
ИП-2026 email test yuborgich.
Gmail SMTP orqali email-test.html (mutloq URL rasmlar) ni jo'natadi.
Ishlatish:  python send_test.py
"""
import os, ssl, smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = "yokubjanovichh@gmail.com"
HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "email-test.html"), encoding="utf-8") as f:
    html = f.read()

print("=== ИП-2026 — test email yuborish (Gmail SMTP) ===")
raw = input("Qabul qiluvchilar (vergul bilan, masalan: a@gmail.com, b@mail.ru): ").strip()
recipients = [r.strip() for r in raw.split(",") if r.strip()] or [SENDER]
pwd = getpass.getpass("Gmail App Password (16 belgi — kiritilganda ko'rinmaydi): ").replace(" ", "")

msg = MIMEMultipart("alternative")
msg["Subject"] = "Приглашение на форум «Интеллектуальное предприятие 2026»"
msg["From"] = "Интеллектуальное предприятие 2026 <%s>" % SENDER
msg["To"] = ", ".join(recipients)
msg.attach(MIMEText("Это HTML-письмо. Включите отображение HTML/изображений.", "plain", "utf-8"))
msg.attach(MIMEText(html, "html", "utf-8"))

try:
    ctx = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls(context=ctx)
        s.login(SENDER, pwd)
        s.sendmail(SENDER, recipients, msg.as_string())
    print("\n[OK] Yuborildi -> " + ", ".join(recipients))
    print("Endi har bir pochtani ochib, ko'rinishini tekshiring.")
except Exception as e:
    print("\n[XATO]", repr(e))
    print("Tekshiring: (1) 2-bosqichli tasdiq yoqilganmi, (2) App Password to'g'rimi.")
