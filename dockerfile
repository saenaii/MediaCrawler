FROM mcr.microsoft.com/playwright/python:v1.33.0-jammy
WORKDIR /app/
COPY . .

RUN apt-get update && apt-get install -y libgl1 python3.10-venv
RUN python3 -m venv venv && /bin/bash -c "source venv/bin/activate" && pip3 install -r requirements.txt
#RUN playwright install && playwright install-deps

CMD ["python3", "/app/MediaCrawler/main.py", "--platform", "xhs", "--lt", "cookie", "--type", "detail"]