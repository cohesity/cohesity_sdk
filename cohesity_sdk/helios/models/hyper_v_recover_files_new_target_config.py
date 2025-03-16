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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.credentials import Credentials
from cohesity_sdk.helios.models.recover_target import RecoverTarget
from typing import Optional, Set
from typing_extensions import Self

class HyperVRecoverFilesNewTargetConfig(BaseModel):
    """
    Specifies the configuration for recovering files and folders to a new target.
    """ # noqa: E501
    absolute_path: Optional[StrictStr] = Field(description="Specifies the path location to recover files to.", alias="absolutePath")
    target_vm: Optional[RecoverTarget] = Field(description="Specifies the target VM to recover files and folders to.", alias="targetVm")
    target_vm_credentials: Optional[Credentials] = Field(description="Specifies the credentials for the target VM.", alias="targetVmCredentials")
    __properties: ClassVar[List[str]] = ["absolutePath", "targetVm", "targetVmCredentials"]

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
        """Create an instance of HyperVRecoverFilesNewTargetConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target_vm
        if self.target_vm:
            _dict['targetVm'] = self.target_vm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_vm_credentials
        if self.target_vm_credentials:
            _dict['targetVmCredentials'] = self.target_vm_credentials.to_dict()
        # set to None if absolute_path (nullable) is None
        # and model_fields_set contains the field
        if self.absolute_path is None and "absolute_path" in self.model_fields_set:
            _dict['absolutePath'] = None

        # set to None if target_vm (nullable) is None
        # and model_fields_set contains the field
        if self.target_vm is None and "target_vm" in self.model_fields_set:
            _dict['targetVm'] = None

        # set to None if target_vm_credentials (nullable) is None
        # and model_fields_set contains the field
        if self.target_vm_credentials is None and "target_vm_credentials" in self.model_fields_set:
            _dict['targetVmCredentials'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HyperVRecoverFilesNewTargetConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "absolutePath": obj.get("absolutePath"),
            "targetVm": RecoverTarget.from_dict(obj["targetVm"]) if obj.get("targetVm") is not None else None,
            "targetVmCredentials": Credentials.from_dict(obj["targetVmCredentials"]) if obj.get("targetVmCredentials") is not None else None
        })
        return _obj


