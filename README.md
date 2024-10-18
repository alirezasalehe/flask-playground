### Usage

Install requirements: ```pip install -r requirements.txt```

Run project: ```python src/main.py```

Shorten a URL: ```curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" --data '{"url": "https://golabi.com"}'```

Use shortened URL: ```curl http://localhost:5000/{response_of_previous_curl}```

### TODO
- Dockerize project
- Add postgres database
- Write tests
