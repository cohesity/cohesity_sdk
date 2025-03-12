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
from cohesity_sdk.cluster.models.entity_identifier import EntityIdentifier
from cohesity_sdk.cluster.models.workload_sub_type import WorkloadSubType
from typing import Set
from typing_extensions import Self

class WorkloadStatsSchema(BaseModel):
    """
    Specifies the workload types.
    """ # noqa: E501
    entity_id: Optional[StrictStr] = Field(default=None, description="Specifies the Id of an Entity.", alias="entityId")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of an Entity.")
    entities: Optional[List[EntityIdentifier]] = Field(default=None, description="Specifies the entities part of Workload schema.")
    var_schema: Optional[StrictStr] = Field(default=None, description="Specifies the Schema Name of Workload.", alias="schema")
    sub_types: Optional[List[WorkloadSubType]] = Field(default=None, description="Specifies the Workload Sub-Types.", alias="subTypes")
    __properties: ClassVar[List[str]] = ["entityId", "name", "entities", "schema", "subTypes"]

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
        """Create an instance of WorkloadStatsSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item_entities in self.entities:
                if _item_entities:
                    _items.append(_item_entities.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sub_types (list)
        _items = []
        if self.sub_types:
            for _item_sub_types in self.sub_types:
                if _item_sub_types:
                    _items.append(_item_sub_types.to_dict())
            _dict['subTypes'] = _items
        # set to None if entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.entity_id is None and "entity_id" in self.model_fields_set:
            _dict['entityId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if entities (nullable) is None
        # and model_fields_set contains the field
        if self.entities is None and "entities" in self.model_fields_set:
            _dict['entities'] = None

        # set to None if var_schema (nullable) is None
        # and model_fields_set contains the field
        if self.var_schema is None and "var_schema" in self.model_fields_set:
            _dict['schema'] = None

        # set to None if sub_types (nullable) is None
        # and model_fields_set contains the field
        if self.sub_types is None and "sub_types" in self.model_fields_set:
            _dict['subTypes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkloadStatsSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": obj.get("entityId"),
            "name": obj.get("name"),
            "entities": [EntityIdentifier.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "schema": obj.get("schema"),
            "subTypes": [WorkloadSubType.from_dict(_item) for _item in obj["subTypes"]] if obj.get("subTypes") is not None else None
        })
        return _obj


