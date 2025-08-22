from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import json
from urllib import request as urlrequest, parse

from ..config import AppConfig
from ..utils.logger import get_logger

try:  # optional dependency
    import requests
except Exception:  # pragma: no cover - requests may be missing
    requests = None  # type: ignore


@dataclass
class APIResponse:
    status_code: int
    data: Any

    def json(self) -> Any:
        return self.data


class APIClient:
    """Simple HTTP client for API testing."""

    def __init__(self, config: AppConfig | None = None) -> None:
        self.config = config or AppConfig()
        self.logger = get_logger(self.__class__.__name__)
        self.session = requests.Session() if requests else None

    def _full_url(self, path: str) -> str:
        return f"{self.config.api_base_url.rstrip('/')}/{path.lstrip('/')}"

    def get(self, path: str, **kwargs: Any) -> APIResponse:
        url = self._full_url(path)
        self.logger.info("GET %s", url)
        if requests:
            resp = self.session.get(url, **kwargs)  # type: ignore[call-arg]
            resp.raise_for_status()
            return APIResponse(resp.status_code, resp.json())
        with urlrequest.urlopen(url) as resp:
            data = json.loads(resp.read().decode())
            return APIResponse(resp.status, data)

    def post(
        self,
        path: str,
        data: Any = None,
        json_data: Any = None,
        **kwargs: Any,
    ) -> APIResponse:
        url = self._full_url(path)
        self.logger.info("POST %s", url)
        if requests:
            resp = self.session.post(url, data=data, json=json_data, **kwargs)  # type: ignore[call-arg]
            resp.raise_for_status()
            return APIResponse(resp.status_code, resp.json())
        headers = {}
        if json_data is not None:
            body = json.dumps(json_data).encode()
            headers["Content-Type"] = "application/json"
        elif data is not None:
            body = parse.urlencode(data).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        else:
            body = None
        req = urlrequest.Request(url, data=body, headers=headers)
        with urlrequest.urlopen(req) as resp:
            resp_data = json.loads(resp.read().decode())
            return APIResponse(resp.status, resp_data)
