from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ToolResult:
    tool: str
    status: str
    stdout: str = ""
    stderr: str = ""
    return_code: Optional[int] = None
    error: Optional[str] = None

    def is_success(self):
        return self.status == "success"

    def is_empty(self):
        return self.status == "empty"

    def is_failed(self):
        return self.status in ["failed", "timeout", "not_found"]

    def to_dict(self):
        return asdict(self)
