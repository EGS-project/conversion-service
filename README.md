```
export PYTHONPATH=$PWD 
```
if no venv `python3 -m venv venv`
```
source venv/bin/activate
```
```
pip install -r src/requirements/base.txt 
```
```
docker compose up rabbitmq -d   
```

Two terminals (left/right)
 - ```
    python tests/broker/receiver.py  
    ```
 - ```
    python tests/broker/sender.py     
    ```