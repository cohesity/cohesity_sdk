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
from cohesity_sdk.models.aws_iam_role_params import AwsIAmRoleParams
from cohesity_sdk.models.aws_iam_user_params import AwsIAmUserParams
from cohesity_sdk.models.aws_use_sts_params import AwsUseSTSParams
from typing import Optional, Set
from typing_extensions import Self

class AwsAuthenticationMethodsParams(BaseModel):
    """
    Specifies the Authentication Methods parameters which are specific to AWS related External Targets.
    """ # noqa: E501
    authentication_type: Optional[StrictStr] = Field(description="Specifies the AWS External Target Authentication type.", alias="authenticationType")
    i_am_role_params: Optional[AwsIAmRoleParams] = Field(default=None, alias="iAmRoleParams")
    i_am_user_params: Optional[AwsIAmUserParams] = Field(default=None, alias="iAmUserParams")
    use_sts_params: Optional[AwsUseSTSParams] = Field(default=None, alias="useSTSParams")
    __properties: ClassVar[List[str]] = ["authenticationType", "iAmRoleParams", "iAmUserParams", "useSTSParams"]

    @field_validator('authentication_type')
    def authentication_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kUseIAMUser', 'kUseIAMRole', 'kUseSTS', 'kUseHelios']):
            raise ValueError("must be one of enum values ('kUseIAMUser', 'kUseIAMRole', 'kUseSTS', 'kUseHelios')")
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
        """Create an instance of AwsAuthenticationMethodsParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of i_am_role_params
        if self.i_am_role_params:
            _dict['iAmRoleParams'] = self.i_am_role_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of i_am_user_params
        if self.i_am_user_params:
            _dict['iAmUserParams'] = self.i_am_user_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of use_sts_params
        if self.use_sts_params:
            _dict['useSTSParams'] = self.use_sts_params.to_dict()
        # set to None if authentication_type (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_type is None and "authentication_type" in self.model_fields_set:
            _dict['authenticationType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsAuthenticationMethodsParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authenticationType": obj.get("authenticationType"),
            "iAmRoleParams": AwsIAmRoleParams.from_dict(obj["iAmRoleParams"]) if obj.get("iAmRoleParams") is not None else None,
            "iAmUserParams": AwsIAmUserParams.from_dict(obj["iAmUserParams"]) if obj.get("iAmUserParams") is not None else None,
            "useSTSParams": AwsUseSTSParams.from_dict(obj["useSTSParams"]) if obj.get("useSTSParams") is not None else None
        })
        return _obj


