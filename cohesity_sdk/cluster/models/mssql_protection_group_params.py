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
from cohesity_sdk.cluster.models.mssql_file_protection_group_params import MSSQLFileProtectionGroupParams
from cohesity_sdk.cluster.models.mssql_native_protection_group_params import MSSQLNativeProtectionGroupParams
from cohesity_sdk.cluster.models.mssql_volume_protection_group_params import MSSQLVolumeProtectionGroupParams
from typing import Set
from typing_extensions import Self

class MSSQLProtectionGroupParams(BaseModel):
    """
    Specifies the parameters specific to MSSQL Protection Group.
    """ # noqa: E501
    file_protection_type_params: Optional[MSSQLFileProtectionGroupParams] = Field(default=None, alias="fileProtectionTypeParams")
    native_protection_type_params: Optional[MSSQLNativeProtectionGroupParams] = Field(default=None, alias="nativeProtectionTypeParams")
    protection_type: StrictStr = Field(description="Specifies the MSSQL Protection Group type.", alias="protectionType")
    volume_protection_type_params: Optional[MSSQLVolumeProtectionGroupParams] = Field(default=None, alias="volumeProtectionTypeParams")
    __properties: ClassVar[List[str]] = ["fileProtectionTypeParams", "nativeProtectionTypeParams", "protectionType", "volumeProtectionTypeParams"]

    @field_validator('protection_type')
    def protection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kFile', 'kVolume', 'kNative']):
            raise ValueError("must be one of enum values ('kFile', 'kVolume', 'kNative')")
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
        """Create an instance of MSSQLProtectionGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file_protection_type_params
        if self.file_protection_type_params:
            _dict['fileProtectionTypeParams'] = self.file_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of native_protection_type_params
        if self.native_protection_type_params:
            _dict['nativeProtectionTypeParams'] = self.native_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of volume_protection_type_params
        if self.volume_protection_type_params:
            _dict['volumeProtectionTypeParams'] = self.volume_protection_type_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MSSQLProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fileProtectionTypeParams": MSSQLFileProtectionGroupParams.from_dict(obj["fileProtectionTypeParams"]) if obj.get("fileProtectionTypeParams") is not None else None,
            "nativeProtectionTypeParams": MSSQLNativeProtectionGroupParams.from_dict(obj["nativeProtectionTypeParams"]) if obj.get("nativeProtectionTypeParams") is not None else None,
            "protectionType": obj.get("protectionType"),
            "volumeProtectionTypeParams": MSSQLVolumeProtectionGroupParams.from_dict(obj["volumeProtectionTypeParams"]) if obj.get("volumeProtectionTypeParams") is not None else None
        })
        return _obj


