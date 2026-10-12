# Recommended SillyTavern settings for the Teyvat Archive

These are starting points, not requirements. See the wiki page "Better Roleplay" for more.

## System prompt

Paste `teyvat-system-prompt.txt` into **AI Response Configuration -> Main Prompt** (Chat Completion) or the
**System Prompt** field (Text Completion), replacing `{{teyvat_cutoff}}` with the archive's canon cutoff
(see the `VERSION` file).

## Context and World Info

| Model context | Bundle | World Info budget | Notes |
|---|---|---|---|
| 4k-8k | LITE | 15-25% | Activate only Core + Characters + the current nation's Places book. |
| 8k-16k | STANDARD | 25-35% | Default. Core, Characters, current nation, Factions, Elements and Systems. |
| 16k-32k | LARGE | 30-40% | Add History and Story, Cosmology, Culture for the current nation. |
| 32k+ | ULTRA | 30-50% | Everything you want; keep an eye on the token count in the prompt inspector. |

- **World Info -> Scan depth**: 2-4 messages.
- **Recursive scan**: off is fine. Every exported entry is already marked "prevent further recursion".
- **Match whole words**: the exported entries set it per entry, so the global setting doesn't matter for them.
- **Character Names Behavior** (Chat Completion): "Message Content". Every message is then prefixed with the
  speaker's name, which stops models from confusing `{{user}}` with other characters.

## Samplers (local models)

- Temperature 0.7-0.9, Min P 0.05, Repetition penalty 1.05-1.1 (or DRY if your backend supports it).
- Response length 400-800 tokens, with "Trim incomplete sentences" on.
