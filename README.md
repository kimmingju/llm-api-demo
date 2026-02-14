## What this demonstrates (Internal Agent Builder)
- Secure API key handling via environment variables (.env) — no hardcoding
- Minimal LLM call pipeline (input → structured summary + action items)
- Production-friendly error handling for common API failures (e.g., quota/billing)
- Extensible foundation for internal automation agents (docs/tickets/emails → structured outputs)

## Note on running
This demo requires an active API billing/quota setup for the provided key.
If you see `insufficient_quota (429)`, configure billing/credits in the provider console and retry.
