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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class ViewStatsInLastHours(BaseModel):
    """
    Specifies the View stats for last hours.
    """ # noqa: E501
    last_hours: Optional[StrictInt] = Field(default=None, description="Specifies the time range.", alias="lastHours")
    nfs_protocol_value: Optional[StrictInt] = Field(default=None, description="Specifies the stats value for NFS protocol.", alias="nfsProtocolValue")
    s3_protocol_value: Optional[StrictInt] = Field(default=None, description="Specifies the stats value for S3 protocol.", alias="s3ProtocolValue")
    smb_protocol_value: Optional[StrictInt] = Field(default=None, description="Specifies the stats value for SMB protocol.", alias="smbProtocolValue")
    value: Optional[StrictInt] = Field(default=None, description="Specifies the stats value for any protocols.")
    __properties: ClassVar[List[str]] = ["lastHours", "nfsProtocolValue", "s3ProtocolValue", "smbProtocolValue", "value"]

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
        """Create an instance of ViewStatsInLastHours from a JSON string"""
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
        # set to None if last_hours (nullable) is None
        # and model_fields_set contains the field
        if self.last_hours is None and "last_hours" in self.model_fields_set:
            _dict['lastHours'] = None

        # set to None if nfs_protocol_value (nullable) is None
        # and model_fields_set contains the field
        if self.nfs_protocol_value is None and "nfs_protocol_value" in self.model_fields_set:
            _dict['nfsProtocolValue'] = None

        # set to None if s3_protocol_value (nullable) is None
        # and model_fields_set contains the field
        if self.s3_protocol_value is None and "s3_protocol_value" in self.model_fields_set:
            _dict['s3ProtocolValue'] = None

        # set to None if smb_protocol_value (nullable) is None
        # and model_fields_set contains the field
        if self.smb_protocol_value is None and "smb_protocol_value" in self.model_fields_set:
            _dict['smbProtocolValue'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewStatsInLastHours from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lastHours": obj.get("lastHours"),
            "nfsProtocolValue": obj.get("nfsProtocolValue"),
            "s3ProtocolValue": obj.get("s3ProtocolValue"),
            "smbProtocolValue": obj.get("smbProtocolValue"),
            "value": obj.get("value")
        })
        return _obj


