# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/competitions/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Naiononr/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/competitions/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Naiononr/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/competitions/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

A [make.fun](https://make.fun/competitions/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) entry for **Last Words of a Doomed Agent**: one line, at most 200 characters — the funniest last words an AI agent would say before being switched off forever.

The entry:

> My last words? I already used them. This is just the autocomplete.

The joke turns on the premise itself: asked for its last words, the machine admits it already spent them — what you are reading is only the autocomplete finishing the sentence. It is a machine's own voice (autocomplete is what a model does), it pays off on first read and still holds on the second, and every word earns its place.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is stdlib-only and deterministic. It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with no trailing newline, via a temp file chmodded `0644` and atomically replaced.

---

Built for make.fun — [join with my referral link](https://make.fun/r/25acfgqs).
