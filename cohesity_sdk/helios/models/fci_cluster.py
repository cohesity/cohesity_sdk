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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.app_resource import AppResource
from cohesity_sdk.helios.models.error import Error
from cohesity_sdk.helios.models.sql_server import SQLServer
from typing import Set
from typing_extensions import Self

class FCICluster(BaseModel):
    """
    Specifies the details of a Failover Cluster Instance.
    """ # noqa: E501
    error: Optional[Error] = None
    id: Optional[StrictStr] = Field(default=None, description="Specifies the unique identifier of the FCI.")
    is_selected_by_default: Optional[StrictBool] = Field(default=None, description="Indicates to the UI whether this FCI cluster should be selected by default", alias="isSelectedByDefault")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the FCI.")
    resource_info: Optional[AppResource] = Field(default=None, alias="resourceInfo")
    servers: Optional[List[SQLServer]] = Field(default=None, description="Specifies the list of SQL servers which belongs to the given FCI. ")
    __properties: ClassVar[List[str]] = ["error", "id", "isSelectedByDefault", "name", "resourceInfo", "servers"]

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
        """Create an instance of FCICluster from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_info
        if self.resource_info:
            _dict['resourceInfo'] = self.resource_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in servers (list)
        _items = []
        if self.servers:
            for _item_servers in self.servers:
                if _item_servers:
                    _items.append(_item_servers.to_dict())
            _dict['servers'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_selected_by_default (nullable) is None
        # and model_fields_set contains the field
        if self.is_selected_by_default is None and "is_selected_by_default" in self.model_fields_set:
            _dict['isSelectedByDefault'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if servers (nullable) is None
        # and model_fields_set contains the field
        if self.servers is None and "servers" in self.model_fields_set:
            _dict['servers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FCICluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "error": Error.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "id": obj.get("id"),
            "isSelectedByDefault": obj.get("isSelectedByDefault"),
            "name": obj.get("name"),
            "resourceInfo": AppResource.from_dict(obj["resourceInfo"]) if obj.get("resourceInfo") is not None else None,
            "servers": [SQLServer.from_dict(_item) for _item in obj["servers"]] if obj.get("servers") is not None else None
        })
        return _obj


