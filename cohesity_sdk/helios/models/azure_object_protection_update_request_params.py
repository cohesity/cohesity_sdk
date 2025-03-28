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
from cohesity_sdk.helios.models.azure_native_object_protection_params import AzureNativeObjectProtectionParams
from cohesity_sdk.helios.models.azure_sql_object_protection_params import AzureSqlObjectProtectionParams
from typing import Set
from typing_extensions import Self

class AzureObjectProtectionUpdateRequestParams(BaseModel):
    """
    Specifies the parameters which are specific to Azure related Object Protection update request.
    """ # noqa: E501
    protection_type: Optional[StrictStr] = Field(default=None, description="Specifies the Azure Protection Job type.", alias="protectionType")
    azure_sql_protection_type_params: Optional[AzureSqlObjectProtectionParams] = Field(default=None, alias="azureSqlProtectionTypeParams")
    native_protection_type_params: Optional[AzureNativeObjectProtectionParams] = Field(default=None, alias="nativeProtectionTypeParams")
    __properties: ClassVar[List[str]] = ["protectionType", "azureSqlProtectionTypeParams", "nativeProtectionTypeParams"]

    @field_validator('protection_type')
    def protection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAgent', 'kNative', 'kSnapshotManager', 'kAzureSQL']):
            raise ValueError("must be one of enum values ('kAgent', 'kNative', 'kSnapshotManager', 'kAzureSQL')")
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
        """Create an instance of AzureObjectProtectionUpdateRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of azure_sql_protection_type_params
        if self.azure_sql_protection_type_params:
            _dict['azureSqlProtectionTypeParams'] = self.azure_sql_protection_type_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of native_protection_type_params
        if self.native_protection_type_params:
            _dict['nativeProtectionTypeParams'] = self.native_protection_type_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureObjectProtectionUpdateRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "protectionType": obj.get("protectionType"),
            "azureSqlProtectionTypeParams": AzureSqlObjectProtectionParams.from_dict(obj["azureSqlProtectionTypeParams"]) if obj.get("azureSqlProtectionTypeParams") is not None else None,
            "nativeProtectionTypeParams": AzureNativeObjectProtectionParams.from_dict(obj["nativeProtectionTypeParams"]) if obj.get("nativeProtectionTypeParams") is not None else None
        })
        return _obj


