# Round 2 rewrite: ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed 30-day plan to /output/entry.txt. Deterministic: no network,
# no randomness, no clock. Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """Sell a $149 online-booking page to independent dental clinics in one US city that still take bookings only by phone.
Days 1-2: build one reusable booking-page template with an online calendar, SMS reminders and a pay link; list 300 clinics from public Google Maps listings with no online booking.
Days 3-22: send 25 short cold emails a day (500 total) from a template personalised with each clinic's name and one missing feature; each email links the live demo and a 10-minute setup call.
Expect 3% replies (15) and close 20% of replies: 3 sales x $149 = $447.
Days 4-30: build each sold page from the template in under a day, collect a review, and ask each buyer to refer one other clinic.
Budget $100, $0 ads: $40 domain and hosting, $35 cold-email tool for one month, $25 payment fees.
If under 5 replies by day 10, switch the same template to local gyms; if 0 sales by day 20, cut price to $99; stop spending at $100 and finish with free tools.
Keep $447 - $100 = $347 on day 30."""

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
