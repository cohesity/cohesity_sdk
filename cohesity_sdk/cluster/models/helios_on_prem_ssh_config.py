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
from typing import Set
from typing_extensions import Self

class HeliosOnPremSSHConfig(BaseModel):
    """
    Params for a HeliosOnPremVM SSH access.
    """ # noqa: E501
    ssh_support_user_password_set: Optional[StrictBool] = Field(default=None, description="Specifies if SSH password is set for support user.", alias="sshSupportUserPasswordSet")
    ssh_support_user_sudo_enabled: Optional[StrictBool] = Field(default=None, description="Specifies if SSH sudo access is set for support user.", alias="sshSupportUserSudoEnabled")
    __properties: ClassVar[List[str]] = ["sshSupportUserPasswordSet", "sshSupportUserSudoEnabled"]

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
        """Create an instance of HeliosOnPremSSHConfig from a JSON string"""
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
            "ssh_support_user_password_set",
            "ssh_support_user_sudo_enabled",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if ssh_support_user_password_set (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_support_user_password_set is None and "ssh_support_user_password_set" in self.model_fields_set:
            _dict['sshSupportUserPasswordSet'] = None

        # set to None if ssh_support_user_sudo_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_support_user_sudo_enabled is None and "ssh_support_user_sudo_enabled" in self.model_fields_set:
            _dict['sshSupportUserSudoEnabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosOnPremSSHConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sshSupportUserPasswordSet": obj.get("sshSupportUserPasswordSet"),
            "sshSupportUserSudoEnabled": obj.get("sshSupportUserSudoEnabled")
        })
        return _obj


