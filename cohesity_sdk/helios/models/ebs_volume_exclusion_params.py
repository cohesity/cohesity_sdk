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
from cohesity_sdk.helios.models.tag_params import TagParams
from typing import Optional, Set
from typing_extensions import Self

class EbsVolumeExclusionParams(BaseModel):
    """
    Specifies the parameters to exclude EBS volumes attached to EC2 instances at global and object level. A volume satisfying any of these criteria will be excluded.
    """ # noqa: E501
    device_names: Optional[List[StrictStr]] = Field(default=None, description="Array of device names to exclude. Eg - /dev/sda.", alias="deviceNames")
    max_volume_size_bytes: Optional[StrictInt] = Field(default=None, description="Any volume larger than this size will be excluded.", alias="maxVolumeSizeBytes")
    raw_query: Optional[StrictStr] = Field(default=None, description="Raw boolean query given as input by the user to exclude volume based on tags. In the current version, the query contains only tags. Eg. query 1 - \"K1\" = \"V1\" AND \"K2\" IN (\"V2\", \"V3\") AND \"K4\" != \"V4\" Eg. query 2 - \"K1\" != \"V1\" OR \"K2\" NOT IN (\"V2\", \"V3\") OR \"K4\" = \"V4\" All Keys and Values must be wrapped inside double quotes. Comparision Operators supported - IN, NOT IN, =, !=. Logical Operators supported - AND, OR. We cannot have AND, OR together in the query. Only one of them is allowed. The processed form for this query is stored in the above tagParamsArray.", alias="rawQuery")
    tag_params_array: Optional[List[Optional[TagParams]]] = Field(default=None, description="Array of TagParams objects. Each TagParams object consists of two vectors: for exclusion and inclusion. Each TagPararms object is present as an ORed item. User can only input queries of form: (<> AND <> AND <> ..) OR (<> AND <> AND <> ..) OR (..) OR (..) OR .. There cannot be an OR operator inside the bracket. Example query: (K1 = V1 AND K2 = V2 AND K3 != V3) OR (K4 = V4 AND K6 != V6). This will lead to formation of two items in tagParamsArray. First item: {exclusionTagArray: [(K1, V1),  (K2, V2)], inclusionTagArray: [(K3, V3)]} Second item: {exclusionTagArray: [(K4, V4)], inclusionTagArray: [(K6, V6)]}.", alias="tagParamsArray")
    volume_ids: Optional[List[StrictStr]] = Field(default=None, description="Array of volume IDs that are to be excluded. This is only for object level exclusion.", alias="volumeIds")
    volume_types: Optional[List[StrictStr]] = Field(default=None, description="Array of volume types to exclude. Eg - gp2, gp3.", alias="volumeTypes")
    __properties: ClassVar[List[str]] = ["deviceNames", "maxVolumeSizeBytes", "rawQuery", "tagParamsArray", "volumeIds", "volumeTypes"]

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
        """Create an instance of EbsVolumeExclusionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tag_params_array (list)
        _items = []
        if self.tag_params_array:
            for _item_tag_params_array in self.tag_params_array:
                if _item_tag_params_array:
                    _items.append(_item_tag_params_array.to_dict())
            _dict['tagParamsArray'] = _items
        # set to None if device_names (nullable) is None
        # and model_fields_set contains the field
        if self.device_names is None and "device_names" in self.model_fields_set:
            _dict['deviceNames'] = None

        # set to None if max_volume_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.max_volume_size_bytes is None and "max_volume_size_bytes" in self.model_fields_set:
            _dict['maxVolumeSizeBytes'] = None

        # set to None if raw_query (nullable) is None
        # and model_fields_set contains the field
        if self.raw_query is None and "raw_query" in self.model_fields_set:
            _dict['rawQuery'] = None

        # set to None if tag_params_array (nullable) is None
        # and model_fields_set contains the field
        if self.tag_params_array is None and "tag_params_array" in self.model_fields_set:
            _dict['tagParamsArray'] = None

        # set to None if volume_ids (nullable) is None
        # and model_fields_set contains the field
        if self.volume_ids is None and "volume_ids" in self.model_fields_set:
            _dict['volumeIds'] = None

        # set to None if volume_types (nullable) is None
        # and model_fields_set contains the field
        if self.volume_types is None and "volume_types" in self.model_fields_set:
            _dict['volumeTypes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EbsVolumeExclusionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deviceNames": obj.get("deviceNames"),
            "maxVolumeSizeBytes": obj.get("maxVolumeSizeBytes"),
            "rawQuery": obj.get("rawQuery"),
            "tagParamsArray": [TagParams.from_dict(_item) for _item in obj["tagParamsArray"]] if obj.get("tagParamsArray") is not None else None,
            "volumeIds": obj.get("volumeIds"),
            "volumeTypes": obj.get("volumeTypes")
        })
        return _obj


