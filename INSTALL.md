# Install

Detailed install instructions for the VBBL 2025 Claude Skill. For a quick
overview, see [README.md](README.md#install).

---

## Prerequisites

- **Claude Code** or **Claude.ai** with skills enabled.
- **Python 3.8+** on your `PATH` (only needed if you plan to run
  `scripts/lookup.py` directly — Claude runs it for you inside the skill).

---

## Option 1 — Personal install (Claude Code)

```bash
git clone https://github.com/dorianbanks/Vancouver-Building-By-law-Skill.git
cd Vancouver-Building-By-law-Skill
mkdir -p ~/.claude/skills
cp -R vanbc ~/.claude/skills/vanbc
```

Restart Claude Code. Ask a VBBL question — the skill should auto-trigger.
Run `/plugin list` and look for `vanbc`.

### Updating

```bash
cd Vancouver-Building-By-law-Skill
git pull
cp -R vanbc ~/.claude/skills/vanbc
```

---

## Option 2 — Project-scoped install

From your project root:

```bash
mkdir -p .claude/skills
git clone https://github.com/dorianbanks/Vancouver-Building-By-law-Skill.git /tmp/vanbc-src
cp -R /tmp/vanbc-src/vanbc .claude/skills/vanbc
rm -rf /tmp/vanbc-src
```

Commit `.claude/skills/vanbc` (or add to `.gitignore` if you prefer
everyone install it themselves). Claude Code picks it up automatically
when started in that directory.

---

## Option 3 — Organization-wide upload (Claude Team / Enterprise)

If your Claude plan has **Organization Settings → Add Skill** on
[claude.ai](https://claude.ai), an admin can upload the skill once and it
becomes available to every org member.

```bash
git clone https://github.com/dorianbanks/Vancouver-Building-By-law-Skill.git
cd Vancouver-Building-By-law-Skill/vanbc
zip -r ../vanbc.zip .
cd ..
```

Then in claude.ai: **Settings → Organization → Skills → Add Skill**, and
upload `vanbc.zip`.

> **Size note:** the bundled two-volume PDF set is ~17 MB. If the upload
> UI enforces a smaller cap, see
> [Trimming the skill](#trimming-the-skill-for-upload-size-limits).

---

## Verifying the install

Open Claude Code (or claude.ai) and ask:

```
What does VBBL 2025 Sentence 3.2.2.47.(1) say?
```

You should see Claude:

1. Acknowledge the `vanbc` skill.
2. Resolve the article with `lookup.py`.
3. Read the PDF at the resolved page.
4. Quote the sentence with a *(PDF p. N)* citation.
5. Close with a City-of-Vancouver AHJ disclaimer.

If you get a generic answer with no PDF reference, the skill did not
load — confirm `~/.claude/skills/vanbc/SKILL.md` exists and restart
Claude Code.

---

## Trimming the skill for upload size limits

The two-volume PDF dominates the bundle. If an org-upload UI rejects
the size:

1. **Host the PDFs externally.** Remove `vanbc/assets/*.pdf` from the
   zip and host them somewhere the skill has access to. Update
   `SKILL.md` and the workflow guides to reference the new path.
2. **Ship only the index.** Omit the PDFs entirely — the skill still
   resolves citations to pages via `references/index.json`, and the
   user opens the PDF manually. You lose the quote-from-authoritative-
   text step, which is the main value prop — not recommended.

The included PDFs are the preferred distribution.

---

## Uninstall

```bash
rm -rf ~/.claude/skills/vanbc        # personal install
rm -rf .claude/skills/vanbc          # project install
```

For org-uploaded skills, remove via the same claude.ai admin UI used to
install.
