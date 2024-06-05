## Test for CI/CD

### How to run
first have to enter `./app`
```sh
cd ./app
```

in typical mode
```sh
fastapi run main.py
```
or
```sh
fastapi run main.py --port $PORT
```

in dev mode
```sh
fastapi dev main.py
```
or 
```sh
fastapi dev main.py --port $PORT
```

### Testing
simply run **pytest**
```sh
pytest
```

### Reference Dcoumentations 
- [Document Request Files](https://fastapi.tiangolo.com/tutorial/request-files/#__tabbed_2_2)