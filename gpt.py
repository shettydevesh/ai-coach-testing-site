import requests as r

def gpt_answer(query):
    try:
        response = r.post("https://level-ai-personal-coach.level.game/api/coach/prompt", json={
        "question": query,
        "user_id": "510a7e73-b6b9-11ee-9b59-06099339ad11"
        }, headers={"Content-Type": "application/json"})
        answer = response.json()
        return answer['message']
            
    except Exception as e:
        print(e)