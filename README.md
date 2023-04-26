# unstructured-local

[![main.yml](https://github.com/winstxnhdw/unstructured-local/actions/workflows/main.yml/badge.svg)](https://github.com/winstxnhdw/unstructured-local/actions/workflows/main.yml)
[![dependabot.yml](https://github.com/winstxnhdw/unstructured-local/actions/workflows/dependabot.yml/badge.svg)](https://github.com/winstxnhdw/unstructured-local/actions/workflows/dependabot.yml)
[![CodeQL](https://github.com/winstxnhdw/unstructured-local/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/winstxnhdw/unstructured-local/actions/workflows/github-code-scanning/codeql)

A locally hosted FastAPI server with HTTP/2 support for [unstructured](https://github.com/Unstructured-IO/unstructured).

## Setup

Use the following example docker compose file.

```yaml
services:
  unstructured:
    environment:
      UNSTRUCTURED_PORT: ${UNSTRUCTURED_PORT}
    image: ghcr.io/winstxnhdw/unstructured-local:main
    container_name: ${UNSTRUCTURED_CONTAINER_NAME}
    privileged: true
    healthcheck:
      test: ['CMD-SHELL', 'curl http://localhost:${UNSTRUCTURED_PORT}/v1/']
      interval: 5s
      retries: 5
```

## Usage

### Extract elements from a file

<details>

<summary><code>POST</code> <code><b>/v1/extract</b></code> <code>(extract all elements into strings from a file)</code></summary>

#### Body

> | name       |  type    | data type               | description                                                           |
> |------------|----------|-------------------------|-----------------------------------------------------------------------|
> | file       | required | `binary`                | file for string extraction                                            |

#### Responses

> | http code     | content-type                   | response                                                               |
> |---------------|--------------------------------|------------------------------------------------------------------------|
> | `200`         | `text/plain`                   | concatenated string of all elements                                    |

</details>

<details>

<summary><code>POST</code> <code><b>/v1/extract_text</b></code> <code>(extract all texts from a file)</code></summary>

#### Body

> | name       |  type    | data type               | description                                                           |
> |------------|----------|-------------------------|-----------------------------------------------------------------------|
> | file       | required | `binary`                | file for string extraction                                            |

#### Responses

> | http code     | content-type                   | response                                                               |
> |---------------|--------------------------------|------------------------------------------------------------------------|
> | `200`         | `text/plain`                   | concatenated string of extracted text                                  |

</details>
