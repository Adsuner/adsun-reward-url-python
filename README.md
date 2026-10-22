# Adsun Reward URL — Python (FastAPI) server example

FastAPI endpoint for Adsun's **Reward URL** callback with a shared secret and duplicate protection.

## Run

```bash
pip install -r requirements.txt
export REWARD_KEY=change-me
uvicorn main:app --port 3000
```

Replace `YOUR_BLOCK_ID` with the block ID from your Adsun publisher panel.

## Debug mode

`debug: true` shows a test ad: no billing, and the Reward URL is **not** called.
Use it outside Telegram too (otherwise you get `NoUserData`). Remove it before going live.

## Links

- Docs: https://adsun.io/documentation
- Mini App monetization: https://adsun.io/telegram-mini-app-monetization

## License

MIT
