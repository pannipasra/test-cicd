## Test for CI/CD [UPDATE 9:33 07/06/2024]

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
- [Github Actions + Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-github-action)
- [Github Actions + Azure Container Registry + Azure Web App](https://medium.com/t-t-software-solution/deploy-node-js-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-azure-app-service-plan-azure-container-registry-%E0%B9%81%E0%B8%A5%E0%B8%B0-github-action-460998dd805f)