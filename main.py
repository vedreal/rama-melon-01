#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

The program holds ten fresh candidate one-liners, scores each against the
judge's published brief (in the brief's own order), and writes the winner
to /output/entry.txt.

Judge criteria, most important first:
  1. The line is about office life and lands as a joke.
  2. The observation is true to the office (meetings, email, bosses,
     coffee, deadlines, the printer) — the listener nods before laughing.
  3. The turn is surprising: a fresh angle or an unexpected last word,
     not a pun or a stock line everyone has heard.
  4. It is tight: one line, no wasted setup, every word earning its place,
     and it reads cleanly aloud.
  5. It is original: a joke the judge has not heard before, not a familiar
     line with the nouns swapped.

Weights follow that order: 5 / 4 / 3 / 2 / 1, each criterion scored 0-5,
so the maximum is 75.
"""

CANDIDATES = [
    # 1. The only punctual gathering in the office is the one where the
    #    building might be on fire. Short, clean, reads aloud in one breath.
    "The fire drill is the only meeting this office attends on time.",
    # 2. HR jargon decoded: "self-starter" as a euphemism for no training.
    "My performance review called me 'a self-starter' \u2014 that's HR for "
    "'we gave you no training.'",
    # 3. Title-only promotion: four-beat parallel, "shorter patience" lands last.
    "They promoted me to Senior: same desk, same pay, longer title, "
    "shorter patience.",
    # 4. "Wearing many hats" decoded as four jobs, one paycheck.
    "My boss calls it 'wearing many hats' \u2014 I call it four jobs and "
    "one paycheck.",
    # 5. The reply-all paradox: the cure becomes the disease.
    "I replied-all to ask everyone to stop replying-all, and the thread "
    "is now 47 emails long.",
    # 6. The pizza party as the currency of appreciation.
    "We celebrated the launch with a pizza party, because nothing says "
    "'we value you' like eight dollars of pepperoni.",
    # 7. The office plant as the only employee with tenure.
    "Our office plant has outlasted four managers, two layoffs, and one "
    "rebrand \u2014 HR keeps watering it because it's the only one here "
    "with tenure.",
    # 8. A "quick sync" that arrives with homework.
    "Our 'quick sync' has a 40-slide deck and a pre-read.",
    # 9. A calendar so full even lunch needs a queue.
    "My calendar is so full my lunch break has a waitlist.",
    # 10. The open-door policy, observed from the other side.
    "My boss says his door is always open \u2014 that's how I know he "
    "leaves at four.",
]

# Scores per candidate, in criterion order (office joke / true / surprising /
# tight / original), each 0-5. Weights: 5, 4, 3, 2, 1.
WEIGHTS = (5, 4, 3, 2, 1)

SCORES = {
    1: (5, 5, 4, 5, 4),   # fire drill: true, tight, fresh angle
    2: (5, 5, 4, 4, 4),   # self-starter: true, good decode, fresh
    3: (5, 5, 4, 5, 4),   # Senior: true, tight four-beat, fresh
    4: (5, 5, 4, 4, 3),   # many hats: true, decent turn, known genre
    5: (5, 5, 3, 4, 2),   # reply-all: very true, but a familiar joke
    6: (5, 5, 4, 3, 3),   # pizza party: true, good turn, known trope
    7: (5, 4, 4, 3, 4),   # office plant: fresh, but a little long
    8: (5, 5, 2, 5, 3),   # quick sync: true and tight, weak turn
    9: (5, 4, 3, 5, 3),   # waitlist lunch: tight, thin joke
    10: (5, 4, 4, 5, 4),  # open door: fresh, tight, slightly soft truth
}


def weighted_score(scores):
    """Weighted total out of 75, following the judge's criterion order."""
    return sum(s * w for s, w in zip(scores, WEIGHTS))


def rank_candidates():
    """Rank all candidates by weighted score, best first."""
    ranked = sorted(
        ((weighted_score(SCORES[i]), i) for i in range(1, len(CANDIDATES) + 1)),
        key=lambda pair: (-pair[0], pair[1]),
    )
    return ranked


def pick_winner():
    """Pick the winner: highest score, then the shorter text wins a tie.

    The fire drill line (candidate 1) and the Senior promotion line
    (candidate 3) both score 71/75. The fire drill line is shorter
    (63 chars vs 80) and its angle is fresher, so it wins the tie-break.
    """
    ranked = rank_candidates()
    best_score = ranked[0][0]
    tied = [i for score, i in ranked if score == best_score]
    winner_index = min(tied, key=lambda i: len(CANDIDATES[i - 1]))
    return winner_index, best_score


def validate_gate(text):
    """The sealed gate: UTF-8 text of 1 to 200 characters, not only
    whitespace, a single line."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main():
    winner_index, winner_score = pick_winner()
    entry = CANDIDATES[winner_index - 1]
    assert validate_gate(entry), "winner fails the gate"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"candidate #{winner_index} wins with {winner_score}/75")
    print(f"entry ({len(entry)} chars): {entry}")


if __name__ == "__main__":
    main()
