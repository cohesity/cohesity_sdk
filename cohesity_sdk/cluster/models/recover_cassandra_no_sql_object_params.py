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
from cohesity_sdk.cluster.models.no_sql_object_property import NoSqlObjectProperty
from typing import Set
from typing_extensions import Self

class RecoverCassandraNoSqlObjectParams(BaseModel):
    """
    Specifies the fully qualified object name and other attributes of each object to be recovered.
    """ # noqa: E501
    object_name: Optional[StrictStr] = Field(description="Specifies the fully qualified name of the object to be restored.", alias="objectName")
    object_properties: Optional[List[NoSqlObjectProperty]] = Field(default=None, description="Specifies the properties to be applied to the object at the time of recovery.", alias="objectProperties")
    rename_to: Optional[StrictStr] = Field(default=None, description="Specifies the new name to which the object should be renamed to after the recovery.", alias="renameTo")
    __properties: ClassVar[List[str]] = ["objectName", "objectProperties", "renameTo"]

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
        """Create an instance of RecoverCassandraNoSqlObjectParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in object_properties (list)
        _items = []
        if self.object_properties:
            for _item_object_properties in self.object_properties:
                if _item_object_properties:
                    _items.append(_item_object_properties.to_dict())
            _dict['objectProperties'] = _items
        # set to None if object_name (nullable) is None
        # and model_fields_set contains the field
        if self.object_name is None and "object_name" in self.model_fields_set:
            _dict['objectName'] = None

        # set to None if object_properties (nullable) is None
        # and model_fields_set contains the field
        if self.object_properties is None and "object_properties" in self.model_fields_set:
            _dict['objectProperties'] = None

        # set to None if rename_to (nullable) is None
        # and model_fields_set contains the field
        if self.rename_to is None and "rename_to" in self.model_fields_set:
            _dict['renameTo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverCassandraNoSqlObjectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objectName": obj.get("objectName"),
            "objectProperties": [NoSqlObjectProperty.from_dict(_item) for _item in obj["objectProperties"]] if obj.get("objectProperties") is not None else None,
            "renameTo": obj.get("renameTo")
        })
        return _obj


