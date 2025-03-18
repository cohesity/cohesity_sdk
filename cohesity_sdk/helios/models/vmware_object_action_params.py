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
from cohesity_sdk.helios.models.vmware_object_enable_app_protection_params import VmwareObjectEnableAppProtectionParams
from typing import Set
from typing_extensions import Self

class VmwareObjectActionParams(BaseModel):
    """
    Specifies the parameters to perform an action on VMware Objects.
    """ # noqa: E501
    action: Optional[StrictStr] = Field(description="Specifies the action on the Object.")
    enable_app_protection_params: Optional[VmwareObjectEnableAppProtectionParams] = Field(default=None, alias="enableAppProtectionParams")
    __properties: ClassVar[List[str]] = ["action", "enableAppProtectionParams"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enableAppProtection', 'disableAppProtection', 'upgradeCdpIoFilter', 'uninstallCdpIoFilter', 'reEnableCDP']):
            raise ValueError("must be one of enum values ('enableAppProtection', 'disableAppProtection', 'upgradeCdpIoFilter', 'uninstallCdpIoFilter', 'reEnableCDP')")
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
        """Create an instance of VmwareObjectActionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of enable_app_protection_params
        if self.enable_app_protection_params:
            _dict['enableAppProtectionParams'] = self.enable_app_protection_params.to_dict()
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareObjectActionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "enableAppProtectionParams": VmwareObjectEnableAppProtectionParams.from_dict(obj["enableAppProtectionParams"]) if obj.get("enableAppProtectionParams") is not None else None
        })
        return _obj


