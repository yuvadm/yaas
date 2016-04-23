# Youtube-dl-as-a-Service

POC for youtube-dl-as-a-Service

## Usage

Install the requirements, ideally inside a virtualenv:

```bash
$ pip install -r requirements.txt
```

Run the server:

```bash
$ python yaas.py
```

Enjoy at [http://127.0.0.1:5000/](http://127.0.0.1:5000/). Files are saved locally on disk at `static/vids`. Totally unsecure; prone to abuse; use wisely.
