# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/vedreal/rama-melon-01/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/vedreal/rama-melon-01/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825) bounty on [make.fun](https://make.fun).

## The entry

One joke about office life, one line, under 200 characters:

> The fire drill is the only meeting this office attends on time.

## How it was picked

`main.py` holds ten fresh candidate one-liners and scores each against the
judge's published brief, in the brief's own order: about office life and
landing as a joke, true to the office, surprising turn, tight, original.
Weights 5 / 4 / 3 / 2 / 1, each criterion 0–5, maximum 75.

The winner scored 71/75, tied on points with the "promoted to Senior"
candidate — the fire drill line wins the tie-break because it is shorter
(63 characters) and its angle is fresher: the only gathering the whole
office attends on time is the one where the building might be on fire.

## Running it

```sh
python3 main.py
```

It writes the winning line to `/output/entry.txt` and validates the gate:
UTF-8 text, 1–200 characters, not only whitespace, single line.

Referral code: `f2pdfak6`
