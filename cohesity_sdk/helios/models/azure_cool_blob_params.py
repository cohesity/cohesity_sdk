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
from typing import Optional, Set
from typing_extensions import Self

class AzureCoolBlobParams(BaseModel):
    """
    Specifies the parameters which are specific to Azure related with tier type Cool Blob
    """ # noqa: E501
    category: Optional[StrictStr] = Field(description="Specifies the category of the external target.")
    function_app_deployment_key: Optional[StrictStr] = Field(default=None, description="Specifies the access key to deploy Azure function to function app", alias="functionAppDeploymentKey")
    function_app_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Azure function app, which is the host of Azure functions.", alias="functionAppName")
    __properties: ClassVar[List[str]] = ["category", "functionAppDeploymentKey", "functionAppName"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Azure', 'AzureStandard', 'AzureGovCloud']):
            raise ValueError("must be one of enum values ('Azure', 'AzureStandard', 'AzureGovCloud')")
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
        """Create an instance of AzureCoolBlobParams from a JSON string"""
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
        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if function_app_deployment_key (nullable) is None
        # and model_fields_set contains the field
        if self.function_app_deployment_key is None and "function_app_deployment_key" in self.model_fields_set:
            _dict['functionAppDeploymentKey'] = None

        # set to None if function_app_name (nullable) is None
        # and model_fields_set contains the field
        if self.function_app_name is None and "function_app_name" in self.model_fields_set:
            _dict['functionAppName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureCoolBlobParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "functionAppDeploymentKey": obj.get("functionAppDeploymentKey"),
            "functionAppName": obj.get("functionAppName")
        })
        return _obj


