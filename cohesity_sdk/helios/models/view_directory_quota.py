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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.view_directory_quota_policy import ViewDirectoryQuotaPolicy
from typing import Optional, Set
from typing_extensions import Self

class ViewDirectoryQuota(BaseModel):
    """
    Specifies a View directory quota.
    """ # noqa: E501
    directory_path: Optional[StrictStr] = Field(description="Specifies the directory path.", alias="directoryPath")
    directory_walk_pending: Optional[StrictBool] = Field(default=None, description="Specifies whether directory quota walk is pending.", alias="directoryWalkPending")
    quota_policy: ViewDirectoryQuotaPolicy = Field(alias="quotaPolicy")
    usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the directory usage in bytes.", alias="usageBytes")
    __properties: ClassVar[List[str]] = ["directoryPath", "directoryWalkPending", "quotaPolicy", "usageBytes"]

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
        """Create an instance of ViewDirectoryQuota from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "directory_walk_pending",
            "usage_bytes",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of quota_policy
        if self.quota_policy:
            _dict['quotaPolicy'] = self.quota_policy.to_dict()
        # set to None if directory_path (nullable) is None
        # and model_fields_set contains the field
        if self.directory_path is None and "directory_path" in self.model_fields_set:
            _dict['directoryPath'] = None

        # set to None if directory_walk_pending (nullable) is None
        # and model_fields_set contains the field
        if self.directory_walk_pending is None and "directory_walk_pending" in self.model_fields_set:
            _dict['directoryWalkPending'] = None

        # set to None if usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.usage_bytes is None and "usage_bytes" in self.model_fields_set:
            _dict['usageBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewDirectoryQuota from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "directoryPath": obj.get("directoryPath"),
            "directoryWalkPending": obj.get("directoryWalkPending"),
            "quotaPolicy": ViewDirectoryQuotaPolicy.from_dict(obj["quotaPolicy"]) if obj.get("quotaPolicy") is not None else None,
            "usageBytes": obj.get("usageBytes")
        })
        return _obj


