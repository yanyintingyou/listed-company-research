# Tests

Run the lightweight integrity test from the repository root:

```bash
python3 tests/test_skill_integrity.py
```

The test uses only the Python standard library. It checks:

- cross-agent frontmatter shape;
- required skill sections;
- Hermes adapter presence;
- Codex compatibility preservation;
- routed reference links;
- unsafe or stale patterns;
- absence of embedded backup directories;
- reasonable `SKILL.md` size.
