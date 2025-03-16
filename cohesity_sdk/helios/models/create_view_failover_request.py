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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.planned_failover_params import PlannedFailoverParams
from cohesity_sdk.helios.models.unplanned_failover_params import UnplannedFailoverParams
from typing import Optional, Set
from typing_extensions import Self

class CreateViewFailoverRequest(BaseModel):
    """
    Specifies the request parameters to create a view failover task.
    """ # noqa: E501
    planned_failover_params: Optional[PlannedFailoverParams] = Field(default=None, description="Specifies parameters to create a planned failover.", alias="plannedFailoverParams")
    type: Optional[StrictStr] = Field(description="Specifies the failover type.<br> 'Planned' indicates this is a planned failover.<br> 'Unplanned' indicates this is an unplanned failover, which is used when source cluster is down.")
    unplanned_failover_params: Optional[UnplannedFailoverParams] = Field(default=None, description="Specifies parameters to create an unplanned failover.", alias="unplannedFailoverParams")
    __properties: ClassVar[List[str]] = ["plannedFailoverParams", "type", "unplannedFailoverParams"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Planned', 'Unplanned']):
            raise ValueError("must be one of enum values ('Planned', 'Unplanned')")
        return value

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
        """Create an instance of CreateViewFailoverRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of planned_failover_params
        if self.planned_failover_params:
            _dict['plannedFailoverParams'] = self.planned_failover_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unplanned_failover_params
        if self.unplanned_failover_params:
            _dict['unplannedFailoverParams'] = self.unplanned_failover_params.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateViewFailoverRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plannedFailoverParams": PlannedFailoverParams.from_dict(obj["plannedFailoverParams"]) if obj.get("plannedFailoverParams") is not None else None,
            "type": obj.get("type"),
            "unplannedFailoverParams": UnplannedFailoverParams.from_dict(obj["unplannedFailoverParams"]) if obj.get("unplannedFailoverParams") is not None else None
        })
        return _obj


