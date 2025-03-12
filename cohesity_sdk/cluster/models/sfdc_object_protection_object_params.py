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
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.sfdc_object_field_exclusion import SfdcObjectFieldExclusion
from typing import Set
from typing_extensions import Self

class SfdcObjectProtectionObjectParams(BaseModel):
    """
    Specifies the object parameters to create an Sfdc Object Protection.
    """ # noqa: E501
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the ids of the objects to be excluded in the Object Protection.", alias="excludeObjectIds")
    field_exclusion_list: Optional[List[SfdcObjectFieldExclusion]] = Field(default=None, description="Specifies the list of field names to be excluded in an Sfdc object. A user can specify multiple such entries in this list.", alias="fieldExclusionList")
    id: StrictInt = Field(description="Specifies the id of the Sfdc Org being protected. This cannot be the id of a leaf level object. By default, the Sfdc Org is auto-protected.")
    __properties: ClassVar[List[str]] = ["excludeObjectIds", "fieldExclusionList", "id"]

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
        """Create an instance of SfdcObjectProtectionObjectParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in field_exclusion_list (list)
        _items = []
        if self.field_exclusion_list:
            for _item_field_exclusion_list in self.field_exclusion_list:
                if _item_field_exclusion_list:
                    _items.append(_item_field_exclusion_list.to_dict())
            _dict['fieldExclusionList'] = _items
        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if field_exclusion_list (nullable) is None
        # and model_fields_set contains the field
        if self.field_exclusion_list is None and "field_exclusion_list" in self.model_fields_set:
            _dict['fieldExclusionList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SfdcObjectProtectionObjectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "fieldExclusionList": [SfdcObjectFieldExclusion.from_dict(_item) for _item in obj["fieldExclusionList"]] if obj.get("fieldExclusionList") is not None else None,
            "id": obj.get("id")
        })
        return _obj


