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

class CassandraSearchParams(BaseModel):
    """
    Specifies the parameters which are specific for searching Cassandra objects.
    """ # noqa: E501
    cassandra_object_types: List[StrictStr] = Field(description="Specifies one or more Cassandra object types to be searched.", alias="cassandraObjectTypes")
    search_string: Optional[StrictStr] = Field(description="Specifies the search string to search the Cassandra Objects", alias="searchString")
    __properties: ClassVar[List[str]] = ["cassandraObjectTypes", "searchString"]

    @field_validator('cassandra_object_types')
    def cassandra_object_types_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['CassandraKeyspaces', 'CassandraTables']):
                raise ValueError("each list item must be one of ('CassandraKeyspaces', 'CassandraTables')")
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
        """Create an instance of CassandraSearchParams from a JSON string"""
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
        # set to None if search_string (nullable) is None
        # and model_fields_set contains the field
        if self.search_string is None and "search_string" in self.model_fields_set:
            _dict['searchString'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CassandraSearchParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cassandraObjectTypes": obj.get("cassandraObjectTypes"),
            "searchString": obj.get("searchString")
        })
        return _obj


