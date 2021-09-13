# Ethereum_crawler

## Quickstart

Install dependencies:

```bash

pip3 install -r requirements.txt
```

Run flask application to extract and visualize assignment data:

```bash

python3 applications.py

```


---

Test:

```
Open following link in browser to access the frontend:

http://192.168.0.105:5000/?tx_id=0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f&block_start=9000000&block_end=9099999&date=2020-12-12

cURL request is as below:

curl --location --request GET 'http://192.168.0.105:5000/?tx_id=0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f&block_start=9000000&block_end=9099999&date=2020-12-12%0A'
```



## Running in Docker

1. Install Docker: https://docs.docker.com/install/

2. Build a docker image
        
        > docker build --tag ethereum-crawler:latest .
        > docker image ls
        
        
3. Run a container out of the image  

        > docker run ethereum-crawler:latest
        > curl --location --request GET 'http://192.168.0.105:5000/?tx_id=0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f&block_start=9000000&block_end=9099999&date=2020-12-12%0A'

        
