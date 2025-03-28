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
from cohesity_sdk.helios.models.vmware_sql_credential_params import VmwareSQLCredentialParams
from typing import Set
from typing_extensions import Self

class VmwareObjectEnableSqlProtectionParams(BaseModel):
    """
    Specifies the parameters for enabling SQL protection.
    """ # noqa: E501
    credentials: Optional[VmwareSQLCredentialParams] = None
    use_installed_agent: Optional[StrictBool] = Field(default=None, description="Specifies if agent is already installed.", alias="useInstalledAgent")
    __properties: ClassVar[List[str]] = ["credentials", "useInstalledAgent"]

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
        """Create an instance of VmwareObjectEnableSqlProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # set to None if use_installed_agent (nullable) is None
        # and model_fields_set contains the field
        if self.use_installed_agent is None and "use_installed_agent" in self.model_fields_set:
            _dict['useInstalledAgent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareObjectEnableSqlProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "credentials": VmwareSQLCredentialParams.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "useInstalledAgent": obj.get("useInstalledAgent")
        })
        return _obj


