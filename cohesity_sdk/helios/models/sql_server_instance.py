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
from cohesity_sdk.helios.models.resource_endpoint import ResourceEndpoint
from typing import Set
from typing_extensions import Self

class SQLServerInstance(BaseModel):
    """
    Specifies the details of a SQL server.
    """ # noqa: E501
    endpoints: Optional[List[ResourceEndpoint]] = Field(default=None, description="Specifies the information about endpoint associated with this SQL server instance.")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the unique id of the SQL server instance.")
    is_online: Optional[StrictStr] = Field(default=None, description="Specifies the wehther the SQL server instance is online or not.", alias="isOnline")
    is_partof_fci: Optional[StrictBool] = Field(default=None, description="Specifies whether this SQL server instance is a part of Failover cluster or not.", alias="isPartofFCI")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the SQL server instance.")
    __properties: ClassVar[List[str]] = ["endpoints", "id", "isOnline", "isPartofFCI", "name"]

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
        """Create an instance of SQLServerInstance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item_endpoints in self.endpoints:
                if _item_endpoints:
                    _items.append(_item_endpoints.to_dict())
            _dict['endpoints'] = _items
        # set to None if endpoints (nullable) is None
        # and model_fields_set contains the field
        if self.endpoints is None and "endpoints" in self.model_fields_set:
            _dict['endpoints'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if is_online (nullable) is None
        # and model_fields_set contains the field
        if self.is_online is None and "is_online" in self.model_fields_set:
            _dict['isOnline'] = None

        # set to None if is_partof_fci (nullable) is None
        # and model_fields_set contains the field
        if self.is_partof_fci is None and "is_partof_fci" in self.model_fields_set:
            _dict['isPartofFCI'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SQLServerInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endpoints": [ResourceEndpoint.from_dict(_item) for _item in obj["endpoints"]] if obj.get("endpoints") is not None else None,
            "id": obj.get("id"),
            "isOnline": obj.get("isOnline"),
            "isPartofFCI": obj.get("isPartofFCI"),
            "name": obj.get("name")
        })
        return _obj


