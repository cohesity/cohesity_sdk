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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class DataTieringTaskStats(BaseModel):
    """
    Specifies the stats of data tiering task.
    """ # noqa: E501
    bytes_read: Optional[StrictInt] = Field(default=None, description="Specifies total logical bytes read for creating the snapshot.", alias="bytesRead")
    bytes_written: Optional[StrictInt] = Field(default=None, description="Specifies total size of data in bytes written after taking backup.", alias="bytesWritten")
    logical_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies total logical size of object(s) in bytes.", alias="logicalSizeBytes")
    changed_entity_count: Optional[StrictInt] = Field(default=None, description="Specifies changed entity count.", alias="changedEntityCount")
    entity_count: Optional[StrictInt] = Field(default=None, description="Specifies total entity count.", alias="entityCount")
    is_tiering_goal_met: Optional[StrictBool] = Field(default=False, description="Specifies whether tiering goal has been met.", alias="isTieringGoalMet")
    total_tiered_bytes: Optional[StrictInt] = Field(default=None, description="Specifies total amount of data successfully tiered from the NAS source.", alias="totalTieredBytes")
    __properties: ClassVar[List[str]] = ["bytesRead", "bytesWritten", "logicalSizeBytes", "changedEntityCount", "entityCount", "isTieringGoalMet", "totalTieredBytes"]

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
        """Create an instance of DataTieringTaskStats from a JSON string"""
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
        # set to None if bytes_read (nullable) is None
        # and model_fields_set contains the field
        if self.bytes_read is None and "bytes_read" in self.model_fields_set:
            _dict['bytesRead'] = None

        # set to None if bytes_written (nullable) is None
        # and model_fields_set contains the field
        if self.bytes_written is None and "bytes_written" in self.model_fields_set:
            _dict['bytesWritten'] = None

        # set to None if logical_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.logical_size_bytes is None and "logical_size_bytes" in self.model_fields_set:
            _dict['logicalSizeBytes'] = None

        # set to None if changed_entity_count (nullable) is None
        # and model_fields_set contains the field
        if self.changed_entity_count is None and "changed_entity_count" in self.model_fields_set:
            _dict['changedEntityCount'] = None

        # set to None if entity_count (nullable) is None
        # and model_fields_set contains the field
        if self.entity_count is None and "entity_count" in self.model_fields_set:
            _dict['entityCount'] = None

        # set to None if is_tiering_goal_met (nullable) is None
        # and model_fields_set contains the field
        if self.is_tiering_goal_met is None and "is_tiering_goal_met" in self.model_fields_set:
            _dict['isTieringGoalMet'] = None

        # set to None if total_tiered_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.total_tiered_bytes is None and "total_tiered_bytes" in self.model_fields_set:
            _dict['totalTieredBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTieringTaskStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bytesRead": obj.get("bytesRead"),
            "bytesWritten": obj.get("bytesWritten"),
            "logicalSizeBytes": obj.get("logicalSizeBytes"),
            "changedEntityCount": obj.get("changedEntityCount"),
            "entityCount": obj.get("entityCount"),
            "isTieringGoalMet": obj.get("isTieringGoalMet") if obj.get("isTieringGoalMet") is not None else False,
            "totalTieredBytes": obj.get("totalTieredBytes")
        })
        return _obj


