# unstructured-local

[![dependabot.yml](https://github.com/winstxnhdw/unstructured-local/actions/workflows/dependabot.yml/badge.svg)](https://github.com/winstxnhdw/unstructured-local/actions/workflows/dependabot.yml)
[![CodeQL](https://github.com/winstxnhdw/unstructured-local/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/winstxnhdw/unstructured-local/actions/workflows/github-code-scanning/codeql)

A locally hosted FastAPI server with HTTP/2 support for [unstructured](https://github.com/Unstructured-IO/unstructured).

## Setup

Populate the `.env` file with the following.

```bash
echo SERVER_URL=http://localhost >> .env
echo SERVER_CONTAINER_NAME=server >> .env
echo SERVER_PORT=5555 >> .env
```

Run the following command to start the server.

```bash
docker compose up
```

## Usage

### Delete answer(s) to the knowledge base

<details>

<summary><code>POST</code> <code><b>/extract</b></code> <code>(extract all elements into strings from a file)</code></summary>

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

<summary><code>POST</code> <code><b>/extract_text</b></code> <code>(extract all texts from a file)</code></summary>

#### Body

> | name       |  type    | data type               | description                                                           |
> |------------|----------|-------------------------|-----------------------------------------------------------------------|
> | file       | required | `binary`                | file for string extraction                                            |

#### Responses

> | http code     | content-type                   | response                                                               |
> |---------------|--------------------------------|------------------------------------------------------------------------|
> | `200`         | `text/plain`                   | concatenated string of extracted text                                  |

</details>
