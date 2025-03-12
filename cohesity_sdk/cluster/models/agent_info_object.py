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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.error import Error
from typing import Set
from typing_extensions import Self

class AgentInfoObject(BaseModel):
    """
    Specifies the upgrade state of the agent.
    """ # noqa: E501
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the upgrade for an agent completed as a Unix epoch Timestamp (in microseconds).", alias="endTimeUsecs")
    error: Optional[Error] = None
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the source where the agent is installed.")
    previous_software_version: Optional[StrictStr] = Field(default=None, description="Specifies the software version of the agent before upgrade.", alias="previousSoftwareVersion")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the upgrade for an agent started as a Unix epoch Timestamp (in microseconds).", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the upgrade status of the agent.<br> 'Scheduled' indicates that upgrade for the agent is yet to start.<br> 'Started' indicates that upgrade for the agent is started.<br> 'Succeeded' indicates that agent was upgraded successfully.<br> 'Failed' indicates that upgrade for the agent has failed.<br> 'Skipped' indicates that upgrade for the agent was skipped.")
    __properties: ClassVar[List[str]] = ["endTimeUsecs", "error", "name", "previousSoftwareVersion", "startTimeUsecs", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Scheduled', 'Started', 'Succeeded', 'Failed', 'Skipped']):
            raise ValueError("must be one of enum values ('Scheduled', 'Started', 'Succeeded', 'Failed', 'Skipped')")
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
        """Create an instance of AgentInfoObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if previous_software_version (nullable) is None
        # and model_fields_set contains the field
        if self.previous_software_version is None and "previous_software_version" in self.model_fields_set:
            _dict['previousSoftwareVersion'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentInfoObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "error": Error.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "name": obj.get("name"),
            "previousSoftwareVersion": obj.get("previousSoftwareVersion"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status")
        })
        return _obj


