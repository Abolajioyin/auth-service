from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional

@dataclass
class Metrics:
    total_requests: int = 0
    label_counts: Dict[str, int] = field(default_factory=dict)
    total_latency_ms: float = 0.0
    last_request_at: Optional[str] = None

    def record(self, label: str, latency_ms: float):
        self.total_requests += 1
        self.total_latency_ms += latency_ms
        self.label_counts[label] = self.label_counts.get(label, 0) + 1
        self.last_request_at = datetime.utcnow().isoformat()

    @property
    def avg_latency_ms(self) -> float:
        if self.total_requests == 0:
            return 0.0
        return round(self.total_latency_ms / self.total_requests, 2)

metrics = Metrics()
