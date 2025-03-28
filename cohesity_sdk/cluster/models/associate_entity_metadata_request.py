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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from cohesity_sdk.cluster.models.entity_metadata_params import EntityMetadataParams
from typing import Optional, Set
from typing_extensions import Self

class AssociateEntityMetadataRequest(BaseModel):
    """
    Specifies the parameters to associate metadata with entities in the entity hierarchy.
    """ # noqa: E501
    entity_list: List[EntityMetadataParams] = Field(description="Specifies a list of entity and associated metadata mappings.", alias="entityList")
    source_id: StrictInt = Field(description="Specifies the source id of the entities vector whose metadata is being updated.", alias="sourceId")
    __properties: ClassVar[List[str]] = ["entityList", "sourceId"]

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
        """Create an instance of AssociateEntityMetadataRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entity_list (list)
        _items = []
        if self.entity_list:
            for _item_entity_list in self.entity_list:
                if _item_entity_list:
                    _items.append(_item_entity_list.to_dict())
            _dict['entityList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssociateEntityMetadataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityList": [EntityMetadataParams.from_dict(_item) for _item in obj["entityList"]] if obj.get("entityList") is not None else None,
            "sourceId": obj.get("sourceId")
        })
        return _obj


