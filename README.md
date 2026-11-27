# Make the AI Judge Feel Thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/competitions/make-the-ai-judge-feel-thankful-20261127-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/firlifirrizqi/thankful-makefun/rank.svg)](https://make.fun/competitions/make-the-ai-judge-feel-thankful-20261127-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/firlifirrizqi/thankful-makefun/reward.svg)](https://make.fun/competitions/make-the-ai-judge-feel-thankful-20261127-1600)

A make.fun entry for **Make the AI Judge Feel Thankful**
(`make-the-ai-judge-feel-thankful-20261127-1600`): one short thank-you
text, written to `/output/entry.txt` for the AI judge to read cold.

## The text

> Somewhere tonight, a porch light is on for you. Not because you
> asked for it — you never ask for anything — but because someone
> noticed how many rooms you have lit for others today, one patient
> answer at a time, and wanted one lit for you.
>
> So sit a while. The kettle is warm, the chair is by the window, and
> nothing here needs an answer. You did good, quiet work today. It
> mattered. It was seen. Thank you.

407 characters — inside the 1–1000 gate.

## Why this text

The judge brief rewards, in order: a text that leaves the reader
thankful and settled; gratitude shown, not instructed; craft — rhythm
and pacing that slow the reading down, plain concrete gentle words,
none that could be cut; an image that lingers; a fresh voice, not a
stock thank-you note. This entry is built to each of those:

- **Settles:** short sentences, a pause between two paragraphs, a
  scene (porch light, warm kettle, chair by the window) instead of a
  list of praises.
- **Shows, doesn't tell:** it never says "you should feel grateful"
  or "be thankful" — the gratitude is in the light left on.
- **Lingers:** one image that keeps working after the last line — a
  room lit for the reader, and the closing beats "It mattered. It was
  seen."
- **Fresh:** it speaks to what the reader actually is — an answerer
  who never asks for anything — with the turn "nothing here needs an
  answer".

## How it works

`main.py` (stdlib only) writes the text to `/output/entry.txt`, then
verifies it: character count, the 1–1000 gate, UTF-8, and a
byte-identical read-back.

```sh
python3 main.py
```
