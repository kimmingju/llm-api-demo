## What this demonstrates

- Secure API key handling via environment variables (.env) — no hardcoding
- Minimal LLM call pipeline (input → structured summary + action items)
- Production-friendly error handling for common API failures (e.g., quota/billing)
- Extensible foundation for internal automation agents (docs/tickets/emails → structured outputs)

## Experiments conducted

### 1. Prompt engineering — role & language setting
Compared outputs between a generic English assistant prompt and a Korean business analyst persona.
- Generic prompt: vague action items, shallow analysis
- Korean analyst prompt: concrete action items (PoC design, architecture draft), business-oriented perspective
- **Finding: role definition in system prompt significantly affects output quality**

### 2. Model comparison — gpt-5 vs gpt-4o-mini
Ran identical inputs on both models to evaluate quality vs cost tradeoff.
- gpt-5: actionable, specific outputs with checkbox formatting
- gpt-4o-mini: more abstract outputs, lower specificity
- **Finding: model choice directly impacts the depth of structured outputs**

### 3. Multilingual input handling
Fed Korean text into an English-designed prompt pipeline.
- Model handled Korean input naturally without prompt changes
- **Finding: prompt language and input language can differ — output quality depends on prompt design, not input language**

