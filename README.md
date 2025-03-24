<h1 align="center">Test Suite</h1>
<h3 align="center">Part of <a href="https://github.com/iragca/page-one">Page One</a></h3>

## Prequisites

- docker
- uv (pip install uv)

## Tests

</details><details>
<summary>Backend branch</summary><br>

Start the environment
```
docker compose -f docker_backend/docker-compose.yml up -d
```

Run an integration test.
```
uv run pytest docker_backend/test_backend.py
```

Once finished, compose down
```
docker compose -f docker_backend/docker-compose.yml down
```