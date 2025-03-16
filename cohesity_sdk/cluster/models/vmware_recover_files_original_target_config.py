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
from cohesity_sdk.cluster.models.credentials import Credentials
from typing import Optional, Set
from typing_extensions import Self

class VmwareRecoverFilesOriginalTargetConfig(BaseModel):
    """
    Specifies the configuration for recovering files and folders to the original target.
    """ # noqa: E501
    alternate_path: Optional[StrictStr] = Field(default=None, description="Specifies the alternate path location to recover files to.", alias="alternatePath")
    recover_method: StrictStr = Field(description="Specifies the method to recover files and folders.", alias="recoverMethod")
    recover_to_original_path: Optional[StrictBool] = Field(description="Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified.", alias="recoverToOriginalPath")
    target_vm_credentials: Optional[Credentials] = Field(default=None, alias="targetVmCredentials")
    __properties: ClassVar[List[str]] = ["alternatePath", "recoverMethod", "recoverToOriginalPath", "targetVmCredentials"]

    @field_validator('recover_method')
    def recover_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AutoDeploy', 'UseExistingAgent', 'UseHypervisorApis']):
            raise ValueError("must be one of enum values ('AutoDeploy', 'UseExistingAgent', 'UseHypervisorApis')")
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
        """Create an instance of VmwareRecoverFilesOriginalTargetConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target_vm_credentials
        if self.target_vm_credentials:
            _dict['targetVmCredentials'] = self.target_vm_credentials.to_dict()
        # set to None if alternate_path (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_path is None and "alternate_path" in self.model_fields_set:
            _dict['alternatePath'] = None

        # set to None if recover_to_original_path (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to_original_path is None and "recover_to_original_path" in self.model_fields_set:
            _dict['recoverToOriginalPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareRecoverFilesOriginalTargetConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alternatePath": obj.get("alternatePath"),
            "recoverMethod": obj.get("recoverMethod"),
            "recoverToOriginalPath": obj.get("recoverToOriginalPath"),
            "targetVmCredentials": Credentials.from_dict(obj["targetVmCredentials"]) if obj.get("targetVmCredentials") is not None else None
        })
        return _obj


