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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.file_filtering_policy import FileFilteringPolicy
from cohesity_sdk.cluster.models.file_size_policy import FileSizePolicy
from typing import Optional, Set
from typing_extensions import Self

class CommonTieringPolicy(BaseModel):
    """
    Specifies the common tiering params between uptiering and downtiering.
    """ # noqa: E501
    enable_audit_logging: Optional[StrictBool] = Field(default=False, description="Specifies whether to audit log the file tiering activity.", alias="enableAuditLogging")
    file_path: Optional[FileFilteringPolicy] = Field(default=None, alias="filePath")
    file_size: Optional[FileSizePolicy] = Field(default=None, alias="fileSize")
    __properties: ClassVar[List[str]] = ["enableAuditLogging", "filePath", "fileSize"]

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
        """Create an instance of CommonTieringPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file_path
        if self.file_path:
            _dict['filePath'] = self.file_path.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_size
        if self.file_size:
            _dict['fileSize'] = self.file_size.to_dict()
        # set to None if enable_audit_logging (nullable) is None
        # and model_fields_set contains the field
        if self.enable_audit_logging is None and "enable_audit_logging" in self.model_fields_set:
            _dict['enableAuditLogging'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonTieringPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enableAuditLogging": obj.get("enableAuditLogging") if obj.get("enableAuditLogging") is not None else False,
            "filePath": FileFilteringPolicy.from_dict(obj["filePath"]) if obj.get("filePath") is not None else None,
            "fileSize": FileSizePolicy.from_dict(obj["fileSize"]) if obj.get("fileSize") is not None else None
        })
        return _obj


