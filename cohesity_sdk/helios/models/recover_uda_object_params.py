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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RecoverUdaObjectParams(BaseModel):
    """
    Specifies details of objects to be recovered.
    """ # noqa: E501
    object_id: Optional[StrictInt] = Field(default=None, description="Specifies the ID of the object.", alias="objectId")
    object_name: Optional[StrictStr] = Field(default=None, description="Specifies the fully qualified name of the object to be restored.", alias="objectName")
    overwrite: Optional[StrictBool] = Field(default=None, description="Set to true to overwrite an existing object at the destination. If set to false, and the same object exists at the destination, then recovery will fail for that object.")
    rename_to: Optional[StrictStr] = Field(default=None, description="Specifies the new name to which the object should be renamed to after the recovery.", alias="renameTo")
    __properties: ClassVar[List[str]] = ["objectId", "objectName", "overwrite", "renameTo"]

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
        """Create an instance of RecoverUdaObjectParams from a JSON string"""
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
        # set to None if object_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_id is None and "object_id" in self.model_fields_set:
            _dict['objectId'] = None

        # set to None if object_name (nullable) is None
        # and model_fields_set contains the field
        if self.object_name is None and "object_name" in self.model_fields_set:
            _dict['objectName'] = None

        # set to None if overwrite (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite is None and "overwrite" in self.model_fields_set:
            _dict['overwrite'] = None

        # set to None if rename_to (nullable) is None
        # and model_fields_set contains the field
        if self.rename_to is None and "rename_to" in self.model_fields_set:
            _dict['renameTo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverUdaObjectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objectId": obj.get("objectId"),
            "objectName": obj.get("objectName"),
            "overwrite": obj.get("overwrite"),
            "renameTo": obj.get("renameTo")
        })
        return _obj


