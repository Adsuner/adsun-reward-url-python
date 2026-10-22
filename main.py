import os
from fastapi import FastAPI, HTTPException

app = FastAPI()
seen: set[str] = set()   # use your database in production
coins: dict[int, int] = {}

@app.get("/api/adsun-reward")
async def adsun_reward(userid: int, block: str = "", ts: str = "", key: str = ""):
    if key != os.environ.get("REWARD_KEY"):
        raise HTTPException(403, "forbidden")
    rid = f"{userid}:{block}:{ts}"
    if rid in seen:
        return "duplicate"
    seen.add(rid)
    coins[userid] = coins.get(userid, 0) + 100
    return "ok"
