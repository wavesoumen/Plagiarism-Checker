from fastapi import FastAPI, HTTPException
from typing import List
from googlesearch import search
import os

app = FastAPI()

@app.post("/check_plagiarism/")
async def check_plagiarism(input_text: str) -> dict:
    try:
        domain = "co.id"
        link_blocked = ["id.linkedin.com", "linkedin.com", "youtube.com", "instagram.com", "facebook.com", "tokopedia.com",
                        "twitter.com", "reddit.com", "bukalapak.com", "shopee.com", "blibli.com"]

        filename = "word.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(input_text)

        inputan_mentah = input_text
        inputan = inputan_mentah.replace("\n", " ").split(". ")

        hasil_plagiarism_final = []
        hasil_link_final = []

        for i in range(len(inputan)):
            query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
            for j, link in enumerate(search(query, tld=domain, num=10, stop=10, pause=2)):
                if i != j:
                    continue
                hasil_plagiarism_final.append(inputan[i])
                hasil_link_final.append(link)

        for i in range(len(hasil_plagiarism_final)):
            for j in range(len(hasil_link_final)):
                if i != j:
                    continue
                while True:
                    for k in range(len(link_blocked)):
                        if link_blocked[k] in hasil_link_final[j]:
                            break
                    else:
                        break
                    break

        count = len(inputan)
        count_hasil = len(hasil_link_final)
        hasil_persen = (count_hasil / count) * 100

        response_data = {
            "plagiarism_percentage": hasil_persen,
            "plagiarized_text": hasil_plagiarism_final,
            "links": hasil_link_final
        }
        
        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
