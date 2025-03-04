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
from cohesity_sdk.models.user_id_mapping_params import UserIdMappingParams
from typing import Optional, Set
from typing_extensions import Self

class IdMappingParams(BaseModel):
    """
    Specifies the params of the user id mapping info of an Active Directory.
    """ # noqa: E501
    sid_mapped_to_unix_root_user: Optional[StrictStr] = Field(description="Specifies the sid of an Active Directory domain user mapping to unix root user.", alias="sidMappedToUnixRootUser")
    user_id_mapping_params: UserIdMappingParams = Field(alias="userIdMappingParams")
    __properties: ClassVar[List[str]] = ["sidMappedToUnixRootUser", "userIdMappingParams"]

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
        """Create an instance of IdMappingParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_id_mapping_params
        if self.user_id_mapping_params:
            _dict['userIdMappingParams'] = self.user_id_mapping_params.to_dict()
        # set to None if sid_mapped_to_unix_root_user (nullable) is None
        # and model_fields_set contains the field
        if self.sid_mapped_to_unix_root_user is None and "sid_mapped_to_unix_root_user" in self.model_fields_set:
            _dict['sidMappedToUnixRootUser'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdMappingParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sidMappedToUnixRootUser": obj.get("sidMappedToUnixRootUser"),
            "userIdMappingParams": UserIdMappingParams.from_dict(obj["userIdMappingParams"]) if obj.get("userIdMappingParams") is not None else None
        })
        return _obj


