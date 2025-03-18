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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.continuous_snapshot_params import ContinuousSnapshotParams
from typing import Set
from typing_extensions import Self

class IsilonObjectProtectionParams(BaseModel):
    """
    Specifies the parameters which are specific to Isilon object protection.
    """ # noqa: E501
    continuous_snapshots: Optional[ContinuousSnapshotParams] = Field(default=None, alias="continuousSnapshots")
    protocol: Optional[StrictStr] = Field(default=None, description="Specifies the protocol of the NAS device being backed up.")
    use_changelist: Optional[StrictBool] = Field(default=None, description="Specify whether to use the Isilon Changelist API to directly discover changed files/directories for faster incremental backup. Cohesity will keep an extra snapshot which will be deleted by the next successful backup.", alias="useChangelist")
    __properties: ClassVar[List[str]] = ["continuousSnapshots", "protocol", "useChangelist"]

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3']):
            raise ValueError("must be one of enum values ('kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3')")
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
        """Create an instance of IsilonObjectProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of continuous_snapshots
        if self.continuous_snapshots:
            _dict['continuousSnapshots'] = self.continuous_snapshots.to_dict()
        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        # set to None if use_changelist (nullable) is None
        # and model_fields_set contains the field
        if self.use_changelist is None and "use_changelist" in self.model_fields_set:
            _dict['useChangelist'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IsilonObjectProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continuousSnapshots": ContinuousSnapshotParams.from_dict(obj["continuousSnapshots"]) if obj.get("continuousSnapshots") is not None else None,
            "protocol": obj.get("protocol"),
            "useChangelist": obj.get("useChangelist")
        })
        return _obj


