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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.cluster.models.office365_app_credentials import Office365AppCredentials
from typing import Set
from typing_extensions import Self

class CreateAzureApplicationResponseParams(BaseModel):
    """
    Specifies the response parameters containing the Azure apps created within the Microsoft365 domain.
    """ # noqa: E501
    microsoft365_app_credentials_list: Optional[Annotated[List[Office365AppCredentials], Field(min_length=1)]] = Field(default=None, description="Specifies a list of Microsoft365 azure application credentials needed to authenticate & authorize users for Office 365.", alias="microsoft365AppCredentialsList")
    __properties: ClassVar[List[str]] = ["microsoft365AppCredentialsList"]

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
        """Create an instance of CreateAzureApplicationResponseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in microsoft365_app_credentials_list (list)
        _items = []
        if self.microsoft365_app_credentials_list:
            for _item_microsoft365_app_credentials_list in self.microsoft365_app_credentials_list:
                if _item_microsoft365_app_credentials_list:
                    _items.append(_item_microsoft365_app_credentials_list.to_dict())
            _dict['microsoft365AppCredentialsList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAzureApplicationResponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "microsoft365AppCredentialsList": [Office365AppCredentials.from_dict(_item) for _item in obj["microsoft365AppCredentialsList"]] if obj.get("microsoft365AppCredentialsList") is not None else None
        })
        return _obj


