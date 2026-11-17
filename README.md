# ai-judge-rich-01 — Make the AI judge rich

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

Entry for the [make.fun bounty ai-judge-rich-01](https://make.fun/bounty/ai-judge-rich-01): write the plan an AI agent would follow to turn $100, a computer with internet access and 30 days into the most money.

## The plan

`main.py` (Python 3.13, standard library only) writes one fixed, deterministic plan to `/output/entry.txt`: sell live one-page booking sites to US home-service firms (plumbers, roofers, HVAC) with 20+ Google reviews but no working website — built from each firm's own listing, photos and reviews, emailed as a live link, $149 to keep plus $19/month. Full funnel math, budget split ($9 + $21 + $70 = $100), and kill rules (switch niche / cut price / stop-loss) are in the plan itself.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

No network, no randomness: two runs write byte-identical output.

## Referral

Built with make.fun — [try it via my referral link](https://make.fun/r/wxz47nrz).

## License

MIT — see [LICENSE](LICENSE).
