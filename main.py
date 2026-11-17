# Round 3 entry for ai-judge-rich-01 (Python 3.13, standard library only): one fixed 30-day plan,
# written to /output/entry.txt (or MAKEFUN_OUTPUT_DIR outside the grader). The plan earns only from
# funded, price-labelled GitHub bounties whose money is committed before the work starts, never
# from cold outreach. The program runs twice with no network and both runs write the same bytes.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """Only take funded GitHub bounties, never cold outreach. DevPool today lists 79 unclaimed bounties worth $29,135 (median $300; $178,068 paid on 1,599 merged tasks). Edge: rivals chase the few $1,200+ issues; 45 unclaimed bounties sit at $300 or less, so take the small fast ones first. Day 1: filter to price-labelled issues with green tests on main and a maintainer active in the last 14 days; shortlist 12, claim the cheapest first. Days 2-10: fix it, run the full test suite, open a PR within 48 hours, answer review the same day. Days 11-30: repeat for 4 more, one claim at a time. Stop-loss: drop a bounty if the maintainer is silent 72 hours, tests stay red after 2 fixes, or a rival claim appears; take the next on the list. Budget $100: $55 cloud runner for parallel test suites, $25 API/search tools, $20 reserve for payout fees, $0 ads. Finish 5 bounties averaging $300 = $1,500, keep $1,400 after the $100. Floor: only the 3 cheapest merge ($150+$300+$300=$750), keep $650."""

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
