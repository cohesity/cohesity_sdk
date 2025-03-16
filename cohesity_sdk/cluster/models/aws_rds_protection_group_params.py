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
from cohesity_sdk.cluster.models.aws_rds_protection_group_object_params import AwsRdsProtectionGroupObjectParams
from typing import Optional, Set
from typing_extensions import Self

class AwsRdsProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to AWS RDS related Protection Groups.
    """ # noqa: E501
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    exclude_rds_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of arrays of RDS Tag Ids that Specify db instaces to Exclude.", alias="excludeRdsTagIds")
    objects: Optional[List[AwsRdsProtectionGroupObjectParams]] = Field(default=None, description="Specifies the objects to be included in the Protection Group.")
    rds_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of arrays of RDS Tag Ids that Specify db instaces to Protect.", alias="rdsTagIds")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    __properties: ClassVar[List[str]] = ["excludeObjectIds", "excludeRdsTagIds", "objects", "rdsTagIds", "sourceId", "sourceName"]

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
        """Create an instance of AwsRdsProtectionGroupParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "source_id",
            "source_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if exclude_rds_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_rds_tag_ids is None and "exclude_rds_tag_ids" in self.model_fields_set:
            _dict['excludeRdsTagIds'] = None

        # set to None if rds_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.rds_tag_ids is None and "rds_tag_ids" in self.model_fields_set:
            _dict['rdsTagIds'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsRdsProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "excludeRdsTagIds": obj.get("excludeRdsTagIds"),
            "objects": [AwsRdsProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "rdsTagIds": obj.get("rdsTagIds"),
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName")
        })
        return _obj


