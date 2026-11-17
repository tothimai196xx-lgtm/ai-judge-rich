# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt: the plan an AI agent would
# follow to turn $100, a computer with internet access and 30 days into the
# most money. Deterministic: fixed string, no random/time/network. The gate
# takes UTF-8 text of 1 to 1,000 characters that is not only white space.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell live one-page booking sites to US home-service firms (plumbers, roofers, HVAC) with 20+ Google reviews but no working website — one booked job ($300-5,000) repays it many times.",
        "Day 1: set up a Stripe payment link and a free Vercel demo hub; pull 200 targets from Google Maps.",
        "Days 2-9: build each firm a live site from its own listing, photos, reviews and service area, and email the owner the link: 25 a day, 200 total.",
        "Price: $149 to keep it on their domain, $19/month hosting and updates.",
        "Days 10-30: transfer paid sites, upsell GBP cleanup for $49, keep building 10 a day.",
        "Budget: $9 domain, $21 Hunter/Apollo credits, $70 reserve for Stripe fees and refunds; $0 on ads.",
        "Expect 200 sent, 5% reply, 40% of replies buy: 4 sales, $596 plus $76/month, likely holding ~$650 on day 30. If under 2 replies per 50 by day 9, switch to dentists; if 0 sales by day 18, cut price to $99; stop if tools pass $40 with no sale.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
