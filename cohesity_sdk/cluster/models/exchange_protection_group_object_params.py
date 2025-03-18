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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.exchange_app_params import ExchangeAppParams
from typing import Set
from typing_extensions import Self

class ExchangeProtectionGroupObjectParams(BaseModel):
    """
    Specifies the object identifier to for the exchange protection group.
    """ # noqa: E501
    app_params: Optional[List[ExchangeAppParams]] = Field(default=None, description="Specifies the specific parameters required for Exchange app configuration.", alias="appParams")
    id: Optional[StrictInt] = Field(description="Specifies the id of the registered Exchange DAG(Database Availability Group) source or Exchange physical source.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the registered Exchange DAG(Database Availability Group) source or Exchange physical source.")
    __properties: ClassVar[List[str]] = ["appParams", "id", "name"]

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
        """Create an instance of ExchangeProtectionGroupObjectParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in app_params (list)
        _items = []
        if self.app_params:
            for _item_app_params in self.app_params:
                if _item_app_params:
                    _items.append(_item_app_params.to_dict())
            _dict['appParams'] = _items
        # set to None if app_params (nullable) is None
        # and model_fields_set contains the field
        if self.app_params is None and "app_params" in self.model_fields_set:
            _dict['appParams'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExchangeProtectionGroupObjectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appParams": [ExchangeAppParams.from_dict(_item) for _item in obj["appParams"]] if obj.get("appParams") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


