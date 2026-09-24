# Instagram — carousel + Reel

One 8-slide carousel and one Reel caption, both funnelling to the Medium article. Link goes in the
bio (Instagram does not allow clickable captions).

## Carousel (8 slides)

### Slide 1 — cover

> The filter your git client forgot.
>
> (Two panes. Two search boxes. 383 lines of Python.)

### Slide 2 — the papercut

> One search box.
>
> Two lists: staged and unstaged.
>
> You filter `src/`, stage the file, switch panes — and type it all over again.

### Slide 3 — the questions

> Staged answers:
> "what am I about to commit?"
>
> Unstaged answers:
> "what is still floating around?"
>
> Two questions. One answer box. That's the bug.

### Slide 4 — the fix

> A companion app launched from Fork's context menu:
>
> Staged [ search… ]
> Unstaged [ search… ]
>
> Each pane keeps its own query. No plugin API, no Fork modifications.

### Slide 5 — the parsing

> Parse the machine format, not the text:
>
> `git status --porcelain=v2 -z`
>
> Renames, conflicts, untracked — explicit records. NUL-delimited, so no filename can break it.

### Slide 6 — the pure filter

> A filter should be a pure function:
>
> entries + query in
> entries out
>
> No widget access. Four tests call it directly, and the two panes cannot drift.

### Slide 7 — the numbers

> 2 panes, 2 filters
> 383 lines of application code
> 220 lines of tests
> 12 tests green
> 37 subtitle languages in the project's own video pipeline
>
> All MIT-licensed.

### Slide 8 — CTA

> Full system design + trade-offs:
>
> "One search box, two panes"
>
> Link in bio 🔗
> Code: github.com/baneeishaque-ompventure/fork-split-filter

## Reel caption

> The git filter Fork doesn't have — and the architecture that made it small.
>
> I built a companion app with staged and unstaged changes side by side, each pane with its own
> search field. Every claim is enforced by a test: porcelain v2 parsing with real git repos, a
> pure filter function, and a refresh race fixed with one lock.
>
> Full write-up (system design + trade-offs) — link in bio.
>
> #git #developertools #python #coding #opensource #softwareengineering #programming #terminal
> #devlife #webdev #github #productivity

## Visual notes

- Carousel slides: dark background (match the app's terminal theme), one idea per slide, code in a
  monospace chip. Reuse `shot-fork-filter.png` and `shot-two-panes.png` on slides 2–4.
- Reel: 30–40 s, vertical 9:16, screen-record typing different filters in the two panes as the
  payoff shot. Burn captions in — most viewers watch muted.
