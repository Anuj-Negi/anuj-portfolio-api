# anuj-portfolio-api

Tiny FastAPI backend for the "Ask me anything" box. It sends the visitor's question plus
`app/profile.md` to the Claude API and returns the answer.

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then put your ANTHROPIC_API_KEY in it
uvicorn app.main:app --reload --port 8000
```

Try it: `curl -X POST localhost:8000/api/ask -H 'Content-Type: application/json' -d '{"question":"Have you led teams?"}'`
Interactive docs: http://localhost:8000/docs

## Change what it knows
Edit `app/profile.md`. That file is the entire knowledge base.
