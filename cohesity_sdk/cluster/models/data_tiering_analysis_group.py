# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.data_tiering_analysis_group_run import DataTieringAnalysisGroupRun
from cohesity_sdk.cluster.models.data_tiering_schedule import DataTieringSchedule
from cohesity_sdk.cluster.models.data_tiering_source import DataTieringSource
from typing import Optional, Set
from typing_extensions import Self

class DataTieringAnalysisGroup(BaseModel):
    """
    Specifies the data tiering analysis group.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(description="Specifies the name of the data tiering analysis group.")
    schedule: Optional[DataTieringSchedule] = None
    source: Optional[DataTieringSource] = None
    id: Optional[StrictStr] = Field(default=None, description="Specifies the ID of the data tiering analysis group.")
    last_run: Optional[DataTieringAnalysisGroupRun] = Field(default=None, alias="lastRun")
    last_successful_run: Optional[DataTieringAnalysisGroupRun] = Field(default=None, alias="lastSuccessfulRun")
    __properties: ClassVar[List[str]] = ["name", "schedule", "source", "id", "lastRun", "lastSuccessfulRun"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataTieringAnalysisGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_run
        if self.last_run:
            _dict['lastRun'] = self.last_run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_successful_run
        if self.last_successful_run:
            _dict['lastSuccessfulRun'] = self.last_successful_run.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTieringAnalysisGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "schedule": DataTieringSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "source": DataTieringSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "id": obj.get("id"),
            "lastRun": DataTieringAnalysisGroupRun.from_dict(obj["lastRun"]) if obj.get("lastRun") is not None else None,
            "lastSuccessfulRun": DataTieringAnalysisGroupRun.from_dict(obj["lastSuccessfulRun"]) if obj.get("lastSuccessfulRun") is not None else None
        })
        return _obj


