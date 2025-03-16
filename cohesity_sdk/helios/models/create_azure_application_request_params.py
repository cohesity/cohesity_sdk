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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.office365_app_credentials import Office365AppCredentials
from typing import Optional, Set
from typing_extensions import Self

class CreateAzureApplicationRequestParams(BaseModel):
    """
    Specifies the request parameters for creating Azure Applications
    """ # noqa: E501
    access_token: Optional[StrictStr] = Field(description="Specifies the access token for Azure PowerShell Application access.", alias="accessToken")
    app_count: StrictInt = Field(description="Specifies the count of Azure application to be created.", alias="appCount")
    existing_microsoft365_app_credentials_list: Optional[List[Office365AppCredentials]] = Field(default=None, description="Specifies a list of Microsoft365 azure application credentials already added within the Microsoft365 source.", alias="existingMicrosoft365AppCredentialsList")
    microsoft365_region: Optional[StrictStr] = Field(default=None, description="Specifies the region where Office 365 Exchange environment is.", alias="microsoft365Region")
    username: Optional[StrictStr] = Field(description="Specifies the username to access Microsoft365 source.")
    __properties: ClassVar[List[str]] = ["accessToken", "appCount", "existingMicrosoft365AppCredentialsList", "microsoft365Region", "username"]

    @field_validator('microsoft365_region')
    def microsoft365_region_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Default', 'China', 'Germany', 'UsDoD', 'UsGccHigh']):
            raise ValueError("must be one of enum values ('Default', 'China', 'Germany', 'UsDoD', 'UsGccHigh')")
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
        """Create an instance of CreateAzureApplicationRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in existing_microsoft365_app_credentials_list (list)
        _items = []
        if self.existing_microsoft365_app_credentials_list:
            for _item_existing_microsoft365_app_credentials_list in self.existing_microsoft365_app_credentials_list:
                if _item_existing_microsoft365_app_credentials_list:
                    _items.append(_item_existing_microsoft365_app_credentials_list.to_dict())
            _dict['existingMicrosoft365AppCredentialsList'] = _items
        # set to None if access_token (nullable) is None
        # and model_fields_set contains the field
        if self.access_token is None and "access_token" in self.model_fields_set:
            _dict['accessToken'] = None

        # set to None if microsoft365_region (nullable) is None
        # and model_fields_set contains the field
        if self.microsoft365_region is None and "microsoft365_region" in self.model_fields_set:
            _dict['microsoft365Region'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAzureApplicationRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessToken": obj.get("accessToken"),
            "appCount": obj.get("appCount"),
            "existingMicrosoft365AppCredentialsList": [Office365AppCredentials.from_dict(_item) for _item in obj["existingMicrosoft365AppCredentialsList"]] if obj.get("existingMicrosoft365AppCredentialsList") is not None else None,
            "microsoft365Region": obj.get("microsoft365Region"),
            "username": obj.get("username")
        })
        return _obj


