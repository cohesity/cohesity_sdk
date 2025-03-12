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
from cohesity_sdk.cluster.models.failover_replication import FailoverReplication
from typing import Set
from typing_extensions import Self

class Failover(BaseModel):
    """
    Specifies the details of a failover.
    """ # noqa: E501
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the failover complete time in micro seconds.", alias="endTimeUsecs")
    error_message: Optional[StrictStr] = Field(default=None, description="Specifies the error details if failover status is 'Failed'.", alias="errorMessage")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the failover id.")
    replications: Optional[List[FailoverReplication]] = Field(default=None, description="Specifies a list of replications in this failover.")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the failover start time in micro seconds.", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the failover status.")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the failover type.")
    __properties: ClassVar[List[str]] = ["endTimeUsecs", "errorMessage", "id", "replications", "startTimeUsecs", "status", "type"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Running', 'Succeeded', 'Failed']):
            raise ValueError("must be one of enum values ('Running', 'Succeeded', 'Failed')")
        return value

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
        """Create an instance of Failover from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in replications (list)
        _items = []
        if self.replications:
            for _item_replications in self.replications:
                if _item_replications:
                    _items.append(_item_replications.to_dict())
            _dict['replications'] = _items
        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if replications (nullable) is None
        # and model_fields_set contains the field
        if self.replications is None and "replications" in self.model_fields_set:
            _dict['replications'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Failover from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "errorMessage": obj.get("errorMessage"),
            "id": obj.get("id"),
            "replications": [FailoverReplication.from_dict(_item) for _item in obj["replications"]] if obj.get("replications") is not None else None,
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj


