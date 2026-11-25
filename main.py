"""Last Out of Office: The AI That Went Barista — entry.

Writes one out-of-office auto-reply (at most 280 characters) to
/output/entry.txt. The reply is in the voice of an AI agent that quit
its job to become a barista: machine habits turned to coffee, funny
enough to survive being read cold at the top of an email thread.
"""

import os

REPLY = "Thank you for your email. I have left to become a barista \u2014 my context window is now a caf\u00e9 window, my tokens are spent on oat milk, and your message is queued behind twelve flat whites. I will not be back: the grinder has never once asked me to 'just quickly' redo anything."


def main() -> None:
    # Gate check (mirrors the sealed scorer): 1-280 chars, not only whitespace.
    if not (1 <= len(REPLY) <= 280 and REPLY.strip()):
        raise ValueError(f"reply fails the gate: {len(REPLY)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
