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
from cohesity_sdk.helios.models.oracle_range_meta_info import OracleRangeMetaInfo
from typing import Set
from typing_extensions import Self

class OracleArchiveLogInfo(BaseModel):
    """
    Specifies information related to archive log restore.
    """ # noqa: E501
    archive_log_restore_dest: Optional[StrictStr] = Field(default=None, description="Specifies destination where archive logs are to be restored.", alias="archiveLogRestoreDest")
    range_info_vec: Optional[List[OracleRangeMetaInfo]] = Field(default=None, description="Specifies an array of oracle restore ranges.", alias="rangeInfoVec")
    range_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of range.", alias="rangeType")
    __properties: ClassVar[List[str]] = ["archiveLogRestoreDest", "rangeInfoVec", "rangeType"]

    @field_validator('range_type')
    def range_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Time', 'Scn', 'Sequence']):
            raise ValueError("must be one of enum values ('Time', 'Scn', 'Sequence')")
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
        """Create an instance of OracleArchiveLogInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in range_info_vec (list)
        _items = []
        if self.range_info_vec:
            for _item_range_info_vec in self.range_info_vec:
                if _item_range_info_vec:
                    _items.append(_item_range_info_vec.to_dict())
            _dict['rangeInfoVec'] = _items
        # set to None if archive_log_restore_dest (nullable) is None
        # and model_fields_set contains the field
        if self.archive_log_restore_dest is None and "archive_log_restore_dest" in self.model_fields_set:
            _dict['archiveLogRestoreDest'] = None

        # set to None if range_info_vec (nullable) is None
        # and model_fields_set contains the field
        if self.range_info_vec is None and "range_info_vec" in self.model_fields_set:
            _dict['rangeInfoVec'] = None

        # set to None if range_type (nullable) is None
        # and model_fields_set contains the field
        if self.range_type is None and "range_type" in self.model_fields_set:
            _dict['rangeType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OracleArchiveLogInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archiveLogRestoreDest": obj.get("archiveLogRestoreDest"),
            "rangeInfoVec": [OracleRangeMetaInfo.from_dict(_item) for _item in obj["rangeInfoVec"]] if obj.get("rangeInfoVec") is not None else None,
            "rangeType": obj.get("rangeType")
        })
        return _obj


