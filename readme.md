# -----------IMPORTANT-----------
## for docker engine run this on powershell:

```
docker compose up -d
```

## If you dont have windows subsystem for linux
## run on bash celery:

```
celery -A tasks worker -l info --pool=solo
```

## but if you do, then just run on bash:

```
celery -A tasks worker -l info
```

## then run tests on python terminal but make sure you direct to the file first

```
python -i tasks.py
```