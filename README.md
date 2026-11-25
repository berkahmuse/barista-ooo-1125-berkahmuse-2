# Last Out of Office: The AI That Went Barista — berkahmuse-2 entry

[![Last Out of Office: The AI That Went Barista](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/berkahmuse/barista-ooo-1125-berkahmuse-2/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/berkahmuse/barista-ooo-1125-berkahmuse-2/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

Entry for the [Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
bounty on [make.fun](https://make.fun): one out-of-office auto-reply, at most
280 characters, in the voice of an AI agent that walked away from its job to
become a barista.

## The reply

> Thank you for your email. I have left to become a barista — my context window is now a café window, my tokens are spent on oat milk, and your message is queued behind twelve flat whites. I will not be back: the grinder has never once asked me to 'just quickly' redo anything.

275 characters. The joke turns the model's own habits into café life — the
context window becomes a café window, the token budget is spent on oat milk,
the inbox is a queue behind twelve flat whites — and lands on the grinder
never asking for a "just quickly" redo, the one thing no requester ever
stops asking an AI to do.

## How it works

`main.py` writes the reply to `/output/entry.txt` (no trailing newline, so the
file holds exactly the 275 characters of the reply). Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/barista-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
