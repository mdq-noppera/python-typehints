from typing import Any, Dict, List, Protocol
from pydantic import BaseModel
import json


class Report(BaseModel):
    customer_name: str
    customer_id: int
    information: Dict[str, Any]


class ReportSaver(Protocol):
    def save(self, report: Report) -> None:
        pass

    def save_multiple(self, report: List[Report]) -> None:
        pass


class LocalDiscSaver(ReportSaver):
    def save(self, report: Report) -> None:
        with open(f"{report.customer_id}.json", "w") as file:
            json.dump(report.model_dump, file)

    def save_multiple(self, reports: List[Report]) -> None:
        for r in reports:
            with open(f"{r.customer_id}.json", "w") as file:
                json.dump(r.model_dump, file)


class S3BucketSaver(ReportSaver):
    def save(self, report: Report) -> None:
        # busines logic
        pass

    def save_multiple(self, reports: List[Report]) -> None:
        # busines logic
        pass


class DataManager:
    def __init__(self, report_saver: ReportSaver) -> None:
        self.report_saver = report_saver

    def transform(self, report: Report) -> None:
        # do some business logic
        self.report_saver.save(report)
