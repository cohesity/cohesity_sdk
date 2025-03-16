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
from cohesity_sdk.cluster.models.azure_object_level_params import AzureObjectLevelParams
from cohesity_sdk.cluster.models.data_transfer_info import DataTransferInfo
from typing import Optional, Set
from typing_extensions import Self

class AzureNativeObjectProtectionParams(BaseModel):
    """
    Specifies the parameters which are specific to Azure Object Protection Groups using Azure native APIs. Atlease one of tags or objects must be specified.
    """ # noqa: E501
    data_transfer_info: Optional[DataTransferInfo] = Field(default=None, alias="dataTransferInfo")
    objects: Optional[List[AzureObjectLevelParams]] = Field(default=None, description="Specifies the objects to be protected.")
    __properties: ClassVar[List[str]] = ["dataTransferInfo", "objects"]

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
        """Create an instance of AzureNativeObjectProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data_transfer_info
        if self.data_transfer_info:
            _dict['dataTransferInfo'] = self.data_transfer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureNativeObjectProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataTransferInfo": DataTransferInfo.from_dict(obj["dataTransferInfo"]) if obj.get("dataTransferInfo") is not None else None,
            "objects": [AzureObjectLevelParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None
        })
        return _obj


